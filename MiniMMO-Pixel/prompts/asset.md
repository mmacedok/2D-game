# Modelo de prompt para um asset

Troque o que está entre <>. Anexe sempre `art/referencia/vila-aprovada.jpg`.

```
Pixel art sprite for a top-down 3/4 fantasy medieval RPG, matching the attached village reference exactly:
same palette (blue slate roofs, grey cobblestone, vivid green grass, red banners with gold fleur-de-lis),
same dark 1px-style outline, same light from top-left, same camera angle (top-down 3/4, not isometric,
not side view).

Subject: <o que é, em uma frase. Ex.: "a goblin with a rusty dagger, facing down, idle pose">.
Size feel: <tile 16x16 | character 16x24 inside 32x32 | monster 32x32 | boss 64x64 | icon 16x16>,
chunky readable shapes that will still read after being shrunk to that size.

ONE single subject, centered, full body visible, nothing cropped.
Background: solid flat pure magenta #FF00FF, no ground, no cast shadow on the background, no frame,
no text, no watermark.
Flat colors, hard edges, no gradients, no glow, no blur, no dithering.
```

Depois: `python tools/pixelize.py ...` e `python tools/check_art.py` (ver AGENTS.md, seção 4).
