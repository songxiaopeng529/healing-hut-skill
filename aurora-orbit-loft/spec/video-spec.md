# 极光环庭 LOFT 视频制作脚本

## 1. 成片规格

- 默认主视觉：`../images/01-aurora-orbit-loft-preview.jpeg`
- 时长：12.0 秒
- 画幅：9:16，1080×1920，30 fps
- 镜头：单镜头，全程固定
- 字幕、Logo、UI：无
- 原片音频：静音，环境声和音乐留待后期
- 情绪：极寒世界之外，室内安静、柔软、稳定

## 2. 9:16 适配

- 原图为 1536×2048（3:4）。先等比缩放为 1080×1440，禁止使用 `cover`、中心裁切或自动放大。
- 将 1080×1440 的完整原图放在 1080×1920 画布中央，只向顶部扩展 240px、向底部扩展 240px。
- 原图覆盖的中央 1080×1440 区域必须逐像素保留，不允许生成式改写、缩放、裁边或横向重构。
- 顶部 240px 只补充流线天花与灯带；底部 240px 只补充下沉会客岛、地毯和地板。
- 原图左右边界必须完整保留，二楼整张床、中央承重核心、完整弧形楼梯、一楼会客岛和右侧窗框必须同时可见。
- 禁止把画面重新居中到窗户、楼梯或承重核心，禁止把室内缩窄成狭长构图。
- 9:16 适配必须在进入时间轴前一次完成。

## 3. 绝对固定镜头

- 0.0–12.0 秒相机位置、焦距、透视、裁切、旋转和景深完全不变。
- 缩放始终为 100%，X/Y 坐标逐帧锁定。
- 禁止推拉、平移、摇摄、旋转、环绕、漂移、视差和手持抖动。
- 禁止呼吸式缩放、自动重构图、景深变化和焦点拉动。
- 中央承重核心、弧形楼梯、每一级踏步、二楼楼板、护栏、床、沙发、茶几、灯具、猫和装饰逐帧稳定。
- 室内窗帘和植物不得随外部风雪摆动，强调玻璃幕墙完全密闭。
- 二楼床必须在所有帧中完整可见，不得被画面边缘、承重核心或自动裁切遮挡。
- 一楼会客岛不得移出画面；房屋主体宽度不得在时间轴中收缩。

## 4. 动态范围

动态只发生在右侧玻璃之外以及玻璃外表面：

1. 极光：缓慢流动、伸展和轻微亮度变化。
2. 窗外中景雪：细小至中等尺寸的斜向雪粒，提供清晰风向。
3. 窗外远景雪：稀疏、缓慢，不形成白色雾墙。
4. 远景空气：仅有极轻薄冷雾，冰湖、白桦林和远山始终可辨认。
5. 白桦枝：受风缓慢摆动，不出现剧烈折断。
6. 冰湖：仅保留极轻微的冷色反光变化，不生成液态大浪。
7. 玻璃：只保留贴附在玻璃外表面的微小水珠，以及少量长度不超过单块玻璃高度 15% 的短水痕。

禁止室内飘雪、窗框变形、玻璃震动、闪电和极光照亮整个室内。

### 暴雪强度与曝光上限

- 禁止使用“白障”“白化”“纯白雪幕”“全画面雪雾”或任何覆盖整个画面的天气层。
- 禁止大尺寸近景雪片、镜头前雪花、全屏粒子层和全屏半透明白色蒙版。
- 所有雪粒必须位于每块玻璃窗格的独立蒙版内部，并处于玻璃平面之后。
- 在 1080p 画面中，雪粒直径以 2–8px 为主，不得出现占画面明显面积的巨大雪片。
- 常态雪粒覆盖率控制在窗区的 10%–18%；高潮段最多提高到 20%–25%。
- 雪雾不透明度不得超过 12%；任何时刻至少 65% 的窗区仍能辨认白桦树、冰湖、山体或极光。
- 窗区平均亮度相对首帧提升不得超过 10%；室内平均亮度、对比度和白平衡必须保持不变。
- 禁止自动曝光拉升、全画面泛白、Bloom 扩散、柔焦、雾化和对比度下降。

