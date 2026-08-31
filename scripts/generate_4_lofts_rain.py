#!/usr/bin/env python3
import asyncio
import base64
import json
import os
from pathlib import Path
from typing import Optional

import httpx


API_URL = "https://ark.cn-beijing.volces.com/api/v3/images/generations"
API_KEY = os.environ["ARK_API_KEY"]
ENDPOINT_ID = os.environ["SEEDREAM_ENDPOINT_ID"]
OUTPUT_DIR = Path(__file__).resolve().parents[1] / "assets" / "loft-variants"
ANCHOR_PATH = OUTPUT_DIR / "01-anchored-sakura-city-rain.jpeg"
ROMANTIC_OUTPUT_DIR = (
    Path(__file__).resolve().parents[1] / "assets" / "romantic-loft-variants"
)
COZY_COTTAGE_V2_DIR = (
    Path(__file__).resolve().parents[1] / "assets" / "cozy-cottage-v2"
)
RAINY_FLOWER_BEDROOM_DIR = (
    Path(__file__).resolve().parents[1] / "assets" / "rainy-flower-bedroom"
)
ROMANTIC_PREVIEW_PATH = ROMANTIC_OUTPUT_DIR / "01-rain-garden-loft-preview.jpeg"
BLIZZARD_PREVIEW_PATH = ROMANTIC_OUTPUT_DIR / "02-blizzard-soft-nest-preview.jpeg"
CRESCENT_STAIR_PREVIEW_PATH = (
    ROMANTIC_OUTPUT_DIR / "03-blizzard-crescent-ribbon-stair-preview.jpeg"
)
COZY_COTTAGE_V2_PREVIEW_PATH = (
    COZY_COTTAGE_V2_DIR / "01-winter-hearth-cottage-preview.jpeg"
)
RAINY_FLOWER_BEDROOM_PREVIEW_PATH = (
    RAINY_FLOWER_BEDROOM_DIR / "01-rainy-flower-bedroom-preview.jpeg"
)

ANCHOR_PROMPT = """
Create a photorealistic, close, near-frontal interior architectural cutaway of one fixed, buildable two-floor loft.
The camera is directly at the removed front wall with a 24-28 mm architectural lens. The interior fills 92 percent
of the frame. Do not show an exterior facade, foundation, stilts, surrounding ground, or distant miniature house.

LOCKED FLOOR PLAN, DO NOT IMPROVISE:
- Exactly two floors and one roof. No third floor and no hidden mezzanine.
- Ground floor front-left: one double-height living room with sofa, coffee table, rug and media cabinet.
- Ground floor rear-left: one open L-shaped kitchen and dining zone. Clearly show refrigerator, sink, worktop,
  cooktop, hood, oven, cabinets and a two-seat dining table.
- Ground floor rear-center: exactly one compact enclosed toilet room, separate from the kitchen and not under the
  staircase. Its front cutaway clearly shows one toilet bowl, one hand-washing sink, mirror and tiled wall.
  Its single open doorway faces the central circulation aisle. This bathroom door is the only visible interior door.
- Ground floor entire right side: exactly one straight conventional wooden staircase, fully visible in side profile.
  Its bottom step rests on the ground floor at front-right. It has 17 continuous walkable steps, no turn and no
  intermediate landing. Its final top step is flush with a 1.2 m wide second-floor landing at rear-right.
  The stair cannot end at a wall, railing, window, room, or void. Handrails run continuously on both sides.
  The area below the stair is open shelving only, never a room, toilet or closed door.
- Second floor occupies the rear 55 percent of the footprint. It contains one open loft bedroom suite only:
  bed against the solid rear wall, two nightstands, wardrobe, desk and reading chair. No bedroom door, no partition,
  no extra room. The stair landing opens directly and visibly into this bedroom zone.
- The second-floor front edge is one straight floor edge with a continuous 110 cm safety railing. The railing wraps
  safely around the stair opening but never blocks the last stair. No balcony, no projecting platform, no bridge,
  no split-level floor. The bed is at least 1.5 m behind the guarded edge.
- Clear circulation and realistic furniture clearances. All four spaces - living room, kitchen, toilet and bedroom -
  must be simultaneously recognizable in the same image.

HEALING RAIN ATMOSPHERE:
Heavy rain exists outside only. Every window shows diagonal rain beyond the glass and large droplets and long water
trails on the exterior surface. Interior remains dry, bright and warmly illuminated. Use cream walls, honey-oak
joinery, cherry-blossom pink and mint textiles, a cream sofa, floral bedding, layered cushions, warm table lamps,
framed botanical art, books, ceramics, flowers and healthy plants. Colorful, refined, orderly and cozy, never dark.
Premium interior-design magazine photography, realistic materials, sharp details, 8k.
""".strip()

