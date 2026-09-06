# Artifact Contract

This document defines the minimum content and naming for every generated visual
pack.

## Directory Contract

```text
<style-slug>/
├── images/
│   ├── 01-<concept>-master.jpeg
│   ├── 02-<variant>.jpeg
│   ├── 03-<variant>.jpeg
│   ├── 04-<variant>.jpeg
│   ├── 05-<variant>.jpeg
│   └── 06-<variant>.jpeg
├── scripts/
│   └── generate_images.py
├── spec/
│   └── design-spec.md
└── video/
    ├── video-storyboard.md
    └── xiaohongshu-copy.md
```

Five-image packs omit `06-*`.

## Design Specification Template

```markdown
# <Chinese concept name>

## Concept
<One paragraph defining the emotional and visual promise.>

## Fixed Architecture
- floor count
- load-bearing system
- exact room locations
- circulation and safety
- window geometry
- camera and lens

## Exterior And Weather
- landscape
- weather direction and intensity
- indoor/outdoor boundary

## Material And Color
- base colors
- warm accents
- cool accents
- structural materials
- soft furnishing ratio

## Image Set
1. 01 master: <style>
2. 02 variant: <style>
...

## Immutable Elements
<Elements that variants may never move or redesign.>

## Negative Constraints
<Structural, visual and generation failure modes.>

## Acceptance Criteria
<Observable checks rather than subjective claims.>
```

## Image Generator Contract

The generated `scripts/generate_images.py` should use this behavioral interface:

```bash
# Generate master, inspect it, then generate variants
IMAGE_MODE=master python3 scripts/generate_images.py
IMAGE_MODE=variants python3 scripts/generate_images.py

# Generate the complete pack
IMAGE_MODE=all python3 scripts/generate_images.py

# Retry one variant with a one-based index
IMAGE_MODE=variants IMAGE_STYLE_INDEX=3 python3 scripts/generate_images.py
```

Implementation requirements:

- Python 3, `asyncio`, `httpx`, `pathlib` and `base64`
- `POST https://ark.cn-beijing.volces.com/api/v3/images/generations`
- model from `SEEDREAM_ENDPOINT_ID`
- bearer token from `ARK_API_KEY`
- default image size `1536x2048`
- watermark disabled
- local download before the temporary URL expires
- sequential variant generation by default for predictable recovery
- two or three bounded retries for network failures
- useful API error body printed without secrets

The master prompt must describe the complete architecture independently. The
variant prompt must begin with a strict preservation block before describing
new furnishings.

## Video Storyboard Template

```markdown
# <Selected image> Video Storyboard

## Production Settings
## 9:16 Source Adaptation
## Absolute Camera Lock
## Allowed Motion
## Weather And Glass Masks
## 12-Second Timeline
## Indoor Stability
## Audio
## Direct-Use English Prompt
## Negative Prompt
## Acceptance Checklist
```

For a 1536 x 2048 source:

1. Scale the complete image to 1080 x 1440.
2. Center it on a 1080 x 1920 canvas.
3. Outpaint 240 px above and 240 px below.
4. Preserve the original central area.
5. Finish outpainting before animation.

Weather limits:

- create a separate hard mask for each pane
- place rain or snow behind the glass
- place droplets only on the exterior glass surface
- render frames and sills above weather layers
- keep at least 65%-75% of the exterior readable
- forbid full-frame overlays, whiteout and exposure pumping

## Xiaohongshu Copy Template

```markdown
# Xiaohongshu Copy

## 互动版

<One short scene-specific question. Use 2-3 choices only when useful.>

## 浪漫版

<Two to four short lines using concrete details from the image.>

## 标签

#治愈系小屋 #冬日氛围感 #梦想中的家
```

## Final Acceptance Matrix

| Artifact | Required check |
|---|---|
| Images | 5-6 local files, correct dimensions, each opened and inspected |
| Layout | Master is buildable; variants preserve camera and architecture |
| Generator | Syntax check passes; supports master, variants and indexed retry |
| Design spec | Contains architecture, style, invariants and rejection rules |
| Storyboard | Fixed camera, timeline, masks, direct prompt and negatives |
| Copy | Exactly one interactive and one romantic version |
| Security | No API key or credential stored in the pack |
