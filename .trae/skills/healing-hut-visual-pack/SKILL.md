---
name: "healing-hut-visual-pack"
description: "Builds healing-home packs with 5-6 images, generation code, a design spec, fixed-camera storyboard, and Xiaohongshu copy. Invoke for new cozy interior styles or complete visual packs."
---

# Healing Hut Visual Pack

Create a complete, production-ready visual content pack for a refined, warm and
healing residential concept. The result must include actual generated images,
reproducible image-generation code, a design specification, a fixed-camera video
storyboard and two concise Xiaohongshu captions.

## Required Reading

Before proposing or generating a concept, read:

1. `references/taste-dna.md`
2. `references/artifact-contract.md`

When image generation is required, also invoke and fully read the installed
`byted-seedream-image-generate` skill before making image requests.

## Invocation Modes

Determine the mode from the user's wording.

### Collaborative Mode

Use this by default when the user wants to discuss, design, explore or refine a
new style.

1. Inspect nearby project folders and existing design specs so the new concept
   does not repeat an earlier layout.
2. Ask only for missing high-impact preferences. Cover layout, decoration,
   exterior view and weather; combine these into one compact question when
   possible.
3. Present one concrete concept brief in chat:
   - concept name and one-sentence promise
   - floor count and structural system
   - room zoning and circulation
   - camera position and framing
   - exterior landscape and weather
   - palette, materials and soft-furnishing strategy
   - intended video motion
4. Wait for explicit approval before creating the style folder or generating
   images.
5. Incorporate revisions and ask for approval again when the architecture or
   visual direction materially changes.

### Direct Mode

Use this only when the user explicitly asks to generate directly, skip
discussion or decide autonomously.

1. Inspect existing sibling concepts first.
2. Select a buildable concept that is visibly different from existing work in
   its floor plan, structural motif and exterior setting.
3. Apply the shared taste DNA without copying a previous composition.
4. State the chosen concept briefly, then proceed without waiting for another
   approval.

## Output Directory

Create one kebab-case folder for each approved style:

```text
<style-slug>/
├── images/
├── scripts/
├── spec/
└── video/
```

Use lowercase directory names by default to match the workspace convention. If
the user explicitly requires different capitalization, follow it exactly.

Run the bundled scaffolder from this skill directory:

```bash
python3 scripts/scaffold_style.py \
  --root "<workspace-root>" \
  --slug "<style-slug>" \
  --image-count 6
```

## End-to-End Workflow

### 1. Lock The Concept

Write the approved design into `<style-slug>/spec/design-spec.md`. It must define:

- concept and emotional target
- exact architecture and load paths
- room inventory, dimensions where useful and circulation
- camera position, lens and mandatory visible elements
- exterior landscape, weather and glass boundary
- palette, materials, furniture and soft-surface ratio
- immutable layout rules
- negative constraints and acceptance criteria

Resolve physical contradictions in writing before generating an image.

### 2. Plan 5-6 Images

Generate 6 images by default; use 5 when the user asks for the smaller set.

The default set uses one architectural master plus style-controlled variants:

```text
01-<concept>-master.jpeg
02-<variant-name>.jpeg
03-<variant-name>.jpeg
04-<variant-name>.jpeg
05-<variant-name>.jpeg
06-<variant-name>.jpeg
```

- Image 01 establishes the approved architecture, camera and complete room.
- Images 02-06 use image-to-image with Image 01 as the immutable reference.
- Variants may change movable furniture, textiles, colors, lighting fixtures,
  decor and surface finishes.
- Variants must not move walls, doors, windows, stairs, slabs, structural
  supports, room zones, fixed circulation or the camera.
- If the user explicitly requests distinct layouts, create separate masters
  while preserving the common style DNA.

### 3. Create One Reproducible Generator

Create `<style-slug>/scripts/generate_images.py`.

Requirements:

- Read `ARK_API_KEY` and `SEEDREAM_ENDPOINT_ID` from environment variables.
- Never hardcode, print or commit credentials.
- Use the Seedream image generation endpoint and save local JPEG or PNG files.
- Support text-to-image for the master and image-to-image for variants.
- Support `all`, `master` and `variants` modes.
- Support a one-based style index for retrying one failed variant.
- Include bounded retries for transient HTTP and download failures.
- Print local output paths and byte sizes after generation.
- Keep prompts in the script so the image set is reproducible.

Prefer the user's existing Seedream endpoint configuration. Do not silently
switch models or services.

### 4. Generate And Inspect

Generate the master first. Open it and verify:

- structure is physically supported
- every stair reaches a clear upper landing, if stairs exist
- beds have a wall, guard or safe floor-level placement
- doors and circulation have meaningful destinations
- required rooms and furniture are present
- weather remains outside
- the full composition is visible

Do not generate variants from a flawed master. Revise the prompt and regenerate
the master first.

After approval or a successful internal check, generate the remaining images
from the accepted master. Open every result. Retry only the failed or drifting
variant. Never claim success based only on an HTTP response.

### 5. Write The Video Storyboard

Choose the strongest representative image unless the user names one. Create:

```text
<style-slug>/video/video-storyboard.md
```

Default video rules:

- 12 seconds, vertical 9:16, 1080 x 1920, 30 fps
- one fixed camera for the entire shot
- no pan, tilt, dolly, zoom, orbit, drift, shake or focus pull
- fit a 3:4 source with `contain`, then outpaint only top and bottom
- never crop out important architecture or furniture
- animate primarily exterior weather and landscape
- use separate hard masks for every visible glass pane
- keep precipitation behind glass and water only on the exterior surface
- prevent whiteout, full-frame fog, exposure pumping and indoor weather
- keep architecture and furniture pixel-stable
- use restrained animal motion only when it can remain anatomically stable
- end near the opening state for a clean loop

Include:

- production settings
- source-image adaptation
- camera lock
- allowed and forbidden motion
- weather and glass compositing
- second-by-second timeline
- audio policy
- direct-use English generation prompt
- negative prompt
- acceptance checklist

### 6. Write Xiaohongshu Copy

Create:

```text
<style-slug>/video/xiaohongshu-copy.md
```

Provide exactly two short versions:

1. `互动版`: ask one easy, scene-specific question with 2-3 choices or one
   direct invitation to comment.
2. `浪漫版`: 2-4 short lines with concrete imagery from the scene.

Add one shared line of 3-5 relevant hashtags. Avoid feature lists, long
explanations, exaggerated claims and generic motivational language.

### 7. Final Validation

Before delivery:

- confirm all four required directories exist
- confirm 5-6 actual image files exist
- confirm all images have the intended dimensions and format
- run a syntax check on `generate_images.py`
- verify the design spec, storyboard and Xiaohongshu copy exist
- run a whitespace or diff check when the workspace uses Git
- report local clickable paths for every deliverable

## Completion Contract

Do not call the pack complete until it contains:

- 5-6 generated images
- 1 reproducible image-generation script
- 1 design specification
- 1 fixed-camera video storyboard and direct-use prompt
- 1 Xiaohongshu copy file containing interactive and romantic versions

If credentials or an external image service are unavailable, finish all
possible text and code artifacts, state the exact blocker, and do not pretend
that image files were generated.
