#!/usr/bin/env python3
import asyncio
import base64
import json
import os
from pathlib import Path
from typing import Dict, List, Optional

import httpx


API_URL = "https://ark.cn-beijing.volces.com/api/v3/images/generations"
API_KEY = os.environ["ARK_API_KEY"]
ENDPOINT_ID = os.environ["SEEDREAM_ENDPOINT_ID"]
ROOT = Path(__file__).resolve().parents[1]
IMAGES_DIR = ROOT / "images"
MASTER_PATH = IMAGES_DIR / "01-glass-garden-sunrise.jpeg"

MASTER_PROMPT = """
Create a photorealistic, physically buildable, single-level Winter Glasshouse Retreat. Use a vertical 3:4
architectural-interior composition from a fixed front-left viewpoint, eye level slightly elevated, approximately
24 mm lens. Show the complete room without cutting off the roof, bedroom, lounge or floor circulation.

IMMUTABLE ARCHITECTURAL LAYOUT:
- Exactly one ground floor. No stairs, mezzanine, bridge, loft or suspended platform.
- Build a broad conservatory envelope across the RIGHT side and overhead: one continuous curved glass wall flowing
  into an arched glass roof. The glazing stands on a substantial cream masonry base and is supported by evenly spaced
  ivory structural ribs, visible cross-purlins and a solid rear wall. All members look thick, engineered and stable.
- Place one low oval indoor tree planter exactly at the center. Its pale terrazzo retaining wall doubles as a bench.
  Grow one modest sculptural olive tree whose entire trunk and crown remain safely below the glass roof.
- Place one oval conversation lounge in the FRONT-CENTER, sunken only 18 cm. Give it exactly one broad, clearly
  visible entry step facing the camera and a continuous 90 cm circulation route around it. The lounge boundary,
  planter and passage never overlap.
- Build one sheltered bedroom alcove at the LEFT-REAR. Three substantial plaster walls surround a normal floor-standing
  bed. The headboard rests against the rear wall, the bedside passage is open, and the wide front opening connects
  directly to the main floor. It is not a floating bed or exposed platform.
- Run one linear tea-and-light-meal counter along the REAR wall between bedroom and glazing, with a real sink,
  integrated under-counter refrigerator, closed storage and lit display niches. One discreet flush door in the far
  left rear wall clearly leads to the enclosed bathroom. Add no other doors.
- Use slip-resistant pale terrazzo around the garden and warm timber flooring in the bedroom. Keep every doorway,
  work zone and route unobstructed. No fireplace.

STYLE 01 - GLASS GARDEN SUNRISE:
Create a bright, youthful, feminine but sophisticated interior in warm ivory, coral pink, lemon yellow, water-green,
raspberry accents and pale oak. Fill the unchanged sunken oval with a custom curved cloud-soft boucle sofa, a rounded
lemon ottoman, coral and aqua cushions, thick tufted botanical rugs, knitted throws and a translucent flower-shaped
coffee table. Dress the bedroom in a scalloped coral upholstered bed, an ivory feather duvet, water-green quilt and
layered oversized pillows. Use frosted petal pendants, slim champagne-metal details, curved oak cabinetry, handmade
ceramics, orchids and small flowering plants. At least 65 percent of visible furniture surfaces should feel soft.
Place one orange tabby cat curled on the lounge beside a natural-wood acoustic guitar.

OUTSIDE AND LIGHT:
Outside the right glasshouse is a crisp blue-white winter garden with snow-covered birch trees, low shrubs, distant
frosted hills and gentle falling snow. Snow, frost and moisture remain strictly outside the glazing; the interior is
completely dry. Warm 2500K concealed lighting, sunrise-pink daylight and realistic glass reflections create a strong
cold-outside, warm-inside contrast. The image is vivid, airy and inviting, with editorial interior-photography
quality, realistic materials, sharp structural detail and natural HDR.

Avoid fragile steel framing, impossible glass structure, unsupported roof, extra floors, stairs, blocked paths,
tree piercing roof, deep pit, duplicate furniture, random doors, restaurant appearance, showroom emptiness, indoor
snow, wet interior, dark exposure, brown-dominant palette, purple neon, childish decor, people, text and watermark.
""".strip()

PRESERVE = """
Use the supplied Glass Garden Sunrise image as an immutable architecture, landscape and camera reference. Preserve
the exact 3:4 crop, viewpoint, lens, perspective, single-floor room dimensions, right curved glass wall and arched
glass roof, every ivory structural rib and cross-purlin, cream masonry base, rear and left walls, central oval tree
planter, the same olive tree and branches, front-center 18 cm sunken oval lounge, its one broad entry step, all
circulation clearances, left-rear three-wall bedroom alcove, rear tea counter, sink, cabinetry, bathroom door, floor
boundaries and outdoor snow-garden composition. Do not add, remove, move, resize or redesign any architectural
element, opening, level, planter, tree, window, room or route. Keep the interior completely dry and the snow outside.
Change only movable furniture, upholstery, bedding, rugs, lamps, decorative objects, small plants, art and surface
colors. Keep one orange tabby cat and one natural-wood acoustic guitar in the lower lounge. No fireplace, people,
text or watermark. Render as bright photorealistic high-end interior photography, never as an illustration.
""".strip()

