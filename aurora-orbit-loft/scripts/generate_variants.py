#!/usr/bin/env python3
import asyncio
import base64
import json
import os
from pathlib import Path
from typing import Dict, List

import httpx


API_URL = "https://ark.cn-beijing.volces.com/api/v3/images/generations"
API_KEY = os.environ["ARK_API_KEY"]
ENDPOINT_ID = os.environ["SEEDREAM_ENDPOINT_ID"]
ROOT = Path(__file__).resolve().parents[1]
REFERENCE_PATH = ROOT / "images" / "01-aurora-orbit-loft-preview.jpeg"

PRESERVE = """
Use the supplied Aurora Orbit Loft image as an immutable architectural and camera reference. Preserve exactly the
same crop, perspective, two floors, central cylindrical load-bearing core, every curved stair tread, open upper stair
exit, 35 cm crescent mezzanine slab, supporting columns, curved parapets, right-side corner glass wall, upper bed
location, ground-floor sunken conversation island, circulation and winter landscape composition. Do not add, remove,
move or redesign any wall, column, slab, stair, guard, window, room or level. Keep the bed fully on the upper slab and
the stair physically continuous. Preserve the frozen lake, birch trees, mountains, blizzard and subtle aurora outside.
Keep one orange tabby cat in the lower lounge. Change only movable furniture design, upholstery, bedding, rugs,
curtains, lamps, artwork, plants, decorative objects and surface finishes. No fireplace, text or watermark.
""".strip()

VARIANTS: List[Dict[str, str]] = [
    {
        "name": "02-arctic-nordic-couture",
        "prompt": (
            PRESERVE
            + " Restyle the entire interior as Nordic Arctic couture. Use pearl white, glacier blue, cranberry red, "
            "forest green and pale ash. Replace the lower seating with a soft cloud-like modular boucle sofa following "
            "the same oval island, rounded pale-ash tables, knitted berry cushions, plaid wool throws and a sculpted "
            "white wool rug. Use opal-glass pendants, minimal botanical prints and woven baskets. Replace the upper bed "
            "with a low pale-ash upholstered frame, glacier-blue duvet, cranberry quilt, oversized knit pillows and a "
            "soft forest-green chaise. Bright, tactile and polished, not sparse."
        ),
    },
    {
        "name": "03-neo-memphis-sunrise",
        "prompt": (
            PRESERVE
            + " Restyle the entire interior as sophisticated neo-Memphis sunrise design. Use coral orange, cobalt "
            "blue, aqua, lemon yellow and warm ivory. Replace the lower seating with interlocking wave-shaped sofa "
            "modules, rounded geometric poufs, translucent colored acrylic tables and a bold abstract tufted rug, all "
            "within the unchanged island. Use sculptural globe-and-arc pendants, playful ceramic objects and graphic "
            "art. Replace the upper bed with a rounded cobalt frame, coral headboard, lemon bench and color-blocked "
            "bedding. Fashion-forward, joyful and luxurious, never childish."
        ),
    },
    {
        "name": "04-art-nouveau-jewel-garden",
        "prompt": (
            PRESERVE
            + " Restyle the entire interior as contemporary Art Nouveau jewel garden. Use emerald, raspberry, "
            "peacock blue, cream and champagne brass. Replace the lower seating with a flowing petal-shaped emerald "
            "velvet sofa, raspberry lounge chairs, brass-edged organic tables and a botanical embroidered rug. Use "
            "curved opal flower lamps, trailing plants, sculptural vases and refined botanical reliefs. Replace the "
            "upper bed with a scalloped peacock velvet frame, layered jewel bedding and an emerald reading chaise. "
            "Luminous, feminine and sumptuous, not dark or antique."
        ),
    },
    {
        "name": "05-japanese-future-textile",
        "prompt": (
            PRESERVE
            + " Restyle the entire interior as warm Japanese future textile design. Use ivory, indigo, persimmon, "
            "celadon and pale cedar. Replace the lower seating with low quilted modular cushions on a curved cedar "
            "plinth, indigo shibori pillows, persimmon throws, celadon poufs and layered wool-over-tatami rugs. Use "
            "floating washi lanterns, handmade ceramics, restrained ikebana and translucent resin tables. Replace the "
            "upper bed with a low cedar platform, padded ivory headboard and indigo-persimmon bedding. Soft, serene, "
            "contemporary and richly tactile, never austere."
        ),
    },
]


def image_data_uri(path: Path) -> str:
    encoded = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:image/jpeg;base64,{encoded}"


async def generate_one(
    client: httpx.AsyncClient,
    variant: Dict[str, str],
    reference: str,
) -> dict:
    output_path = ROOT / "images" / f"{variant['name']}.jpeg"
    body = {
        "model": ENDPOINT_ID,
        "prompt": variant["prompt"],
        "image": reference,
        "size": "1536x2048",
        "watermark": False,
        "output_format": "jpeg",
    }
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }
    print(f"Generating {output_path.name}...", flush=True)
    response = await client.post(API_URL, headers=headers, json=body)
    if response.is_error:
        print(response.text, flush=True)
    response.raise_for_status()
    image_url = response.json()["data"][0]["url"]
    image_response = await client.get(image_url)
    image_response.raise_for_status()
    output_path.write_bytes(image_response.content)
    print(f"Saved {output_path.name}", flush=True)
    return {
        "name": variant["name"],
        "path": str(output_path),
        "url": image_url,
        "bytes": output_path.stat().st_size,
    }


async def main() -> None:
    if not REFERENCE_PATH.exists():
        raise FileNotFoundError(f"Missing reference image: {REFERENCE_PATH}")
    reference = image_data_uri(REFERENCE_PATH)
    variants = VARIANTS
    style_index = os.getenv("AURORA_STYLE_INDEX")
    if style_index:
        requested_index = int(style_index)
        if not 1 <= requested_index <= len(variants):
            raise ValueError(f"Invalid AURORA_STYLE_INDEX: {requested_index}")
        variants = [variants[requested_index - 1]]

    async with httpx.AsyncClient(
        timeout=httpx.Timeout(900.0),
        follow_redirects=True,
    ) as client:
        results = await asyncio.gather(
            *[generate_one(client, variant, reference) for variant in variants]
        )
    print(json.dumps(results, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    asyncio.run(main())
