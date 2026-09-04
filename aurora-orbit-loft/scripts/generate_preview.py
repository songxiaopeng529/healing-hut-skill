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
REFERENCE_PATH = (
    ROOT.parent
    / "suspended-nest-futurist-loft"
    / "images"
    / "04-refined-solid-bamboo-rain-loft.jpeg"
)
OUTPUT_PATH = ROOT / "images" / "01-aurora-orbit-loft-preview.jpeg"

PROMPT = """
Use the supplied image only as a reference for its bright feminine color confidence, biomorphic softness, refined
microcement walls and editorial quality. Design a completely NEW physically buildable two-floor Aurora Orbit Loft.
Do not copy the reference floor plan, stair position, bamboo weather or hammock structure.

NEW ARCHITECTURAL LAYOUT:
- Exactly two floors. Place one 1.6 m diameter cylindrical load-bearing core slightly right of center. Finish it in
  pearl-white fluted microcement with inset lit niches, storage and curved display shelves.
- Build one broad 210-degree curved staircase wrapping around the solid core. Use 18 continuous wedge-shaped pale-ash
  treads; each tread has at least 28 cm usable depth on the walking line. The inner edge anchors into the core and the
  outer edge rests on a continuous curved structural beam. Provide continuous champagne-metal handrails and guards.
  The first tread rests on the ground floor and the final tread arrives flush at an unobstructed upper landing.
- Create one 35 cm thick crescent-shaped upper floor extending from the core toward the left-rear wall. Support it with
  the central core, the rear shear wall and two broad rounded perimeter columns. Wrap the slab in smooth ivory
  microcement. No exposed skeletal steel and no floating slab.
- On the upper crescent platform, place one normal low bed fully on the floor inside a blush padded half-moon alcove.
  Add layered bedding, wardrobe and reading chaise. Keep the bed 1.5 m behind a continuous 1.1 m curved solid parapet
  with limited laminated-glass inserts. The stair opening remains clear.
- On the ground floor, create a low oval conversation island sunken only 18 cm, reached by one broad visible step.
  Fill it with a continuous pearl-boucle sofa, coral and aqua modules, lemon poufs, thick abstract rugs, knitted throws
  and a sculptural translucent table. Maintain a 90 cm circulation ring around it.
- Replace any fireplace with a curved media-and-tea wall containing ribbed glass cabinets, a record player, ceramics,
  fashion books, orchids and concealed lighting. Kitchen and bathroom remain in an unseen rear service core.

WINDOW AND WINTER:
Create a two-story curved corner glass wall on the RIGHT side. Outside is an ice-blue frozen lake, sculptural snowdrifts,
white birch trees bending in a fierce blizzard, distant mountains and a subtle green-gold aurora. Show diagonal snow,
ice crystals and meltwater trails outside the glass. Interior remains completely dry.

FASHION-FORWARD STYLE:
Use pearl ivory, coral pink, raspberry red, aqua, cobalt blue, lemon yellow, pale ash and champagne silver. Add flower-
petal lounge chairs, gradient woven textiles, frosted sculptural pendants, curved fluted panels, floral plaster reliefs,
glowing ceiling ribbons and acrylic side tables. At least 70 percent of furnishing surfaces feel soft. Add one orange
tabby cat resting on the conversation island beside a natural-wood guitar. Bright 2500K layered light, vivid, youthful,
luxurious and avant-garde, never childish or old-fashioned. Photorealistic architecture, HDR, sharp detail, 8k.

Avoid copied old layout, exposed steel mezzanine, thin floor slab, suspended bed, fireplace, broken stair, spiral stair,
blocked upper exit, indoor snow, dark brown dominance, antique furniture, purple neon, people, text or watermark.
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
