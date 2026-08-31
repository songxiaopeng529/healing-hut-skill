# Healing Hut

Prompt-driven toolkit for generating cozy healing LOFT interiors, curating visual styles, and planning short-form image-to-video content.

This repository combines reusable image-generation scripts, visual-direction notes, finished reference assets, and production-ready short-video specifications for warm, sheltered interiors set against rain or snow.

## Features

- Curated prompts for colorful, photorealistic LOFT and cottage interiors
- Repeatable Python workflows for image generation and variation
- Visual style distillation notes covering composition, lighting, stairs, and spatial order
- Short-form video specifications for camera motion, weather effects, sound, and export
- Reference JPEG assets and social-post copy for creative iteration

## Project structure

```text
assets/                    Generated references and style variants
scripts/                   Image-generation and download workflows
work/                      Draft publishing copy and working notes
aesthetic-distillation-v2.md
production-notes.md
video-spec.md
```

## Installation

Python 3.10 or newer is recommended.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

## Configuration

The generation scripts use environment variables so credentials never need to be stored in source code.

```bash
export ARK_API_KEY="your-api-key"
export SEEDREAM_ENDPOINT_ID="your-endpoint-id"
```

See [`.env.example`](./.env.example) for the complete list of supported variables. The scripts do not load `.env` automatically; export the values in your shell or use your preferred environment manager.

## Usage

Generate the original four LOFT concepts:

```bash
python scripts/generate_4_lofts.py
```

Run the anchored rain and style-variation workflow:

```bash
LOFT_MODE=all python scripts/generate_4_lofts_rain.py
```

`LOFT_MODE` also supports focused tasks such as `anchor`, `variants`, `romantic-preview`, `blizzard-preview`, `crescent-stair-preview`, `cozy-cottage-v2-preview`, and `rainy-flower-bedroom-preview`.

Download four short-lived result URLs after exporting `LOFT_IMAGE_URL_1` through `LOFT_IMAGE_URL_4`:

```bash
python scripts/download_4_lofts.py
```

## Testing

There is no automated test suite yet. A quick syntax check is available with:

```bash
python -m compileall scripts
```

## Contributing

Issues and pull requests are welcome. Keep credentials and signed asset URLs out of commits, preserve reproducible prompt settings, and document meaningful visual changes.

## License

No license has been declared yet. Unless a license is added, reuse rights are not granted by default.

## Links

- [Repository](https://github.com/songxiaopeng529/healing-hut-skill)
- [Issues](https://github.com/songxiaopeng529/healing-hut-skill/issues)