PRESERVE_ARCHITECTURE = """
Use the supplied image as an immutable architectural and camera reference. Preserve exactly the same two-floor
geometry, crop, viewpoint, walls, floor slabs, ceiling, windows, one straight staircase, every stair tread, top
landing, safety railings, kitchen footprint, toilet-room position, single bathroom doorway, furniture circulation,
living-room position and bedroom position. Do not add, remove, move, widen or redesign any architectural element.
Do not add doors, partitions, rooms, balconies, platforms, stairs or bathrooms. The last stair must remain visibly
flush with the open second-floor landing. Keep the four required spaces simultaneously visible. Change only colors,
movable furniture styling, textiles, lamps, artwork, plants and small decorative objects. Keep heavy rain outside all
windows, visible droplets on exterior glass, and a dry bright warm interior.
""".strip()

VARIANTS = [
    {
        "name": "02-anchored-matcha-forest-rain",
        "prompt": (
            PRESERVE_ARCHITECTURE
            + " Restyle only the decor in a luminous matcha green, ivory, pale oak and lemon-yellow palette. "
            "Use a sage boucle sofa, checked cushions, cream circular rug, pale-oak tables, green linen bedding, "
            "woven pendant lights, botanical prints, ceramic vases, baskets, books and abundant leafy plants. "
            "Through the unchanged windows show a rain-softened bamboo forest. Photorealistic and refined."
        ),
    },
    {
        "name": "03-anchored-amber-teal-city-rain",
        "prompt": (
            PRESERVE_ARCHITECTURE
            + " Restyle only the decor in saturated teal, warm amber, walnut, cream and mustard accents. "
            "Use a deep teal leather sofa, amber velvet cushions, geometric black-and-cream rug, walnut tables, "
            "blue floral bedding, brass lamps, record-player accessories, gallery-wall art, books, pottery and "
            "coral flowers. Through the unchanged windows show a rainy city skyline. Photorealistic and elegant."
        ),
    },
    {
        "name": "04-anchored-coral-coastal-rain",
        "prompt": (
            PRESERVE_ARCHITECTURE
            + " Restyle only the decor in bright coral, turquoise, cream, natural ash wood and sunny-yellow accents. "
            "Use a cream linen sofa, coral and turquoise cushions, woven jute rug, ash tables, coral-and-blue bedding, "
            "rattan lamps, coastal paintings, shells, baskets, books and tropical plants. Through the unchanged "
            "windows show a turquoise sea under heavy rain. Photorealistic, bright, warm and sophisticated."
        ),
    },
]

ROMANTIC_PREVIEW_PROMPT = """
Create a photorealistic, romantic, highly desirable two-floor loft interior during heavy rain. Use a close,
near-frontal architectural cutaway from the removed front wall with a 24-28 mm lens. The interior fills 92 percent
of the vertical frame. Do not show an exterior facade, foundation, stilts, surrounding ground or miniature-house view.

FIXED BUILDABLE FLOOR PLAN:
- Exactly two floors and one roof, no third floor or hidden mezzanine.
- A structurally framed, two-story floor-to-ceiling glass curtain wall spans about 60 percent of the left facade.
  Large rain droplets and long water trails cover the exterior glass. Soft rain curtains and a distant garden are
  visible outside; all rain remains outside and the interior is completely dry.
- Ground-floor front-left is a romantic living room facing the glass: one generous curved cream boucle sofa, oval rug,
  low rounded walnut coffee table and a cushioned rain-watching window bench. A small orange tabby cat is visibly curled
  up asleep on the left sofa cushion. A beautiful natural-wood acoustic guitar rests safely on the opposite sofa
  cushion, fully visible and correctly proportioned. Neither object blocks circulation.
- Ground-floor rear-left is one complete open kitchen with warm walnut cabinetry, pale stone worktop, refrigerator,
  sink, cooktop, hood and oven. A rounded island and a four-seat circular dining table create an intimate dining zone.
- Ground-floor rear-center is exactly one compact enclosed toilet room, not under the staircase. Through its cutaway
  opening clearly show one toilet bowl, one hand-washing sink, mirror and green floral tiles. Its open door faces the
  central aisle. This bathroom door is the only visible interior door.
- The entire right side contains exactly one straight conventional wooden staircase, fully visible in side profile.
  The bottom step rests on the ground floor at front-right. Seventeen continuous rectangular steps rise in one
  uninterrupted flight with no turn and no intermediate landing. The final step is flush with a 1.2 m wide
  second-floor landing at rear-right. Continuous handrails run on both sides. The area below the stair is open
  illuminated bookshelves and plants only, never another room, bathroom or door.
- The second floor occupies the rear 55 percent and contains one open bedroom suite only. No bedroom door, partition,
  extra room, bridge, balcony or projecting platform. The landing opens directly into the bedroom. Place a bed against
  the solid rear wall, facing the large rain window, with two nightstands, wardrobe, curved vanity, reading chair and
  bookshelves. Keep the bed at least 1.5 m behind the open edge.
- The second-floor front edge is a single straight edge protected by one continuous 110 cm oak-and-brass railing.
  The railing wraps around the stair opening without blocking the last step.
- Living room, kitchen, toilet, bedroom, stair bottom, every stair tread and stair-top landing must all be
  simultaneously visible and physically connected.

ROMANTIC INTERIOR DIRECTION:
Use a luminous palette of warm ivory, blush apricot, muted rose, emerald green, honey walnut and small brass accents.
Add gauzy curtains that do not hide the rain, scalloped cushions, floral linen bedding, a paper pendant above the
dining table, warm wall sconces, concealed 2700K cove lighting, botanical paintings, handmade ceramics, stacked books,
fresh flowers and abundant healthy plants. Rounded furniture and gentle arches may appear only in decor and joinery,
never as impossible structural geometry. Bright, intimate, layered, sophisticated and full of lived-in warmth.
Premium interior-design magazine photography, realistic materials, sharp details, 8k.
""".strip()

