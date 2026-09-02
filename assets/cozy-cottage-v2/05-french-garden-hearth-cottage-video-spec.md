# 法式花园围炉小屋视频制作脚本

## 1. 成片规格

- 主视觉：`./05-french-garden-hearth-cottage.jpeg`
- 时长：12.0 秒
- 画幅：9:16，1080×1920，30 fps
- 输出：H.264 MP4，建议码率 12–20 Mbps
- 镜头：全程单镜头、固定机位
- 字幕、Logo、UI：无
- 音频：只保留窗外雨声；不包含音乐、猫叫、风声、脚步声、炉火声或室内环境声
- 情绪目标：窗外寒冷凌冽，室内柔软明亮；通过绝对稳定的室内与持续拍窗的雨夹雪形成安全感

## 2. 强制前处理

源图左下方沙发上存在一只橘猫，但本片明确不需要猫咪。进入视频生成前必须完成以下处理：

1. 使用局部修复移除沙发上的橘猫。
2. 根据周围材质重建象牙白沙发坐垫、粉色毯子及其自然褶皱。
3. 修复区域不得出现猫影、毛发、凹陷轮廓、重复抱枕或纹理接缝。
4. 建议输出干净底图：`./05-french-garden-hearth-cottage-clean.jpeg`。
5. 视频模型只能使用干净底图，不得直接使用含猫原图。
6. 除移除猫咪外，不得改动窗户、楼梯、壁炉、烟道、床、厨房、厕所、吉他、家具和装饰。

## 3. 9:16 适配

- 原图为 3:4，禁止通过左右裁切适配 9:16，否则会破坏山墙窗与楼梯。
- 将画布静态扩展到约 1536×2731，再缩放至 1080×1920。
- 优先向顶部补充坡屋顶与木梁，向底部补充地毯和木地板。
- 正式时间轴开始后，构图、裁切和缩放必须逐帧保持不变。

## 4. 绝对静态镜头规则

- 0.0–12.0 秒相机位置、焦距、透视、旋转和景深完全锁定。
- 缩放始终为 100%，X/Y 位置始终不变。
- 禁止推近、拉远、平移、摇摄、旋转、环绕、漂移、视差和手持抖动。
- 禁止呼吸式缩放、自动重构图、焦点拉动和景深变化。
- 房屋结构、窗框、楼梯、栏杆、壁炉、烟道、床、沙发、餐桌、厨房、厕所和吉他必须逐帧稳定。
- 窗帘、花卉、植物、毯子和所有室内装饰保持静止，强调门窗完全密闭。
- 不得新增人物、动物、家具、房门、窗户、火炉或其他物体。

## 5. 室外天气

- 视觉天气采用寒冷的雨夹雪：保留原图的大雪，同时增加玻璃外侧的冻雨与水痕。
- 所有天气必须严格限制在窗框外部及玻璃外表面，室内不得出现雨滴或雪片。
- 使用三层天气：
  - 近景：较大的高速斜向雨雪颗粒，从左上向右下掠过。
  - 中景：密集、紊乱的雪粒与冻雨，形成明显风向。
  - 远景：雪林轮廓被灰白色雨雪雾间歇遮挡。
- 玻璃外侧增加大小不同的水滴、缓慢下滑的水痕、边缘冰晶与薄霜。
- 不使用闪电、雷击、玻璃震动、玻璃破裂或室内漏雨。

## 6. 室内动态

- 室内原则上保持静止。
- 仅允许壁炉内部火焰做非常轻微、真实的自然变化，亮度波动不超过 2%。
- 壁炉火光不得造成全屋明显闪烁，不得改变墙面和家具颜色。
- 吉他保持静止，不得漂移、倾倒或变形。
- 吊灯、窗帘、床品、抱枕、鲜花和植物均不得运动。

## 7. 12 秒时间轴

### 0.0–2.0 秒

- 第一帧直接呈现完整空间，不使用黑场或标题卡。
- 相机与全部室内元素完全静止。
- 窗外保持中强度雨夹雪，玻璃上已有细小水珠。

### 2.0–5.0 秒

- 近景斜向雨雪略微加密。
- 一条细水痕从左侧山墙窗上方缓慢向下滑动。
- 室内保持稳定，壁炉火焰只做极轻变化。

### 5.0–8.5 秒

