# 雪夜星穹图书馆 LOFT 视频制作脚本

## 1. 成片规格

- 主视觉：`./02-midnight-celestial-library-loft.jpeg`
- 时长：12.0 秒
- 画幅：9:16，1080×1920，30 fps
- 输出：H.264 MP4，建议码率 12–20 Mbps
- 镜头：全程单镜头、固定机位
- 字幕、Logo、UI：无
- 情绪目标：窗外暴雪凌冽，室内壁炉、书墙与软家具形成安静、可靠的庇护感
- 音频：只保留隔着玻璃的外部风雪与细碎冰粒声，不加入音乐、猫叫、炉火声或其他室内声音

## 2. 输入与画幅处理

- 使用主视觉作为第一帧和不可变的空间参考。
- 原图为 3:4，制作前生成式扩展至约 1536×2731，再缩放为 1080×1920。
- 优先向顶部补充天花板，向底部补充地毯和木地板。
- 禁止左右裁切，不得丢失左侧拱窗、右侧楼梯、书墙、壁炉、望远镜或二楼床铺。
- 正式时间轴开始后不得再次改变构图。
- 同目录的 `03`、`04`、`05` 风格图片可以替换为主视觉，其他规则保持不变。

## 3. 绝对固定机位

- 0.0–12.0 秒相机位置、焦距、透视、旋转、景深和裁切完全锁定。
- 缩放始终为 100%，X/Y 坐标逐帧保持一致。
- 禁止推近、拉远、平移、摇摄、旋转、环绕、漂移、视差和手持抖动。
- 禁止呼吸式缩放、自动重构图、焦点拉动和景深变化。
- 拱窗、书墙、楼梯、踏步、栏杆、楼板、壁炉、烟道、床、沙发、望远镜和装饰必须逐帧稳定。

## 4. 室外暴雪

- 暴雪严格位于玻璃外侧，室内不得出现任何雪粒。
- 使用三层天气制造纵深：
  - 近景：尺寸较大的高速斜向雪片，从左上向右下掠过。
  - 中景：密集、紊乱并带轻微旋涡的雪粒。
  - 远景：灰白雪雾间歇遮挡松树轮廓。
- 玻璃外侧保留冰晶、积雪边缘、细小水珠和缓慢下滑的融雪水痕。
- 允许窗外松枝受风轻微摆动。
- 窗框、窗帘、室内植物和书页保持静止，强调建筑完全密闭。
- 禁止闪电、雷击、玻璃震动、玻璃破裂、室内漏雪和突然全屏白障。

## 5. 室内动态

- 室内主体保持静止，只允许以下微动态：
  - 壁炉内部火焰轻微自然变化，亮度波动不超过 2%。
  - 沙发上的猫咪保持睡眠，仅有极轻呼吸、一次耳朵轻动和一次尾尖轻摆。
- 猫咪不得站起、奔跑、跳跃、叫喊或离开沙发。
- 猫咪外形、毛色、四肢和尾巴数量必须始终一致。
- 望远镜、书籍、窗帘、床品、地毯、灯具和家具完全静止。
- 不得出现书页翻动、窗帘飘动、植物摇摆、家具位移或灯光闪烁。

## 6. 12 秒时间轴

### 0.0–2.0 秒：建立空间

- 第一帧直接显示完整图书馆 LOFT。
- 相机与所有室内物体锁定。
- 猫咪安静睡眠，腹部随呼吸轻微起伏。
- 窗外保持中强度暴雪。

### 2.0–5.0 秒：雪势增强

- 近景斜向雪片略微加速。
- 左侧拱窗外的一根松枝轻微受风摆动。
- 一条细小融雪水痕从玻璃上方缓慢下滑。
- 猫咪右耳轻动一次。

### 5.0–8.5 秒：视觉高潮

- 暴雪达到全片最高强度，远景松树被雪雾短暂遮挡。
- 玻璃外侧新增两条速度不同的水痕，边缘冰晶保持稳定。
- 壁炉火焰轻微抬高后恢复，不影响全屋曝光。
- 室内其他像素保持稳定。

### 8.5–10.5 秒：缓慢回落

- 雪势从峰值回落至中强度。
- 猫咪尾尖轻摆一次，身体继续保持睡姿。
- 水痕继续向下滑动，窗外仍然寒冷。