BLIZZARD_PREVIEW_PROMPT = """
Create a photorealistic, intensely cozy two-floor soft-nest loft during a violent winter blizzard. Use a close,
near-frontal architectural interior cutaway from the removed front wall with a 24-28 mm lens. The interior fills
92 percent of the vertical frame. This is an emotional hero room, not a complete-home floor-plan presentation.
Do not show a kitchen, toilet, bathroom, appliances, service doors, exterior facade, foundation or distant model.
Kitchen and bathroom exist in an unseen service core behind the camera and are completely outside this composition.

PHYSICALLY BUILDABLE TWO-FLOOR STRUCTURE:
- Exactly two floors and one roof, no third floor and no hidden mezzanine.
- The left facade is a structurally framed two-story floor-to-ceiling glass wall. Outside is a fierce blizzard with
  dense wind-driven snow, snow-covered trees and a cold blue-grey night. Snow and ice cling to the exterior glass,
  with meltwater trails and frosted edges. All snow remains outside; the interior is completely dry.
- Ground floor center-left contains one enormous 2.8 m circular upholstered lounge bed, only 20 cm above the floor.
  It has a thick mattress, continuous padded curved backrest, quilted cover, layered wool blankets, faux-fur throws
  and many soft velvet, boucle and knitted pillows. A small orange tabby cat sleeps curled up on the lounge bed.
  A correctly proportioned natural-wood acoustic guitar rests safely beside the pillows on the same lounge bed.
- Surround the lounge with two overlapping deep-pile rugs, a large faux-fur floor cushion, two soft poufs, a low
  rounded walnut table, thick full-height curtains, a padded rain-and-snow viewing bench, books and a blanket basket.
- The entire right wall contains exactly one straight wooden staircase. Its first step rests on the ground floor at
  front-right. Seventeen continuous rectangular steps rise in one uninterrupted flight, with no turn or intermediate
  landing. The final step is flush with a wide second-floor landing. Continuous handrails run on both sides.
  Under the stair are open illuminated bookshelves, folded blankets and plants only; no room and no door.
- The second floor occupies the rear half and contains one protected sleeping nest only. A huge low soft bed sits
  inside a deep alcove enclosed by solid walls on the back and both sides. The open front side is protected by one
  continuous 110 cm safety railing, and the bed remains at least 1.5 m behind it. The stair landing opens directly
  into the sleeping nest with no door, partition, balcony, bridge, level change or obstruction.
- The upper bed has an extra-thick mattress, oversized duvet, layered quilts, knitted throws, many pillows, a padded
  headboard, upholstered wall panels, two warm bedside lamps and a soft bench. Include a compact reading nook with
  an enveloping armchair and footstool, without creating another room.
- Stair bottom, every tread, top landing and its direct connection to the upper sleeping area are fully visible.

ATMOSPHERE AND MATERIALS:
At least 65 percent of visible furnishings are soft textiles. Use warm ivory, oatmeal, blush apricot, caramel,
muted rose, moss green and honey-walnut accents. Add 2400-2700K concealed cove lighting, warm stair lights, paper
lanterns, soft wall sconces, candles in safe glass holders, gauzy inner curtains plus thick outer curtains, floral
textiles, books, handmade ceramics and healthy plants. Keep the interior bright and warmly exposed, not dark.
The extreme cold blue blizzard outside must contrast strongly with the luminous amber cocoon inside.
Premium interior-design photography, realistic construction, tactile textile detail, cinematic but natural, 8k.
""".strip()

CRESCENT_STAIR_PROMPT = """
Use the supplied blizzard soft-nest loft image as the visual reference. Preserve the exact camera position,
two-floor structure, floor-to-ceiling snow windows, upper sleeping nest, circular ground-floor lounge bed, cat,
acoustic guitar, rugs, curtains, lighting, colors, furniture positions and violent blizzard outside.

CHANGE ONLY THE STAIRCASE AND ITS RAILING:
- Replace the straight staircase on the right with one broad, elegant crescent-shaped ribbon staircase.
- This is a gently curving quarter-arc staircase, NOT a spiral staircase, NOT a helix, and has no center pole.
- The bottom step rests at the same ground-floor front-right starting point.
- Approximately 17 wide, solid, closed-riser walnut steps follow one continuous shallow crescent curve.
- Every tread is physically walkable and maintains safe usable depth across its full walking line.
- There is no intermediate landing, no branch, no missing step, no floating tread and no change of direction.
- The final top step arrives flush at the same wide second-floor sleeping-nest entrance, visibly unobstructed.
- The outer edge is wrapped by one continuous sculptural ivory plaster ribbon parapet, 110 cm high.
- The inner edge has a continuous rounded walnut handrail supported by slim brushed-brass balusters.
- The upper guardrail flows naturally out of the stair parapet without a break, gate, wall or balcony.
- A warm concealed LED line follows beneath the curved ribbon edge.
- Beneath the curve, integrate open illuminated bookshelves, folded blankets and plants only; no room or door.
- Show the whole stair path clearly in the image, including bottom step, every tread and top connection.

The result must look structurally buildable, luxurious, romantic and sculptural. Keep the interior bright, soft and
warm against the cold blue blizzard. Do not alter any other part of the reference image. Photorealistic premium
interior-design magazine photography, tactile textiles, realistic construction, sharp detail, 8k.
""".strip()

