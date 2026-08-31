#!/usr/bin/env python3
"""Build a normalized, labeled contact sheet for aesthetic candidates."""

from __future__ import annotations

import argparse
import math
import sys
from pathlib import Path

try:
    from PIL import Image, ImageDraw, ImageFont, ImageOps
except ModuleNotFoundError as exc:
    raise SystemExit("Pillow is required: install it with 'python3 -m pip install Pillow'") from exc


IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("sources", nargs="+", type=Path, help="Candidate images or directories")
    parser.add_argument("--output", required=True, type=Path, help="Output PNG or JPEG path")
    parser.add_argument("--columns", type=int, help="Grid columns; defaults to a near-square grid")
    parser.add_argument("--cell-width", type=int, default=512)
    parser.add_argument("--cell-height", type=int, default=384)
    parser.add_argument("--label-height", type=int, default=44)
    parser.add_argument("--gap", type=int, default=16)
    parser.add_argument("--margin", type=int, default=24)
    parser.add_argument("--force", action="store_true", help="Replace an existing output")
    return parser.parse_args()


def is_contact_sheet(path: Path) -> bool:
    return "contact-sheet" in path.stem.casefold().replace("_", "-")


def collect_images(sources: list[Path], output: Path) -> list[Path]:
    found: list[Path] = []
    for source in sources:
        if source.is_dir():
            found.extend(
                path
                for path in source.iterdir()
                if path.is_file()
                and path.suffix.lower() in IMAGE_EXTENSIONS
                and not is_contact_sheet(path)
            )
        elif source.is_file() and source.suffix.lower() in IMAGE_EXTENSIONS and not is_contact_sheet(source):
            found.append(source)
        else:
            raise ValueError(f"unsupported or missing source: {source}")

    output_resolved = output.resolve()
    unique = {path.resolve(): path for path in found if path.resolve() != output_resolved}
    return sorted(unique.values(), key=lambda path: (path.name.casefold(), str(path)))


def validate_args(args: argparse.Namespace) -> None:
    for name in ("cell_width", "cell_height", "label_height", "gap", "margin"):
        value = getattr(args, name)
        minimum = 0 if name in {"gap", "margin"} else 1
        if value < minimum:
            raise ValueError(f"--{name.replace('_', '-')} must be at least {minimum}")
    if args.columns is not None and args.columns < 1:
        raise ValueError("--columns must be at least 1")
    if args.output.suffix.lower() not in {".png", ".jpg", ".jpeg"}:
        raise ValueError("--output must end in .png, .jpg, or .jpeg")


def normalized_tile(path: Path, width: int, height: int) -> Image.Image:
    with Image.open(path) as opened:
        image = ImageOps.exif_transpose(opened).convert("RGBA")
        contained = ImageOps.contain(image, (width, height), Image.Resampling.LANCZOS)

    background = Image.new("RGBA", (width, height), "#2b2b2b")
    x = (width - contained.width) // 2
    y = (height - contained.height) // 2
    background.alpha_composite(contained, (x, y))
    return background.convert("RGB")


def load_font(label_height: int) -> ImageFont.ImageFont:
    try:
        return ImageFont.truetype("DejaVuSans.ttf", max(12, min(24, label_height // 2)))
    except OSError:
        return ImageFont.load_default()


def fit_label(draw: ImageDraw.ImageDraw, text: str, width: int, font: ImageFont.ImageFont) -> str:
    if draw.textbbox((0, 0), text, font=font)[2] <= width:
        return text
    candidate = text
    while candidate and draw.textbbox((0, 0), candidate + "...", font=font)[2] > width:
        candidate = candidate[:-1]
    return candidate + "..."


def build_sheet(paths: list[Path], args: argparse.Namespace) -> Image.Image:
    columns = args.columns or math.ceil(math.sqrt(len(paths)))
    rows = math.ceil(len(paths) / columns)
    cell_height = args.cell_height + args.label_height
    width = args.margin * 2 + columns * args.cell_width + (columns - 1) * args.gap
    height = args.margin * 2 + rows * cell_height + (rows - 1) * args.gap
    sheet = Image.new("RGB", (width, height), "#151515")
    draw = ImageDraw.Draw(sheet)
    font = load_font(args.label_height)

    for index, path in enumerate(paths):
        row, column = divmod(index, columns)
        x = args.margin + column * (args.cell_width + args.gap)
        y = args.margin + row * (cell_height + args.gap)
        sheet.paste(normalized_tile(path, args.cell_width, args.cell_height), (x, y))
        draw.rectangle((x, y + args.cell_height, x + args.cell_width, y + cell_height), fill="#202020")
        label = fit_label(draw, path.stem, args.cell_width - 20, font)
        bbox = draw.textbbox((0, 0), label, font=font)
        text_height = bbox[3] - bbox[1]
        draw.text(
            (x + 10, y + args.cell_height + (args.label_height - text_height) // 2),
            label,
            fill="#f5f5f5",
            font=font,
        )
    return sheet


def main() -> int:
    args = parse_args()
    try:
        validate_args(args)
        if args.output.exists() and not args.force:
            raise ValueError(f"output already exists: {args.output}; use --force to replace it")
        paths = collect_images(args.sources, args.output)
        if not paths:
            raise ValueError("no supported images found")
        sheet = build_sheet(paths, args)
        args.output.parent.mkdir(parents=True, exist_ok=True)
        output_format = "JPEG" if args.output.suffix.lower() in {".jpg", ".jpeg"} else "PNG"
        sheet.save(args.output, format=output_format, quality=92)
    except (OSError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    print(f"Wrote {args.output} with {len(paths)} candidate(s) in {sheet.width}x{sheet.height}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
