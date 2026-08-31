#!/usr/bin/env python3
import asyncio
import os
from pathlib import Path

import httpx


OUTPUT_DIR = Path(__file__).resolve().parents[1] / "assets" / "loft-variants"
IMAGE_NAMES = [
    "01-sakura-pink-urban-night.jpeg",
    "02-matcha-forest-sunlight.jpeg",
    "03-amber-orange-urban-night.jpeg",
    "04-ocean-coastal-seaview.jpeg",
]


def configured_images() -> list[tuple[str, str]]:
    """Load short-lived download URLs from environment variables."""
    return [
        (name, os.environ[f"LOFT_IMAGE_URL_{index}"])
        for index, name in enumerate(IMAGE_NAMES, start=1)
    ]


async def download_one(
    client: httpx.AsyncClient,
    name: str,
    url: str,
    index: int,
) -> Path:
    path = OUTPUT_DIR / name
    print(f"[{index}] Downloading {name} ...", flush=True)
    response = await client.get(url)
    response.raise_for_status()
    path.write_bytes(response.content)
    size_kb = len(response.content) / 1024
    print(f"[{index}] Saved -> {path} ({size_kb:.1f} KB)", flush=True)
    return path


async def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    images = configured_images()
    async with httpx.AsyncClient(timeout=120.0, follow_redirects=True) as client:
        paths = await asyncio.gather(
            *[
                download_one(client, name, url, index)
                for index, (name, url) in enumerate(images, start=1)
            ]
        )

    print("\nAll saved:")
    for path in paths:
        print(f"  {path}")


if __name__ == "__main__":
    asyncio.run(main())