CRESCENT_STYLE_PRESERVE = """
Use the supplied crescent-ribbon-stair blizzard loft image as an immutable architecture and composition reference.
Preserve the exact camera, crop, two-floor structure, floor slabs, ceiling, windows, upper sleeping nest, circular
ground-floor lounge bed, crescent ribbon staircase, every stair tread, both stair endpoints, parapets, glass guardrail,
open shelves, cat, acoustic guitar and all circulation clearances. Do not add, remove, move or redesign any wall,
window, floor, stair, landing, railing, room, door or large furniture footprint. The crescent staircase must remain
physically continuous from the ground floor to the upper sleeping area. Keep the same orange tabby cat sleeping on
the lounge and the same guitar beside the pillows. Keep the fierce blizzard outside the unchanged glass wall and
the interior dry, bright and warmly illuminated. Change only palette, movable furniture upholstery, bedding, rugs,
curtains, lamps, artwork, plants, books and small decorative objects. Photorealistic premium interior photography.
""".strip()

CRESCENT_STYLE_VARIANTS = [
    {
        "name": "04-crescent-nordic-berry-snow",
        "prompt": (
            CRESCENT_STYLE_PRESERVE
            + " Restyle the decor as a romantic Nordic alpine snow retreat. Use luminous ivory, pale ash wood, "
            "cranberry red, cloud blue and small forest-green accents. Dress the circular lounge in ivory boucle "
            "with cranberry plaid wool blankets, oversized cable-knit cushions and sheepskins. Use pale-blue and "
            "cranberry layered bedding upstairs, slim opal-glass lamps, handwoven geometric rugs, simple winter "
            "botanical prints, birch accessories, baskets of blankets and restrained evergreen branches. Keep the "
            "space airy, tactile, colorful and very warm, never grey or minimal to the point of feeling empty."
        ),
    },
    {
        "name": "05-crescent-art-nouveau-jewel-snow",
        "prompt": (
            CRESCENT_STYLE_PRESERVE
            + " Restyle the decor as a lush contemporary Art Nouveau soft nest. Use emerald green, dusty plum, "
            "peacock blue, warm cream and antique brass. Upholster the circular lounge in deep emerald velvet with "
            "plum, peacock and embroidered botanical cushions, layered with a cream faux-fur throw. Use richly "
            "quilted jewel-tone bedding upstairs, curved brass-and-opal lamps, flowing floral rugs, botanical artwork, "
            "sculptural vases, trailing plants and delicate stained-glass-inspired accents. Keep it bright, elegant, "
            "romantic and sumptuous rather than dark, theatrical or antique."
        ),
    },
    {
        "name": "06-crescent-japanese-indigo-snow",
        "prompt": (
            CRESCENT_STYLE_PRESERVE
            + " Restyle the decor as a warm contemporary Japanese textile loft. Use natural cedar, warm ivory, "
            "indigo blue, persimmon orange and moss green. Cover the circular lounge with thick ivory cotton, indigo "
            "shibori cushions, persimmon quilted throws and soft moss floor poufs. Use layered indigo-and-ivory bedding "
            "upstairs, washi paper lanterns, woven tatami-inspired rugs softened by wool overlays, ceramic tea ware, "
            "low rounded wood tables, ikebana branches, linen curtains and carefully arranged books. Keep the room "
            "plush, intimate, colorful and softly glowing, not sparse or austere."
        ),
    },
]