- 窗外出现全片最强的一阵雨夹雪，远处松树短暂被雪雾遮挡。
- 玻璃表面新增两至三条速度不同的水痕。
- 不得让窗户整体变白，仍需保留树木轮廓和空间纵深。

### 8.5–10.5 秒

- 雨雪强度缓慢回落至中强度。
- 水痕继续下滑，已有水珠轻微汇聚。
- 室内灯光、家具和构图完全不变。

### 10.5–12.0 秒

- 天气状态逐渐接近首帧，方便循环播放。
- 最后 0.3 秒保持稳定，不淡黑、不移动画面。

## 8. 音频规范

- 全片只允许一条持续的窗外雨声轨道。
- 声音应为室内听到的雨水拍打大型双层玻璃，带轻微低通和距离感。
- 为匹配雪景，雨声可包含少量细碎冰粒敲击玻璃的质感，但主体仍是连续雨声。
- 禁止加入暴风、呼啸风声、雷声、猫叫、脚步、衣料摩擦、炉火噼啪、房间底噪、旁白和背景音乐。
- 0.0 秒做 0.1 秒防爆音淡入；11.8–12.0 秒做 0.2 秒淡出。
- 建议响度：综合约 -22 至 -20 LUFS，峰值不高于 -8 dBFS，为后期背景音乐保留空间。
- 采样率：48 kHz；若使用 AAC，建议 192–256 kbps。
- 雨声必须连续、无明显循环接缝，声像固定，不随画面变化左右漂移。

## 9. 可直接使用的视频生成提示词

```text
Create a 12-second vertical 9:16 photorealistic image-to-video shot using the supplied clean French garden winter
cottage image as an immutable first-frame and composition reference. The source must be the cat-removed clean plate.

ABSOLUTELY LOCK THE CAMERA for the entire 12 seconds. Keep camera position, lens, framing, perspective, crop, scale,
rotation and depth of field unchanged. No dolly, zoom, pan, tilt, orbit, drift, parallax, shake, focus pull, breathing
zoom or automatic reframing. Keep every interior pixel stable: pitched roof, beams, gable windows, staircase, railings,
upper bedroom, bed, fireplace, chimney, kitchen, bathroom, sofa, chairs, table, guitar, curtains, flowers and plants.

Animate only the weather outside the windows and the subtle flame inside the closed fireplace. Outside, create a
fierce cold sleet storm: fast diagonal foreground rain-and-snow particles, turbulent middle-distance flakes, distant
grey-white precipitation haze, snow-covered pine trees intermittently obscured, exterior ice crystals, droplets and
slow water trails sliding down the outside of the glass. Keep all precipitation strictly outdoors. Never animate the
window frames, curtains, plants or furniture. The fireplace flame may vary naturally by no more than two percent and
must not make the room flicker.

Timeline: 0.0-2.0s medium-heavy sleet; 2.0-5.0s slightly denser diagonal precipitation and one slow glass water trail;
5.0-8.5s the strongest gust with two or three additional water trails and partial distant whiteout; 8.5-10.5s weather
gradually settles; 10.5-12.0s returns close to the opening weather state for looping. Hold the final frame for 0.3s.

No cat, no animal, no people, no new objects, no indoor precipitation, no lightning, no structural deformation,
no texture flicker, no moving guitar, no moving fabrics and no transitions.
```

## 10. 音频生成提示词

```text
Generate a seamless 12-second stereo ambience recorded from inside a warm, tightly sealed cottage: steady rain
striking a large double-glazed window, softened by the glass and indoor distance, with occasional fine sleet grains
tapping the exterior surface. Stable intensity, no stereo movement, no obvious loop point. No wind howl, no thunder,
no fireplace crackle, no footsteps, no fabric sounds, no animal sounds, no voices and no music. Integrated loudness
around -21 LUFS, true peak below -8 dBFS, 48 kHz.
```

## 11. 输出验收

- 成片严格为 12.0 秒，允许误差不超过 0.1 秒。
- 全片构图逐帧一致，无任何相机运动。
- 画面中不存在猫咪或其他动物。
- 只有窗外天气、玻璃外侧水痕和极轻壁炉火焰发生运动。
- 室内不出现雨雪，窗帘与植物保持静止。
- 音频中只能听见隔着玻璃的雨声与少量冰粒声。
- 不得听见风声、雷声、炉火声、猫叫、脚步声、旁白或音乐。
- 输出 H.264 MP4，1080×1920，30 fps。
