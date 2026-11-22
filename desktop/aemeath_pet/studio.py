"""Per-state animation, dialogue, typography and optional sound editor."""
import threading,time
from PySide6.QtCore import Qt,QSize,QTimer,QUrl,QObject,Signal
from PySide6.QtGui import QPixmap,QIcon,QFontDatabase,QDesktopServices
from PySide6.QtWidgets import QDialog,QWidget,QVBoxLayout,QHBoxLayout,QFormLayout,QLabel,QListWidget,QListWidgetItem,QLineEdit,QComboBox,QPushButton,QAbstractItemView,QTabWidget,QScrollArea,QDoubleSpinBox,QSpinBox,QCheckBox,QPlainTextEdit,QFileDialog,QFrame,QTreeWidget,QTreeWidgetItem,QMenu,QMessageBox
from .binding_editor import TRIGGERS
from .bindings import PLAYBACKS
from .appearance import stylesheet
from .voice_editor import VoicePoolEditor
from .control_guard import GuardedField
from .presentation_size import PresentationControl
from .media_library import IMAGE_FILTER,IMAGE_HELP,IMAGE_EXTS,import_images
from .emoji_import import DOWNLOAD_URL,import_zips,imported_packs,delete_pack
import pathlib

ZIP_FILTER='呜哇小站表情包压缩包 (*.zip)'

class ImportJob(QObject):
    step=Signal(str); done=Signal(object)