COZY_COTTAGE_V2_PROMPT = """
Create a photorealistic high-end interior-design magazine cutaway of one physically buildable two-floor cozy cottage,
vertical 3:4 composition with safe space for a later 9:16 crop. Use a close elevated three-quarter view from slightly
front-left so the complete ground floor, second floor and both flights of the staircase are simultaneously visible.
The cottage fills 90 percent of the frame. Do not show a distant model, foundation, stilts or unrelated exterior.

LOCKED ARCHITECTURE:
- Exactly two floors under one pitched roof. The rear 60 percent supports the second floor; the front living room is
  double height. Main circulation headroom is at least 2.4 m. No third floor or hidden mezzanine.
- Ground-floor front-left: a double-height living room with one large curved cream upholstered sofa, generous ottoman,
  rounded wood coffee table, thick wool rug, irregular long-pile rug and a padded window daybed. Add abundant knitted
  cushions, quilted blankets and faux-fur throws. One orange tabby cat rests on the sofa and one natural-wood acoustic
  guitar stands safely beside it without blocking circulation.
- On the solid inner living-room wall, install one compact closed-combustion fireplace with a glass fire door,
  fireproof stone hearth and a real enclosed flue continuing vertically through the roof. Keep fireplace, sofa,
  curtains and staircase at safe realistic distances. Use a small steady amber flame.
- Ground-floor rear-left: one complete kitchen and circular dining area with warm wood cabinets, refrigerator, sink,
  worktop, cooktop, hood, oven, round dining table and four upholstered chairs. Maintain a clear work triangle.
- Ground-floor rear-center: exactly one enclosed bathroom, fully separate from kitchen and stairs. Its cutaway view
  shows one toilet, one hand-washing sink and mirror. Its only door opens toward the central corridor, never toward
  the kitchen or living room.
- Ground-floor front-right: clear main entry and compact upholstered shoe bench.
- Right side: one code-compliant L-shaped wooden staircase, 1.05 m wide. The first flight starts at front-right and
  rises through exactly 8 continuous rectangular steps to a fully supported 1.15 m by 1.15 m square landing at
  rear-right. The stair then turns exactly 90 degrees. A second flight of exactly 9 continuous rectangular steps
  rises from that landing to the second-floor landing. The final step is flush with the second-floor slab.
  Show the first flight, square turning landing, second flight and upper exit clearly. Continuous 1.1 m guards and
  handrails protect both flights and the landing. No floating steps, missing treads, split stairs or blocked exits.
  Under the first flight are open bookshelves, blanket baskets, wall lights and plants only, never a room or door.
- Second floor: exactly one master bedroom at the rear with a wide low bed against a solid wall, thick mattress,
  oversized duvet, layered knitted throws, many pillows, padded headboard, soft bench, wardrobe and vanity. A reading
  nook sits beside the large window with an enveloping armchair, footstool and small round table. The stair exit opens
  directly into the bedroom zone without another door. Every open edge has a continuous 1.1 m safety railing, and the
  bed remains at least 1.5 m from the edge. No second bedroom, balcony, bridge or mystery door.

WINTER AND WARMTH:
A large structurally framed two-story gable window fills the front-left facade. Outside is a fierce bone-chilling
winter blizzard: fast diagonal snow, turbulent snow fog, snow-laden pine trees, distant whiteout, exterior ice crystals
and meltwater trails. All snow stays outside. Inside is dry, bright and warmly exposed at 2400-2700K using fireplace
light, hidden cove lights, paper lamps, wall sconces and stair lighting.

Use warm ivory, oatmeal, blush apricot, cranberry red, moss green, honey oak and small brass accents. At least 65
percent of visible furnishings should feel soft and tactile. Include full-height curtains that do not hide the snow,
botanical art, books, ceramics, flowers and healthy plants. Romantic, colorful, layered and sophisticated, never dark.
Ultra-realistic textiles, wood, glass, flame and snow, sharp detail, HDR, 8k.

Strictly avoid: extra floors, extra rooms, duplicate bathrooms, unexplained doors, mini balconies, broken stairs,
stairs ending at walls, railing blocking the upper exit, floating furniture, bed near an unguarded edge, indoor snow,
fabric intersections, deformed architecture, neon cyberpunk lighting, people, text or watermark.
""".strip()

COZY_COTTAGE_V2_FIX_PROMPT = """
Use the supplied winter hearth cottage image as a reference. Preserve its two-floor cottage identity, pitched timber
ceiling, huge snowy gable window, living room, kitchen, single bathroom, fireplace, cat, guitar, soft furnishings,
master bedroom, colors and blizzard atmosphere. Correct the camera and staircase architecture as follows.

CAMERA: move the viewpoint closer to the removed front wall so the interior fills about 92 percent of the frame.
Crop away the exterior roof silhouette, white background, foundation slab and miniature-dollhouse appearance, while
keeping enough pitched interior ceiling to read as a cottage.

STAIRCASE: rebuild the right-side stair as one clearly readable, code-compliant L-shaped stair. The first flight starts
on the ground floor at front-right and climbs through 8 continuous rectangular steps along the right wall to a fully
supported 1.15 m square landing at rear-right. At this visible landing, the stair turns exactly 90 degrees left. The
second flight then climbs through 9 continuous rectangular steps along the rear wall to a clearly open 1.2 m wide
gap in the second-floor edge. The final tread is visibly flush with the second-floor bedroom landing. Show the entire
route from bottom step through both flights and the square landing to the unobstructed upper opening. Continuous
handrails and 1.1 m guards protect both flights and landing. The upper guardrail stops neatly at the stair opening
and resumes after it; it must not block access. No missing tread, floating tread, branch, extra stair, door, wall,
bed or furniture may obstruct the path. Keep the bathroom completely separate from and outside the stair footprint.

Preserve physical construction, warm soft textiles, small safe fireplace and fierce outdoor blizzard. Photorealistic
premium interior-design photography, close architectural cutaway, sharp detail, 8k.
""".strip()

