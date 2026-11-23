<div align="center">
  <img src="icon.png" width="192" height="192" alt="爱弥斯桌宠图标：鸭牌预设里的爱弥斯与 DeepSeek 小标">

# 爱弥斯桌宠 · DeepSeek Harness 完整版插件

**《鸣潮》爱弥斯陪你使用 DeepSeek Harness：跟随任务切换表情，用她的声音回应你。**

[English](README.en.md) · [问题反馈](https://github.com/Doya16/dsh-aemeath/issues)

![三套表情预设：鸭牌、雾雪、Stephen，各 16 种交互](desktop/docs/images/events-presets.jpg)

</div>

插件版的桌宠程序与 [爱弥斯 DeepSeek 桌宠](https://github.com/Doya16/aemeath-deepseek-pet) 完整包相同：三套表情预设（鸭牌、雾雪、Stephen）、90 条带字幕的爱弥斯语音、余额框与本轮花费飘字，还能导入呜哇小站下载的爱弥斯表情包。插件负责下载、启动和连接 Harness，不需要另装连接插件。

**使用条件：** Windows 10（1809 及以后）/ 11 x64、本机 DeepSeek Harness。首次启动时下载完整程序（约 186 MiB），无需安装 Python。

## 开始使用

1. 安装并登录 [DeepSeek Harness](https://www.deepseek.com/harness/)。
2. 在 Harness 的插件管理中安装并启用 `dsh-aemeath`。
3. 点击窗口右下角 **爱弥斯桌宠 → 下载并安装完整版**。下载来源可选自动、GitHub 或镜像加速（中国大陆网络）。
4. 点击 **启动桌宠**。右键桌宠 → **设置…**，或从插件入口点击 **打开完整设置**。

完整包版用户迁入：在完整包版「设置 → 保存与迁移」导出配置素材 ZIP，再在插件版的同一位置导入。两者不要同时运行，否则会出现两只桌宠。

首次安装并成功启动桌宠后，右下角的部署面板和「爱弥斯桌宠」按钮会自动隐藏；以后在 **Harness 设置 → 爱弥斯桌宠** 启动、关闭、打开完整设置或更新完整版，也可以恢复入口。爱弥斯的入口按钮比其他桌宠插件的入口更高，同时启用时不会叠在一起。

## 三套表情预设

| 预设 | 画师 | 来源合集 |
| --- | --- | --- |
| **Stephen**（默认） | Stephen樽 | 爱弥斯·演唱会捏捏动态表情包（大寸）等捏捏表情包 |
| **鸭牌** | 春也Huruya | 爱弥斯动态表情包（鸭牌） |
| **雾雪** | 雾雪 | 爱弥斯动态表情包（雾雪）、日服生日会、围巾冬装、慵懒情侣衫、家居服、古风 |

每套预设给 16 种交互配好了 16 张互不相同的表情；在 **设置 → 桌面与声音 → 表情预设** 切换，三套预设共用同一组语音。

![桌面与声音：表情预设下拉框](desktop/docs/images/preset-switch.png)

## 更多表情包：从呜哇小站导入

1. **设置 → 交互工作室 → GIF 素材**，点 **前往下载**，在 [呜哇小站](https://emoji.wuwa.games/archives?character=爱弥斯) 打开喜欢的合集，点 **打包下载全部**。
2. 点 **导入下载好的压缩包…**（可以一次选多个），或者直接把压缩包拖进设置窗口。
3. 导入的表情按 **画师 → 合集** 分组；点缩略图即可绑定到当前动作，合集可以删除。

| 还没导入时 | 导入之后 |
| --- | --- |
| ![还没导入时：前往下载 / 导入下载好的压缩包](desktop/docs/images/studio-download-hint.png) | ![导入后按画师和合集分组](desktop/docs/images/studio-imported.png) |

静态图和不是爱弥斯的图片默认跳过；和预设相同、或已经导入过的图片不会重复复制。导入的表情包保存在插件数据目录里，更新、卸载插件都不会删除。插件和桌宠不附带、也不会自动下载站内的表情包；表情包版权归各画师，转载或二次分发请先联系站长和画师。

## 陪伴、提醒与更新

- 任务进行时，表情依次切换为思考、查阅、编辑、执行、等你回应；结束时显示完成、出错或暂停。台词一旦开始就会说完。
- 底部余额框显示账户余额，点击刷新；任务完成时飘出本轮花费和用时，并撒彩色纸屑。
- 贴边藏起、全屏隐藏、每日小结、喝水和久坐提醒、点击穿透的顶部小锁。
- 桌宠内一键更新：只更新程序文件，保留表情、语音、导入的表情包和全部设置；更新清单由发布者离线密钥签名（Ed25519），签名不对就不会安装。

## 适用范围与说明

- 面向 **Windows 10/11 x64 本机 DeepSeek Harness**；普通 DeepSeek 聊天网页、macOS、Linux 和远程服务器不在支持范围。
- 插件读取了哪些数据、下载和运行了什么，见 [数据与运行说明](docs/SECURITY.md)；本版的测试范围见 [验证记录](docs/VALIDATION.md)。
- 首次下载完整程序后校验固定的 SHA-256；npm 包只有连接、下载和启动入口，约 0.3 MB。

## 素材来源与致谢

表情包来自 [呜哇小站](https://emoji.wuwa.games/) 收录的画师作品：**鸭牌** —— 春也Huruya；**雾雪** —— 雾雪；**Stephen** —— Stephen樽。感谢各位画师，也感谢呜哇小站整理收录。桌宠的 设置 → 版本与更新 → **关于与致谢** 里列出每套预设用到的合集，以及你导入的表情包的画师。

角色语音来自《鸣潮》爱弥斯的角色语音。角色、表情包图片与原版语音的权利归各自权利人所有（《鸣潮》© 库洛游戏）。本项目为个人制作的同人作品，与库洛游戏和呜哇小站无关；表情包仅供个人、非商业使用，请勿倒卖或用于付费分发。

程序代码采用 [MIT](LICENSE)；角色、表情包、语音与字体遵循各自的许可，详见 [素材说明](CREDITS.txt) 和 [第三方说明](desktop/THIRD_PARTY.txt)。

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

## 开发与验证

完整环境、源码提交记录、打包产物及发布校验见 [构建说明](docs/BUILD.md)。

```powershell
npm test
python -m pip install -r desktop/tools/requirements-build.txt
cd desktop
python -m unittest discover -s tests
cd ..
python desktop/tools/build_portable.py
python tools/package-runtime.py
npm pack
```

`desktop/` 是完整版源代码和默认素材；`lib/` 是 Harness 连接与启动入口。上游版本记录在 [UPSTREAM.json](desktop/UPSTREAM.json)。构建出的程序和 ZIP 不提交到 Git，发布为 Release 附件。
