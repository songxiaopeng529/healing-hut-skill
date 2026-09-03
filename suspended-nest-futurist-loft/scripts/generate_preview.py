#!/usr/bin/env python3
import asyncio
import base64
import json
import os
from pathlib import Path

import httpx


API_URL = "https://ark.cn-beijing.volces.com/api/v3/images/generations"
API_KEY = os.environ["ARK_API_KEY"]
ENDPOINT_ID = os.environ["SEEDREAM_ENDPOINT_ID"]
ROOT = Path(__file__).resolve().parents[1]
REFERENCE_PATH = ROOT / "images" / "02-right-window-hammock-lounge.jpeg"
OUTPUT_PATH = ROOT / "images" / "03-vivid-bamboo-rain-hammock-lounge.jpeg"

PROMPT = """
Use the supplied right-window hammock-lounge loft image as an immutable architectural reference. Preserve exactly the
same camera, crop, two floors, right-side arched curtain window, left-rear mezzanine, solid upper bed, complete
L-shaped stair, fireplace, flue, low suspended lounge, independent portal frame, four tension cables, circulation,
cat and guitar. Do not move or redesign any structural element, stair, guard, window, floor, bed or hammock support.

CHANGE THE EXTERIOR:
Replace the frozen lake and snow with a lush emerald bamboo forest in a violent summer rainstorm. Dense bamboo fills
the entire view beyond the right window. Strong wind bends the tall bamboo culms and streams all leaves in one clear
direction, creating a visible swaying rhythm. Show diagonal heavy rain, rain mist, wet leaves, distant green hills,
large droplets and long water trails on the exterior glass. All rain remains outside; the interior stays dry.

RESTYLE THE ENTIRE INTERIOR AS BRIGHT FASHION-FORWARD FEMININE FUTURISM:
- Remove the dark, old-fashioned industrial mood. Refinish exposed steel arches and portal frame in pearl white and
  champagne silver. Replace dark walnut surfaces with pale ash, glossy warm-white resin and small brushed-brass details.
- Restyle the suspended lounge with vivid coral-pink woven sides, a pearl boucle mattress, raspberry velvet cushions,
  aqua quilted throws and lemon-yellow accents. Keep the cat and guitar naturally positioned.
- Replace all dark chairs and poufs with sculptural petal-shaped seating in coral, aqua, citron and ivory. Use a soft
  abstract rug with flowing color fields, a translucent acrylic low table and rounded lacquered side tables.
- Restyle the upper bed with a curved blush upholstered headboard, crisp ivory duvet, coral-and-aqua gradient quilt,
  embroidered floral pillows and a soft lemon bed-end bench. Keep the bed firmly on the mezzanine floor.
- Replace plain pendant lamps with contemporary frosted flower-petal pendants in warm 2500K light. Add thin concealed
  light lines, modern botanical artwork, playful ceramic objects, fashion books, orchids and fresh green plants.
- Use light ivory sheer curtains and coral outer curtains without covering the bamboo view.

The result is vivid, youthful, sophisticated and feminine without becoming childish, sugary, vintage or cluttered.
Use pearl ivory, coral pink, raspberry, aqua, lemon yellow, fresh green and light ash as a balanced multicolor palette.
Keep at least 70 percent soft textile surfaces. Premium contemporary interior editorial, ultra-realistic, HDR, 8k.

Avoid old dark wood, brown-dominant palette, antique furniture, beige monotony, purple neon, princess styling,
structural changes, suspended upper bed, missing cables, indoor rain, duplicate cats, people, text or watermark.
""".strip()


async def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    if not REFERENCE_PATH.exists():
        raise FileNotFoundError(f"Missing reference image: {REFERENCE_PATH}")
    reference = base64.b64encode(REFERENCE_PATH.read_bytes()).decode("ascii")
    body = {
        "model": ENDPOINT_ID,
        "prompt": PROMPT,
        "image": f"data:image/jpeg;base64,{reference}",
        "size": "1536x2048",
        "watermark": False,
        "output_format": "jpeg",
    }
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }

    async with httpx.AsyncClient(
        timeout=httpx.Timeout(900.0),
        follow_redirects=True,
    ) as client:
        print(f"Generating {OUTPUT_PATH.name}...", flush=True)
        response = await client.post(API_URL, headers=headers, json=body)
        if response.is_error:
            print(response.text, flush=True)
        response.raise_for_status()
        image_url = response.json()["data"][0]["url"]
        image_response = await client.get(image_url)
        image_response.raise_for_status()
        OUTPUT_PATH.write_bytes(image_response.content)

    print(
        json.dumps(
            {
                "path": str(OUTPUT_PATH),
                "url": image_url,
                "bytes": OUTPUT_PATH.stat().st_size,
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    asyncio.run(main())