VARIANTS: List[Dict[str, str]] = [
    {
        "name": "02-nordic-iceberry-conservatory",
        "prompt": (
            PRESERVE
            + """

STYLE 02 - NORDIC ICE-BERRY CONSERVATORY:
Restyle the interior with pearl white, glacier blue, cranberry red, forest green and pale ash. Fit the unchanged
sunken oval with a low wraparound pearl boucle sofa, glacier-blue quilted lounge modules, cranberry wool cushions,
forest-green ottomans, chunky plaid throws and a thick abstract white rug. Use rounded pale-ash tables, opal-glass
pendants, woven baskets and clean botanical prints. Redress the unchanged bedroom with a pale-ash upholstered bed,
cloudy white duvet, glacier quilt, cranberry coverlet and oversized knitted pillows. Finish the fixed tea cabinetry
in pale ash and muted green. The result is bright, tactile, tailored and abundant, never sparse or monochromatic.
"""
        ).strip(),
    },
    {
        "name": "03-jewel-garden-salon",
        "prompt": (
            PRESERVE
            + """

STYLE 03 - CONTEMPORARY JEWEL GARDEN SALON:
Restyle the interior in luminous emerald, raspberry, peacock blue, warm cream and restrained champagne brass. Fit
the unchanged sunken oval with a flowing petal-shaped emerald velvet sofa, raspberry lounge modules, peacock-blue
pillows, a cream botanical embroidered rug and low organic glass tables with fine brass edges. Add curved opal
flower lamps, refined botanical relief art, jewel-toned ceramics and trailing plants. Redress the unchanged bedroom
with a scalloped peacock velvet bed, cream feather duvet, raspberry quilt and layered jewel cushions. Finish the
fixed tea cabinetry in warm cream with ribbed glass. Feminine, lush and contemporary, but bright rather than dark,
never antique, theatrical or nightclub-like.
"""
        ).strip(),
    },
    {
        "name": "04-japanese-warm-textile-glasshouse",
        "prompt": (
            PRESERVE
            + """

STYLE 04 - JAPANESE WARM-TEXTILE GLASSHOUSE:
Restyle the interior with warm ivory, indigo, persimmon orange, celadon and pale cedar. Fit the unchanged sunken oval
with low quilted modular cushions on a curved pale-cedar base, indigo shibori pillows, persimmon knitted throws,
celadon poufs and layered wool-over-tatami rugs. Use softly glowing washi pendants, rounded translucent resin tables,
handmade ceramics and restrained ikebana. Redress the unchanged bedroom with a low floor-standing pale-cedar bed,
thick ivory padded headboard, cloud duvet and indigo-persimmon bedding. Finish the fixed tea cabinetry in pale cedar
and celadon lacquer. Soft, serene, current and richly tactile, never austere, beige-dominant or historically themed.
"""
        ).strip(),
    },
]


def image_data_uri(path: Path) -> str:
    encoded = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:image/jpeg;base64,{encoded}"


async def post_with_retries(
    client: httpx.AsyncClient,
    *,
    body: dict,
    attempts: int = 3,
) -> str:
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }
    last_error: Optional[Exception] = None
    for attempt in range(1, attempts + 1):
        try:
            response = await client.post(API_URL, headers=headers, json=body)
            if response.is_error:
                print(response.text, flush=True)
            response.raise_for_status()
            return response.json()["data"][0]["url"]
        except (httpx.HTTPError, KeyError, IndexError) as exc:
            last_error = exc
            if attempt == attempts:
                raise
            await asyncio.sleep(2**attempt)
    raise RuntimeError("Image request failed") from last_error


async def download_with_retries(
    client: httpx.AsyncClient,
    image_url: str,
    output_path: Path,
    attempts: int = 3,
) -> None:
    for attempt in range(1, attempts + 1):
        try:
            response = await client.get(image_url)
            response.raise_for_status()
            output_path.write_bytes(response.content)
            return
        except httpx.HTTPError:
            if attempt == attempts:
                raise
            await asyncio.sleep(2**attempt)


async def generate(
    client: httpx.AsyncClient,
    *,
    prompt: str,
    output_path: Path,
    reference: Optional[str] = None,
) -> dict:
    body = {
        "model": ENDPOINT_ID,
        "prompt": prompt,
        "size": "1536x2048",
        "watermark": False,
        "output_format": "jpeg",
    }
    if reference:
        body["image"] = reference

    print(f"Generating {output_path.name}...", flush=True)
    image_url = await post_with_retries(client, body=body)
    await download_with_retries(client, image_url, output_path)
    print(f"Saved {output_path.name}", flush=True)
    return {
        "name": output_path.stem,
        "path": str(output_path),
        "url": image_url,
        "bytes": output_path.stat().st_size,
    }


async def main() -> None:
    IMAGES_DIR.mkdir(parents=True, exist_ok=True)
    mode = os.getenv("GLASSHOUSE_MODE", "all")
    if mode not in {"all", "master", "variants"}:
        raise ValueError(f"Invalid GLASSHOUSE_MODE: {mode}")

    timeout = httpx.Timeout(900.0, connect=60.0)
    results = []
    async with httpx.AsyncClient(timeout=timeout, follow_redirects=True) as client:
        if mode in {"all", "master"}:
            results.append(
                await generate(
                    client,
                    prompt=MASTER_PROMPT,
                    output_path=MASTER_PATH,
                )
            )

        if mode in {"all", "variants"}:
            if not MASTER_PATH.exists():
                raise FileNotFoundError(f"Missing master image: {MASTER_PATH}")
            reference = image_data_uri(MASTER_PATH)
            variants = VARIANTS
            style_index = os.getenv("GLASSHOUSE_STYLE_INDEX")
            if style_index:
                requested_index = int(style_index)
                if not 1 <= requested_index <= len(variants):
                    raise ValueError(
                        f"Invalid GLASSHOUSE_STYLE_INDEX: {requested_index}"
                    )
                variants = [variants[requested_index - 1]]

            for variant in variants:
                output_path = IMAGES_DIR / f"{variant['name']}.jpeg"
                results.append(
                    await generate(
                        client,
                        prompt=variant["prompt"],
                        output_path=output_path,
                        reference=reference,
                    )
                )

    print(json.dumps(results, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    asyncio.run(main())
