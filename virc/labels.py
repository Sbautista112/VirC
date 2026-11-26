"""Load and sanity-check the labeled test set in eval/labels.csv.

Run from the repo root:
    .venv\\Scripts\\python -m virc.labels
"""

import csv
import sys
from collections import Counter
from pathlib import Path

from virc import taxonomy

REPO = Path(__file__).resolve().parents[1]
LABELS = REPO / "eval" / "labels.csv"
PHOTOS = REPO / "data" / "photos"
MIN_PER_CATEGORY = 3  # with fewer photos than this, per-category accuracy is just noise


def load_labels(path: Path) -> list[dict[str, str]]:
    """Read the labels file into one dict per row, keyed by column name."""
    # TODO(you): csv.DictReader does most of the work. Open the file with
    # newline="" (the csv module docs explain why).
    raise NotImplementedError


def check_row(row: dict[str, str]) -> list[str]:
    """Return every problem with one row. An empty list means the row is fine."""
    # TODO(you):
    #  - the photo named in "filename" exists in PHOTOS
    #  - every other column's value passes taxonomy.is_valid()
    #  - messages should say which photo and what's wrong, e.g.
    #    "IMG_4876.jpeg: 'jeens' is not a valid category"
    #  If you have multi-value columns (e.g. season), pick a separator such as
    #  "fall;winter" and split on it before checking each value.
    raise NotImplementedError


def count_by(rows: list[dict[str, str]], field: str) -> Counter[str]:
    """How many rows have each value of `field`, e.g. Counter({"jeans": 4, "hoodie": 2})."""
    # TODO(you): look up collections.Counter.
    raise NotImplementedError


def main() -> None:
    # TODO(you):
    #  1. Load the rows.
    #  2. Check every row and print each problem. Also catch the same filename
    #     appearing twice.
    #  3. Print how many photos each category has; flag any under MIN_PER_CATEGORY.
    #  4. Flag categories in the taxonomy that have no photos at all.
    #  5. If anything was wrong, end with sys.exit(1).
    #     Question for you: why would a script want to exit with an error code
    #     instead of just printing the problems?
    raise NotImplementedError


if __name__ == "__main__":
    main()
