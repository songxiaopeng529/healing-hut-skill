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
REFERENCE_PATH = ROOT / "images" / "03-vivid-bamboo-rain-hammock-lounge.jpeg"
OUTPUT_PATH = ROOT / "images" / "04-refined-solid-bamboo-rain-loft.jpeg"

PROMPT = """
Use the supplied vivid bamboo-rain hammock-lounge loft image as the visual reference. Preserve the same close camera,
right-side arched bamboo-rain window, upper bed location, left stair route, low suspended lounge, independent portal
frame, four hammock cables, cat, guitar, circulation and bright coral-aqua palette.

REBUILD THE ARCHITECTURE TO FEEL SOLID AND REFINED:
- Remove every fireplace element completely: no firebox, hearth, chimney, black flue or smoke pipe.
- Replace the fireplace wall with a sophisticated floor-to-ceiling curved storage composition: pearl microcement,
  rounded closed cabinets, pale-ash shelves, asymmetrical illuminated niches, ribbed glass doors, orchids, ceramics,
  fashion books and concealed warm lighting.
- Replace all exposed black or thin steel roof arches and mezzanine framing with substantial pearl-white architectural
  construction. Use a 35 cm thick curved reinforced-concrete or engineered-timber mezzanine slab wrapped in smooth
  pearl microcement. Support it with broad rounded load-bearing walls and two integrated oval columns. No visible
  skeletal steel frame beneath the upper floor.
- Give the upper floor a continuous 1.1 m curved solid parapet with a brass cap and only a few inset laminated-glass
  panels. Keep a clear opening exactly where the stair arrives. The bed stays safely 1.5 m behind the edge.
- Refine the left L-shaped staircase with solid pearl-white sidewalls, closed pale-ash risers, wide wood treads, one
  supported rectangular landing and a continuous rounded champagne-brass handrail. Keep both flights complete and
  the final tread flush with the upper slab. No open industrial stringers.
- Make the ground floor visually substantial with continuous pale terrazzo and pale-ash flooring, deep baseboards,
  integrated floor edges and realistic wall-to-floor junctions.

MAKE WALL DECORATION HIGHLY DETAILED:
Use smooth microcement, curved fluted wall panels, padded blush wall sections, shallow floral-relief plaster, slim
brass reveals, rounded crown transitions and precisely lit display niches. Avoid blank unfinished walls.

PRESERVE THE FASHION-FORWARD FEMININE INTERIOR:
Keep the coral-pink hammock sofa with pearl boucle mattress, raspberry and aqua cushions, lemon accents, flower-petal
chairs, translucent acrylic table, abstract multicolor rug, coral curtains, frosted floral pendants and warm 2500K
lighting. Keep the upper bed firmly on the solid floor with curved blush headboard and vivid layered bedding.
Outside the right window, preserve the wind-bent emerald bamboo forest, diagonal heavy rain, rain mist, wet leaves,
distant green hills, large exterior droplets and long glass water trails. All rain stays outside.

The result is structurally reassuring, luxurious, youthful, vivid and finely finished, not industrial or old-fashioned.
Premium contemporary interior editorial, ultra-realistic materials, HDR, sharp detail, 8k.

Avoid fireplace, chimney, exposed skeletal mezzanine steel, thin slab, unsupported upper floor, open stair stringers,
blank walls, dark wood dominance, antique furniture, purple neon, suspended upper bed, missing hammock cables, indoor
rain, duplicate cats, people, text or watermark.
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
