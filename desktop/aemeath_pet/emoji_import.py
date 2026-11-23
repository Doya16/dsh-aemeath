"""Import 爱弥斯 sticker packs that the user downloaded from 呜哇小站 (emoji.wuwa.games).

The pet ships only its three presets. More packs come from the site's 「打包下载全部」 zips, which the user
downloads in a browser and imports here; the pet never downloads or bundles the site's library.

A site zip is flat, named <pack slug>.gif.zip, with UTF-8 members such as 001-XXS01_喇叭.gif.
Each image is identified by SHA-256 in resources/emoji-index.json (artist, pack, clean name; skip = 静态图 /
不是爱弥斯). Images the index does not know are named from the file name (minus NNN- and the code prefix), the
pack comes from the zip name and static images are recognised by frame count.
Imports go to assets/imported/<artist>/<pack>/<name>.<ext>; update packages never write under assets/.
"""
import collections,hashlib,json,os,pathlib,re,shutil,zipfile
from .media_library import inspect_image

SITE='https://emoji.wuwa.games/'
DOWNLOAD_URL='https://emoji.wuwa.games/archives?character=爱弥斯'
IMPORTED='assets/imported'
INDEX='resources/emoji-index.json'
EXTS={'.gif','.png','.webp'}
MAX_FILE=20*1024*1024          # same limit as inspect_image
MAX_ZIP_TOTAL=800*1024*1024    # images taken from one zip
MAX_TOTAL=2*1024*1024*1024     # images taken in one import
MAX_MEMBERS=5000
UNKNOWN_ARTIST='未注明画师'
REASONS={'static':'静态图','other':'不是爱弥斯','preset':'与内置预设相同','duplicate':'已导入过','not_image':'不是图片',
         'too_large':'超过大小上限','unsafe':'路径不安全','broken':'无法读取'}


def load_index(root):
    """{'images': {sha256: {...}}, 'packs': {slug: (artist, title)}}; empty when the shipped index is missing."""
    try: data=json.loads((pathlib.Path(root)/INDEX).read_text('utf8'))
    except (OSError,ValueError): data={}
    images=data.get('images') if isinstance(data.get('images'),dict) else {}
    titles={}
    for row in data.get('packs') or []:
        if isinstance(row,list) and len(row)==2 and all(isinstance(x,str) for x in row): titles[row[0]]=row[1]
    packs={}
    for entry in images.values():
        slug=entry.get('slug')
        if slug and slug not in packs: packs[slug]=(entry.get('artist') or UNKNOWN_ARTIST,entry.get('pack') or titles.get(slug,slug))
    for slug,title in titles.items(): packs.setdefault(slug,(UNKNOWN_ARTIST,title))
    from .credits import load as load_credits
    for pack in load_credits(root)['packs']:
        artist='&'.join(pack.get('artists') or []) or ('鸣潮官方' if pack['title'].startswith('【官转】') else UNKNOWN_ARTIST)
        packs.setdefault(pack['slug'],(artist,pack['title']))
    return {'images':images,'packs':packs}


def safe_part(text,fallback='未命名'):
    """One Windows-safe path component."""
    text=re.sub(r'[\\/:*?"<>|\x00-\x1f]+',' ',str(text or '')).strip().rstrip('. ')
    if text.split('.')[0].lower() in {'con','prn','aux','nul',*(f'com{i}' for i in range(1,10)),*(f'lpt{i}' for i in range(1,10))}: text='_'+text
    return text[:80] or fallback


def zip_slug(path):
    """aimisi-05.gif.zip -> aimisi-05 (also 'aimisi-05.gif (1).zip' as browsers save a second copy)."""
    stem=pathlib.Path(path).name
    stem=re.sub(r'\.zip$','',stem,flags=re.I)
    stem=re.sub(r'\s*\(\d+\)$','',stem)
    stem=re.sub(r'\.(gif|png|webp|jpe?g)$','',stem,flags=re.I)
    return re.sub(r'\s*\(\d+\)$','',stem).strip() or '未命名合集'


def clean_name(member):
    """001-XXS01_喇叭.gif -> 喇叭; 12N02_吃饭.gif -> 吃饭; a name without such prefixes stays as it is."""
    stem=pathlib.PurePosixPath(member).stem
    name=re.sub(r'^\d{1,4}[-_ ]','',stem)
    coded=re.sub(r'^(?=[A-Za-z0-9]*\d)[A-Za-z0-9]{1,12}_','',name)
    return (coded or name or stem).strip()


def unsafe(name):
    p=pathlib.PurePosixPath(name)
    return not name or '\\' in name or ':' in name or name.startswith('/') or p.is_absolute() or '..' in p.parts


def digest(path):
    with open(path,'rb') as f: return hashlib.file_digest(f,'sha256').hexdigest()


def existing_hashes(root):
    folder=pathlib.Path(root)/IMPORTED; found=set()
    if folder.is_dir():
        for p in folder.rglob('*'):
            if p.is_file() and p.suffix.lower() in EXTS:
                try: found.add(digest(p))
                except OSError: pass
    return found


def preset_hashes(root):
    try: rows=json.loads((pathlib.Path(root)/'assets/catalog.json').read_text('utf8'))
    except (OSError,ValueError): return set()
    return {r.get('sha256') for r in rows if isinstance(r,dict) and r.get('sha256')}


