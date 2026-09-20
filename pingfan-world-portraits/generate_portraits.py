#!/usr/bin/env python3
import asyncio
import json
import os
from pathlib import Path
from typing import Optional

import httpx


API_URL = "https://ark.cn-beijing.volces.com/api/v3/images/generations"
API_KEY = os.environ["ARK_API_KEY"]
ENDPOINT_ID = os.environ["SEEDREAM_ENDPOINT_ID"]
ROOT = Path(__file__).resolve().parent
IMAGES_DIR = ROOT / "images"

PORTRAITS = [
    {
        "name": "01-sun-shaoping",
        "prompt": """
Create an original photorealistic portrait of Sun Shaoping from the novel Ordinary World. Do not reference any film
or television adaptation, actor, celebrity or existing character design. Reconstruct him only from the novel's
social background and personality. He is an eighteen- or nineteen-year-old rural young man from northern Shaanxi in
the late 1970s: taller than average and very lean from poverty, but standing straight with quiet dignity. Give him a
young, plain, slightly angular Chinese face, naturally wind-weathered tan skin, and calm, perceptive eyes expressing
self-respect, stubborn endurance and a hunger for knowledge. He wears a clean but faded dark-blue coarse-cotton
jacket with small careful patches, old trousers and cloth shoes, and holds a well-read book. Place him at the edge of
a county high-school courtyard with plain, completely unmarked grey-tile classrooms and loess hills in the distance,
in cold early-spring daylight. Keep every wall and building free of signs, posters and writing. Half-length vertical
environmental portrait, authentic 1970s Chinese documentary photography, natural skin
texture, restrained color, dignified rather than miserable. One person only. No modern objects, glamour makeup,
fashion styling, text, caption, logo, watermark or collage.
""".strip(),
    },
    {
        "name": "02-sun-shaoan",
        "prompt": """
Create an original photorealistic portrait of Sun Shaoan from the novel Ordinary World. Do not reference any film or
television adaptation, actor, celebrity or existing character design. He is a northern Shaanxi farmer in his
twenties in the late 1970s, the elder brother who carries his family's burdens. He has a sturdy build, broad
shoulders, strong forearms and work-worn hands, deeply sun-browned skin and a straightforward square Chinese face.
His steady expression combines resilience, practical intelligence, responsibility and fatigue from years of hard
labor. He wears a durable grey-blue coarse-cotton work jacket with rolled sleeves and trousers lightly marked with
yellow earth. Place him between terraced fields and cave dwellings in Shuangshui Village, with a farm tool and newly
stacked bricks only faintly visible behind him. Warm low side-light after work. Half-length vertical environmental
portrait, authentic late-1970s northern Shaanxi documentary photography, rugged but orderly, dependable and active.
One person only. No modern machinery, glamour styling, text, logo, watermark or collage.
""".strip(),
    },
    {
        "name": "03-tian-runye",
        "prompt": """
Create an original photorealistic portrait of Tian Runye from the novel Ordinary World. Do not reference any film or
television adaptation, actor, celebrity or existing character design. She is a woman in her early twenties from
Shuangshui Village who works as a county primary-school teacher in the late 1970s. Her natural Chinese face is
pleasant and refined without makeup; her gentle eyes carry kindness, restraint, quiet sadness and inner resolve.
Style her hair simply and accurately for a young northern Chinese woman of the period. She wears a neat but modest
pale grey-blue cotton jacket over a white shirt and holds lesson notebooks against her chest. Place her beside a
wooden window in a county primary-school corridor, with grey plaster walls and distant loess hills. Soft afternoon
daylight. Half-length vertical documentary portrait, calm, clean and subtly scholarly, never glamorous or sugary.
One person only. No modern objects, text, caption, logo, watermark or collage.
""".strip(),
    },
    {
        "name": "04-hao-hongmei",
        "prompt": """
Create an original photorealistic portrait of Hao Hongmei from the novel Ordinary World. Do not reference any film
or television adaptation, actor, celebrity or existing character design. She is an eighteen- or nineteen-year-old
rural senior high-school student from an extremely poor family in northern Shaanxi in the late 1970s. She is
described as the most beautiful girl in her class. Make her unmistakably eighteen or nineteen, with mature young-woman
facial proportions rather than a child's face. She is slender and naturally striking: a graceful oval Chinese face,
clear dark eyes, fine brows, balanced features and an elegant, reserved presence. Her beauty is immediately apparent
despite having no makeup, fashionable haircut, jewelry or expensive clothes. Her sensitive, watchful eyes reveal
self-respect, social unease and a longing to appear presentable. Arrange her dark hair in one long, simple, tidy braid.
She wears a faded, slightly oversized old cotton coat whose collar and cuffs have been carefully mended, and carries
a much-used cloth schoolbag. Poverty must be visible only in the worn clothing and bag, never by making her childish,
dirty, sickly or unattractive. Place her at the doorway of an old county high-school classroom, with wooden desks and
grey walls softly receding behind her in cold winter daylight. Close half-length vertical documentary portrait with
natural skin and restrained color. Treat her with empathy and dignity, never as a fashion model, spectacle or
melodrama. One person only. No modern objects, glamour makeup, text, logo, watermark or collage.
""".strip(),
    },
    {
        "name": "05-jin-bo",
        "prompt": """
Create an original photorealistic portrait of Jin Bo from the novel Ordinary World. Do not reference any film or
television adaptation, actor, celebrity or existing character design. He is a northern Shaanxi man around twenty in
the late 1970s, the son of a truck driver and Sun Shaoping's loyal friend. He has a lean, agile build, an open and
clear Chinese face, candid eyes, and a natural warm smile that conveys humor, loyalty and romantic idealism. He wears
a neat but worn period jacket over a plain shirt and carries an old canvas shoulder bag. Place him beside the road
leading from northern Shaanxi toward the high plateau, with a historically accurate old Chinese truck far behind
him and a broad western horizon. Wind lifts his collar in warm late-afternoon light. Half-length vertical road
documentary portrait expressing freedom and yearning for distant places. One person only. No modern vehicle,
celebrity likeness, fashion styling, text, logo, watermark or collage.
""".strip(),
    },
    {
        "name": "06-tian-xiaoxia",
        "prompt": """
Create an original photorealistic portrait of Tian Xiaoxia from the novel Ordinary World. Do not reference any film
or television adaptation, actor, celebrity or existing character design. She is a Chinese woman in her early
twenties in the early 1980s, first a university student and then a young newspaper reporter. Although raised in a
cadre family, she is unspoiled, intellectually curious, independent, brave and deeply compassionate. Give her an
upright, energetic posture, a fresh natural Chinese face without glamour makeup, and bright direct eyes filled with
clarity and readiness to act. She has historically accurate natural short hair and wears a simple white shirt, dark
jacket and trousers, with an old canvas reporter bag across her body and a small notebook in hand. Place her on a
windy provincial-city street with period bicycles, a plain grey wall and gathering clouds behind her. Do not show
an office facade, storefront, signboard, poster, writing, Chinese character, red mark or text-like shape anywhere.
A breeze before rain, natural daylight.
Half-length vertical news-documentary portrait, open, intelligent and full
of life, never a fashion model. One person only. No modern objects, text, logo, watermark or collage.
""".strip(),
    },
    {
        "name": "07-sun-lanxiang",
        "prompt": """
Create an original photorealistic portrait of university-age Sun Lanxiang from the novel Ordinary World. Do not
reference any film or television adaptation, actor, celebrity or existing character design. She is a nineteen- or
twenty-year-old university student in the early 1980s, the gifted youngest daughter of an impoverished farming family
from northern Shaanxi. Make her unmistakably a young adult, not a child. She is slender and naturally attractive,
with a fresh oval Chinese face, clear intelligent eyes, neat brows and a calm, self-possessed expression. Her quiet
confidence comes from exceptional academic ability, discipline and the knowledge that studying has carried her far
beyond the circumstances of her childhood. She is modest, warm and grounded rather than fashionable or privileged.
Arrange her dark hair in a simple long braid. She wears a clean but inexpensive pale shirt under a faded navy cotton
jacket, plain dark trousers and no makeup or jewelry. An old canvas book bag crosses her shoulder, and she holds two
well-used plain cloth-covered notebooks against her chest, with completely blank covers and no printed books. Place
her on a provincial university campus in the early 1980s,
with plain grey-brick teaching buildings, mature plane trees and several period bicycles softly out of focus. Keep
all buildings completely unmarked: no signboard, poster, writing, Chinese character or text-like shape. Gentle autumn
morning light. Half-length vertical documentary portrait with natural skin texture and restrained color, expressing
intelligence, composure, hope and the dignity of a first-generation college student. One person only. No modern
objects, modern campus architecture, glamour makeup, luxury clothing, text, logo, watermark or collage.
""".strip(),
    },
]


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
) -> dict:
    body = {
        "model": ENDPOINT_ID,
        "prompt": prompt,
        "size": "1536x2048",
        "watermark": False,
        "output_format": "jpeg",
    }
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
    portrait_index = os.getenv("PORTRAIT_INDEX")
    portraits = PORTRAITS
    if portrait_index:
        requested_index = int(portrait_index)
        if not 1 <= requested_index <= len(PORTRAITS):
            raise ValueError(f"Invalid PORTRAIT_INDEX: {requested_index}")
        portraits = [PORTRAITS[requested_index - 1]]

    results = []
    timeout = httpx.Timeout(900.0, connect=60.0)
    async with httpx.AsyncClient(timeout=timeout, follow_redirects=True) as client:
        for portrait in portraits:
            output_path = IMAGES_DIR / f"{portrait['name']}.jpeg"
            results.append(
                await generate(
                    client,
                    prompt=portrait["prompt"],
                    output_path=output_path,
                )
            )

    print(json.dumps(results, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    asyncio.run(main())
