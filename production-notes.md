# 都市雨夜 LOFT｜参考蒸馏与 12 秒制作脚本

## 1. 参考视频的真正配方

- 原片约 **7.0 秒**，源画面约 **2160×3240（2:3 竖图）**，不是多镜头叙事，而是“一张超精细主图 + 局部动态 + 极慢推镜”。
- 核心构图是高机位、近似正面的 **多层复式剖面 / 娃娃屋视角**。楼板、楼梯、门洞构成稳定网格；家具负责提供尺度和生活感。
- 室内为暖色灯池，窗外是蓝灰雨夜。治愈感来自“外面天气很坏，里面绝对安全”的冷暖反差，而不是把全屋统一调成橙黄色。
- 真正明显的动态集中在窗区：远处雨幕、玻璃雨痕、城市雾气和反光。室内结构与家具几乎不动。
- 镜头只做极慢推近。原片可理解为约 3%–6% 的数字推镜；若拉长到 12 秒，可控制在 6%–9%，并叠加不超过 1.5% 的微漂移。
- 音频至少两层：无歌词的温柔氛围音乐 + 持续雨声。雷声最多一次，而且要远、低、软。

一句话公式：**精美都市 LOFT 静帧 × 暴雨窗景三层动态 × 极慢单镜头推进 × 温暖无歌词音乐。**

## 2. 本版差异化设计

保持都市复式 LOFT 和暴雨治愈感，但全部更换陈列逻辑：

- 主题：鲜艳、温暖、密闭的“雨夜唱片收藏家 LOFT”。
- 色盘：奶油暖墙、橙红沙发、孔雀绿与青绿色柜体、芥末黄、钴蓝点缀、蜂蜜色木地板；颜色饱满但不做儿童房。
- 布局：保留一层下沉式弧形沙发、厨房岛台与唱片角；夹层高度降低，右侧改为只有几级的宽缓楼梯；二层为实体墙围合的书房与卧室。
- 视觉锚点：左侧唯一都市雨窗、橙红下沉式沙发、孔雀绿厨房、纸灯笼吊灯和唱片聆听角。
- 密闭感：全屋只保留左侧一扇明确主窗；其他开口改为实体墙、书架、柜体和普通门洞，不出现玻璃卧室或连续落地窗。
- 城市感：唯一主窗外必须出现高层建筑、湿冷蓝灰天光和被雨雾软化的灯点；不出现森林、树屋、山景或自然木屋语义。

主图：[`assets/urban-rain-loft-master.png`](./assets/urban-rain-loft-master.png)

## 3. 12 秒单镜头分镜

| 时间 | 画面与镜头 | 窗景动态 | 声音与目的 |
|---|---|---|---|
| 0.0–1.0s | 第一帧直接亮出完整复式 LOFT，不黑场、不标题。画幅从 100% 开始。 | 暴雨从第一帧就存在；近玻璃雨珠清晰，远城雨幕偏软。 | 雨声与柔和钢琴立即进入，用“外冷内暖”的反差完成视觉钩子。 |
| 1.0–3.2s | 极慢向雨窗与沙发区推进至约 102.5%，略向左上漂移。 | 中层斜雨快速下落；城市灯点仅有极轻微雾化变化。 | 让观众发现短楼梯、实体墙围合的上层书房和卧室。 |
| 3.2–5.6s | 推至约 104.5%；沙发和茶几产生很轻的前景视差，建筑线条保持绝对稳定。 | 一颗较大的玻璃水珠开始形成竖向水痕。 | 钢琴保持稀疏，不跟画面逐拍同步，开始沉浸。 |
| 5.6–8.0s | 推至约 106.5%，不切镜；焦点仍锁在整个 LOFT，不做拉焦。 | 主水痕滑落；远雨短暂加密，窗外蓝灰亮度仅抬高 2%–3%。 | 7.4s 可加入一次很远的低频闷雷，绝不做刺眼闪电。 |
| 8.0–10.5s | 推至约 108.5%；发光楼梯与厨房暖光仅做 1%–2% 的呼吸。 | 城市雾气轻移，雨速保持；不要让雨落进室内。 | 情绪从“观察”转为“被包裹”，BGM 不升高潮。 |
| 10.5–12.0s | 推至 109%–110% 后缓停，最后 0.4 秒基本静止。 | 水痕离开主要视觉区，雨幕继续。 | 音乐和雨声在末尾 0.2 秒柔和淡出；需要循环时再做 0.4–0.6 秒交叉淡化。 |