### 玻璃雨雪遮罩规则

- 必须为每一块玻璃窗格单独建立封闭蒙版，天气层不得使用全画面透明叠加。
- 窗外降雪层位于玻璃与远景之后；玻璃水珠层只位于玻璃表面；窗框、竖梃、横梃和窗台必须覆盖在所有天气层之上。
- 所有水珠和水痕必须被窗格边界硬裁切，不能跨越窗框或跨到相邻窗格。
- 水痕必须在窗台内缘之前自然消失，绝不能越过窗台延伸到地面、沙发、楼梯、栏杆、承重核心或室内空气中。
- 禁止镜头水滴、摄影机镜片上的水、前景悬空水滴、超大水滴和贯穿整幅画面的长水线。
- 水珠尺寸保持细小，最多只出现 1–2 条短水痕；主要动态应由窗外暴雪和极光承担。

## 5. 极光运动原则

- 极光位于远景天空，不能覆盖白桦树、窗框或室内。
- 采用两层半透明光幕：
  - 主光幕：绿色偏金，缓慢从右向左漂移。
  - 次光幕：淡青色，轻微上下起伏。
- 极光运动应像缓慢展开的丝绸，不像闪烁霓虹灯。
- 亮度变化控制在 8% 以内，避免跳变、频闪和过曝。
- 12 秒末尾的形态应接近开头，以便循环。

## 6. 12 秒时间轴

### 0.0–2.0 秒：建立空间

- 第一帧直接出现完整房间，无黑场和标题。
- 室内完全静止。
- 窗外保持中强度斜向降雪。
- 绿色极光位于右上方，缓慢舒展。

### 2.0–5.0 秒：极光展开

- 主极光向左侧缓慢延伸约 5%–8%。
- 淡青色次光幕轻轻向上浮动。
- 近景雪片略微增加，白桦枝向左摆动一次。
- 一条细小融雪水痕在右侧某一块玻璃的上半部短距离下滑，不超过该窗格高度的 15%，并在窗格内部消失。

### 5.0–8.0 秒：暴雪微高潮

- 一阵横向强风使窗格内部的中景雪粒密度增加约 10%–15%。
- 远山和白桦林仍然清晰可辨，只允许局部、低透明度的薄雪雾掠过。
- 主极光亮度轻微提升，不超过初始亮度的 8%。
- 玻璃外侧只新增少量细小水珠，不新增贯穿窗格的长水痕。

### 8.0–10.5 秒：天气回落

- 雪雾逐渐散开，重新露出冰湖和远山轮廓。
- 白桦枝缓慢回弹。
- 极光光幕收窄，向初始位置回移。
- 细小水珠保持附着或在各自窗格内部短距离移动，任何水迹都不能接近或越过窗台。

### 10.5–12.0 秒：循环收束

- 风雪恢复至片头中强度。
- 极光形态接近首帧。
- 最后 0.3 秒保持稳定，不淡黑、不移动镜头。

## 7. 室内稳定性

- 不允许灯光呼吸、色温变化或家具阴影漂移。
- 猫咪保持睡姿，不抬头、不跑动、不眨眼，避免触发室内大范围重绘。
- 床品、抱枕、地毯和窗帘不发生形变。
- 楼梯、护栏和中央核心不得融化、断裂或改变曲率。
- 不得新增人物、动物、家具、门窗或光源。

## 8. 音频

- 默认输出无音轨或全程静音 AAC。
- 不生成风声、雪声、猫叫、脚步、室内底噪、旁白或音乐。
- 后期若需要，可单独添加隔着双层玻璃的低频风雪声与背景音乐。

## 9. 可直接使用的视频提示词

