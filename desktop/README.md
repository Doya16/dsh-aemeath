<!-- README language switch -->
[![中文](https://img.shields.io/badge/%E4%B8%AD%E6%96%87-1677ff?style=for-the-badge)](README.md) [![English](https://img.shields.io/badge/English-555555?style=for-the-badge)](README.en.md)
<!-- /README language switch -->

<div align="center">

# 爱弥斯 DeepSeek 桌宠

**《鸣潮》爱弥斯陪你使用 DeepSeek Harness：跟随任务切换表情，用她的声音回应你。**

[下载 Windows 版](https://github.com/Doya16/aemeath-deepseek-pet/releases/latest) · [使用指南](docs/USAGE.md) · [问题反馈](https://github.com/Doya16/aemeath-deepseek-pet/issues) · [English](README.en.md)

![三套表情预设：鸭牌、雾雪、Stephen，各 16 种交互](docs/images/events-presets.jpg)

</div>

让爱弥斯陪你使用 **DeepSeek Harness 官方 Windows 客户端**：任务进行时换表情，完成后用语音和字幕气泡回应，底部显示账户余额，完成时飘字显示这一轮的花费和用时。

适用于 **Windows 10/11 x64**。完整包附带 **三套表情预设（鸭牌、雾雪、Stephen）、90 条带字幕的爱弥斯语音**、两款字体和 Harness 连接插件。更多爱弥斯表情包可以从 [呜哇小站](https://emoji.wuwa.games/archives?character=爱弥斯) 下载后一键导入。无需安装 Python。

## 安装方法

**系统要求**：Windows 10（1809 及以后）或 Windows 11，64 位；Windows 7 / 8 无法运行。需要先安装官方 **DeepSeek Harness** 桌面客户端，并登录、打开过一次。

1. 打开 [Releases](https://github.com/Doya16/aemeath-deepseek-pet/releases/latest)，下载 **Aemeath-DeepSeek-Windows-v1.0.0.zip**。
2. 解压：右键压缩包 →「全部解压缩」，或用 7-Zip / WinRAR 选「解压到 Aemeath-DeepSeek-Windows-v…\」（和压缩包同名的文件夹）。
   - 不要选「解压到当前文件夹」：压缩包里没有外层文件夹，文件会散在下载目录里。
   - 不要解压到 `C:\Program Files` 这类不能写入的位置，也不要在压缩软件里直接双击运行。
3. 进入解压出来的文件夹，双击 **一键部署.cmd**。它会检查文件，提示你**完全退出** Harness（托盘图标右键 → 退出，登录状态会保留）后安装 Harness 连接插件，创建桌面和开始菜单快捷方式，然后启动爱弥斯。
4. 重新打开 Harness，开始任务。桌宠自动跟随最近活动的会话，同步状态和余额。

暂时不想退出 Harness 时，可以在提示处输入 `S` 跳过插件，之后再运行一次「一键部署.cmd」，或在 **设置 → 连接 DeepSeek → 安装 / 更新 Harness 连接插件** 中安装。无需填写 API Key。

**如果被系统或安全软件拦下：** 弹出「Windows 已保护你的电脑」时，点「更多信息」→「仍要运行」。程序没有购买商业代码签名，所以 Windows 会这样提示。安全软件拦截时请把这个文件夹加入信任区；全部源码公开在本仓库，每个版本的发布页都附有 SHA256SUMS 校验文件。

以后有新版本，桌宠会自己提示，点 **更新并重启爱弥斯** 即可一键更新，设置和素材都会保留。声音默认开启，音量为 10%，在「设置 → 桌面与声音」中调整或关闭。

## 三套表情预设

| 预设 | 画师 | 来源合集 |
| --- | --- | --- |
| **Stephen**（默认） | Stephen樽 | 爱弥斯·演唱会捏捏动态表情包（大寸）等捏捏表情包 |
| **鸭牌** | 春也Huruya | 爱弥斯动态表情包（鸭牌） |
| **雾雪** | 雾雪 | 爱弥斯动态表情包（雾雪）、日服生日会、围巾冬装、慵懒情侣衫、家居服、古风 |

每套预设都给 16 种交互配好了 16 张互不相同的表情：

| 鼠标互动 | 任务状态 | 其他 |
| --- | --- | --- |
| 单击摸头、双击、鼠标停留、拖动中、松开放下、递奶茶 | 思考、查阅资料、编辑内容、执行工具、等待你回应、任务完成、任务出错、任务暂停 | 待机陪伴、状态未更新 |

在 **设置 → 桌面与声音 → 表情预设** 切换。三套预设共用同一组语音；在交互工作室里单独换过表情的动作，切换预设后保持你的选择。

![桌面与声音：表情预设下拉框](docs/images/preset-switch.png)

## 更多表情包：从呜哇小站导入

桌宠只附带上面三套预设。爱弥斯的其他表情包收录在 [呜哇小站](https://emoji.wuwa.games/archives?character=爱弥斯)，下载后导入即可：

1. **设置 → 交互工作室 → GIF 素材**，点 **前往下载**，在浏览器里打开喜欢的合集，点 **打包下载全部**。
2. 点 **导入下载好的压缩包…**（可以一次选多个），或者直接把压缩包拖进设置窗口。
3. 导入的表情按 **画师 → 合集** 分组；点缩略图即可绑定到当前动作。

| 还没导入时 | 导入之后 |
| --- | --- |
| ![还没导入时：前往下载 / 导入下载好的压缩包](docs/images/studio-download-hint.png) | ![导入后按画师和合集分组](docs/images/studio-imported.png) |

- 按图片内容识别画师、合集和动作名，例如 `001-XXS01_喇叭.gif` 显示为「喇叭」；新合集用压缩包名作合集名。
- 静态图和不是爱弥斯的图片默认跳过（可勾选导入静态图）；和预设相同、或已经导入过的图片不会重复复制。
- 导入的表情包保存在程序目录的 `assets/imported/`，一键更新不会动它们；选中合集点 **删除这个合集** 即可删除。
- 桌宠不附带、也不会自动下载站内的表情包。表情包版权归各画师，转载或二次分发请先联系站长和画师。

## 语音与字幕

- **90 条爱弥斯语音**，按 16 种交互配好，每条都有字幕；同一动作有多条时随机抽取。
- **台词一旦开始就会说完**：她说话时再点、双击、拖动或递奶茶，动作照常变化，只是不出新声音；动作结束后，这句台词的表情会回来，直到说完。
- **字幕气泡**：角色上方显示台词，默认字体为站酷快乐体；字号、宽度在 **设置 → 字体与大小** 调，也可以直接拖动气泡左右边缘。
- **安静陪伴（静音）**：右键勾选后立即停止声音；取消后恢复原来的音量。
- 每句台词何时开始、何时结束，记录在程序目录的 `voice-log.txt`，反馈“台词没说完”时可以附上。

## 跟随任务、余额与本轮花费

- 任务进行时，表情依次切换为思考、查阅、编辑、执行、等你回应；结束时显示完成、出错或暂停。多个会话的完成提醒依次出现。
- 在 **设置 → 连接 DeepSeek → 跟随的会话** 中选择“自动跟随最近活动”（默认），或固定跟随一个会话。
- 底部余额框显示账户充值与赠送余额合计，悬停看明细；点击余额框或右键 → **刷新余额** 立即重读。
- 任务完成时，角色旁飘出本轮花费（按 token 用量和官方价格估算）和用时，并撒彩色纸屑；样式、顺序和位置都能调整或关闭。

## 桌面陪伴

- **贴边藏起**、**全屏隐藏**、**每日小结**、**喝水和久坐提醒**（爱弥斯递上一杯奶茶，可设“稍后再提醒”的分钟数）。
- **顶部小锁**：锁定后点击穿透到下面的窗口；小锁仍可点。
- **随 Harness 启动 / 退出**：在 **设置 → 连接 DeepSeek** 勾选。
- Windows 音量合成器显示「爱弥斯 · DeepSeek」；托盘提示「爱弥斯 · DeepSeek」。关闭程序：右键 → **关闭爱弥斯**。

## 自定义

右键桌宠 → **设置 → 交互工作室**，先在左侧选一个动作，再为它选表情、播放规则、气泡和语音。支持 GIF、动画 WebP、PNG、JPG/JPEG；语音支持 WAV、MP3、OGG、FLAC、M4A、AAC；字体支持 TTF、OTF、TTC。自带 **霞鹜文楷** 和 **站酷快乐体** 两款字体。

## 一键更新

桌宠启动后在后台检查新版本，默认每 6 小时一次。点击 **更新并重启爱弥斯**，即可完成下载、校验、安装和重启；只更新程序文件，保留表情、语音、导入的表情包和全部个人设置。更新清单由发布者离线密钥签名（Ed25519），签名不对就不会安装。更新来源可选 **自动选择 / GitHub 官方源 / 镜像加速（中国大陆网络）**。如果某次更新说明需要更新连接插件，按提示重新运行「一键部署.cmd」或在连接设置中重装即可。详见 [更新与恢复](docs/UPDATES.md)。

## 保存与换电脑

设置自动保存。在 **设置 → 保存与迁移** 可以导出 **配置与素材包**（ZIP）或 **Windows 便携完整包**。换电脑后安装并登录 Harness，启动桌宠，再在连接设置中安装一次连接插件。Harness 的登录信息和聊天记录不在桌宠包里。

## 适用范围

- 面向官方 Harness 桌面客户端；网页版普通 DeepSeek 聊天不在连接范围。
- 连接插件名为 `dsh-aemeath-pet`，与其他桌宠的连接插件互不影响，可以同时安装。

## 常见问题

**一键部署提示“在压缩包里直接运行”？** 先把整个 ZIP 解压到一个文件夹，再双击里面的「一键部署.cmd」。

**连接插件没装上？** 确认已从托盘完全退出 Harness（不是只关窗口），并且 Harness 至少打开过一次；然后再运行一次「一键部署.cmd」。

**表情没有跟随新任务？** 重新打开 Harness 后开始一个新任务；在「设置 → 连接 DeepSeek」选择「自动跟随最近活动」。

**遇到其他问题？** 到 [Issues](https://github.com/Doya16/aemeath-deepseek-pet/issues) 附上系统版本、Harness 版本、操作步骤和报错截图；台词问题请附上 `voice-log.txt`。

## 素材来源与致谢

表情包来自 [呜哇小站](https://emoji.wuwa.games/) 收录的画师作品：**鸭牌** —— 春也Huruya；**雾雪** —— 雾雪；**Stephen** —— Stephen樽。感谢各位画师创作这些表情包，也感谢呜哇小站整理收录。设置 → 版本与更新 → **关于与致谢** 里列出每套预设用到的合集，以及你导入的表情包的画师。

![关于与致谢](docs/images/about.png)

### 呜哇小站收录的全部爱弥斯表情包

每组表情包下面写的群号、约稿说明和作者链接都列在这里，桌宠的「关于与致谢」里也有同样的列表。

<!-- STICKER-CREDITS -->

呜哇小站收录的爱弥斯表情包共 43 组，画师：Stephen樽、嗷懒叽、雾雪、飞过海机、春也Huruya、Gwenevyr、腐朽的书、早茶步、猫屋敷梨梨&春也Haruya、圆圆、时时今晚吃什么；另有鸣潮官方表情包转载。

表情包说明里的群：爱弥一生一世（1036168246）；星炬学院 爱弥斯联合（1103460714）；飞行雪绒の小窝（1057194050）；小爱弥斯捏捏表情包约稿交流群（画师 圆圆）（1063144481）；千咲应援团（1124633691）。

作者与来源链接：全角色琵琶曲 v3.0 https://www.bilibili.com/video/BV1tVnb6UEiL；飞过海机 https://space.bilibili.com/30905275 https://www.bilibili.com/video/BV1qAi1ByEQe；Gwenevyr https://vgen.co/Gwenevyr；春也Huruya https://www.bilibili.com/video/BV1StgN6RE4x；雾雪 https://www.bilibili.com/video/BV1PGDqBqEMD https://www.bilibili.com/video/BV1UV9zBsEcS；鸣潮官方 https://jingxuan.douyin.com/m/video/7655191335334399259 https://www.bilibili.com/h5/mall/digital-card/home?act_id=113956 https://www.bilibili.com/h5/mall/digital-card/home?act_id=113353 https://x.com/WW_JP_Official/status/2059847130424959437 https://store.line.me/stickershop/product/34587241/ja https://x.com/WW_JP_Official/status/2029164964712476733。

站内表情包页面的许可：CC BY-NC-SA 4.0（站内文章声明：转载请注明出处）。

| 合集 | 画师 | 表情包说明（群号、约稿） | 链接 |
| --- | --- | --- | --- |
| [爱弥斯捏捏表情包](https://emoji.wuwa.games/archives/aimisi-same-pack-merged-20261005) | Stephen樽 | 感谢B站UP Stephen樽 的精心绘制 |  |
| [爱弥斯 · 春贺 动态表情包（懒牌）](https://emoji.wuwa.games/archives/aimisi-magical-girl-a-20261122) | 嗷懒叽 | 欢迎喜欢小爱的潮友们加入 爱弥一生一世（1036168246）~ |  |
| [全角色琵琶曲 v3.0](https://emoji.wuwa.games/archives/all-characters-pipa-v3-20261023) | 未注明画师 | 共28张动态表情。 | [www.bilibili.com](https://www.bilibili.com/video/BV1tVnb6UEiL) |
| [爱弥斯 · 古风 动态表情包·(雾雪N16）](https://emoji.wuwa.games/archives/aimisi-gufeng-dlc15-20261021) | 雾雪 | 感谢来自潮友 夜宵是牛油果 的约稿~同时也欢迎喜欢小爱的大家加入爱弥斯联合(1103460714） |  |
| [爱弥斯 · 小爱同学](https://emoji.wuwa.games/archives/feiguohaiji-bv1qai1byeqe-20261009) | 飞过海机 | 共15张静态表情。原作者：飞过海机；含 AI 生成内容。 | [space.bilibili.com](https://space.bilibili.com/30905275) [www.bilibili.com](https://www.bilibili.com/video/BV1qAi1ByEQe) |
| [爱弥斯演唱会捏捏表情包（小寸）](https://emoji.wuwa.games/archives/aimisi-concert-small-merged-20261005) | Stephen樽 | 感谢来自群聊 爱弥一生一世（1036168246）的约稿 |  |
| [爱弥斯·演唱会捏捏动态表情包（大寸）](https://emoji.wuwa.games/archives/aimisi-concert-merged-20261005) | Stephen樽 | 感谢来自群聊 爱弥一生一世（1036168246）的约稿 |  |
| [爱弥斯X男漂 · 校服动态表情包（雾雪）](https://emoji.wuwa.games/archives/aimisi-rover-school-poi) | 雾雪 | 感谢来自 猫薄荷 的约稿，欢迎喜欢小爱的大家加群爱弥一生一世（1036168246） |  |
| [爱弥斯动态表情包（鸭牌）](https://emoji.wuwa.games/archives/aimisi-gb0224-a-20260927) | 春也Huruya | 感谢来自群飞行雪绒の小窝（1057194050）的约稿 |  |
| [爱弥斯 Cheek Puff 捏脸表情包](https://emoji.wuwa.games/archives/aimisi-cheek-puff-slow) | Gwenevyr | 感谢来自 YCH Cheek Puff TrielaTea 的约稿，也感谢画师：Gwenevyr（https://vgen.co/Gwenevyr）的制作 | [vgen.co](https://vgen.co/Gwenevyr) |
| [爱弥斯 静态表情包（书牌）](https://emoji.wuwa.games/archives/backlog-20260927-g040) | 腐朽的书 | 感谢来自 腐朽的书 的倾情制作~ |  |
| [吃月饼角色合集（书牌）](https://emoji.wuwa.games/archives/backlog-20260927-g011-v1) | 腐朽的书 | 感谢来着 腐朽的书 的倾情制作 |  |
| [爱弥斯静态表情包 .Ver 早茶步](https://emoji.wuwa.games/archives/aimisi-zaochabu) | 早茶步 | 感谢来着潮友的约稿 |  |
| [爱弥斯国服二周年服饰动态表情包（雾雪）](https://emoji.wuwa.games/archives/aimisi-06-wuxue-cn-2nd) | 雾雪 | 感谢来自群聊 爱弥一生一世（1036168246）的约稿 |  |
| [爱弥斯致新世界演唱会动态表情包（雾雪）](https://emoji.wuwa.games/archives/aimisi-07-concert) | 雾雪 | 感谢来自群聊 爱弥一生一世（1036168246）的约稿 |  |
| [爱弥斯韩服二周年服饰动态表情包（雾雪）](https://emoji.wuwa.games/archives/aimisi-04) | 雾雪 | 感谢来自群聊 爱弥一生一世（1036168246）的约稿 |  |
| [儿童节小小爱动态表情包（鸭牌）](https://emoji.wuwa.games/archives/aimisi-05) | 春也Huruya | 感谢来自群聊 爱弥一生一世（1036168246）的约稿 |  |
| [爱弥斯动态表情包（板牌）](https://emoji.wuwa.games/archives/aimisi-01) | 猫屋敷梨梨&春也Haruya | 感谢来自群聊 爱弥一生一世（1036168246）的约稿 |  |
| [猫耳爱弥斯动态表情包（板牌）](https://emoji.wuwa.games/archives/aimisi-01-cat-ears) | 猫屋敷梨梨&春也Haruya | 感谢来自群聊 爱弥一生一世（1036168246）的约稿 |  |
| [爱弥斯鸣潮二周年动态表情包（懒A）](https://emoji.wuwa.games/archives/aimisi-super-q) | 嗷懒叽 | 超级Q动态表情爱弥斯，共 20 张动态表情。 |  |
| [小小爱动态表情包（鸭牌）](https://emoji.wuwa.games/archives/aimisi-xiaoai-03-yapai) | 春也Huruya | 感谢来自萝莉控们的众筹约稿 | [www.bilibili.com](https://www.bilibili.com/video/BV1StgN6RE4x) |
| [小小爱动态表情包（雾雪）](https://emoji.wuwa.games/archives/aimisi-xiaoai-01-wuxue) | 雾雪 | 感谢来自萝莉控们的众筹约稿 | [www.bilibili.com](https://www.bilibili.com/video/BV1PGDqBqEMD) [www.bilibili.com](https://www.bilibili.com/video/BV1UV9zBsEcS) |
| [致新世界演唱会特辑](https://emoji.wuwa.games/archives/new-world-concert-special) | 雾雪 | 感谢来自角色厨们的约稿 |  |
| [小爱弥斯捏捏表情包](https://emoji.wuwa.games/archives/aimisi-xiao) | 圆圆 | 1063144481约稿的交流群，后续有鸣潮的表情包也会直接分享在这个群里 |  |
| [爱弥斯动态表情包（雾雪）](https://emoji.wuwa.games/archives/aimisi-haohaoxiao) | 雾雪 | 感谢来自 好好咲w 的动态表情包 同时也欢迎爱厨加群（1036168246）游玩 |  |
| [爱弥斯动态表情包（时时）](https://emoji.wuwa.games/archives/aimisi-03) | 时时今晚吃什么 | 感谢来自群聊 爱弥一生一世（1036168246）的约稿 |  |
| [千咲的岁共朋友（雾雪）](https://emoji.wuwa.games/archives/chisa-suigong-friends) | 雾雪 | 感谢来自群聊 好好咲w的约稿，同时也欢迎喜欢小千的大家加入 千咲应援团（1124633691） |  |
| [聚爆烤肉三人队（雾雪）](https://emoji.wuwa.games/archives/chisa-aimisi-daniya) | 雾雪 | 感谢来自 好好咲 的约稿 |  |
| [爱弥斯日服生日会动态表情包（雾雪）](https://emoji.wuwa.games/archives/aimisi-xinjilemu-outfit-5) | 雾雪 | 感谢来自 辛吉勒姆 的约稿，也欢迎喜欢小爱的各位加入群聊 星炬学院 爱弥斯联合（1103460714） |  |
| [爱弥斯校服动态表情包（雾雪）](https://emoji.wuwa.games/archives/aimisi-xinjilemu-outfit-4) | 雾雪 | 感谢来自群聊 星炬学院 爱弥斯联合（1103460714）的约稿 |  |
| [爱弥斯家居服动态表情包（雾雪）](https://emoji.wuwa.games/archives/aimisi-xinjilemu-outfit-3) | 雾雪 | 感谢来自群聊 星炬学院 爱弥斯联合（1103460714）的约稿 |  |
| [爱弥斯围巾冬装动态表情包（雾雪）](https://emoji.wuwa.games/archives/aimisi-xinjilemu-outfit-2) | 雾雪 | 感谢来自群聊 星炬学院 爱弥斯联合（1103460714）的约稿 |  |
| [爱弥斯慵懒情侣衫动态表情包（雾雪）](https://emoji.wuwa.games/archives/aimisi-xinjilemu-outfit-1) | 雾雪 | 感谢来自群聊 星炬学院 爱弥斯联合（1103460714）的约稿 |  |
| [爱弥斯X漂泊者双人表情包（雾雪）](https://emoji.wuwa.games/archives/aimisi-rover-xinjilemu) | 雾雪 | 感谢来自群聊 星炬学院 爱弥斯联合（1103460714）的约稿 |  |
| [猫耳小爱 X 阿漂双人表情包（雾雪）](https://emoji.wuwa.games/archives/aimisi-02) | 雾雪 | 感谢来自群聊 爱弥一生一世（1036168246）的约稿 |  |
| [【官转】mini共鸣日常表情包](https://emoji.wuwa.games/archives/official-mini-daily-cn) | 鸣潮官方 | 转载自鸣潮官方，本站仅做收集整理。共16张静态表情，国内发布版。 | [jingxuan.douyin.com](https://jingxuan.douyin.com/m/video/7655191335334399259) |
| [【官转】B站致予新世界表情包（静态）](https://emoji.wuwa.games/archives/official-bili-new-world-static) | 鸣潮官方 | 转载自鸣潮官方，本站仅做收集整理。共25张静态表情。 | [www.bilibili.com](https://www.bilibili.com/h5/mall/digital-card/home?act_id=113956) |
| [【官转】B站致予新世界表情包（动态）](https://emoji.wuwa.games/archives/official-bili-new-world-animated) | 鸣潮官方 | 转载自鸣潮官方，本站仅做收集整理。共25张动态表情。 | [www.bilibili.com](https://www.bilibili.com/h5/mall/digital-card/home?act_id=113956) |
| [【官转】B站二周年潮声庆典表情包（静态）](https://emoji.wuwa.games/archives/official-bili-2nd-anniversary-static) | 鸣潮官方 | 转载自鸣潮官方，本站仅做收集整理。共25张静态表情。 | [www.bilibili.com](https://www.bilibili.com/h5/mall/digital-card/home?act_id=113353) |
| [【官转】B站二周年潮声庆典表情包（动态）](https://emoji.wuwa.games/archives/official-bili-2nd-anniversary-animated) | 鸣潮官方 | 转载自鸣潮官方，本站仅做收集整理。共25张动态表情。 | [www.bilibili.com](https://www.bilibili.com/h5/mall/digital-card/home?act_id=113353) |
| [【官转】共鸣者印象录·第十三章表情包](https://emoji.wuwa.games/archives/official-resonators-ch13) | 鸣潮官方 | 转载自鸣潮官方，本站仅做收集整理。共16张动态表情。 | [x.com](https://x.com/WW_JP_Official/status/2059847130424959437) |
| [【官转】共鸣日常·LINE配字表情包](https://emoji.wuwa.games/archives/official-mini-daily) | 鸣潮官方 | 转载自鸣潮官方，本站仅做收集整理。共16张静态表情，LINE日文配字版。 | [store.line.me](https://store.line.me/stickershop/product/34587241/ja) |
| [【官转】Irasutoya联名表情包](https://emoji.wuwa.games/archives/official-irasutoya) | 鸣潮官方 | 转载自鸣潮官方，本站仅做收集整理。共16张静态表情。 | [x.com](https://x.com/WW_JP_Official/status/2029164964712476733) |

<!-- /STICKER-CREDITS -->

角色语音来自《鸣潮》爱弥斯的角色语音。角色、表情包图片与原版语音的权利归各自权利人所有（《鸣潮》© 库洛游戏）。本项目为个人制作的同人作品，与库洛游戏和呜哇小站无关。表情包仅供个人、非商业使用，请勿倒卖或用于付费分发。程序依赖及字体的许可不适用于角色素材；详见 [素材说明](assets/CREDITS.txt) 和 [第三方许可](THIRD_PARTY.txt)。

<details>
<summary>从源码运行</summary>

安装 Python 3.12，在项目目录执行：

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m aemeath_pet
```

程序模块位于 `aemeath_pet/`；连接插件位于 `integrations/deepseek/`；构建、发布和快捷方式工具位于 `tools/`。构建便携版：`.\.venv\Scripts\python.exe -m pip install -r tools/requirements-build.txt`，再运行 `.\.venv\Scripts\python.exe tools/build_portable.py`，输出在 `dist/爱弥斯DeepSeek桌宠/`。运行检查：`.\.venv\Scripts\python.exe -m unittest discover -s tests`；连接插件：在 `integrations/deepseek` 中运行 `node --test`。

</details>
