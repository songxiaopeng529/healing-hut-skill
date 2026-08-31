#!/usr/bin/env python3
import asyncio
import httpx
import json
import os
import sys

API_KEY = os.environ["ARK_API_KEY"]
ENDPOINT_ID = os.environ["SEEDREAM_ENDPOINT_ID"]
API_URL = "https://ark.cn-beijing.volces.com/api/v3/images/generations"

PROMPTS = [
    {
        "name": "01_樱花粉都市夜景三层LOFT",
        "prompt": (
            "Photorealistic architectural cross-section interior of a cozy warm wood style 3-story urban LOFT, "
            "bright vivid cherry blossom pink and cream white color palette, high-angle dollhouse cutaway view, "
            "extremely well-lit, NOT dark at all, bright warm yellow lighting throughout. "
            "Ground floor: cream L-shaped sofa with pink cushions, wooden coffee table with fruit tray and wine glasses, "
            "fluffy area rug, open kitchen with light oak cabinets, sink, gas stove, oven, mini fridge, bathroom nook "
            "with toilet and sink through doorway. "
            "TWO CONTINUOUS WOODEN STAIRCASES with white metal railings: first staircase CLEARLY CONNECTS floor 1 to "
            "floor 2 with every individual step physically walkable, no floating steps. "
            "Second floor: 2 bedrooms with cherry blossom pink bed linens and cute cartoon pillows, study desk with "
            "computer monitor, bookshelf full of books, wardrobe with hanging clothes. "
            "Second CONTINUOUS staircase from floor 2 to floor 3, every step visible and walkable. "
            "Third floor: 2 bedrooms with floral bedcovers, wardrobe area, open decorative shelves with plants. "
            "Left side full-height floor-to-ceiling windows showing glittering city night skyline with neon lights. "
            "Starry LED ceiling pattern, potted cherry blossom branches, framed cute art, LED strip lights under every "
            "stair step, potted colorful flowers on every level, warm cozy healing atmosphere, sharp focus, "
            "ultra detailed interior design magazine quality, 8k"
        ),
        "size": "1536x2048",
    },
    {
        "name": "02_抹茶森系玻璃阳光三层LOFT",
        "prompt": (
            "Photorealistic architectural cross-section interior of a warm wood style 3-story forest LOFT, "
            "bright vivid matcha sage green and cream white color palette, warm wood furniture tones, "
            "flooded with bright natural sunlight, NOT dark at all. "
            "Ground floor: plush matcha green leather sofa with brown cushions, large round fluffy cream rug, "
            "home office with wooden desk, dual computer monitors, ergonomic chair, washing machine below counter, "
            "built-in bookshelves full of books. "
            "SINGLE CONTINUOUS WHITE WOOD STAIRCASE wrapping around the right side, CLEARLY CLIMBS from floor 1 "
            "THROUGH floor 2 TO floor 3 with EVERY STEP INDIVIDUALLY VISIBLE and physically walkable, no breaks, "
            "complete path from bottom to top with white metal railing. "
            "Second floor: open kitchen with light wood cabinets, gas stove, oven, range hood, round platform bed "
            "with thick matcha green quilt, small dining area. "
            "Third floor: staircase continues clearly up, suspended round platform bedroom with sage green duvet "
            "and fluffy pillows, cozy reading nook. "
            "GLASS SKYLIGHT AND FULL-HEIGHT WINDOWS on all sides showing lush green bamboo forest and leafy tree canopy. "
            "Starry LED ceiling lights, hanging climbing vines on interior walls, potted fiddle leaf fig plant, "
            "small tabby cat sleeping on a shelf, recessed spotlights, warm fairy lights, cozy delicate healing "
            "atmosphere, dollhouse cutaway perspective, sharp focus, ultra detailed, photorealistic interior "
            "photography, 8k"
        ),
        "size": "1536x2048",
    },
    {
        "name": "03_琥珀橙都市夜景三层LOFT",
        "prompt": (
            "Photorealistic architectural cutaway interior of a warm wood style 3-story urban LOFT, "
            "bright vivid amber orange and teal and cream color palette, extremely well-illuminated, NOT dark, "
            "bright warm ambient lighting in every room. "
            "Ground floor: dark forest green leather L-shaped sofa with bright yellow and cartoon character cushions, "
            "large round black-and-white patterned rug, wooden TV cabinet with flat screen TV playing cartoon, "
            "open kitchen with teal lower walls, light oak upper cabinets, sink, gas stove, built-in oven, "
            "fresh fruit bowls on countertops. "
            "DOUBLE WOODEN STAIRCASE with black metal railings: FIRST FLIGHT CONTINUOUSLY CONNECTS floor 1 to "
            "floor 2 with EVERY STEP WALKABLE and clearly visible, no impossible gaps. "
            "Second floor: 2 bedrooms with blue floral quilted bed linens on wooden bed frames, nightstands with lamps, "
            "study desk with computer, large bookshelf, wardrobe with hanging clothes. "
            "SECOND STAIR FLIGHT CONTINUOUSLY CLIMBS from floor 2 to floor 3, complete path, all steps present. "
            "Third floor: another bedroom, open study area with desk. "
            "Huge left-side windows showing night city skyline with glowing skyscrapers, top triangular skylight "
            "showing bamboo trees. Wall-mounted wood shelves with ceramic vases and pottery, framed oil paintings "
            "everywhere, wall sconce lamps with warm bulbs, potted pink yellow flowers on all floors, LED lights "
            "on stairs, warm wood cozy delicate style, dollhouse cross-section view, sharp focus, ultra detailed, "
            "architectural photography, 8k"
        ),
        "size": "1536x2048",
    },
    {
        "name": "04_奶盐海风海景三层LOFT",
        "prompt": (
            "Photorealistic architectural cross-section interior of a warm wood style 3-story coastal LOFT, "
            "bright vivid ocean blue and cream white and sandy beige color palette, flooded with bright coastal "
            "sunlight, NOT dark, cheerful airy atmosphere. "
            "Ground floor: cream white sectional sofa with ocean blue striped cushions, wooden coffee table with "
            "fresh seafood platter and fruit, woven jute area rug, open kitchen with white shaker cabinets, "
            "blue subway tile backsplash, sink, gas stove, oven, breakfast bar with stools, powder room with "
            "sink and toilet. "
            "TWO LIGHT WOOD STAIRCASES with white railing: FIRST STAIRCASE CONTINUOUSLY CONNECTS floor 1 to floor 2 "
            "with EVERY INDIVIDUAL STEP CLEARLY VISIBLE AND WALKABLE, no breaks in the steps. "
            "Second floor: 2 bedrooms with nautical blue striped bedspreads on wood bed frames, ocean themed "
            "framed art, study desk with sea view, wardrobe with linen clothes. "
            "SECOND STAIRCASE CONTINUES from floor 2 to floor 3, complete path, all steps present, nautical rope "
            "handrail accent. "
            "Third floor: master bedroom with plush reading chair, floor lamp, open wardrobe. "
            "Large left-side floor-to-ceiling windows showing turquoise ocean view with gentle waves and whitecaps, "
            "seagulls flying in bright blue sky, top skylight with puffy white clouds. Potted palm plants, seashell "
            "decorations, woven rattan lampshades, driftwood wall art, LED step lights, warm natural sunlight "
            "pouring through windows, cozy warm wood beach house aesthetic, dollhouse cutaway perspective, sharp "
            "focus, ultra detailed interior design, 8k quality"
        ),
        "size": "1536x2048",
    },
]

HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}",
}

async def generate_one(task, idx, timeout=600):
    body = {
        "model": ENDPOINT_ID,
        "prompt": task["prompt"],
        "size": task["size"],
        "watermark": False,
        "output_format": "jpeg",
    }
    print(f"[{idx}] Generating: {task['name']} ...", flush=True)
    try:
        async with httpx.AsyncClient(timeout=float(timeout)) as client:
            resp = await client.post(API_URL, headers=HEADERS, json=body)
            resp.raise_for_status()
            data = resp.json()
            if "data" in data and len(data["data"]) > 0:
                url = data["data"][0]["url"]
                print(f"[{idx}] SUCCESS: {task['name']}", flush=True)
                return {"name": task["name"], "url": url, "error": None}
            else:
                err = data.get("error", "unknown")
                print(f"[{idx}] API ERROR: {err}", flush=True)
                return {"name": task["name"], "url": None, "error": str(err)}
    except Exception as e:
        print(f"[{idx}] EXCEPTION: {e}", flush=True)
        return {"name": task["name"], "url": None, "error": str(e)}

async def main():
    results = await asyncio.gather(*[generate_one(t, i+1) for i, t in enumerate(PROMPTS)])
    print("\n" + "="*80)
    print("FINAL RESULTS")
    print("="*80)
    for r in results:
        status = "OK" if r["url"] else "FAIL"
        print(f"  [{status}] {r['name']}")
        if r["url"]:
            print(f"         {r['url']}")
        else:
            print(f"         Error: {r['error']}")
    print(json.dumps(results, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    asyncio.run(main())
