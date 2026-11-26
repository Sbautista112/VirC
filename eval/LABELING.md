# Labeling guide

How each photo in `labels.csv` gets its labels. The point is consistency: if the same item could get two different labels depending on the day, the test set can't grade anything.

## The file

- `labels.csv`: one row per photo in `data/photos/`, with `filename` matching the photo's name exactly.
- Columns: `filename`, then one column per field in `virc/taxonomy.py`. Add a column when you add an attribute.
- Values must come from the taxonomy. Check with `.venv\Scripts\python -m virc.labels`.

## Rules

_Write these as you go, especially every time you hesitate over a photo._

- TODO: e.g. how to label an item that's in more than one category's territory
- TODO: e.g. which color wins for a two-color item

## Tricky cases

| Item | Could be | Decided | Why |
|---|---|---|---|
| _e.g. zip hoodie_ | _top / outerwear_ | | |

## Coverage

Aim for at least 3 to 5 photos per category, not just a big total. Note categories you can't cover yet (nothing like that in your closet) here so you know the score says nothing about them.
