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
MASTER_PATH = IMAGES_DIR / "01-rainfall-theater-master.jpeg"
STAIR_REPAIR_PATH = IMAGES_DIR / "01-rainfall-theater-stair-corrected-v3.jpeg"

MASTER_PROMPT = """
Create an unprecedented yet physically buildable three-story residence named Rainfall Theater Spiral Loft. Make a
photorealistic vertical 3:4 architectural interior from a fixed front-left viewpoint at 1.6 m eye height with a
22 mm lens. Show all three inhabited levels in one coherent frame, without a dollhouse cutaway.

ARCHITECTURE AND LOAD PATH:
- Exactly three inhabited floors and no fourth floor. Total interior height is about 9.3 m.
- Place one solid 2.4 by 1.8 m oval reinforced-concrete structural core at the center of the atrium.
- Wrap one continuous 1.05 m wide clockwise helical staircase around the outside of this core. It has exactly two
  connected sections: 18 solid treads from ground floor to a broad second-floor landing, then 18 more solid treads
  from that landing to a broad third-floor landing. Anchor every tread to the core and one continuous outer stringer.
  Each landing is flush, broad and unobstructed. The stair stops on floor three. Use pale-oak treads, continuous
  champagne handrails and guards with thick solid bases. No gap, blocked exit or decorative false stair.
- Floor two is a broad 40 cm thick boomerang-shaped library deck extending toward the rear-right. Floor three is a
  sheltered 40 cm thick oval bedroom deck anchored at the left-rear. Both slabs are visibly supported by the central
  core, rear shear walls and substantial rounded columns. No thin steel mezzanine or floating platform.
- Protect every open edge with a continuous 1.1 m guard made from a thick upholstered solid base plus laminated glass.
- Build a three-story folded-wave glass curtain wall across the RIGHT side, with strong vertical mullions, horizontal
  rails and a masonry sill. The roof and rear wall are solid and clearly connected to the structure.

ROOM LOGIC:
- Ground floor is a social cinema lounge. Place one large 85-98 inch television fully recessed into a substantial
  curved acoustic media wall on the LEFT, never on glass and never across the stair. Show a colorful original
  vintage-style cat-and-mouse animation on screen with no text or recognizable franchise characters. Place one deep
  curved sofa at front-right directly facing the television. Keep the screen and sofa visibly aligned. Add a complete
  kitchen with sink, cooktop, refrigerator and rounded island at left-rear, plus one enclosed bathroom in the solid
  service block with one meaningful flush door. Keep a clear 90 cm route to every function and the first stair tread.
- Floor two contains NO BEDROOM and NO BED. Make it a creative library, music and game level: one continuous curved
  book wall attached to the solid rear wall, a two-person desk, record player and speakers, a low upholstered reading
  island and a refined console-gaming sofa. Keep every object away from the stair landing and circulation ring.
- Floor three contains the ONLY BED in the home: one primary bedroom with a floor-standing upholstered bed against a
  continuous solid rear wall, wardrobe, vanity and window chaise. Place a compact enclosed bathroom over the lower
  wet-service zone. Keep the final stair landing and one-meter route completely clear.

VISUAL STYLE:
Use warm ivory sculpted plaster, pearl microcement, pale oak, champagne metal and laminated clear glass. Create a
glazed-textile futurist palette with luminous celadon green, cherry red, cobalt blue, lemon yellow and soft coral.
Make at least 70 percent of visible furniture tactile and soft: deep boucle seating, padded acoustic panels, thick
geometric rugs, knitted throws, oversized cushions, a feather duvet and a sculpted headboard. Use colored-glass
pendants, bright ceramics, books and restrained trailing plants. Place one sleeping orange tabby on the ground-floor
sofa beside a natural-wood acoustic guitar. Bright warm 2600K layered light, sophisticated and feminine, vivid but
never childish. This decor must look clearly different from the earlier coral-and-walnut version.

EXTERIOR:
Beyond the right glazing is a bright rainy morning in a basalt canyon with several tall waterfalls, wet ferns,
wind-bent foliage and cool diagonal rain. Keep the waterfalls, cliffs and distant misty hills readable. Rain, spray
and water trails remain strictly outside the sealed glass; the interior is completely dry. Strong cool-outside,
warm-inside contrast without dark blue-night grading.

Photorealistic high-end architectural photography, realistic scale, crisp load-bearing details, natural HDR, sharp
materials. Avoid a second bed, any bed on floor two, duplicate television, television on glass, television blocking
stairs, impossible stairs, missing landings, blocked exits, disconnected treads, extra floors, thin unsupported slabs,
unsafe bed, missing guards, duplicate rooms, random doors, indoor rain, full-frame wet-glass overlay, white fog, dark
industrial styling, brown-dominant grading, purple neon, people, captions, logo or watermark.
""".strip()