### 镜头硬约束

- 全片只用一个镜头，不切换机位，不旋转，不手持抖动。
- 室内结构、家具、楼梯、灯具、窗框必须锁死；禁止 AI 形变、增生和漂移。
- 总推近 6%–9%，微漂移不超过 1.5%；不要明显景深呼吸。
- 雨分三层：慢速玻璃水痕、中速窗外斜雨、低清晰度远景雨雾。所有雨层都由窗框蒙版约束。
- 室内只允许灯光 1%–2% 的轻微呼吸；城市灯点变化不超过 2%。

## 4. 图生视频提示词

### 主提示词

> Preserve the exact architecture, furniture layout, short right-side staircase, single left rain window, sunken orange-red sofa, teal kitchen, study and bedroom from the input image. A photorealistic colorful and enclosed urban multi-level loft at night during a heavy rainstorm, viewed as a vertical architectural cutaway. Ultra-slow cinematic dolly-in toward the single city window and living area, total movement under ten percent, tiny upward-left drift. Only the weather moves: layered diagonal rain outside that one window, slow water droplets and trails on the exterior glass, subtle city haze and soft wet reflections. The saturated coral, teal, mustard, cobalt and warm cream interior remains almost perfectly stable; amber lamps have only a one-to-two-percent breathing variation. Calm, cozy, safe, bright, premium architectural visualization, realistic glass and rain physics, stable geometry, one continuous shot, 12 seconds.

### 负面约束

> no forest, no cabin, no countryside, no camera shake, no cuts, no orbit, no rapid zoom, no focus hunting, no furniture movement, no architectural morphing, no new objects, no people appearing, no rain indoors, no window-frame deformation, no new windows, no glass bedroom walls, no flickering neon, no dramatic lightning flash, no dark moody grade, no text, no logo

若工具支持“运动画笔 / 区域蒙版”，只涂窗玻璃和窗外城市；室内全部设为静止区。建议先生成 6 秒最稳定版本，再在剪辑软件中减速并做可控推镜，比一次性让模型自由生成 12 秒更稳。

## 5. 后期拆层与音频

建议拆成四层：

1. 室内与建筑结构：完全静止，承担主体画质。
2. 窗框与室内近景：放在雨层上方，负责遮挡关系。
3. 玻璃雨痕与反光：慢速、较清晰、少量大水珠。
4. 远处城市与雨幕：更软、更快、略带蓝灰雾气。

声音建议：60–68 BPM 的 felt piano + warm ambient pad，无歌词、无鼓；雨声比音乐低约 3 dB；可选远雷在 7.4 秒出现一次。全片目标响度约 -14 至 -16 LUFS，峰值不高于 -1 dBTP。

## 6. 导出

- 抖音成片：1080×1920，9:16，30 fps。
- 编码：H.264，高码率 12–20 Mbps；AAC 48 kHz。
- 当前主图为 1024×1536（2:3），制作前建议先超分至 2048×3072，再通过扩图或轻裁切适配 9:16；不要直接横向拉伸。

## 7. 本次生成方式与最终图像提示词

- 生成方式：OpenAI 内置 `imagegen`，单张高质量 2:3 竖图；以前一张图仅作材质完成度参考，不继承森林题材。
- 最终图像提示词：`Edit the provided image into a brighter, more colorful, cozy enclosed urban LOFT while preserving the successful ground-floor composition: keep the sunken curved sofa, oval coffee table, compact kitchen, vinyl listening corner, and lived-in first-floor layout. Lower the mezzanine substantially; replace the tall staircase with a much shorter, gentler staircase of only a few broad steps along the right wall; remove most glass partitions and extra glazing; use solid colorful walls, a normal doorway, built-in shelves and warm opaque surfaces upstairs. Keep exactly one clearly visible rain window on the left, smaller and more framed than before; close all other window openings. Use saturated coral-red and burnt orange upholstery, teal and turquoise built-ins, sunny mustard-yellow accents, warm cream walls, cobalt-blue details, colorful books and art, honey-colored wood and warm amber lamps. Bright, rich and lively but tasteful and photorealistic. Preserve the vertical 2:3 high-angle frontal architectural cutaway composition, crisp stable geometry and premium editorial detail. No forest, no cabin, no excessive glass, no dark moody palette, no giant staircase, no text, no watermark.`
