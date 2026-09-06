#!/usr/bin/env python3
import argparse
import json
import re
from pathlib import Path


SLUG_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
SUBDIRECTORIES = ("images", "scripts", "spec", "video")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create the standard directory structure for a visual pack."
    )
    parser.add_argument(
        "--root",
        type=Path,
        required=True,
        help="Workspace directory that will contain the new style folder.",
    )
    parser.add_argument(
        "--slug",
        required=True,
        help="Kebab-case style identifier, for example cloud-courtyard-retreat.",
    )
    parser.add_argument(
        "--image-count",
        type=int,
        choices=(5, 6),
        default=6,
        help="Planned number of images in the pack.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if not SLUG_PATTERN.fullmatch(args.slug):
        raise SystemExit(
            "--slug must use lowercase kebab-case: letters, digits and hyphens"
        )

    root = args.root.expanduser().resolve()
    if not root.is_dir():
        raise SystemExit(f"Workspace root does not exist: {root}")

    style_root = root / args.slug
    if style_root.exists() and not style_root.is_dir():
        raise SystemExit(f"Style path exists but is not a directory: {style_root}")

    paths = {}
    for directory in SUBDIRECTORIES:
        path = style_root / directory
        path.mkdir(parents=True, exist_ok=True)
        paths[directory] = str(path)

    expected_images = [
        f"{index:02d}-<descriptive-name>.jpeg"
        for index in range(1, args.image_count + 1)
    ]
    result = {
        "style_root": str(style_root),
        "directories": paths,
        "expected_images": expected_images,
        "required_files": [
            str(style_root / "scripts" / "generate_images.py"),
            str(style_root / "spec" / "design-spec.md"),
            str(style_root / "video" / "video-storyboard.md"),
            str(style_root / "video" / "xiaohongshu-copy.md"),
        ],
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