### 10.5–12.0 秒：循环收束

- 天气状态逐渐接近首帧，便于循环播放。
- 最后 0.3 秒保持稳定，不淡黑、不移动画面。

## 7. 音频规范

- 全片只允许一条窗外风雪环境轨道。
- 听感位置必须在双层玻璃外部，带明显距离感和轻微低通。
- 主体为持续而克制的暴雪风声，并带少量冰粒敲击玻璃的细碎声音。
- 禁止猫叫、炉火噼啪、脚步、衣料摩擦、书页、钟表、房间底噪、旁白和背景音乐。
- 0.0 秒做 0.1 秒防爆音淡入；11.8–12.0 秒做 0.2 秒淡出。
- 建议综合响度：-22 至 -20 LUFS；峰值不高于 -8 dBFS，为后期音乐预留空间。
- 采样率 48 kHz；AAC 192–256 kbps。
- 声像固定，禁止随雪势变化左右漂移，不得出现明显循环接缝。

## 8. 可直接使用的视频生成提示词

```text
Create a 12-second vertical 9:16 photorealistic image-to-video shot using the supplied Midnight Celestial Library
Loft image as the immutable first-frame environment and composition reference.

ABSOLUTELY LOCK THE CAMERA for the entire shot. Keep camera position, lens, framing, perspective, crop, scale,
rotation and depth of field unchanged. No dolly, zoom, pan, tilt, orbit, drift, parallax, camera shake, focus pull,
breathing zoom or automatic reframing. Keep all architecture and interior objects pixel-stable: arched windows,
floors, walnut library, stairs, every tread, upper opening, railings, fireplace, chimney, bed, sofa, telescope,
books, curtains, rugs, lamps and decorations.

Animate only the weather outside the sealed windows, the subtle flame inside the closed fireplace, and tiny sleeping
motions from the single cat. Outside, create a fierce cold blizzard with fast diagonal foreground snow, turbulent
middle-distance flakes, distant grey-white snow haze, partially obscured snow-covered pines, exterior ice crystals,
small droplets and slow meltwater trails on the outside of the glass. Keep all snow strictly outdoors. Interior
curtains and plants remain completely still.

The cat stays asleep on the sofa for all 12 seconds. Show only subtle breathing, one small ear twitch around 3 seconds,
and one gentle tail-tip movement around 9 seconds. The cat never stands, runs, jumps, meows or changes position.
Maintain one anatomically consistent cat with four legs and one tail.

Timeline: 0.0-2.0s medium-heavy snow; 2.0-5.0s slightly stronger diagonal snow and one slow glass water trail;
5.0-8.5s strongest gust with distant partial whiteout and two additional water trails; 8.5-10.5s weather gradually
settles; 10.5-12.0s returns close to the opening state for looping. Hold the final frame for 0.3 seconds.

No people, no additional animals, no indoor snow, no lightning, no moving telescope, no moving books, no moving
fabrics, no object morphing, no structural deformation, no texture flicker, no text, no logo and no transitions.
```

## 9. 音频生成提示词

```text
Generate a seamless 12-second stereo ambience recorded from inside a tightly sealed winter loft. The only audible
source is a fierce blizzard outside double-glazed windows: muffled steady wind with occasional fine ice grains and
soft snow particles striking the exterior glass. Stable distant perspective, gentle low-pass filtering, no stereo
movement and no obvious loop point. No cat sound, no fireplace crackle, no footsteps, no fabric sounds, no book sounds,
no voices, no room tone and no music. Integrated loudness around -21 LUFS, true peak below -8 dBFS, 48 kHz.
```

## 10. 输出验收

- 时长严格为 12.0 秒，误差不超过 0.1 秒。
- 第一帧和最后一帧构图位置一致。
- 全片没有任何相机运动或自动重构图。
- 楼梯、书墙、栏杆、壁炉、床和望远镜无形变、位移或闪烁。
- 猫咪始终睡在原位，只发生三种细微动作。
- 所有暴雪与水痕严格位于窗外或玻璃外侧。
- 音频仅包含隔窗风雪和少量冰粒声。
- 输出 H.264 MP4，1080×1920，30 fps。
