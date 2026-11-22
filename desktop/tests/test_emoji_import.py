"""爱弥斯 sticker packs from 呜哇小站: the zip importer, the picker's hint and groups, and the credits."""
import hashlib,io,json,os,pathlib,shutil,tempfile,unittest,zipfile
from unittest.mock import patch
from PIL import Image
from PySide6.QtCore import QMimeData,QPoint,QPointF,QUrl,Qt
from PySide6.QtGui import QDropEvent,QDragEnterEvent
from PySide6.QtWidgets import QApplication
from aemeath_pet import emoji_import as importer
from aemeath_pet import pet as module
from aemeath_pet import preferences as prefs
from aemeath_pet.media_library import load_catalog

REPO=pathlib.Path(__file__).resolve().parents[1]
SAMPLE=pathlib.Path(os.environ.get('AEMEATH_SAMPLE_ZIP',pathlib.Path.home()/'Downloads/aimisi-05.gif.zip'))


def gif(colour,frames=2,size=(40,40)):
    images=[Image.new('RGB',size,colour)]+[Image.new('RGB',size,(i*40%256,80,120)) for i in range(1,frames)]
    out=io.BytesIO(); images[0].save(out,'GIF',save_all=frames>1,append_images=images[1:],duration=100,loop=0); return out.getvalue()


def noisy():
    out=io.BytesIO(); Image.frombytes('L',(120,120),os.urandom(14400)).save(out,'GIF'); return out.getvalue()


def png(colour):
    out=io.BytesIO(); Image.new('RGB',(30,30),colour).save(out,'PNG'); return out.getvalue()


def sha(data): return hashlib.sha256(data).hexdigest()


def make_root(base):
    """A pet folder with the real presets (hard links), catalog and shipped index."""
    root=pathlib.Path(base)/'爱弥斯桌宠'; (root/'assets').mkdir(parents=True); (root/'resources').mkdir()
    shutil.copytree(REPO/'assets/originals',root/'assets/originals',copy_function=os.link)
    shutil.copy2(REPO/'assets/catalog.json',root/'assets/catalog.json')
    shutil.copy2(REPO/'resources/emoji-index.json',root/'resources/emoji-index.json')
    return root


class ZipImportTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory(); self.root=make_root(self.temp.name); self.downloads=pathlib.Path(self.temp.name)/'下载'; self.downloads.mkdir()
        self.known,self.static,self.other,self.unknown,self.unknown_static=gif('red'),png('blue'),gif('green'),gif('purple'),gif('white',frames=1)
        index=json.loads((self.root/'resources/emoji-index.json').read_text('utf8'))
        index['packs'].append(['test-pack','测试合集（测试画师）'])
        for data,name,skip in ((self.known,'喇叭',''),(self.static,'静态','静态图'),(self.other,'别人','不是爱弥斯')):
            index['images'][sha(data)]=dict(artist='测试画师',pack='测试合集（测试画师）',slug='test-pack',name=name,skip=skip)
        (self.root/'resources/emoji-index.json').write_text(json.dumps(index,ensure_ascii=False),'utf8')

    def tearDown(self): self.temp.cleanup()

    def zip(self,name,members):
        path=self.downloads/name
        with zipfile.ZipFile(path,'w') as z:
            for member,data in members: z.writestr(member,data)
        return path

    def files(self):
        base=self.root/importer.IMPORTED
        return sorted(p.relative_to(base).as_posix() for p in base.rglob('*') if p.is_file() and not p.name.startswith('.'))

    def test_index_names_images_and_skips_static_and_other_characters(self):
        path=self.zip('test-pack.gif.zip',[('001-XXS01_随便.gif',self.known),('002-XXS02_x.png',self.static),('003-XXS03_y.gif',self.other)])
        report=importer.import_zips([path],self.root)
        self.assertEqual(self.files(),['测试画师/测试合集（测试画师）/喇叭.gif'])
        self.assertEqual(report.skipped['static'],1); self.assertEqual(report.skipped['other'],1)
        self.assertIn('静态图 1',report.text()); self.assertIn('不是爱弥斯 1',report.text())

    def test_static_images_come_in_when_asked_but_other_characters_never(self):
        path=self.zip('test-pack.gif.zip',[('002-XXS02_x.png',self.static),('003-XXS03_y.gif',self.other),('004-Q4_静止.gif',self.unknown_static)])
        importer.import_zips([path],self.root,include_static=True)
        self.assertEqual(self.files(),['测试画师/测试合集（测试画师）/静态.png','测试画师/测试合集（测试画师）/静止.gif'])

    def test_unknown_images_are_named_from_the_file_and_the_zip(self):
        path=self.zip('new-pack-2027.gif (1).zip',[('007-AB12_转圈圈.gif',self.unknown),('008-AB13_不动.gif',self.unknown_static),('009-hello.gif',gif('olive'))])
        report=importer.import_zips([path],self.root)
        self.assertEqual(self.files(),[f'{importer.UNKNOWN_ARTIST}/new-pack-2027/hello.gif',f'{importer.UNKNOWN_ARTIST}/new-pack-2027/转圈圈.gif'])
        self.assertEqual(report.skipped['static'],1)

    def test_a_known_pack_slug_names_new_images_after_the_pack(self):
        path=self.zip('test-pack.gif.zip',[('020-NEW01_新动作.gif',self.unknown)])
        importer.import_zips([path],self.root)
        self.assertEqual(self.files(),['测试画师/测试合集（测试画师）/新动作.gif'])

    def test_presets_and_earlier_imports_are_not_copied_twice(self):
        preset=(self.root/'assets/originals/yp-idle.gif').read_bytes()
        path=self.zip('test-pack.gif.zip',[('001-a.gif',preset),('002-b.gif',self.known)])
        first=importer.import_zips([path],self.root); second=importer.import_zips([path],self.root)
        self.assertEqual(first.skipped['preset'],1); self.assertEqual(len(first.added),1)
        self.assertEqual(second.skipped['duplicate'],1); self.assertFalse(second.added); self.assertEqual(len(self.files()),1)

    def test_unsafe_names_large_files_and_other_files_are_refused(self):
        outside=pathlib.Path(self.temp.name)/'evil.gif'
        path=self.zip('test-pack.gif.zip',[('../evil.gif',self.unknown),('/abs.gif',self.unknown),('C:/x.gif',self.unknown),('readme.txt',b'hi'),('big.gif',noisy())])
        with patch.object(importer,'MAX_FILE',2000): report=importer.import_zips([path],self.root)
        self.assertFalse(outside.exists()); self.assertEqual(self.files(),[])
        self.assertEqual(report.skipped['unsafe'],3); self.assertEqual(report.skipped['not_image'],1); self.assertEqual(report.skipped['too_large'],1)

    def test_total_size_cap_stops_a_zip(self):
        path=self.zip('test-pack.gif.zip',[(f'{i:03}-c{i}.gif',gif((i*30,0,0))) for i in range(1,6)])
        with patch.object(importer,'MAX_ZIP_TOTAL',len(gif((30,0,0)))*2+10): report=importer.import_zips([path],self.root)
        self.assertEqual(len(report.added),2); self.assertTrue(report.warnings)

    def test_broken_zip_and_non_zip_are_reported_not_raised(self):
        bad=self.downloads/'坏的.zip'; bad.write_bytes(b'not a zip'); other=self.downloads/'x.gif'; other.write_bytes(self.known)
        report=importer.import_zips([bad,other],self.root)
        self.assertEqual(len(report.warnings),2); self.assertFalse(report.added)

    def test_imports_are_listed_by_artist_and_pack_and_a_pack_can_be_deleted(self):
        importer.import_zips([self.zip('test-pack.gif.zip',[('001-a.gif',self.known)]),self.zip('zzz.gif.zip',[('001-b.gif',self.unknown)])],self.root)
        self.assertEqual(importer.imported_packs(self.root),[('未注明画师','zzz',1),('测试画师','测试合集（测试画师）',1)])
        catalog,warnings=load_catalog(self.root); rows=[r for r in catalog if r.get('origin')=='imported']
        self.assertFalse(warnings); self.assertEqual({(r['artist'],r['pack']) for r in rows},{('未注明画师','zzz'),('测试画师','测试合集（测试画师）')})
        self.assertEqual(importer.delete_pack(self.root,'测试画师','测试合集（测试画师）'),1)
        self.assertEqual(importer.imported_packs(self.root),[('未注明画师','zzz',1)]); self.assertFalse((self.root/importer.IMPORTED/'测试画师').exists())
        with self.assertRaises(ValueError): importer.delete_pack(self.root,'..','assets')

    def test_catalog_details_are_cached_until_a_file_changes(self):
        importer.import_zips([self.zip('test-pack.gif.zip',[('001-a.gif',self.known)])],self.root)
        first=load_catalog(self.root)[0]
        with patch('aemeath_pet.media_library.inspect_image',side_effect=AssertionError('re-read')): self.assertEqual(load_catalog(self.root)[0],first)
        target=self.root/importer.IMPORTED/'测试画师/测试合集（测试画师）/喇叭.gif'; target.write_bytes(gif('red',frames=3))
        self.assertEqual(next(r for r in load_catalog(self.root)[0] if r.get('origin')=='imported')['frames'],3)

    def test_names_from_files_and_zips(self):
        self.assertEqual(importer.clean_name('001-XXS01_喇叭.gif'),'喇叭')
        self.assertEqual(importer.clean_name('12N02_吃饭.gif'),'吃饭')
        self.assertEqual(importer.clean_name('003-hello.gif'),'hello')
        self.assertEqual(importer.clean_name('摸头_2.gif'),'摸头_2')
        self.assertEqual(importer.zip_slug('aimisi-05.gif.zip'),'aimisi-05')
        self.assertEqual(importer.zip_slug('aimisi-05.gif (2).zip'),'aimisi-05')
        self.assertEqual(importer.safe_part('a/b:c*'),'a b c'); self.assertEqual(importer.safe_part('CON'),'_CON')