class BindingEditor(QDialog):
    def __init__(self,pet,catalog,asset_table,root,parent=None):
        super().__init__(parent,Qt.WindowType.Widget if parent is not None else Qt.WindowType.Dialog); self.pet=pet; self.catalog=catalog; self.assets=asset_table; self.root=root
        self.state='pet'; self.loading=False; self.preview_animation=None; self.preview_start=0; self.controls={}; self.guards={}
        self.setWindowTitle('爱弥斯 · 交互工作室'); self.setWindowIcon(pet.icon); self.resize(1100,900); self.setMinimumSize(840,570)
        outer=QVBoxLayout(self); outer.setContentsMargins(20,16,20,16)
        heading=QLabel('每一次回应，都可以是你喜欢的样子'); heading.setObjectName('studioHeading'); outer.addWidget(heading)
        outer.addWidget(QLabel('选择左侧状态，配置 GIF、节奏、气泡与语音。修改自动保存。'))
        body=QHBoxLayout(); outer.addLayout(body,1)
        self.triggers=QListWidget(); self.triggers.setMinimumWidth(225); self.triggers.setMaximumWidth(285)
        for state,(label,desc) in TRIGGERS.items():
            item=QListWidgetItem(label); item.setData(Qt.ItemDataRole.UserRole,state); item.setToolTip(desc); self.triggers.addItem(item)
        self.triggers.currentItemChanged.connect(self.select_trigger); body.addWidget(self.triggers,1)
        right=QVBoxLayout(); body.addLayout(right,3)
        top=QHBoxLayout(); right.addLayout(top)
        self.preview=QLabel(); self.preview.setFixedSize(150,150); self.preview.setAlignment(Qt.AlignmentFlag.AlignCenter); self.preview.setStyleSheet('background:#e8eff9;border-radius:12px;'); top.addWidget(self.preview)
        text=QVBoxLayout(); top.addLayout(text,1)
        self.heading=QLabel(); self.description=QLabel(); self.description.setWordWrap(True); self.current=QLabel(); self.current.setWordWrap(True)
        text.addWidget(self.heading); text.addWidget(self.description); text.addWidget(self.current)
        actions=QHBoxLayout(); self.try_button=QPushButton('桌宠试听 / 试看'); self.try_button.clicked.connect(self.try_binding); actions.addWidget(self.try_button)
        self.reset_button=QPushButton('此项恢复默认'); self.reset_button.clicked.connect(self.reset_binding); actions.addWidget(self.reset_button); text.addLayout(actions)
        self.tabs=QTabWidget(); right.addWidget(self.tabs,1)
        gifs=QWidget(); gifbox=QVBoxLayout(gifs)
        self.icons={}; self.importing=False; self.group=('all',); self.job=ImportJob(); self.job.step.connect(lambda text:self.library_status.setText(text)); self.job.done.connect(self.import_finished)
        # Until a pack has been imported: a hint with the two steps. Afterwards the same two buttons sit in the toolbar.
        self.download_hint=QFrame(); self.download_hint.setObjectName('downloadHint'); hint=QVBoxLayout(self.download_hint); hint.setContentsMargins(16,12,16,12)
        hint_text=QLabel('现在只有内置的三套表情预设（鸭牌、雾雪、Stephen）。想要更多爱弥斯表情包：在呜哇小站打开喜欢的合集，点「打包下载全部」，再把下载好的压缩包导入进来。可以一次选多个，也可以直接把压缩包拖进这个窗口。'); hint_text.setWordWrap(True); hint.addWidget(hint_text)
        hint_buttons=QHBoxLayout(); hint.addLayout(hint_buttons)
        self.hint_download=QPushButton('前往下载'); self.hint_download.setObjectName('hintPrimary'); self.hint_download.clicked.connect(self.open_download_page); hint_buttons.addWidget(self.hint_download)
        self.hint_import=QPushButton('导入下载好的压缩包…'); self.hint_import.setObjectName('hintPrimary'); self.hint_import.clicked.connect(self.import_zip_dialog); hint_buttons.addWidget(self.hint_import); hint_buttons.addStretch()
        hint_credit=QLabel('表情包由呜哇小站（emoji.wuwa.games）收录，版权归各画师。桌宠不会自动下载，也不附带站内的表情包；导入后按画师和合集分组。'); hint_credit.setWordWrap(True); hint_credit.setObjectName('hintCredit'); hint.addWidget(hint_credit)
        gifbox.addWidget(self.download_hint)
        files=QHBoxLayout(); gifbox.addLayout(files)
        self.zip_button=QPushButton('导入压缩包…'); self.zip_button.clicked.connect(self.import_zip_dialog); files.addWidget(self.zip_button)
        self.site_button=QPushButton('前往下载'); self.site_button.clicked.connect(self.open_download_page); files.addWidget(self.site_button)
        self.import_button=QPushButton('导入图片…'); self.import_button.clicked.connect(self.import_assets); files.addWidget(self.import_button)
        self.directory_button=QPushButton('打开素材目录'); self.directory_button.clicked.connect(self.open_asset_directory); files.addWidget(self.directory_button)
        self.refresh_button=QPushButton('刷新素材'); self.refresh_button.clicked.connect(self.refresh_gallery); files.addWidget(self.refresh_button)
        self.static_box=QCheckBox('压缩包里的静态图也导入'); self.static_box.setToolTip('默认只导入动图；不是爱弥斯的图片总是跳过。'); files.addWidget(self.static_box); files.addStretch()
        help_text=QLabel(IMAGE_HELP+'\n复制到目录后点“刷新素材”，即可预览并选中。音频请在“语音与配对气泡”添加（WAV/MP3/OGG/FLAC/M4A/AAC）；字体在外观设置添加（TTF/OTF/TTC）。'); help_text.setWordWrap(True); gifbox.addWidget(help_text)
        self.library_status=QLabel(); self.library_status.setWordWrap(True); gifbox.addWidget(self.library_status)
        self.search=QLineEdit(); self.search.setPlaceholderText('搜索 GIF 名称，例如：摸头、思考、加班'); self.search.textChanged.connect(self.filter_gallery); gifbox.addWidget(self.search)
        library=QHBoxLayout(); gifbox.addLayout(library,1)
        groups=QVBoxLayout(); library.addLayout(groups)
        self.groups=QTreeWidget(); self.groups.setHeaderHidden(True); self.groups.setMinimumWidth(190); self.groups.setMaximumWidth(250)
        self.groups.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu); self.groups.customContextMenuRequested.connect(self.group_menu)
        self.groups.currentItemChanged.connect(self.select_group); groups.addWidget(self.groups,1)
        self.delete_pack_button=QPushButton('删除这个合集'); self.delete_pack_button.clicked.connect(self.delete_selected_pack); groups.addWidget(self.delete_pack_button)
        self.gallery=QListWidget(); self.gallery.setViewMode(QListWidget.ViewMode.IconMode); self.gallery.setResizeMode(QListWidget.ResizeMode.Adjust); self.gallery.setMovement(QListWidget.Movement.Static); self.gallery.setIconSize(QSize(88,88)); self.gallery.setGridSize(QSize(142,148)); self.gallery.setWordWrap(True); self.gallery.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.setAcceptDrops(True)
        self.populate_gallery()
        self.gallery.currentItemChanged.connect(self.choose_asset); library.addWidget(self.gallery,1); self.tabs.addTab(gifs,'GIF 素材')
        play=self.form_tab('播放与切换')
        self.playback=self.combo('playback',[(v,k) for k,v in PLAYBACKS.items()]); play.addRow('播放方式',self.playback)
        play.addRow('播放速度',self.number('speed',.1,4,.1,' ×'))
        play.addRow('单次播完后再停留',self.number('hold_seconds',0,600,.5,' 秒'))
        play.addRow('循环总时长',self.number('loop_seconds',0,3600,.5,' 秒',zero='持续到下一次事件'))
        self.next_state=self.combo('next_state',[('回到当前任务 / 待机','auto'),('保持此状态，直到新事件','hold')]+[(label,state) for state,(label,_) in TRIGGERS.items()]); play.addRow('播放结束后切换到',self.next_state)
        interrupt=QCheckBox('允许新的 DeepSeek 状态提前打断'); self.controls['interruptible']=interrupt; interrupt.toggled.connect(lambda v:self.change('interruptible',v)); play.addRow(interrupt)
        desc=QLabel('单次：完整播放一遍，再等待设置的秒数。\n循环：总时长为 0 时持续播放；拖动松开、鼠标移开仍会结束相应交互。'); desc.setWordWrap(True); play.addRow(desc)
        self.timing=QLabel(); self.timing.setWordWrap(True); play.addRow(self.timing)
        bubble=self.form_tab('气泡与字体')
        self.presentation_control=PresentationControl(pet,quota=False); bubble.addRow('气泡宽度（全局）',self.presentation_control)
        bubble.addRow('气泡内容',self.combo('bubble_mode',[('默认 / 已公开进度','auto'),('使用我的台词','custom'),('自定义音频+字幕','audio'),('此状态不显示气泡','off')]))
        self.bubble_text=QPlainTextEdit(); self.bubble_text.setPlaceholderText('例如：事情办好啦！{quota}\n支持 {state}、{quota}、{task}、{progress}'); self.bubble_text.setMinimumHeight(130); self.bubble_text.textChanged.connect(lambda:self.change('bubble_text',self.bubble_text.toPlainText())); self.controls['bubble_text']=self.bubble_text; bubble.addRow('自定义台词',self.guard('bubble_text',self.bubble_text))
        bubble.addRow('气泡显示时长',self.number('bubble_seconds',0,600,.5,' 秒',zero='此状态期间始终显示'))
        families=[('跟随全局气泡字体','')]+[(f,f) for f in pet.font_families]
        for f in ('Microsoft YaHei','Segoe UI'):
            if f not in pet.font_families: families.append((f,f))
        bubble.addRow('这个状态的字体',self.guard('font_family',self.combo('font_family',families,editable=True)))
        bubble.addRow('这个状态的字号',self.number('font_size',0,40,1,' px',zero='跟随全局字号'))
        helper=QLabel('气泡宽度可单独预览、拖边调整；桌宠缩放时按保存的比例同步变化。长文案自动换行，不限制行数。\n“自定义音频+字幕”只显示抽中语音的配对文案，播完收起；没有配对文案时不显示气泡。\n全局字体、额度条字号和设置面板字号在“设置 → 字体与大小”中调整。'); helper.setWordWrap(True); bubble.addRow(helper)
        paired_button=QPushButton('为每条语音填写独立的配对气泡 →'); paired_button.clicked.connect(lambda:self.tabs.setCurrentIndex(3)); bubble.addRow(paired_button)
        voice=self.form_tab('语音与配对气泡')
        paired=QLabel('配对气泡请在“气泡与字体 → 气泡内容”选择“自定义音频+字幕”。'); paired.setWordWrap(True); voice.addRow(paired)
        self.voice_pool=VoicePoolEditor(pet,lambda:self.state); self.voice_pool.changed.connect(lambda rows:self.change('audio_clips',rows)); voice.addRow(self.voice_pool)
        voice.addRow('自动播报频率',self.combo('audio_policy',[('每次进入状态（遵守冷却时间）','entry'),('本次桌宠启动只播一次','session'),('偶尔播放','occasional'),('同一轮任务只播一次','turn')]))
        voice.addRow('偶尔播放 · 每次进入时的概率',self.number('audio_chance',0,100,5,' %'))
        voice.addRow('偶尔播放 · 最短间隔',self.number('audio_min_interval',0,3600,30,' 秒'))
        notice=QLabel('表情会等这个动作的台词说完再切换。台词一旦开始就会完整说完：说话时再次互动，动作照常但不出声，动作结束后这句台词的表情回来，直到说完。对应表情已经结束的台词不再补播；主动试听和“停止声音”仍可中断。思考每轮只播一次，试听不占用次数。'); notice.setWordWrap(True); voice.addRow(notice)
        enabled=QCheckBox('此状态允许播放音频（还需打开全局语音开关）'); self.controls['audio_enabled']=enabled; enabled.toggled.connect(lambda v:self.change('audio_enabled',v)); voice.addRow(enabled)
        for key,label in [('audio_avoid_repeat','有多条可用语音时，避免连续抽中同一条')]:
            control=QCheckBox(label); self.controls[key]=control; control.toggled.connect(lambda value,key=key:self.change(key,value)); voice.addRow(control)
        voice.addRow('进入状态后延迟',self.number('audio_delay',0,60,.1,' 秒'))
        tip=QLabel('相对文件名从全局“音频目录”读取。支持 WAV、MP3、OGG、FLAC、M4A、AAC；实际播放取决于解码器。导出时会打包已绑定的有效音频。'); tip.setWordWrap(True); voice.addRow(tip)
        self.saved=QLabel(); right.addWidget(self.saved)
        self.timer=QTimer(self); self.timer.setInterval(30); self.timer.timeout.connect(self.animate_preview)
        self.apply_style(); self.triggers.setCurrentRow(0)

    @staticmethod
    def asset_group(asset):
        """Where an asset sits in the picker: a built-in preset, my own pictures, or artist → pack of an import."""
        if asset.get('origin')=='imported': return ('pack',asset.get('artist',''),asset.get('pack',''))
        if asset.get('origin')=='custom': return ('custom',)
        return ('preset',asset.get('skin',''))
    @staticmethod
    def group_matches(group,key):
        kind=group[0]
        if kind=='all': return True
        if kind=='presets': return key[0]=='preset'
        if kind=='imports': return key[0]=='pack'
        if kind=='artist': return key[0]=='pack' and key[1]==group[1]
        return key==group
    def icon(self,asset):
        key=(asset['path'],asset.get('sha256'))
        if key not in self.icons:
            pixmap=QPixmap(str(self.root/asset['path'])); self.icons[key]=QIcon(pixmap.scaled(88,88,Qt.AspectRatioMode.KeepAspectRatio,Qt.TransformationMode.SmoothTransformation))
        return self.icons[key]

    def populate_gallery(self):
        self.gallery.blockSignals(True); self.gallery.clear()
        from .packs import PACK_LABELS
        for asset in self.catalog:
            key=self.asset_group(asset)
            where={'preset':lambda:PACK_LABELS.get(key[1],key[1]),'custom':lambda:'我的图片','pack':lambda:key[2]}[key[0]]()
            item=QListWidgetItem(self.icon(asset),pathlib.Path(asset['name']).stem+'\n'+where); item.setData(Qt.ItemDataRole.UserRole,asset['id']); item.setData(Qt.ItemDataRole.UserRole+1,key)
            credit=(' · '+asset['artist']) if asset.get('artist') else ''
            item.setToolTip(asset['name']+' · '+str(asset['frames'])+' 帧\n'+(asset.get('pack') or where)+credit); self.gallery.addItem(item)
        self.gallery.blockSignals(False); self.build_groups(); self.filter_gallery(self.search.text())
        imported=sum(1 for a in self.catalog if a.get('origin')=='imported')
        self.download_hint.setVisible(not imported); self.zip_button.setVisible(bool(imported)); self.site_button.setVisible(bool(imported))
        self.library_status.setText(f'共 {len(self.catalog)} 个素材'+(f'（其中导入的表情包 {imported} 张）' if imported else '')+' · 点击缩略图即可绑定到当前动作')

    def build_groups(self):
        """Left of the gallery: all, the built-in presets, each imported artist with its packs, my own pictures."""
        from .packs import PACKS,PACK_LABELS
        current=self.group; self.groups.blockSignals(True); self.groups.clear(); select=None
        counts={}
        for asset in self.catalog:
            key=self.asset_group(asset); counts[key]=counts.get(key,0)+1
        def node(parent,text,group):
            nonlocal select
            item=QTreeWidgetItem(parent,[text]); item.setData(0,Qt.ItemDataRole.UserRole,group)
            if group==current: select=item
            return item
        everything=node(self.groups,f'全部素材（{len(self.catalog)}）',('all',))
        presets=node(self.groups,'内置预设',('presets',))
        for name in PACKS: node(presets,f"{PACK_LABELS.get(name,name)}（{counts.get(('preset',name),0)}）",('preset',name))
        packs=imported_packs(self.root)
        if packs:
            imports=node(self.groups,'导入的表情包',('imports',)); artists={}
            for artist,pack,count in packs:
                if artist not in artists: artists[artist]=node(imports,artist,('artist',artist))
                node(artists[artist],f'{pack}（{counts.get(("pack",artist,pack),count)}）',('pack',artist,pack))
        if counts.get(('custom',)): node(self.groups,f"我的图片（{counts[('custom',)]}）",('custom',))
        self.groups.expandAll(); self.groups.blockSignals(False)
        if select is None: select=everything; self.group=('all',)
        self.groups.setCurrentItem(select); self.delete_pack_button.setEnabled(self.group[0]=='pack' and not self.importing)
    def select_group(self,item,old=None):
        if item is None: return
        self.group=tuple(item.data(0,Qt.ItemDataRole.UserRole)); self.delete_pack_button.setEnabled(self.group[0]=='pack' and not self.importing)
        self.filter_gallery(self.search.text())
    def group_menu(self,point):
        item=self.groups.itemAt(point)
        if item is None or item.data(0,Qt.ItemDataRole.UserRole)[0]!='pack': return
        self.groups.setCurrentItem(item); menu=QMenu(self); action=menu.addAction('删除这个合集…')
        if menu.exec(self.groups.viewport().mapToGlobal(point))==action: self.delete_selected_pack()

    def refresh_gallery(self):
        warnings=self.pet.refresh_assets(); self.populate_gallery(); self.load_selection()
        if warnings: self.library_status.setText('部分文件未加入：'+'；'.join(warnings[:4]))

    def open_download_page(self):
        if not QDesktopServices.openUrl(QUrl(DOWNLOAD_URL)): self.library_status.setText('浏览器无法自动打开，请手动访问：'+DOWNLOAD_URL)
    def import_zip_dialog(self):
        paths,_=QFileDialog.getOpenFileNames(self,'导入呜哇小站表情包压缩包',str(pathlib.Path.home()/'Downloads'),ZIP_FILTER)
        if paths: self.import_zip_files(paths)
    def set_importing(self,value):
        self.importing=value
        for button in (self.hint_import,self.zip_button,self.import_button,self.refresh_button,self.static_box): button.setEnabled(not value)
        self.delete_pack_button.setEnabled(not value and self.group[0]=='pack')
    def import_zip_files(self,paths,wait=False):
        """Import in the background; the status line shows progress and then what was added and skipped."""
        if self.importing or not paths: return
        self.set_importing(True); include=self.static_box.isChecked(); self.library_status.setText('正在导入压缩包…')
        def work():
            try: report=import_zips(paths,self.root,include_static=include,progress=lambda i,n,name:self.job.step.emit(f'正在导入第 {i}/{n} 个压缩包：{name}…'))
            except Exception as error: report=error
            self.job.done.emit(report)
        thread=threading.Thread(target=work,daemon=True); thread.start()
        if wait: thread.join()
    def import_finished(self,report):
        self.set_importing(False)
        if isinstance(report,Exception): self.library_status.setText('导入失败：'+str(report)); return
        if report.packs: self.group=('pack',*next(reversed(report.packs)))
        self.refresh_gallery(); self.library_status.setText(report.text())
    def confirm_delete(self,artist,pack,count):
        answer=QMessageBox.question(self,'删除合集',f'删除导入的合集「{pack}」（{artist}，{count} 张）？\n用到其中图片的动作会回到当前预设的表情。删除后可以重新导入压缩包。')
        return answer==QMessageBox.StandardButton.Yes
    def delete_selected_pack(self):
        if self.group[0]!='pack' or self.importing: return
        _,artist,pack=self.group; count=next((n for a,p,n in imported_packs(self.root) if (a,p)==(artist,pack)),0)
        if not self.confirm_delete(artist,pack,count): return
        try: removed=delete_pack(self.root,artist,pack)
        except (OSError,ValueError) as error: self.library_status.setText('删除失败：'+str(error)); return
        self.group=('all',); self.refresh_gallery(); self.library_status.setText(f'已删除合集「{pack}」（{removed} 张）。')

    def dragEnterEvent(self,event):
        if self.dropped_files(event): event.acceptProposedAction()
        else: super().dragEnterEvent(event)
    def dropEvent(self,event):
        files=self.dropped_files(event)
        if not files: return super().dropEvent(event)
        event.acceptProposedAction()
        zips=[f for f in files if f.lower().endswith('.zip')]; images=[f for f in files if not f.lower().endswith('.zip')]
        if images:
            imported,warnings=import_images(images,self.root); self.refresh_gallery()
            self.library_status.setText(f'已导入 {len(imported)} 个素材。'+('；'.join(warnings[:4]) if warnings else ''))
        if zips: self.import_zip_files(zips)
    def dropped_files(self,event):
        if self.importing or not event.mimeData().hasUrls(): return []
        files=[u.toLocalFile() for u in event.mimeData().urls() if u.isLocalFile()]
        return [f for f in files if pathlib.Path(f).suffix.lower() in IMAGE_EXTS|{'.zip'}]

    def open_asset_directory(self):
        folder=self.root/'assets/custom'; folder.mkdir(parents=True,exist_ok=True)
        if not QDesktopServices.openUrl(QUrl.fromLocalFile(str(folder))): self.library_status.setText('目录无法自动打开：'+str(folder))

    def import_assets(self):
        paths,_=QFileDialog.getOpenFileNames(self,'导入角色图片',str(self.root/'assets/custom'),IMAGE_FILTER)
        if not paths: return
        imported,warnings=import_images(paths,self.root); self.refresh_gallery()
        self.library_status.setText(f'已导入 {len(imported)} 个素材。'+('；'.join(warnings[:4]) if warnings else '选择缩略图即可绑定。'))

    def form_tab(self,title):
        scroll=QScrollArea(); scroll.setWidgetResizable(True); content=QWidget(); content.setObjectName('settingsBody'); form=QFormLayout(content); form.setContentsMargins(16,16,16,16); form.setSpacing(14); form.setFieldGrowthPolicy(QFormLayout.FieldGrowthPolicy.AllNonFixedFieldsGrow); form.setRowWrapPolicy(QFormLayout.RowWrapPolicy.WrapLongRows); scroll.setWidget(content); self.tabs.addTab(scroll,title); return form
    def combo(self,key,items,editable=False):
        control=QComboBox(); control.setEditable(editable)
        for label,value in items: control.addItem(label,value)
        self.controls[key]=control
        control.currentIndexChanged.connect(lambda:self.change(key,control.currentData() if control.currentData() is not None else control.currentText()))
        if editable: control.lineEdit().editingFinished.connect(lambda:self.change(key,control.currentData() if control.currentData() is not None else control.currentText()))
        return control
    def number(self,key,lo,hi,step,suffix,zero=None):
        control=QDoubleSpinBox(); control.setRange(lo,hi); control.setSingleStep(step); control.setDecimals(2 if key=='speed' else 1); control.setSuffix(suffix); control.setKeyboardTracking(False)
        if zero: control.setSpecialValueText(zero)
        control.valueChanged.connect(lambda v:self.change(key,v)); self.controls[key]=control; return self.guard(key,control)
    def guard(self,key,control):
        wrapper=GuardedField(control); self.guards[key]=wrapper; return wrapper
    def apply_style(self):
        self.setStyleSheet(stylesheet(self.pet.options)+'QLabel#studioHeading{font-size:25px;font-weight:600;color:#2e5280;}'
                           'QFrame#downloadHint{background:#fdf1f6;border:1px solid #f2c4d8;border-radius:12px;}QLabel#hintCredit{color:#8a6f7d;}'
                           'QPushButton#hintPrimary{padding:8px 18px;font-weight:600;}'
                           'QTreeWidget{background:#ffffff;border:1px solid #c6d1ed;border-radius:8px;padding:4px;}QTreeWidget::item{padding:3px 2px;}QTreeWidget::item:selected{background:#dbe8fb;color:#2e5280;}')
    def select_trigger(self,item,old=None):
        if item is not None: self.state=item.data(Qt.ItemDataRole.UserRole); self.load_selection()
    def load_selection(self):
        self.loading=True; b=self.pet.binding(self.state); asset=self.assets[b['asset']]
        self.heading.setText(TRIGGERS[self.state][0]); self.description.setText(TRIGGERS[self.state][1]); self.current.setText(('自定义 · ' if b['custom'] else '预设默认 · ')+asset['name'].removesuffix('.gif'))
        for key,control in self.controls.items():
            value=b[key]
            if isinstance(control,QComboBox):
                idx=control.findData(value)
                if idx<0: control.addItem(str(value),value); idx=control.count()-1
                control.setCurrentIndex(idx)
            elif isinstance(control,QCheckBox): control.setChecked(value)
            elif isinstance(control,QDoubleSpinBox): control.setValue(value)
            elif isinstance(control,QPlainTextEdit): control.setPlainText(value)
            else: control.setText(value)
        for i in range(self.gallery.count()):
            item=self.gallery.item(i)
            if item.data(Qt.ItemDataRole.UserRole)==b['asset']: self.gallery.setCurrentItem(item); self.gallery.scrollToItem(item); break
        self.preview_animation=self.pet.get_animation(b['asset']); self.preview_start=time.monotonic()
        self.voice_pool.set_clips(b['audio_clips'])
        self.loading=False; self.refresh_labels(); self.update_timing(); self.saved.setText('修改自动保存 · '+('已自定义' if b['custom'] else '当前为默认设置')); self.animate_preview()
    def refresh_labels(self):
        for i in range(self.triggers.count()):
            item=self.triggers.item(i); state=item.data(Qt.ItemDataRole.UserRole); item.setText(TRIGGERS[state][0]+(' ·' if self.pet.binding(state)['custom'] else ''))
    def update_timing(self):
        b=self.pet.binding(self.state); seconds=self.assets[b['asset']]['duration_ms']/1000/b['speed']
        self.voice_pool.update_hint(b,self.pet.options)
        if b['next_state']=='hold': ending='当前保持此状态，直到新事件，不执行定时切换。'
        elif b['playback']=='once': ending=f"将在 {seconds+b['hold_seconds']:.2f} 秒后执行切换。"
        elif b['loop_seconds']: ending=f"将在循环 {b['loop_seconds']:g} 秒后执行切换。"
        else: ending='持续循环，直到下一次事件。'
        self.timing.setText(f'当前 GIF 正向播放一遍约 {seconds:.2f} 秒；'+ending)
        mode=PLAYBACKS[b['playback']]
        self.guards['hold_seconds'].lock(f'“{mode}”模式下无法修改“单次播完后再停留”；切换为“播放一次”即可调整。' if b['playback']!='once' else ('“保持此状态”模式下无法修改“单次播完后再停留”；请先更改播放结束后的切换方式。' if b['next_state']=='hold' else ''))
        self.guards['loop_seconds'].lock('“播放一次”模式下无法修改“循环总时长”；切换为循环播放即可调整。' if b['playback']=='once' else ('“保持此状态”模式下无法修改“循环总时长”；请先更改播放结束后的切换方式。' if b['next_state']=='hold' else ''))
        bubble_mode={'auto':'默认 / 已公开进度','off':'此状态不显示气泡','custom':'使用我的台词','audio':'自定义音频+字幕'}[b['bubble_mode']]
        self.guards['bubble_text'].lock(f'“{bubble_mode}”模式下无法修改“自定义台词”；请选择“使用我的台词”。' if b['bubble_mode']!='custom' else '')
        for key,label in [('bubble_seconds','气泡显示时长'),('font_family','这个状态的字体'),('font_size','这个状态的字号')]:
            self.guards[key].lock(f'“此状态不显示气泡”模式下无法修改“{label}”；请先开启气泡。' if b['bubble_mode']=='off' else '')
        if b['bubble_mode']=='audio': self.guards['bubble_seconds'].lock('“自定义音频+字幕”模式下无法修改“气泡显示时长”；气泡随配对语音播放，播完收起。')
        self.guards['audio_delay'].lock('“此状态关闭音频”模式下无法修改“进入状态后延迟”；请先勾选“此状态允许播放音频”。' if not b['audio_enabled'] else '')
        for key,label in [('audio_chance','播放概率'),('audio_min_interval','最短间隔')]:
            hint='“非偶尔播放”模式下无法修改“'+label+'”；请将自动播报频率设为“偶尔播放”。' if b['audio_policy']!='occasional' else ''
            if not b['audio_enabled']:hint='“此状态关闭音频”模式下无法修改“'+label+'”；请先开启此状态的音频。'
            self.guards[key].lock(hint)
    def change(self,key,value):
        if self.loading: return
        ok=self.pet.set_binding(self.state,**{key:value}); self.saved.setText('已自动保存' if ok else '保存失败，请检查文件夹是否可写。'); self.refresh_labels(); self.update_timing()
        if key in ('speed','playback'): self.preview_start=time.monotonic()
    def choose_asset(self,item,old=None):
        if self.loading or item is None: return
        self.pet.set_binding(self.state,asset=item.data(Qt.ItemDataRole.UserRole)); self.load_selection()
    def reset_binding(self): self.pet.reset_binding(self.state); self.load_selection()
    def try_binding(self): self.pet.preview_binding(self.state); self.preview_start=time.monotonic()
    def save_all(self): self.saved.setText('全部配置已保存' if self.pet.save_settings() else '保存失败，请检查目录权限。')
    def filter_gallery(self,text):
        needle=text.strip().casefold()
        for i in range(self.gallery.count()):
            item=self.gallery.item(i); key=tuple(item.data(Qt.ItemDataRole.UserRole+1) or ())
            item.setHidden(not self.group_matches(self.group,key) or needle not in (item.text()+' '+item.toolTip()).casefold())
    def animate_preview(self):
        if self.preview_animation is None: return
        b=self.pet.binding(self.state); frame=self.preview_animation.frame((time.monotonic()-self.preview_start)*1000*b['speed'],playback=b['playback']); self.preview.setPixmap(QPixmap.fromImage(frame).scaled(146,146,Qt.AspectRatioMode.KeepAspectRatio,Qt.TransformationMode.SmoothTransformation))
    def showEvent(self,event): self.refresh_gallery(); self.timer.start(); super().showEvent(event)
    def hideEvent(self,event):
        self.timer.stop()
        if self.pet.controller.owner=='preview': self.pet.clear_override()
        super().hideEvent(event)
