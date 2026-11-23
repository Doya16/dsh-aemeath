"""Credits for every 爱弥斯 sticker pack on 呜哇小站: the text under each pack (group numbers, commissions) and the
artists' links, as collected in resources/sticker-credits.json (tools/import_aemeath_assets.py --credits)."""
import html,json,pathlib,re

CREDITS='resources/sticker-credits.json'
SITE='https://emoji.wuwa.games/'
NUMBER=re.compile(r'(?<!\d)(\d{8,11})(?!\d)')


def load(root):
    try: data=json.loads((pathlib.Path(root)/CREDITS).read_text('utf8'))
    except (OSError,ValueError): return {'packs':[]}
    packs=[p for p in data.get('packs',[]) if isinstance(p,dict) and isinstance(p.get('title'),str) and isinstance(p.get('slug'),str)]
    return dict(data,packs=packs)


def pack_url(pack): return SITE+'archives/'+pack['slug']


def numbers(data):
    """Every group number written under a pack, in first-seen order."""
    return list(dict.fromkeys(n for p in data['packs'] for n in NUMBER.findall(p.get('text',''))))


def groups(data):
    """[(group name, number)]: the named groups of the credits file, then any number only found in a pack's text."""
    named=[(g['name'],g['number']) for g in data.get('groups',[]) if isinstance(g,dict) and g.get('name') and g.get('number')]
    known={n for _,n in named}
    return named+[('爱弥斯群',n) for n in numbers(data) if n not in known]


def artist_links(data):
    """{artist or pack: [links]} for the links written under the packs (author pages, source videos)."""
    out={}
    for pack in data['packs']:
        for artist in pack.get('artists') or ['鸣潮官方' if pack['title'].startswith('【官转】') else pack['title']]:
            for link in pack.get('links',[]):
                out.setdefault(artist,[])
                if link not in out[artist]: out[artist].append(link)
    return out


def summary(data):
    if not data['packs']: return ''
    artists=list(dict.fromkeys(a for p in data['packs'] for a in p.get('artists',[])))
    lines=[f"呜哇小站收录的爱弥斯表情包共 {len(data['packs'])} 组，画师：{'、'.join(artists)}；另有鸣潮官方表情包转载。",
           '表情包说明里的群：'+'；'.join(f'{name}（{number}）' for name,number in groups(data))+'。']
    links=artist_links(data)
    if links: lines.append('作者与来源链接：'+'；'.join(f"{a} {' '.join(ls)}" for a,ls in links.items())+'。')
    if data.get('license'): lines.append('站内表情包页面的许可：'+data['license']+'。')
    return '\n'.join(lines)


def as_html(data):
    """Every pack, for the read-only credits list in the settings (links open in the browser)."""
    rows=[]
    for p in data['packs']:
        who='、'.join(p.get('artists') or (['鸣潮官方'] if p['title'].startswith('【官转】') else ['未注明画师']))
        links=' '.join(f'<a href="{html.escape(u)}">{html.escape(u)}</a>' for u in p.get('links',[]))
        rows.append(f'<p><b>{html.escape(p["title"])}</b> · {html.escape(who)} · {p.get("count","")} 张<br>{html.escape(p.get("text",""))}'
                    +(f'<br>{links}' if links else '')+f'<br><a href="{pack_url(p)}">{pack_url(p)}</a></p>')
    return ''.join(rows)


def as_text(data):
    """Plain-text list for CREDITS.txt / THIRD_PARTY.txt."""
    out=[]
    for p in data['packs']:
        who='、'.join(p.get('artists') or (['鸣潮官方'] if p['title'].startswith('【官转】') else ['未注明画师']))
        out.append(f"- {p['title']}（{who}，{p.get('count','')} 张）：{p.get('text','')}"+''.join(' '+u for u in p.get('links',[]))+' '+pack_url(p))
    return '\n'.join(out)


def as_markdown(data):
    out=['| 合集 | 画师 | 表情包说明（群号、约稿） | 链接 |','| --- | --- | --- | --- |']
    for p in data['packs']:
        who='、'.join(p.get('artists') or (['鸣潮官方'] if p['title'].startswith('【官转】') else ['未注明画师']))
        links=' '.join(f'[{u.split("//")[1].split("/")[0]}]({u})' for u in p.get('links',[]))
        text=p.get('text','').replace('|','\\|')
        out.append(f"| [{p['title']}]({pack_url(p)}) | {who} | {text} | {links} |")
    return '\n'.join(out)
