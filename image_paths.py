from pathlib import Path
import json

root_dir = Path("animals/")

image_paths = sorted(list(root_dir.glob("*/*.jpg")))

image_paths = [str(p) for p in image_paths]

with open("image_paths.json", "w") as f:
    json.dump(image_paths, f)