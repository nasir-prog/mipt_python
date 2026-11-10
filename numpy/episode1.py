from pathlib import Path

import numpy as np
from PIL import Image

folder = Path(__file__).resolve().parent
results = folder / "results"
results.mkdir(exist_ok=True)

for path in sorted((folder / "lunar_images").glob("*.jpg")):
    with Image.open(path) as image:
        pixels = np.array(image.convert("L"), dtype=float)

    low = pixels.min()
    high = pixels.max()
    if high > low:
        pixels = np.rint((pixels - low) * 255 / (high - low))
    else:
        pixels = np.zeros_like(pixels)

    Image.fromarray(pixels.astype(np.uint8)).save(results / (path.stem.removesuffix("_raw") + ".png"))
