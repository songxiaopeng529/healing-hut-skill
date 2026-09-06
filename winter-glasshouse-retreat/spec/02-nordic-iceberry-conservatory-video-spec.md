# 北欧冰莓温室视频制作脚本

## 1. 成片规格

- 主视觉：`../images/02-nordic-iceberry-conservatory.jpeg`
- 时长：12.0 秒
- 画幅：9:16，1080 x 1920，30 fps
- 镜头：单镜头，全程固定
- 输出：H.264 MP4，建议码率 12-20 Mbps
- 字幕、Logo、UI：无
- 原片音频：静音，音乐和环境声留待后期
- 情绪：玻璃外清冷飘雪，室内明亮、柔软、安静且有安全感

## 2. 9:16 适配

- 原图为 1536 x 2048（3:4），先等比缩放至 1080 x 1440。
- 将完整原图置于 1080 x 1920 画布中央，只向顶部和底部各静态扩展 240 px。
- 中央 1080 x 1440 原图区域必须完整保留，不得使用 `cover`、中心裁切、自动放大或横向重构。
- 顶部扩展区延续现有弧形玻璃顶、承重肋和天空；底部扩展区延续下沉客厅边缘与浅色地板。
- 扩图完成后先导出静态 9:16 底图，再进入视频生成，时间轴内不得继续扩图。
- 床、中央树池、完整下沉客厅、猫、吉他、后墙茶饮区和右侧玻璃墙必须始终完整可见。

## 3. 固定镜头硬约束

- 0.0-12.0 秒相机位置、焦距、透视、裁切、缩放、旋转和景深完全不变。
- 禁止推近、拉远、平移、摇摄、旋转、环绕、漂移、视差、手持抖动和焦点拉动。
- 禁止呼吸式缩放、自动重新构图、数字防抖位移和画面横向收窄。
- 弧形玻璃顶、每根结构肋、窗框、窗台、墙体、门洞、树池、下沉边界和台阶必须逐帧对齐。
- 床、茶饮柜、沙发、脚凳、茶几、地毯、画框、吊灯和吉他不得移动、变形或闪烁。
- 室内曝光、白平衡和色彩保持恒定，不随窗外天气明暗变化。

## 4. 允许的动态

### 窗外

- 细小雪粒在玻璃外缓慢斜向飘落，方向为左上至右下。
- 远处白桦细枝做幅度很小、节奏缓慢的风摆。
- 雪地保留极轻微的冷色反光变化，但地形和树木不得变形。
- 天空中的淡粉晨光保持稳定，只允许云层以几乎不可察觉的速度移动。

### 室内

- 橘猫始终蜷卧在右侧沙发原位，眼睛闭合。
- 仅允许腹部有非常轻微、缓慢的呼吸起伏；6.0-6.5 秒可轻动一次右耳。
- 猫的头部、四肢、尾巴、花纹和轮廓不得发生位移或重绘。
- 橄榄树、盆栽、织物、吊灯和所有其他室内物体完全静止，以表现温室密闭。

## 5. 玻璃与雪的分层

- 为每块可见玻璃单独建立硬边蒙版，包括顶部弧形玻璃和右侧立面玻璃。
- 雪粒必须位于玻璃平面之后，只能出现在各窗格内部。
- 窗框、承重肋、横向檩条、实体窗台和室内墙体必须覆盖在雪层上方。
- 雪粒不得越过窗框进入室内，也不得覆盖橄榄树、床、沙发、猫或地板。
- 不添加镜头雪花、镜头水滴、室内悬浮颗粒、玻璃水流或全画面天气滤镜。
- 1080p 下雪粒以 2-6 px 为主；常态覆盖窗区 5%-10%，最高不超过 15%。
- 任意时刻至少 75% 的窗外白桦、雪地和远山保持清晰可辨。
- 禁止白障、全屏泛白、大片近景雪花、雾墙、Bloom、曝光拉升和对比度降低。

## 6. 12 秒时间轴

### 0.0-2.0 秒：建立安静空间

- 第一帧直接显示完整房间，不使用黑场、转场或标题。
- 相机与室内完全稳定。
- 窗外保持稀疏细雪，远处白桦近乎静止。
- 猫保持熟睡，只呈现几乎不可见的呼吸。

### 2.0-5.0 秒：柔和风雪

- 细雪密度缓慢提升至窗区约 8%-10%。
- 右侧远景白桦枝向右轻摆一次，位移幅度不超过枝条长度的 2%。
- 天空薄云极缓慢横移，室内亮度不发生变化。

### 5.0-8.0 秒：短暂微风

- 一阵轻风让雪粒速度略微增加，峰值覆盖率不超过窗区 15%。
- 白桦细枝缓慢回摆，不出现剧烈摇晃或折断。
- 6.0-6.5 秒猫咪右耳轻动一次，随后恢复原位；身体继续平稳呼吸。
- 所有室内家具、织物、植物和灯具保持像静态照片一样稳定。

### 8.0-10.5 秒：雪势回落

- 雪粒逐渐恢复稀疏状态。
- 白桦枝缓慢回到片头位置。
- 猫保持完全放松，不抬头、不睁眼、不移动身体。

### 10.5-12.0 秒：循环收束

- 降雪密度、枝条位置和猫的呼吸状态接近首帧。
- 最后 0.3 秒保持稳定，不淡黑、不移动镜头。