PRESERVE = """
Use the supplied Rainfall Theater Spiral Loft master image as an immutable architecture and camera reference. Preserve the
exact crop, viewpoint, lens, perspective and exactly three floors. Preserve the central oval structural core,
both continuous sections of the helical staircase, every tread, outer stringer, second-floor landing, third-floor
landing, stair termination, 40 cm boomerang library deck, 40 cm oval bedroom deck, rear shear walls, rounded support
columns, every guard, three-story folded-wave glass wall, roof, masonry sill, ground-floor media wall and television,
kitchen, bathroom door, second-floor library-music-game zone, third-floor primary bedroom, all clear circulation and
the basalt waterfall canyon. Do not add, remove, move, resize or redesign any structural element, room, opening,
stair, landing, slab, column, window, television or fixed cabinet. Keep floor two free of beds. Keep the only bed
safely on floor three against its solid wall. Keep rain and waterfall spray outside. Change only movable furniture,
upholstery, bedding, rugs, lamps, art, small plants and surface colors. Keep one sleeping orange tabby and one
natural-wood acoustic guitar in the ground-floor lounge. No people, captions, logo or watermark.
""".strip()

STAIR_REPAIR_PROMPT = """
Use the supplied Rainfall Theater Spiral Loft image as an immutable pixel-level reference. Preserve the exact camera,
crop, perspective, three floor heights, central column location, floor slabs, ceiling, glass wall, window frames,
waterfall landscape, rain, lighting, materials, television hardware and position, media wall, kitchen, bathroom,
entire second-floor library and music area, entire third-floor bedroom, all furniture, rugs, lamps, books, plants,
sleeping orange cat, guitar and every color. Do not redesign, move, remove or add anything outside the staircase, the
small landing interfaces immediately touching it, and the pixels inside the television screen.

Replace only the television screen content with an original non-branded abstract animation frame made from simple
coral, aqua, yellow and blue geometric shapes. Show no animal, person, character, face, lettering, logo, title,
copyrighted cartoon or recognizable franchise. Preserve the television frame, recess, size and viewing direction.

SURGICAL STAIR AND FLOOR-TWO LANDING REPAIR:
- Preserve the exact visible staircase route from the original reference image. Do not relocate either flight. Keep
  the original first tread beside the large white-and-coral GROUND-FLOOR SOFA, the same window-facing spiral around
  the same core, the same tread positions, same radius, same clockwise direction and same outer ribbon silhouette.
- Preserve the original UPPER FLIGHT on the right, window-facing, GREEN-SOFA side of the core. It must continue upward
  from that side exactly as in the reference. Never move its first tread to the rear desk, book wall or left side.
- Repair only the floor-two connection. At the exact point where the lower flight reaches floor two beside the GREEN
  SOFA, cut one clear curved stairwell opening through the slab and add one flat 1.4 m by 1.8 m landing. The final
  lower tread must finish flush with this landing, with no slab face above it and no step hidden under the floor.
- Create one unmistakable 1.05 m wide walk-through opening in the floor-two glass guard. End the guard at two solid
  posts on either side of this opening. No glass, rail, wall, sofa, table or planter may cross the opening.
- Make the landing visibly connect in three directions: down to the ground-floor stair, horizontally into the
  second-floor library and green-sofa lounge, and up to the original upper stair on the same sofa side. A person must
  be able to step off at floor two without continuing upward.
- Keep the original upper flight start immediately beside this landing. Add only the minimum one or two transition
  treads needed to connect the landing to the existing upper helix. Preserve its window-side route and its final
  open arrival at floor three.
- Keep pale-oak treads, champagne structural ribbon, continuous handrails and laminated-glass guards. Preserve equal
  riser heights and a physically supported load path.

This is not a staircase redesign. It is a minimal floor-two opening and landing correction while preserving the
original reference stair's sofa-side path and silhouette.

Avoid two unrelated stairs, changing stair radius, opposite rotation, offset centers, sudden straight segment,
impossible overlap, stairs through a floor slab, blocked landing, missing tread, floating tread, split stringer,
broken handrail, stair ending at a wall, continuous guard across the second-floor exit, stair starting beside the rear
desk, stair starting behind the book wall, extra stairs, extra floor, changed room layout, changed furniture, changed
television hardware, changed cat, changed landscape, recognizable cartoon characters, copyrighted characters, new
objects, people, text, logo or watermark.
""".strip()

