# 模板文件（以《汉隆剃刀》为例）

| 文件 | 作用 |
|---|---|
| lines.py | 旁白脚本：(id, 场景号, 字幕文本, 朗读文本或None, 语速) |
| tts.py | 用 sherpa-onnx Kokoro 合成每句旁白，输出 sent/*.wav 和 durs.json |
| scene.py | 主角女孩/男生、窗户、星星等手绘元件，以及主色 ACC |
| helpers.py | 字幕换行与自动字号、对话气泡、doodle 小人头、火车窗场景 |
| gen.py | 按 TTS 时长生成时间轴，拼出每个场景的 SVG，输出 hr.html |
| head.part / tail.part | 页面外壳与动画引擎（场景切换、data-at 动画、线条抖动、自定义 data-anim） |
| audio.py | 合成配乐与音效、按人声压低音乐、响度标准化，输出 mix.wav / mix.mp3 |
| build.py | 生成渲染用 render.html 和带音频的网页版 *_web.html |
| snap.py | 按时间点截图，用于抽帧检查 |
| render3.py | 按帧区间截图并编码成 mp4（4 个进程并行，再 concat 拼接） |

新做一集：复制整个文件夹，改 lines.py、gen.py 里的场景，改 scene.py 的 ACC 和 head.part 里的主色，替换各脚本中的文件名（hr.html → 新名字）。
运行顺序：tts.py → gen.py → build.py → snap.py 检查 → audio.py → build.py → render3.py ×4 → ffmpeg 拼接并合入 mix.wav。
依赖：Python 3、numpy、soundfile、playwright（Chromium）、ffmpeg、sherpa-onnx 及 Kokoro 模型（路径在 tts.py 里，需要自行下载）。