class Report:
    def __init__(self):
        self.added=[]; self.packs=collections.OrderedDict(); self.skipped=collections.Counter(); self.warnings=[]
    def text(self):
        if self.added:
            groups='；'.join(f'{a} / {p} {n} 张' for (a,p),n in self.packs.items())
            head=f'已导入 {len(self.added)} 张：{groups}。'
        else: head='没有导入新的图片。'
        skipped='、'.join(f'{REASONS[k]} {n}' for k,n in self.skipped.items() if n)
        return head+(f'跳过：{skipped}。' if skipped else '')+(' '+'；'.join(self.warnings[:3]) if self.warnings else '')


def import_zips(paths,root,include_static=False,progress=None):
    """Import images from the given zip files. Returns a Report; never raises for a bad zip or member."""
    root=pathlib.Path(root).resolve(); base=root/IMPORTED; base.mkdir(parents=True,exist_ok=True)
    staging=base/'.importing'; shutil.rmtree(staging,ignore_errors=True); staging.mkdir()
    index=load_index(root); presets=preset_hashes(root); seen=existing_hashes(root); report=Report(); total=0
    try:
        for number,value in enumerate(paths,1):
            path=pathlib.Path(value)
            if progress: progress(number,len(paths),path.name)
            if path.suffix.lower()!='.zip': report.warnings.append(path.name+'：不是 ZIP 压缩包'); continue
            slug=zip_slug(path); zip_artist,zip_pack=index['packs'].get(slug,(None,None))
            try: archive=zipfile.ZipFile(path)
            except (OSError,zipfile.BadZipFile) as error: report.warnings.append(path.name+'：压缩包无法打开'); continue
            with archive:
                members=archive.infolist()
                if len(members)>MAX_MEMBERS: report.warnings.append(path.name+'：文件太多，已跳过'); continue
                taken=0
                for info in members:
                    if info.is_dir(): continue
                    name=info.filename
                    if unsafe(name): report.skipped['unsafe']+=1; continue
                    if pathlib.PurePosixPath(name).suffix.lower() not in EXTS: report.skipped['not_image']+=1; continue
                    if info.file_size>MAX_FILE: report.skipped['too_large']+=1; continue
                    if taken+info.file_size>MAX_ZIP_TOTAL or total+info.file_size>MAX_TOTAL:
                        report.warnings.append(path.name+'：超过单次导入总大小上限，其余图片未导入'); break
                    try:
                        with archive.open(info) as f: data=f.read(MAX_FILE+1)
                    except (OSError,zipfile.BadZipFile,RuntimeError,EOFError,ValueError): report.skipped['broken']+=1; continue
                    if len(data)>MAX_FILE: report.skipped['too_large']+=1; continue
                    taken+=len(data); total+=len(data)
                    sha=hashlib.sha256(data).hexdigest()
                    if sha in presets: report.skipped['preset']+=1; continue
                    if sha in seen: report.skipped['duplicate']+=1; continue
                    known=index['images'].get(sha)
                    if known and known.get('skip')=='不是爱弥斯': report.skipped['other']+=1; continue
                    if known and known.get('skip')=='静态图' and not include_static: report.skipped['static']+=1; continue
                    ext=pathlib.PurePosixPath(name).suffix.lower()
                    temp=staging/(sha[:16]+ext); temp.write_bytes(data)
                    try: info_row=inspect_image(temp,root)
                    except (OSError,ValueError): temp.unlink(missing_ok=True); report.skipped['broken']+=1; continue
                    if not known and info_row['frames']<=1 and not include_static: temp.unlink(missing_ok=True); report.skipped['static']+=1; continue
                    if known: artist,pack,title=known.get('artist') or UNKNOWN_ARTIST,known.get('pack') or zip_pack or slug,known.get('name') or clean_name(name)
                    else: artist,pack,title=zip_artist or UNKNOWN_ARTIST,zip_pack or slug,clean_name(name)
                    folder=base/safe_part(artist)/safe_part(pack); folder.mkdir(parents=True,exist_ok=True)
                    target=folder/(safe_part(title)+ext); n=2
                    while target.exists(): target=folder/f'{safe_part(title)}-{n}{ext}'; n+=1
                    os.replace(temp,target); seen.add(sha)
                    report.added.append(target); key=(folder.parent.name,folder.name); report.packs[key]=report.packs.get(key,0)+1
    finally: shutil.rmtree(staging,ignore_errors=True)
    return report


def imported_packs(root):
    """[(artist, pack, image count)] of what has been imported, sorted by artist then pack."""
    base=pathlib.Path(root)/IMPORTED; rows=[]
    if base.is_dir():
        for artist in sorted(p for p in base.iterdir() if p.is_dir() and not p.name.startswith('.')):
            for pack in sorted(p for p in artist.iterdir() if p.is_dir()):
                count=sum(1 for f in pack.iterdir() if f.is_file() and f.suffix.lower() in EXTS)
                if count: rows.append((artist.name,pack.name,count))
    return rows


def delete_pack(root,artist,pack):
    """Remove one imported pack (and its artist folder once empty). Returns the number of files removed."""
    base=(pathlib.Path(root)/IMPORTED).resolve(); folder=(base/artist/pack).resolve()
    if folder.parent.parent!=base or not folder.is_dir(): raise ValueError('找不到这个合集')
    count=sum(1 for f in folder.rglob('*') if f.is_file()); shutil.rmtree(folder)
    try: folder.parent.rmdir()
    except OSError: pass
    return count