COZY_COTTAGE_V2_PRESERVE = """
Use the supplied winter hearth cottage image as an immutable architectural and camera reference. Preserve the exact
close cutaway viewpoint, two-floor pitched-roof shell, exposed roof beams, gable glass wall, fireplace and vertical
flue, kitchen zone, single bathroom, entry, L-shaped two-flight staircase, turning area, every stair tread, upper
stair opening, bedroom floor, safety railings and all circulation paths. Do not add, remove, move or redesign any
wall, roof, floor slab, window, fireplace, chimney, stair, railing, room, bathroom or door. The staircase must remain
physically continuous from the ground floor to the open upper bedroom landing. Keep the fierce blizzard outside and
the interior dry, bright and warmly illuminated. Keep one orange tabby cat and one acoustic guitar in the living room.
Change all movable furniture designs, upholstery, bedding, rugs, curtains, lighting fixtures, artwork, decorative
objects, plants, and cabinet finishes according to the requested style while keeping each functional zone in the same
place and maintaining realistic clearances. Photorealistic premium interior-design photography, sharp detail, 8k.
""".strip()

COZY_COTTAGE_V2_STYLE_VARIANTS = [
    {
        "name": "02-nordic-berry-hearth-cottage",
        "prompt": (
            COZY_COTTAGE_V2_PRESERVE
            + " Transform the complete furniture and decor into a rich Nordic alpine style. Replace the living-room "
            "seating with a low pale-ivory modular cloud sofa and a rounded pale-ash lounge chair. Use a sculptural "
            "light-ash coffee table, cranberry plaid wool blankets, sky-blue cable-knit cushions, thick white "
            "sheepskins, and a handwoven geometric rug. Replace the dining furniture with a pale-oak round pedestal "
            "table and curved spindle-back chairs with soft seat pads. Use pale-ash kitchen fronts, opal-glass lamps, "
            "simple winter botanical prints, berry-red curtains and layered cloud-blue bedroom textiles. Palette: "
            "ivory, pale ash, cranberry, cloud blue and forest green. Warm, colorful and deeply tactile, never sparse."
        ),
    },
    {
        "name": "03-jewel-art-deco-hearth-cottage",
        "prompt": (
            COZY_COTTAGE_V2_PRESERVE
            + " Transform the complete furniture and decor into luminous contemporary Art Deco. Replace the sofa "
            "with a scalloped emerald velvet sectional and add plum barrel chairs. Use an oval dark-walnut and brass "
            "coffee table, a cream-and-black fan-pattern rug, peacock and burgundy cushions, and a jewel-tone throw. "
            "Replace the dining set with a round fluted-walnut table and upholstered teal chairs. Use deep teal "
            "ribbed kitchen fronts, brass pulls, opal globe pendants, framed geometric botanical art, floor-length "
            "plum velvet curtains, and a tall channel-tufted sapphire bed with emerald and burgundy bedding. Palette: "
            "emerald, peacock blue, dusty plum, warm cream, walnut and antique brass. Bright, sumptuous and romantic."
        ),
    },
    {
        "name": "04-japanese-indigo-hearth-cottage",
        "prompt": (
            COZY_COTTAGE_V2_PRESERVE
            + " Transform the complete furniture and decor into a warm contemporary Japanese textile style. Replace "
            "the sofa with a low deep-cushioned ivory linen modular sofa on a cedar plinth, accompanied by moss-green "
            "floor poufs. Use a low organic cedar slab coffee table, layered wool-over-tatami rugs, indigo shibori "
            "cushions and a persimmon quilt. Replace the dining set with a round solid-cedar table and four curved "
            "wood chairs with linen seats. Use natural cedar kitchen fronts, washi paper lanterns, handmade ceramics, "
            "simple ink botanicals, indigo linen curtains, and a low platform bed with indigo, ivory and persimmon "
            "bedding. Palette: cedar, warm ivory, indigo, persimmon and moss. Plush and intimate, never austere."
        ),
    },
    {
        "name": "05-french-garden-hearth-cottage",
        "prompt": (
            COZY_COTTAGE_V2_PRESERVE
            + " Transform the complete furniture and decor into a romantic contemporary French garden cottage style. "
            "Replace the sofa with a generous skirted ivory-linen curved sofa and add two dusty-rose bouclé armchairs. "
            "Use an aged-oak oval coffee table, layered floral wool rugs, sage and rose cushions, scalloped throws and "
            "soft checked footstools. Replace the dining furniture with a painted-ivory round table and upholstered "
            "cane-back chairs. Use muted sage kitchen cabinetry with aged-brass hardware, pleated fabric lamps, "
            "botanical paintings, flower-filled ceramics, dusty-rose linen curtains, and a softly curved upholstered "
            "bed with sage, rose and butter-yellow floral bedding. Palette: ivory, dusty rose, sage, butter yellow, "
            "aged oak and brass. Fresh, romantic, bright and richly layered without becoming antique or cluttered."
        ),
    },
]