```text
Create a 12-second vertical 9:16 photorealistic image-to-video shot using the supplied Aurora Orbit Loft image as an
immutable first-frame and composition reference.

Before animation, fit the complete 3:4 source image into the 9:16 canvas without cropping: scale the full source to
1080x1440, place it centered on a 1080x1920 canvas, and outpaint only 240 pixels above and 240 pixels below. Preserve
every source pixel inside the central 1080x1440 area. Do not use cover mode, center crop, auto zoom or horizontal
reframing. The full upper bed, central core, complete staircase, lower lounge and right window must remain visible.

ABSOLUTELY LOCK THE CAMERA for the entire shot. Keep camera position, lens, crop, scale, perspective, rotation and
depth of field unchanged. No dolly, zoom, pan, tilt, orbit, drift, parallax, camera shake, breathing zoom, reframing
or focus pull. Keep every interior element pixel-stable: central structural core, curved staircase, every tread,
crescent upper slab, columns, guards, upper bed, sunken lounge, sofa, chairs, table, lights, curtains, plants, decor
and sleeping cat.

Animate only the winter landscape outside the right glass wall and the exterior surface of the glass. Use small and
medium wind-driven snow particles located behind the glass, primarily 2-8 pixels in diameter at 1080p. Normal snow
coverage is 10-18 percent of the window area and the peak is limited to 20-25 percent. Add only a very thin distant
snow haze below 12 percent opacity. At every frame, at least 65 percent of the window must clearly reveal recognizable
birch trunks, frozen lake, mountains or aurora. Let the birch branches sway slowly. Keep the frozen lake solid, with
only subtle cold reflections.

Never create a whiteout, white wall of snow, full-screen snow layer, foreground snow in front of the camera, giant
flakes, full-frame fog, white translucent overlay, exposure ramp, bloom, soft-focus veil or contrast washout. Weather
must not brighten the window area by more than ten percent relative to the first frame and must never alter interior
exposure, color, contrast or visibility.

Animate a distant green-gold aurora as two translucent silk-like light curtains. The main curtain drifts slowly from
right to left while a faint cyan secondary curtain rises gently. Aurora brightness changes by no more than eight
percent and never illuminates or recolors the interior.

Treat every visible glass pane as a sealed planar surface with its own exact hard-edged mask. Place all snow behind
the glass plane. Place only tiny adhered droplets and at most one or two short meltwater traces on the exterior glass
surface. Each droplet layer must be clipped inside its individual pane and occluded by the window frame, mullions and
sill. Every trace must remain inside the pane, travel no more than fifteen percent of that pane's height, and disappear
before reaching the sill. No droplet or water trace may cross a mullion, cross the bottom sill, overlap the floor,
sofa, furniture, staircase, railing, structural core or interior air. All snow and moisture remain strictly outdoors.

Do not create rain or water on the camera lens. No lens droplets, no full-frame wet-glass overlay, no giant foreground
droplets, no suspended three-dimensional water drops and no long vertical water streams across the image.

Timeline: 0.0-2.0s moderate transparent snow and slow aurora; 2.0-5.0s aurora gently expands and one short glass trail
begins; 5.0-8.0s snow density rises by only 10-15 percent while trees, lake, mountains and aurora remain clearly
visible; 8.0-10.5s snow eases; 10.5-12.0s aurora and snowfall return close to their opening state for a seamless loop.
Hold the final frame for 0.3s.

No indoor motion, no moving cat, no moving curtains, no flicker, no morphing, no lightning, no indoor snow, no new
objects, no people, no text, no transitions and absolutely no audio. Never crop out the upper bed or narrow the house.
```

## 10. 输出验收

- 时长严格为 12.0 秒，允许误差不超过 0.1 秒。
- 第一帧与最后一帧的相机和室内构图一致。
- 原始 3:4 画面左右内容全部保留，二楼床、完整楼梯与一楼会客岛始终可见。
- 不存在自动裁切、自动放大、画面横向收窄或主体偏移。
- 动态严格限制在窗外和玻璃外侧。
- 所有玻璃水珠均被单独窗格蒙版裁切，没有任何水迹越过窗框或窗台。
- 画面中不存在镜头水滴、全画面湿玻璃层或室内悬空水滴。
- 极光运动缓慢连续，无闪烁或霓虹跳变。
- 暴雪保持透明层次，高潮段仍能辨认至少 65% 的窗外景物。
- 全片不存在白障、全屏白雾、曝光拉升或大雪覆盖室内的效果。
- 室内没有结构形变、纹理闪烁或新增物体。
- 输出 H.264 MP4，1080×1920，30 fps，建议码率 12–20 Mbps。