VARIANTS: List[Dict[str, str]] = [
    {
        "name": "02-alpine-berry-tailoring",
        "prompt": (
            PRESERVE
            + """

Restyle only the interior finishes and movable decor as Alpine Berry Tailoring. Use pearl white, glacier blue,
cranberry red, forest green and pale ash. Use tailored cloud-boucle seating, deep quilted modules, checked wool
throws, thick loop rugs, opal lamps and pale-ash tables. Dress the single third-floor bedroom with a glacier duvet,
cranberry blanket and oversized forest-green pillows. Keep floor two bed-free. Keep it bright, plush and polished
rather than sparse.
"""
        ).strip(),
    },
    {
        "name": "03-saffron-lagoon-modernism",
        "prompt": (
            PRESERVE
            + """

Restyle only the interior finishes and movable decor as Saffron Lagoon Modernism. Use warm ivory, lagoon turquoise,
saffron yellow, vermilion and pale oak. Use broad wave-shaped sofas, rounded wool ottomans, translucent resin tables,
graphic woven rugs and frosted globe lights. Dress the single third-floor bedroom with a sculptural upholstered frame
and bold color-blocked bedding. Keep floor two bed-free. Keep the result architectural, joyous and mature, never
childish.
"""
        ).strip(),
    },
    {
        "name": "04-celadon-silk-retreat",
        "prompt": (
            PRESERVE
            + """

Restyle only the interior finishes and movable decor as a contemporary Celadon Silk Retreat. Use luminous celadon,
warm ivory, persimmon, muted rose and pale cedar. Add low quilted lounge furniture, padded silk wall panels, thick
wool rugs, woven throws, softly glowing paper-and-glass pendants and handmade ceramics. Dress the single third-floor
bed in layered ivory, celadon and persimmon textiles. Keep floor two bed-free. Serene and richly tactile, but not
beige, austere or historical.
"""
        ).strip(),
    },
    {
        "name": "05-prismatic-flower-salon",
        "prompt": (
            PRESERVE
            + """

Restyle only the interior finishes and movable decor as a Prismatic Flower Salon. Use cream, peacock blue, raspberry,
emerald and restrained colored-glass accents. Add petal-shaped velvet seating, botanical tufted rugs, curved opal
lights, fine champagne-metal tables, floral relief art and jewel-toned bedding. Keep abundant daylight and soft
surfaces. Make it contemporary and luminous, never antique, dark or theatrical.
"""
        ).strip(),
    },
    {
        "name": "06-cobalt-coral-playhouse",
        "prompt": (
            PRESERVE
            + """

Restyle only the interior finishes and movable decor as a sophisticated Cobalt Coral Playhouse. Use cobalt blue,
coral orange, mint green, lemon yellow and warm ivory. Add generous modular lounge pieces, sculptural game seating,
soft geometric rugs, lacquered side tables, playful glass pendants and graphic bedding. Keep the game area refined
and residential, without arcade machines, neon signs or childish motifs.
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
    mode = os.getenv("IMAGE_MODE", "all")
    if mode not in {"all", "master", "repair-stair", "variants"}:
        raise ValueError(f"Invalid IMAGE_MODE: {mode}")

    results = []
    timeout = httpx.Timeout(900.0, connect=60.0)
    async with httpx.AsyncClient(timeout=timeout, follow_redirects=True) as client:
        if mode in {"all", "master"}:
            results.append(
                await generate(
                    client,
                    prompt=MASTER_PROMPT,
                    output_path=MASTER_PATH,
                )
            )

        if mode == "repair-stair":
            if not MASTER_PATH.exists():
                raise FileNotFoundError(f"Missing master image: {MASTER_PATH}")
            results.append(
                await generate(
                    client,
                    prompt=STAIR_REPAIR_PROMPT,
                    output_path=STAIR_REPAIR_PATH,
                    reference=image_data_uri(MASTER_PATH),
                )
            )

        if mode in {"all", "variants"}:
            if not MASTER_PATH.exists():
                raise FileNotFoundError(f"Missing master image: {MASTER_PATH}")
            reference = image_data_uri(MASTER_PATH)
            variants = VARIANTS
            style_index = os.getenv("IMAGE_STYLE_INDEX")
            if style_index:
                requested_index = int(style_index)
                if not 1 <= requested_index <= len(variants):
                    raise ValueError(f"Invalid IMAGE_STYLE_INDEX: {requested_index}")
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
