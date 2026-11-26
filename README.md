# VirC: virtual closet

Track every piece of clothing you own. Take a photo, the pipeline cuts out the background and categorizes the item, and it shows up in your closet.

## Status

Early. Building the image pipeline first.

| Part | Status |
|---|---|
| Image pipeline | Background removal: U²-Net chosen (spike 001). Next: taxonomy and labeled test set |
| Database | Not started |
| UI | Not started |

## Repo layout

- `virc/`: the real pipeline code.
- `eval/`: the labeled test set and labeling guide used to grade models.
- `spikes/`: time-boxed experiments. Throwaway code, kept for the write-ups.
- `docs/decisions/`: decision records explaining why things are built the way they are.
- `data/photos/`: local test photos (git-ignored).