RAINY_FLOWER_BEDROOM_PROMPT = """
Create a photorealistic, exceptionally cozy small bedroom with sophisticated feminine styling, vertical 3:4 premium
interior-design photography. The physically buildable room is 4.4 m by 4.8 m with a 2.8 m ceiling. Use a close
three-quarter camera view from front-left so the bed, rainy bay window, vanity, wardrobe and television are visible.

Center one 1.8 m by 2.0 m rounded upholstered bed against the solid rear wall, never under the window. Use a tall curved
wingback headboard inside a shallow warm-wood arched niche, two bedside tables and warm sconces. Keep clear passages.
On the left wall, install a 2.2 m double-glazed bay window with a deep built-in cushioned seat, drawers, pillows,
blanket, side table and reading lamp. On the right rear wall, install a floor-to-ceiling warm-white framed wardrobe,
beside a floating vanity with upholstered stool, oval brass mirror, jewelry tray and perfume. The only entry door is
front-right and opens safely against the wall.

Mount one slim 40-inch television on the right-front wall, directly visible from bed, at comfortable eye level with
hidden cables. Its gently glowing screen clearly shows a charming classic hand-drawn cat-and-mouse chase cartoon:
one expressive blue-grey cat chasing one small brown mouse through a warm vintage room. No logo, title, subtitles,
interface, watermark or readable text appears on screen. One real orange tabby cat curls on the bay-window cushion,
clearly distinct from the cartoon. A natural-wood acoustic guitar rests on a stable floor stand near the reading chair.

At least 70 percent of visible furnishings feel soft. Use an extra-thick mattress, oversized duvet, floral quilt,
layered knitted throws, many varied pillows, padded bed-end bench, enveloping boucle reading chair with footstool,
full-height curtains, thick wool rug beneath the bed and a small irregular faux-fur rug near the window. Use velvet,
boucle, washed linen, wool, quilting and knit; avoid bare floors and hard empty surfaces.

Outside is a cool blue-grey rainy night garden with wet dark leaves, distant warm lights, dense diagonal rain, large
drops and long water trails on the exterior glass. All rain remains outside. Use sheer ivory inner curtains and
dusty-rose outer curtains without hiding the rain. The dry interior is bright and warmly lit at 2400-2700K by concealed
headboard light, bedside sconces, vanity glow, a small frosted-glass pendant and reading lamp.

Palette: warm ivory, oatmeal, dusty rose, blush apricot, sage green, honey walnut and small antique-brass details.
Add curated botanical paintings, fresh flowers, books, ceramics and healthy plants. Romantic, layered, intimate,
refined and lived-in, never childish or sugary. Ultra-realistic textiles, wood, glass and rainy reflections, HDR, 8k.

Avoid extra beds, extra doors, bathrooms, kitchens, stairs, lofts, people, duplicate cats, malformed animals, blocked
circulation, television blocking the window, random text, logos, indoor rain, distorted furniture or dark exposure.
""".strip()


def image_data_uri(path: Path) -> str:
    encoded = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:image/jpeg;base64,{encoded}"


async def request_image(
    client: httpx.AsyncClient,
    prompt: str,
    output_path: Path,
    reference_image: Optional[str] = None,
) -> dict:
    body = {
        "model": ENDPOINT_ID,
        "prompt": prompt,
        "size": "1536x2048",
        "watermark": False,
        "output_format": "jpeg",
    }
    if reference_image:
        body["image"] = reference_image

    print(f"Generating {output_path.name}...", flush=True)
    response = await client.post(
        API_URL,
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json",
        },
        json=body,
    )
    if response.is_error:
        print(response.text, flush=True)
    response.raise_for_status()
    image_url = response.json()["data"][0]["url"]

    image_response = await client.get(image_url)
    image_response.raise_for_status()
    output_path.write_bytes(image_response.content)
    print(f"Saved {output_path.name}", flush=True)
    return {
        "name": output_path.stem,
        "path": str(output_path),
        "url": image_url,
        "bytes": len(image_response.content),
    }


async def generate_anchor(client: httpx.AsyncClient) -> dict:
    return await request_image(client, ANCHOR_PROMPT, ANCHOR_PATH)


async def generate_romantic_preview(client: httpx.AsyncClient) -> dict:
    ROMANTIC_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    return await request_image(
        client,
        ROMANTIC_PREVIEW_PROMPT,
        ROMANTIC_PREVIEW_PATH,
    )


async def generate_blizzard_preview(client: httpx.AsyncClient) -> dict:
    ROMANTIC_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    return await request_image(
        client,
        BLIZZARD_PREVIEW_PROMPT,
        BLIZZARD_PREVIEW_PATH,
    )


async def generate_crescent_stair_preview(client: httpx.AsyncClient) -> dict:
    if not BLIZZARD_PREVIEW_PATH.exists():
        raise FileNotFoundError(f"Missing reference image: {BLIZZARD_PREVIEW_PATH}")
    ROMANTIC_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    return await request_image(
        client,
        CRESCENT_STAIR_PROMPT,
        CRESCENT_STAIR_PREVIEW_PATH,
        image_data_uri(BLIZZARD_PREVIEW_PATH),
    )


