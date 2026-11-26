# Modelo de prompt para um asset da masmorra / mundo

Troque o que está entre <>. Anexe `art/referencia/vila-aprovada.jpg` e
`art/referencia/clima-masmorra-preview.png`. Salve a conversão em `art/masmorra/<pasta>/`.

```
Pixel art sprite for a top-down 3/4 fantasy medieval action RPG (Diablo-like mood), same drawing style
as the first attached village reference: same chunky shapes, same dark outline, same camera angle
(top-down 3/4, not isometric, not side view). Mood and colors like the second attached image: earthy,
grimy and dark, muted browns, moss greens, wet grey stone, old wood, mud; low saturation.
The only strong colors allowed are magic glows (purple necromancy, sickly green, torch orange).

Subject: <o que é, em uma frase. Ex.: "a rotting zombie peasant with a broken pitchfork, facing down, idle pose">.
Size feel: <tile 16x16 | monster 32x32 | boss 64x64 | object 16x16 to 64x64>,
chunky readable shapes that will still read after being shrunk to that size.

ONE single subject, centered, full body visible, nothing cropped.
Background: solid flat pure magenta #FF00FF, no ground, no cast shadow on the background, no frame,
no text, no watermark.
Flat colors, hard edges, no gradients, no blur, no dithering.
```

Depois: `python tools/pixelize.py art/rascunho/<nome>.png art/masmorra/<pasta>/<nome>.png --largura N --altura N`
e `python tools/check_art.py` (ver AGENTS.md, seção 4).
