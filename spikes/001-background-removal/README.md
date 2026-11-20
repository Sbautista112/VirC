# Spike 001: Background removal

**Question:** Which background-removal model gives clean cutouts of *my* clothing photos, and is it fast enough?

**Time limit:** one evening (~2 h). If time runs out, write down what we learned and decide anyway.

**Throwaway code.** The real pipeline won't import anything from here.

## Candidates

| Model (rembg name) | What it is | Download (approx.) |
|---|---|---|
| `u2net` | U²-Net (2020), general "stands out from the background" model. Your current pick | ~170 MB |
| `isnet-general-use` | ISNet (2022), trained for sharper edges | ~170 MB |
| `birefnet-general` | BiRefNet (2024), high resolution, newest | ~1 GB |
| `u2net_cloth_seg` | U²-Net trained on people wearing clothes; splits them into upper / lower / full body | ~170 MB |

## Success criteria (DRAFT: yours to decide before running)

Set these *before* you look at any results. Change the numbers, then delete this line.

- [ ] Clean cutout (no missing chunks, no leftover background, edges fine at thumbnail size) on at least **8 of 10** photos
- [ ] Average **under 1 s per photo** on the GPU (model load not counted)
- [ ] Handles the hard cases: dark item on a dark background, item on a patterned bed, item on a hanger
- [ ] Tie-breaker: if two models both pass, pick the faster and smaller one

## Photos

Put ~10 photos in `data/photos/` at the repo root. It's git-ignored, so your photos never end up on GitHub. Mix:

- **easy:** item flat on the floor or against a plain wall
- **hard:** on a bed, on a hanger, wrinkled, dark on dark, white on white

JPG or PNG. iPhone HEIC photos need converting to JPG first.

## Run

From the repo root:

```
.venv\Scripts\python spikes\001-background-removal\spike.py
```

Cutouts land in `output/<model>/`, plus `output/comparison.png` with every model side by side.

## Results

_Fill in after running: the timing table, what you saw in the grid, anything surprising._