async def generate_crescent_style_variants(
    client: httpx.AsyncClient,
) -> list[dict]:
    if not CRESCENT_STAIR_PREVIEW_PATH.exists():
        raise FileNotFoundError(
            f"Missing reference image: {CRESCENT_STAIR_PREVIEW_PATH}"
        )
    reference = image_data_uri(CRESCENT_STAIR_PREVIEW_PATH)
    return await asyncio.gather(
        *[
            request_image(
                client,
                variant["prompt"],
                ROMANTIC_OUTPUT_DIR / f"{variant['name']}.jpeg",
                reference,
            )
            for variant in CRESCENT_STYLE_VARIANTS
        ]
    )


async def generate_cozy_cottage_v2_preview(
    client: httpx.AsyncClient,
) -> dict:
    COZY_COTTAGE_V2_DIR.mkdir(parents=True, exist_ok=True)
    return await request_image(
        client,
        COZY_COTTAGE_V2_PROMPT,
        COZY_COTTAGE_V2_PREVIEW_PATH,
    )


async def fix_cozy_cottage_v2_preview(
    client: httpx.AsyncClient,
) -> dict:
    if not COZY_COTTAGE_V2_PREVIEW_PATH.exists():
        raise FileNotFoundError(
            f"Missing reference image: {COZY_COTTAGE_V2_PREVIEW_PATH}"
        )
    reference = image_data_uri(COZY_COTTAGE_V2_PREVIEW_PATH)
    return await request_image(
        client,
        COZY_COTTAGE_V2_FIX_PROMPT,
        COZY_COTTAGE_V2_PREVIEW_PATH,
        reference,
    )


async def generate_cozy_cottage_v2_style_variants(
    client: httpx.AsyncClient,
) -> list[dict]:
    if not COZY_COTTAGE_V2_PREVIEW_PATH.exists():
        raise FileNotFoundError(
            f"Missing reference image: {COZY_COTTAGE_V2_PREVIEW_PATH}"
        )
    reference = image_data_uri(COZY_COTTAGE_V2_PREVIEW_PATH)
    variants = COZY_COTTAGE_V2_STYLE_VARIANTS
    style_index = os.getenv("COZY_STYLE_INDEX")
    if style_index:
        requested_index = int(style_index)
        if not 1 <= requested_index <= len(variants):
            raise ValueError(f"Invalid COZY_STYLE_INDEX: {requested_index}")
        variants = [variants[requested_index - 1]]
    return await asyncio.gather(
        *[
            request_image(
                client,
                variant["prompt"],
                COZY_COTTAGE_V2_DIR / f"{variant['name']}.jpeg",
                reference,
            )
            for variant in variants
        ]
    )


async def generate_rainy_flower_bedroom_preview(
    client: httpx.AsyncClient,
) -> dict:
    RAINY_FLOWER_BEDROOM_DIR.mkdir(parents=True, exist_ok=True)
    return await request_image(
        client,
        RAINY_FLOWER_BEDROOM_PROMPT,
        RAINY_FLOWER_BEDROOM_PREVIEW_PATH,
    )


async def generate_variants(client: httpx.AsyncClient) -> list[dict]:
    if not ANCHOR_PATH.exists():
        raise FileNotFoundError(f"Missing anchor image: {ANCHOR_PATH}")
    reference = image_data_uri(ANCHOR_PATH)
    return await asyncio.gather(
        *[
            request_image(
                client,
                variant["prompt"],
                OUTPUT_DIR / f"{variant['name']}.jpeg",
                reference,
            )
            for variant in VARIANTS
        ]
    )


async def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    mode = os.getenv("LOFT_MODE", "all")
    if mode not in {
        "anchor",
        "variants",
        "all",
        "romantic-preview",
        "blizzard-preview",
        "crescent-stair-preview",
        "crescent-style-variants",
        "cozy-cottage-v2-preview",
        "cozy-cottage-v2-fix",
        "cozy-cottage-v2-style-variants",
        "rainy-flower-bedroom-preview",
    }:
        raise SystemExit(f"Unknown LOFT_MODE: {mode}")

    timeout = httpx.Timeout(900.0)
    results = []
    async with httpx.AsyncClient(timeout=timeout, follow_redirects=True) as client:
        if mode == "romantic-preview":
            results.append(await generate_romantic_preview(client))
        if mode == "blizzard-preview":
            results.append(await generate_blizzard_preview(client))
        if mode == "crescent-stair-preview":
            results.append(await generate_crescent_stair_preview(client))
        if mode == "crescent-style-variants":
            results.extend(await generate_crescent_style_variants(client))
        if mode == "cozy-cottage-v2-preview":
            results.append(await generate_cozy_cottage_v2_preview(client))
        if mode == "cozy-cottage-v2-fix":
            results.append(await fix_cozy_cottage_v2_preview(client))
        if mode == "cozy-cottage-v2-style-variants":
            results.extend(await generate_cozy_cottage_v2_style_variants(client))
        if mode == "rainy-flower-bedroom-preview":
            results.append(await generate_rainy_flower_bedroom_preview(client))
        if mode in {"anchor", "all"}:
            results.append(await generate_anchor(client))
        if mode in {"variants", "all"}:
            results.extend(await generate_variants(client))

    print(json.dumps(results, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    asyncio.run(main())
