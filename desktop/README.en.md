<!-- README language switch -->
[![中文](https://img.shields.io/badge/%E4%B8%AD%E6%96%87-555555?style=for-the-badge)](README.md) [![English](https://img.shields.io/badge/English-1677ff?style=for-the-badge)](README.en.md)
<!-- /README language switch -->

<div align="center">

# Aemeath DeepSeek Desktop Pet

**Aemeath from *Wuthering Waves* keeps you company in the official DeepSeek Harness desktop client: her expression follows your task, and she answers in her own voice.**

[Download for Windows](https://github.com/Doya16/aemeath-deepseek-pet/releases/latest) · [Usage guide (Chinese)](docs/USAGE.md) · [Issues](https://github.com/Doya16/aemeath-deepseek-pet/issues) · [中文](README.md)

![Three expression presets: 鸭牌, 雾雪 and Stephen, 16 interactions each](docs/images/events-presets.jpg)

</div>

Aemeath changes expression while a **DeepSeek Harness** task runs, answers with a voice line and a subtitle bubble when it finishes, and floats what the turn cost and how long it took. Below her, a box shows your account balance.

For **Windows 10/11 x64**. The full package ships **three expression presets (鸭牌, 雾雪, Stephen), 90 subtitled Aemeath voice lines** and two fonts and the Harness connection plugin. More Aemeath sticker packs can be downloaded from [呜哇小站](https://emoji.wuwa.games/archives?character=爱弥斯) and imported in one step. No Python needed.

## Demo

![All three presets at once: pat, double-click, milk tea, done confetti](https://raw.githubusercontent.com/Doya16/aemeath-deepseek-pet/main/docs/images/demo-presets.gif)

[Full demo video · 6:16 · 1920×1080](https://github.com/Doya16/aemeath-deepseek-pet/releases/download/v1.0.0/Aemeath-Promo-v1.0.0.mp4) (Chinese)

| Time | Shows |
| --- | --- |
| 0:00 | Opening |
| 0:08 | 01 Tasks: expressions follow the task (running, needs you / error / paused, several sessions) |
| 1:06 | 02 Interaction: hover, pat, double-click, right-click menu, drag |
| 1:40 | 03 Voice: 90 subtitled lines; bubbles and mute |
| 2:04 | 04 Presets: 鸭牌 / 雾雪 / Stephen, importing 呜哇小站 sticker zips |
| 3:01 | 05 Balance |
| 3:18 | 06 Companion: edge dock, full-screen hide, daily recap, lock and click-through |
| 4:13 | 07 Settings: rest reminder, one settings window, credits |
| 4:52 | 08 Install: GitHub full package, DSH plugin market (page live once listed), one-click update |
| 5:32 | 09 Codex edition: both editions side by side |
| 5:49 | Credits: artists, commissioners and crowdfunders, all 43 packs on 呜哇小站 with links and group numbers |

## Install

**Requirements**: Windows 10 (1809 or later) or Windows 11, 64-bit, with the official **DeepSeek Harness** desktop client installed, signed in and opened once.

1. Download **Aemeath-DeepSeek-Windows-v1.0.1.zip** from [Releases](https://github.com/Doya16/aemeath-deepseek-pet/releases/latest).
2. Extract it into its own folder (Explorer "Extract All", or 7-Zip "Extract to Aemeath-DeepSeek-Windows-v…\"). The zip has no top-level folder. Don't extract into `C:\Program Files`.
3. Double-click **一键部署.cmd** in the extracted folder. It checks the files, asks you to quit Harness from the tray and installs the Harness connection plugin `dsh-aemeath-pet` (type `S` to skip it for now), creates desktop and Start menu shortcuts and starts Aemeath.
4. Right-click the pet → **设置 (Settings)**: pick the session to follow under **连接 DeepSeek**, switch the expression preset under **桌面与声音**, change expressions and voice lines in **交互工作室**.

If SmartScreen shows "Windows protected your PC", click "More info" → "Run anyway": the program has no paid code-signing certificate. Every release lists SHA256SUMS. New versions are offered inside the pet: **更新并重启爱弥斯** updates and restarts, keeping your settings and material.

## Three expression presets

| Preset | Artist | Packs |
| --- | --- | --- |
| **Stephen** (default) | Stephen樽 | 爱弥斯·演唱会捏捏动态表情包（大寸） and other 捏捏 packs |
| **鸭牌** | 春也Huruya | 爱弥斯动态表情包（鸭牌） |
| **雾雪** | 雾雪 | 爱弥斯动态表情包（雾雪）, birthday, winter scarf, couple shirt, home wear and 古风 packs |

Each preset gives the 16 interactions 16 different stickers. Switch under **Settings → 桌面与声音 → 表情预设**; all presets share one set of voice lines, and an interaction you changed by hand keeps your choice.

## More sticker packs from 呜哇小站

1. **Settings → 交互工作室 → GIF 素材** → **前往下载** opens the site; on a pack's page click **打包下载全部**.
2. Click **导入下载好的压缩包…** (several at once), or drop the zips onto the settings window.
3. Imported stickers are grouped by **artist → pack**; click one to bind it to the selected interaction.

Images are recognised by content (artist, pack, clean name, e.g. `001-XXS01_喇叭.gif` becomes 喇叭); new packs take the zip name. Static images and other characters are skipped by default; copies of the presets or of earlier imports are not copied again. Imports live in `assets/imported/`, which updates never touch, and a pack can be deleted from the picker. The pet never bundles or downloads the site's stickers itself; the stickers belong to their artists, so ask the site owner and the artists before redistributing them.

| Before importing | After importing |
| --- | --- |
| ![Hint with the two steps](docs/images/studio-download-hint.png) | ![Grouped by artist and pack](docs/images/studio-imported.png) |

## Voice, tasks and desktop

- **90 Aemeath voice lines** with subtitles, matched to the 16 interactions. A line that has started is always said in full.
- Follows Harness tasks (thinking, reading, editing, running tools, waiting for you, done, error, paused); several sessions' completions queue up; the balance box refreshes on a click; the done float shows the turn's estimated cost and time.
- Done float and confetti, edge docking, full-screen hide, daily recap, drink-and-stretch reminder, click-through lock.
- The Windows volume mixer shows 「爱弥斯 · DeepSeek」.
- Signed one-click updates (Ed25519); source GitHub or a mirror for mainland China.

## Credits

Stickers: artists' work collected on [呜哇小站](https://emoji.wuwa.games/) — **鸭牌** by 春也Huruya, **雾雪** by 雾雪, **Stephen** by Stephen樽. Thank you to the artists and to the site. **Settings → 版本与更新 → 关于与致谢** lists every pack the presets use and the artists of the packs you imported.

### Every Aemeath pack on 呜哇小站

The group numbers, commission notes and author links written under each pack (also listed in the pet's 关于与致谢):

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

Voice lines are Aemeath's character voice from *Wuthering Waves*. Characters, sticker images and original voices belong to their respective owners (*Wuthering Waves* © Kuro Games). This is an unofficial fan project, not affiliated with Kuro Games or 呜哇小站. Stickers are for personal, non-commercial use only. See [assets/CREDITS.txt](assets/CREDITS.txt) and [THIRD_PARTY.txt](THIRD_PARTY.txt).

<details>
<summary>Run from source</summary>

Python 3.12:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m aemeath_pet
```

Portable build: `pip install -r tools/requirements-build.txt`, then `python tools/build_portable.py` (output in `dist/爱弥斯DeepSeek桌宠/`). Tests: `python -m unittest discover -s tests`.

</details>