## 7. 音频

- 默认输出无音轨或全程静音 AAC。
- 不生成风声、雪声、猫叫、呼吸声、脚步、室内底噪、旁白或音乐。
- 后期可单独添加轻柔音乐；如需环境声，仅使用极低音量、隔着双层玻璃的远距离冬风。

## 8. 可直接使用的视频提示词

```text
Create a 12-second vertical 9:16 photorealistic image-to-video shot using the supplied Nordic Ice-Berry
Conservatory image as an immutable first-frame and composition reference.

Before animation, fit the complete 3:4 source image into the 9:16 canvas without cropping. Scale the full source to
1080x1440 and place it in the center of a 1080x1920 canvas. Outpaint only 240 pixels above and 240 pixels below.
Continue the existing curved glass roof and sky above, and the pale floor and sunken-lounge edge below. Preserve the
entire central 1080x1440 source area. Do not use cover mode, center crop, auto zoom or horizontal reframing. Keep the
complete bed, central olive-tree planter, sunken lounge, sleeping cat, guitar, rear tea counter and right glass wall
visible in every frame. Finish this static outpaint before animation begins.

ABSOLUTELY LOCK THE CAMERA for the entire shot. Keep camera position, lens, framing, crop, scale, perspective,
rotation and depth of field unchanged. No dolly, zoom, pan, tilt, orbit, drift, parallax, camera shake, stabilization
movement, focus pull, breathing zoom or automatic reframing. Keep the curved glass roof, every structural rib and
mullion, masonry sill, walls, doorway, central planter, olive tree trunk, sunken-lounge boundary, entry step, bed,
tea cabinetry, sofa, poufs, table, rugs, frames, pendant lights and guitar pixel-stable.

Animate only fine snowfall outside the sealed glasshouse, minimal distant birch-branch movement and extremely subtle
breathing from the sleeping orange tabby. Snow moves slowly from upper left to lower right behind the glass. Use
small 2-6 pixel flakes at 1080p. Normal snow coverage is 5-10 percent of the visible glazing and the brief peak is
limited to 15 percent. At least 75 percent of the outdoor birch trees, snowfield and hills must remain recognizable
at all times. Let only the thinnest distant birch branches sway slowly by no more than two percent of their length.
Allow an almost imperceptible cloud drift in the pale pink sky, without changing interior exposure or color.

Treat every roof and wall glass pane as a separate sealed plane with an exact hard-edged mask. Place all snow behind
the glass plane. Keep structural ribs, mullions, cross-purlins and masonry sills in front of every weather layer.
No flake may cross a frame, enter the room or overlap the olive tree, bed, furniture, cat or floor. Do not add water
trails, lens droplets, foreground snow, indoor particles or a full-frame weather overlay.

Keep the orange tabby curled in exactly the same position with closed eyes. Allow only a tiny slow breathing motion
in the abdomen and one minimal right-ear twitch between 6.0 and 6.5 seconds. Do not move or redraw its head, paws,
tail, fur markings or silhouette. Keep every indoor plant, olive leaf, textile and pendant completely still to show
that the glasshouse is tightly sealed.

Timeline: 0.0-2.0s sparse fine snow and a completely stable room; 2.0-5.0s snow slowly increases to 8-10 percent and
distant birch twigs gently lean once; 5.0-8.0s a mild gust raises snow coverage to no more than 15 percent while the
cat makes one tiny ear twitch; 8.0-10.5s snow eases and branches return; 10.5-12.0s all animated states approach the
opening frame for a seamless loop. Hold the final frame for 0.3 seconds.

Never create a whiteout, snow wall, giant flakes, full-screen fog, white translucent overlay, exposure ramp, bloom,
contrast washout, indoor snow, moving curtains, moving olive leaves, lighting flicker, structural deformation,
melting furniture, duplicated objects, new people, new animals, text, transitions or camera motion. Absolutely no
audio.
```

## 9. 负面提示词

```text
camera movement, dolly, zoom, pan, tilt, orbit, handheld shake, parallax, focus pull, breathing zoom, reframing,
cropping, narrow room, missing bed, missing lounge, whiteout, full-screen snow, foreground snow, giant snowflakes,
indoor snow, lens droplets, water streaks, fog wall, exposure flicker, bloom, moving furniture, moving plants,
moving pendant lights, fabric motion, cat walking, cat waking, cat morphing, extra limbs, structural deformation,
warped glass ribs, duplicated objects, new doors, people, text, logo, watermark, audio
```

## 10. 输出验收

- 时长为 12.0 秒，误差不超过 0.1 秒。
- 输出为 1080 x 1920、30 fps、H.264 MP4。
- 原图左右内容完整保留，床、树池、下沉客厅、猫和吉他全程可见。
- 第一帧与最后一帧构图一致，不存在推拉摇移、裁切变化或画面缩窄。
- 所有结构线条逐帧稳定，无窗框弯曲、家具融化或纹理闪烁。
- 雪只出现在独立窗格内且位于玻璃后方，不跨越窗框或进入室内。
- 高峰期仍可辨认至少 75% 的窗外景物，不出现全屏泛白。
- 猫仅有轻微呼吸和一次耳动，不起身、不睁眼、不改变轮廓。
- 全片无字幕、Logo、水印、人物、新增物体和音频。
