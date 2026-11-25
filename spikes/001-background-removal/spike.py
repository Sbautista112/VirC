"""Spike 001: which background-removal model works best on my clothing photos?

Throwaway code: run it, learn from it, write the decision record. The real
pipeline won't import anything from here.

Run from the repo root:
    .venv\\Scripts\\python spikes\\001-background-removal\\spike.py
"""

import time
import statistics
from pathlib import Path

import onnxruntime as ort
from PIL import Image, ImageDraw, ImageOps
from rembg import new_session, remove

REPO = Path(__file__).resolve().parents[2]
PHOTOS = REPO / "data" / "photos"
OUTPUT = Path(__file__).resolve().parent / "output"
MODELS = ["u2net", "isnet-general-use", "birefnet-general", "u2net_cloth_seg"]
PHOTO_TYPES = {".jpg", ".jpeg", ".png", ".webp"}
MAX_SIDE = 1600  # phone photos are ~4000 px wide; nothing here needs that many pixels
CELL = 256  # size of each square in the comparison grid




def load_photo(path: Path) -> Image.Image:
    """Open a phone photo the right way up, shrunk so its longest side is MAX_SIDE."""
    img = Image.open(path)
    ImageOps.exif_transpose(img, in_place=True)
    img.thumbnail((MAX_SIDE, MAX_SIDE))
    return img.convert("RGB")


def run_model(model_name: str, photos: list[Path]) -> dict[str, float]:
    """Cut out every photo with one model, save the PNGs, and return timings in seconds."""

    #Timing session 
    start_load_s = time.perf_counter()
    session = new_session(model_name)
    end_load_s = time.perf_counter()
    load_s = end_load_s - start_load_s

    
    times = list()
    model_dir = OUTPUT / model_name
    model_dir.mkdir(parents=True, exist_ok=True)
    print(model_name, session.inner_session.get_providers())
    remove(load_photo(photos[0]), session=session)
    #Background removal for each picture.
    for photo in photos:
        img = load_photo(photo)
        remove_timer_start = time.perf_counter()
        output = remove(img, session=session)
        remove_timer_end = time.perf_counter()
        output.save(model_dir / f"{photo.stem}.png")
        times.append(remove_timer_end - remove_timer_start)
    return {
        "load_s": load_s,
        "mean_s": statistics.mean(times),
        "max_s": max(times)
    }


def checkerboard(size: int, square: int = 16) -> Image.Image:
    """Gray-and-white squares, the usual way to show where an image is transparent."""
    board = Image.new("RGB", (size, size), "white")
    draw = ImageDraw.Draw(board)
    for y in range(0, size, square):
        for x in range(0, size, square):
            if (x // square + y // square) % 2:
                draw.rectangle([x, y, x + square - 1, y + square - 1], fill=(205, 205, 205))
    return board


def fit_cell(img: Image.Image) -> Image.Image:
    """Shrink img to fit a CELL x CELL square, centered on a checkerboard."""
    cell = checkerboard(CELL)
    img = img.convert("RGBA")
    img.thumbnail((CELL, CELL))
    offset = ((CELL - img.width) // 2, (CELL - img.height) // 2)
    cell.paste(img, offset, img)  # the third argument uses img's alpha channel as the paste mask
    return cell


def make_grid(photos: list[Path], models: list[str]) -> Path:
    """One row per photo: the original, then each model's cutout. Returns the saved path."""
    columns = ["original", *models]
    label_height = 24
    grid = Image.new("RGB", (CELL * len(columns), label_height + CELL * len(photos)), "white")
    draw = ImageDraw.Draw(grid)
    for col, name in enumerate(columns):
        draw.text((col * CELL + 6, 6), name, fill="black")

    for row, photo in enumerate(photos):
        y = label_height + row * CELL
        grid.paste(fit_cell(load_photo(photo)), (0, y))
        for col, model in enumerate(models, start=1):
            cutout = OUTPUT / model / f"{photo.stem}.png"
            if cutout.exists():
                grid.paste(fit_cell(Image.open(cutout)), (col * CELL, y))

    path = OUTPUT / "comparison.png"
    path.parent.mkdir(parents=True, exist_ok=True)
    grid.save(path)
    return path


def main() -> None:
    # pip installed CUDA and cuDNN as Python packages. This loads their DLLs so
    # ONNX Runtime can find them; without it, every model falls back to the CPU.
    ort.preload_dlls()
    print("ONNX Runtime can use:", ort.get_available_providers())

    photos = sorted(p for p in PHOTOS.glob("*") if p.suffix.lower() in PHOTO_TYPES)
    if not photos:
        raise SystemExit(f"No photos found. Put some JPGs or PNGs in {PHOTOS}")

    results = {model: run_model(model, photos) for model in MODELS}

    print(f"\n{'model':<20}{'load s':>9}{'mean s':>9}{'max s':>9}")
    for model, t in results.items():
        print(f"{model:<20}{t['load_s']:>9.2f}{t['mean_s']:>9.2f}{t['max_s']:>9.2f}")
    print("\nComparison grid:", make_grid(photos, MODELS))


if __name__ == "__main__":
    main()