@unittest.skipUnless(SAMPLE.is_file(),'sample download from 呜哇小站 not on this machine')
class SampleDownloadTests(unittest.TestCase):
    def test_the_childrens_day_pack_imports_twelve_named_images(self):
        with tempfile.TemporaryDirectory() as temp:
            root=make_root(temp); report=importer.import_zips([SAMPLE],root)
            folder=root/importer.IMPORTED/'春也Huruya'/'儿童节小小爱动态表情包（鸭牌）'
            names=[p.stem for p in sorted(folder.iterdir(),key=lambda p:p.stat().st_mtime_ns)]
            self.assertEqual(len(report.added),12)
            self.assertEqual(sorted(names),sorted(['喇叭','波板糖','吹泡泡','竹蜻蜓','小红花','书包','星星眼','粉笔','hello','妈妈','杂鱼','拉报警器']))
            self.assertEqual(importer.imported_packs(root),[('春也Huruya','儿童节小小爱动态表情包（鸭牌）',12)])


class PresetTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app=QApplication.instance() or QApplication([]); cls.app.setQuitOnLastWindowClosed(False)

    def make(self,**settings):
        self.temp=tempfile.TemporaryDirectory(); path=pathlib.Path(self.temp.name)/'settings.json'
        from aemeath_pet.config_io import save_atomic
        save_atomic(path,dict(appearance=dict(audio_muted=True),**settings))
        self.patch=patch.object(module,'SETTINGS',path); self.patch.start()
        self.pet=module.Pet(offline=True); self.pet.timer.stop(); self.pet.slow_timer.stop(); return self.pet

    def tearDown(self):
        if not hasattr(self,'pet'): return
        if getattr(self.pet,'preferences',None): self.pet.preferences.hide()
        self.pet.hide(); self.patch.stop(); self.temp.cleanup()

    def test_three_presets_each_with_sixteen_different_gifs(self):
        pet=self.make(); self.assertEqual(list(module.PACKS),['鸭牌','雾雪','Stephen']); self.assertEqual(pet.pack,module.DEFAULT_PACK)
        for name,states in module.PACKS.items():
            self.assertEqual(len(states),16,name)
            self.assertEqual(len({module.ASSETS[a]['sha256'] for a in states.values()}),16,name)

    def test_the_settings_switch_changes_the_preset_and_keeps_hand_picked_gifs(self):
        pet=self.make(bindings=dict(pet=dict(asset='wx-feed'))); pet.open_preferences('桌面与声音'); combo=pet.preferences.pack
        self.assertEqual([combo.itemData(i) for i in range(combo.count())],list(module.PACKS))
        self.assertEqual(combo.currentData(),module.DEFAULT_PACK)
        combo.setCurrentIndex(combo.findData('鸭牌'))
        self.assertEqual(pet.pack,'鸭牌'); self.assertEqual(pet.settings['pack'],'鸭牌')
        self.assertEqual(pet.binding('idle')['asset'],'yp-idle'); self.assertEqual(pet.binding('pet')['asset'],'wx-feed')

    def test_an_unknown_saved_preset_falls_back_to_the_default(self):
        pet=self.make(pack='旧预设'); self.assertEqual(pet.pack,module.DEFAULT_PACK)
        pet.apply_settings(dict(pet.settings,pack='雾雪')); self.assertEqual(pet.binding('done')['asset'],'wx-done')

    def test_about_names_the_site_and_every_preset_artist(self):
        text=prefs.about_text(module.CATALOG)
        for word in ('呜哇小站','emoji.wuwa.games','春也Huruya','雾雪','Stephen樽','库洛'): self.assertIn(word,text)


class StudioImportTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app=QApplication.instance() or QApplication([]); cls.app.setQuitOnLastWindowClosed(False)

    def setUp(self):
        self.temp=tempfile.TemporaryDirectory(); self.root=make_root(self.temp.name)
        self.saved=(list(module.CATALOG),dict(module.ASSETS))
        from aemeath_pet.config_io import save_atomic
        save_atomic(self.root/'settings.json',dict(appearance=dict(audio_muted=True)))
        self.patches=[patch.object(module,'ROOT',self.root),patch.object(module,'SETTINGS',self.root/'settings.json'),patch.object(prefs,'ROOT',self.root)]
        for p in self.patches: p.start()
        self.pet=module.Pet(offline=True); self.pet.timer.stop(); self.pet.slow_timer.stop()
        self.pet.open_preferences('交互工作室'); self.studio=self.pet.binding_editor; self.studio.refresh_gallery()

    def tearDown(self):
        self.pet.preferences.hide(); self.pet.hide()
        for p in reversed(self.patches): p.stop()
        module.CATALOG[:]=self.saved[0]; module.ASSETS.clear(); module.ASSETS.update(self.saved[1])
        self.app.processEvents(); self.temp.cleanup()

    def sample(self):
        path=pathlib.Path(self.temp.name)/'test-pack.gif.zip'
        with zipfile.ZipFile(path,'w') as z:
            z.writestr('001-A01_转圈.gif',gif('red')); z.writestr('002-A02_跳.gif',gif('blue'))
        return path

    def run_import(self,paths):
        self.studio.import_zip_files(paths,wait=True); self.app.processEvents()

    def group_texts(self):
        out=[]
        def walk(item,depth):
            out.append('  '*depth+item.text(0))
            for i in range(item.childCount()): walk(item.child(i),depth+1)
        for i in range(self.studio.groups.topLevelItemCount()): walk(self.studio.groups.topLevelItem(i),0)
        return out

    def test_hint_first_then_toolbar_and_groups_after_an_import(self):
        s=self.studio
        self.assertFalse(s.download_hint.isHidden()); self.assertTrue(s.zip_button.isHidden()); self.assertTrue(s.site_button.isHidden())
        self.assertEqual([t.strip() for t in self.group_texts()][:5],['全部素材（48）','内置预设','鸭牌 · 春也Huruya（16）','雾雪（16）','Stephen · Stephen樽（16）'])
        with patch('aemeath_pet.studio.QDesktopServices.openUrl',return_value=True) as opened: s.hint_download.click()
        self.assertEqual(opened.call_args[0][0].toString(),importer.DOWNLOAD_URL)
        self.run_import([self.sample()])
        self.assertTrue(s.download_hint.isHidden()); self.assertFalse(s.zip_button.isHidden()); self.assertFalse(s.site_button.isHidden())
        self.assertIn('导入的表情包',[t.strip() for t in self.group_texts()]); self.assertIn('未注明画师',[t.strip() for t in self.group_texts()])
        self.assertEqual(s.group,('pack','未注明画师','test-pack'))
        visible=[s.gallery.item(i).text().split('\n')[0] for i in range(s.gallery.count()) if not s.gallery.item(i).isHidden()]
        self.assertEqual(sorted(visible),['跳','转圈']); self.assertIn('已导入 2 张',s.library_status.text())
        self.assertTrue(s.delete_pack_button.isEnabled())

    def test_an_imported_gif_can_be_bound_and_its_pack_deleted(self):
        s=self.studio; self.run_import([self.sample()])
        item=next(s.gallery.item(i) for i in range(s.gallery.count()) if not s.gallery.item(i).isHidden())
        s.gallery.setCurrentItem(item); aid=item.data(Qt.ItemDataRole.UserRole); self.assertEqual(self.pet.binding('pet')['asset'],aid)
        with patch.object(s,'confirm_delete',return_value=False): s.delete_selected_pack()
        self.assertEqual(len(importer.imported_packs(self.root)),1)
        with patch.object(s,'confirm_delete',return_value=True): s.delete_selected_pack()
        self.assertEqual(importer.imported_packs(self.root),[]); self.assertFalse(s.download_hint.isHidden())
        self.assertEqual(self.pet.binding('pet')['asset'],module.PACKS[self.pet.pack]['pet'])

    def test_dropping_a_zip_on_the_studio_imports_it(self):
        s=self.studio; data=QMimeData(); data.setUrls([QUrl.fromLocalFile(str(self.sample()))])
        enter=QDragEnterEvent(QPoint(10,10),Qt.DropAction.CopyAction,data,Qt.MouseButton.LeftButton,Qt.KeyboardModifier.NoModifier)
        s.dragEnterEvent(enter); self.assertTrue(enter.isAccepted())
        with patch.object(s,'import_zip_files') as start:
            s.dropEvent(QDropEvent(QPointF(10,10),Qt.DropAction.CopyAction,data,Qt.MouseButton.LeftButton,Qt.KeyboardModifier.NoModifier))
        self.assertEqual([pathlib.Path(p).name for p in start.call_args[0][0]],['test-pack.gif.zip'])
        other=QMimeData(); other.setUrls([QUrl.fromLocalFile(str(pathlib.Path(self.temp.name)/'notes.txt'))])
        refused=QDragEnterEvent(QPoint(10,10),Qt.DropAction.CopyAction,other,Qt.MouseButton.LeftButton,Qt.KeyboardModifier.NoModifier); refused.ignore()
        s.dragEnterEvent(refused); self.assertFalse(refused.isAccepted())

    def test_about_lists_the_imported_artists(self):
        self.run_import([self.sample()]); self.pet.open_preferences('版本与更新')
        self.assertIn('未注明画师',self.pet.preferences.imported_credit.text())


if __name__=='__main__':
    unittest.main()
