# Prompts dos sprites frontais

Gerações feitas com ImageGen. A vila aprovada foi anexada a todos os prompts. A prévia 8× do cavaleiro revisado foi anexada às outras cinco classes. Os quatro sprites subterrâneos também receberam a referência de clima da masmorra.

## cavaleiro-frente

- Sprite em `art/personagens/cavaleiro-frente.png`
- Original final em `cavaleiro-frente.png`
- Conversão com `--largura 32 --altura 32 --corpo 16x24`
- 2 tentativas
- OK. A face está visível e o dourado do escudo lê como um leão estilizado.

### Tentativa 1 — rejeitada

Rosto e leão ilegíveis. Veja `art/rejeitadas/sprites/`.

```text
Pixel art sprite for a top-down 3/4 fantasy medieval RPG, matching the attached village reference exactly: same crisp dark 1px-style outline, same light from top-left, same orthogonal top-down 3/4 camera (not isometric, not side view), same character palette and style as the small village guards, especially the red-plumed guard by the fountain.

Subject: one front-facing idle chibi knight with silver armor, visible face with eyes under open helmet, red cape, red helmet plume, compact red shield with gold lion silhouette and a short silver sword held close upright.
Size feel: complete silhouette fits 16x24 inside 32x32, proportion width:height about 2:3. Very simple chunky shapes, big head, few details, readable at 32x32. Make both eyes large enough to survive reduction. Face and both boots point directly toward viewer, slightly elevated orthogonal view showing helmet crown. Keep arms and accessories close so the main figure stays large.

ONE single subject, centered, full body visible, nothing cropped.
Background: uniform solid flat pure magenta #FF00FF, no ground, no cast shadow on the background, no frame, no text, no watermark.
Flat colors, hard edges, no gradients, no glow, no blur, no dithering.
```

### Tentativa 2 — prompt final

```text
Pixel art sprite for a top-down 3/4 fantasy medieval RPG, matching the attached village reference exactly: same crisp dark 1px-style outline, same light from top-left, same orthogonal top-down 3/4 camera (not isometric, not side view), same character palette and style as the small village guards, especially the red-plumed guard by the fountain.

Subject: one front-facing idle chibi knight with silver armor, visible face with eyes under open helmet, red cape, red helmet plume, compact red shield with gold lion silhouette and a short silver sword held close upright.
Size feel: complete silhouette fits 16x24 inside 32x32, proportion width:height about 2:3. Very simple chunky shapes, big head, few details, readable at 32x32. Make both eyes large enough to survive reduction. Face and both boots point directly toward viewer, slightly elevated orthogonal view showing helmet crown. Keep arms and accessories close so the main figure stays large.

ONE single subject, centered, full body visible, nothing cropped.
Background: uniform solid flat pure magenta #FF00FF, no ground, no cast shadow on the background, no frame, no text, no watermark.
Flat colors, hard edges, no gradients, no glow, no blur, no dithering.

Redraw as a hand-placed grid of approximately 16 pixel columns by 24 pixel rows for the whole character, with each logical pixel visibly square and large, like the guards in the village. Prioritize a warm face block at least 5 logical pixels wide, TWO separate black square eyes with one peach pixel between, and a raised silver helmet brim. The eye pair is essential. Keep silver bright and neutral. Make the red shield broad enough for a 3x4 pixel stylized heraldic rampant lion (separate head, raised paw, bent tail, connected body), with plain red border. Use two simple separable boots and a clear broad red cape edge. No busy armor highlights.
```

## mago-frente

- Sprite em `art/personagens/mago-frente.png`
- Original final em `mago-frente.png`
- Conversão com `--largura 32 --altura 32 --corpo 16x24`
- 1 tentativa
- OK. Chapéu azul, barba branca e orbe azul distinguíveis.

### Tentativa 1 — prompt final

```text
Pixel art sprite for a top-down 3/4 fantasy medieval RPG, matching the first attached village reference exactly: same colorful medieval palette, same dark 1px-style outline, same light from top-left, same orthogonal top-down 3/4 camera (not isometric, not side view). Use the second attached image only as the character proportion template: same chibi proportions and head size as the attached knight, with head and feet at comparable heights after conversion.

Subject: a chibi wizard in a royal blue pointed hat and royal blue robe with thick gold trim, long white beard, holding one dark staff crowned with a bright cyan-blue orb. Front-facing idle pose looking straight toward the camera. Both sides of the face are visible and stance reads head-on, slightly viewed from above.
Size feel: 16x24 silhouette inside 32x32; very simple chunky shapes, big head, few details, readable at native sprite size. The entire silhouette should fill the target body aspect ratio, keep equipment tucked in. Build the face out of a broad peach strip with two dark eyes and a big white beard block. Keep the pointed hat compact so the face sits at the knight's face height. Keep the orb adjacent to the hat and make blue the dominant color.

ONE single subject, centered, full body visible, nothing cropped.
Background: uniform solid flat pure magenta #FF00FF, no ground, no cast shadow on the background, no frame, no text, no watermark.
Flat colors, hard edges, no gradients, no blur, no dithering. Any magical light must be represented by hard-edged adjacent color blocks without atmospheric bloom.
```

## necromante-frente

- Sprite em `art/personagens/necromante-frente.png`
- Original final em `necromante-frente.png`
- Conversão com `--largura 32 --altura 32 --corpo 16x24`
- 2 tentativas
- Parcial. A paleta da vila não contém violeta. Manto e chamas ficaram cinza-azulados.

### Tentativa 1 — rejeitada

Roxo neutralizado. Veja `art/rejeitadas/sprites/`.

```text
Pixel art sprite for a top-down 3/4 fantasy medieval RPG, matching the first attached village reference exactly: same colorful medieval palette, same dark 1px-style outline, same light from top-left, same orthogonal top-down 3/4 camera (not isometric, not side view). Use the second attached image only as the character proportion template: same chibi proportions and head size as the attached knight, with head and feet at comparable heights after conversion.

Subject: a chibi skeleton necromancer with dark violet robe and thick gold trim, purple flames above the bare skull, and a staff capped with a small skull. Front-facing idle pose looking straight toward the camera. Both sides of the face are visible and stance reads head-on, slightly viewed from above.
Size feel: 16x24 silhouette inside 32x32; very simple chunky shapes, big head, few details, readable at native sprite size. The entire silhouette should fill the target body aspect ratio, keep equipment tucked in. Make the main ivory skull broad with two square dark sockets; make the staff topper distinctly smaller than the skull of the necromancer. Use saturated violet clusters and one solid gold trim. Keep purple flame tips short and distinct so body and face align with the knight.

ONE single subject, centered, full body visible, nothing cropped.
Background: uniform solid flat pure magenta #FF00FF, no ground, no cast shadow on the background, no frame, no text, no watermark.
Flat colors, hard edges, no gradients, no blur, no dithering. Any magical light must be represented by hard-edged adjacent color blocks without atmospheric bloom.
```

### Tentativa 2 — prompt final

```text
Pixel art sprite for a top-down 3/4 fantasy medieval RPG, matching the first attached village reference exactly: same colorful medieval palette, same dark 1px-style outline, same light from top-left, same orthogonal top-down 3/4 camera (not isometric, not side view). Use the second attached image only as the character proportion template: same chibi proportions and head size as the attached knight, with head and feet at comparable heights after conversion.

Subject: a chibi skeleton necromancer with dusty desaturated violet robe and narrow gold trim, a chunky three-prong violet flame crown above its off-white skull, and a staff capped with a second very small skull. Front-facing idle pose looking straight toward the camera. Both sides of the face are visible and stance reads head-on, slightly viewed from above.
Size feel: 16x24 silhouette inside 32x32; very simple chunky shapes, big head, few details, readable at native sprite size. The entire silhouette should fill the target body aspect ratio, keep equipment tucked in. Make robes predominantly muted lavender-grey (#6F6A6E) and blue-violet slate (#58657B) in large flat blocks; avoid bright magenta, black robes and orange except for a tiny gold trim. Give the flames a clear three-pronged solid silhouette in slate and mauve-gray. Make the main ivory skull broad with two square dark sockets. Match the knight's face and feet heights.

ONE single subject, centered, full body visible, nothing cropped.
Background: uniform solid flat pure magenta #FF00FF, no ground, no cast shadow on the background, no frame, no text, no watermark.
Flat colors, hard edges, no gradients, no blur, no dithering. Any magical light must be represented by hard-edged adjacent color blocks without atmospheric bloom.
```

## arqueira-frente

- Sprite em `art/personagens/arqueira-frente.png`
- Original final em `arqueira-frente.png`
- Conversão com `--largura 32 --altura 32 --corpo 16x24`
- 1 tentativa
- OK. Capuz verde e arco legíveis. Aljava discreta atrás do ombro.

### Tentativa 1 — prompt final

```text
Pixel art sprite for a top-down 3/4 fantasy medieval RPG, matching the first attached village reference exactly: same colorful medieval palette, same dark 1px-style outline, same light from top-left, same orthogonal top-down 3/4 camera (not isometric, not side view). Use the second attached image only as the character proportion template: same chibi proportions and head size as the attached knight, with head and feet at comparable heights after conversion.

Subject: a chibi female archer in a vivid forest-green hood and worn brown leather, holding a short curved bow with a dark string and wearing a quiver with arrow fletchings showing above one shoulder. Front-facing idle pose looking straight toward the camera. Both sides of the face are visible and stance reads head-on, slightly viewed from above.
Size feel: 16x24 silhouette inside 32x32; very simple chunky shapes, big head, few details, readable at native sprite size. The entire silhouette should fill the target body aspect ratio, keep equipment tucked in. Green hood with a large clearly lit face opening, two bold eyes, green shoulder mantle and brown boots. Keep the bow close to the silhouette and the quiver tucked behind the shoulder.

ONE single subject, centered, full body visible, nothing cropped.
Background: uniform solid flat pure magenta #FF00FF, no ground, no cast shadow on the background, no frame, no text, no watermark.
Flat colors, hard edges, no gradients, no blur, no dithering. Any magical light must be represented by hard-edged adjacent color blocks without atmospheric bloom.
```

## sacerdote-frente

- Sprite em `art/personagens/sacerdote-frente.png`
- Original final em `sacerdote-frente.png`
- Conversão com `--largura 32 --altura 32 --corpo 16x24`
- 1 tentativa
- OK. Manto branco e dourado com maça e livro compactos.

### Tentativa 1 — prompt final

```text
Pixel art sprite for a top-down 3/4 fantasy medieval RPG, matching the first attached village reference exactly: same colorful medieval palette, same dark 1px-style outline, same light from top-left, same orthogonal top-down 3/4 camera (not isometric, not side view). Use the second attached image only as the character proportion template: same chibi proportions and head size as the attached knight, with head and feet at comparable heights after conversion.

Subject: a chibi temple priest in a predominantly ivory-white robe with gold borders, holding a compact metal mace and a closed holy book with a gold emblem. Front-facing idle pose looking straight toward the camera. Both sides of the face are visible and stance reads head-on, slightly viewed from above.
Size feel: 16x24 silhouette inside 32x32; very simple chunky shapes, big head, few details, readable at native sprite size. The entire silhouette should fill the target body aspect ratio, keep equipment tucked in. White robe must be the biggest color block, use #F4F1E4 highlights and simple gold stripes. Make mace a single chunky metal head on a short handle, book a small block with a visible gold emblem. Exposed peach face and two boldly separated eyes.

ONE single subject, centered, full body visible, nothing cropped.
Background: uniform solid flat pure magenta #FF00FF, no ground, no cast shadow on the background, no frame, no text, no watermark.
Flat colors, hard edges, no gradients, no blur, no dithering. Any magical light must be represented by hard-edged adjacent color blocks without atmospheric bloom.
```

## ladino-frente

- Sprite em `art/personagens/ladino-frente.png`
- Original final em `ladino-frente.png`
- Conversão com `--largura 32 --altura 32 --corpo 16x24`
- 1 tentativa
- OK. Lenço, olhos expostos e duas lâminas separadas.

### Tentativa 1 — prompt final

```text
Pixel art sprite for a top-down 3/4 fantasy medieval RPG, matching the first attached village reference exactly: same colorful medieval palette, same dark 1px-style outline, same light from top-left, same orthogonal top-down 3/4 camera (not isometric, not side view). Use the second attached image only as the character proportion template: same chibi proportions and head size as the attached knight, with head and feet at comparable heights after conversion.

Subject: a chibi rogue in charcoal gray and black leather gear with a dark scarf covering nose and mouth and one short silver dagger in each hand. Front-facing idle pose looking straight toward the camera. Both sides of the face are visible and stance reads head-on, slightly viewed from above.
Size feel: 16x24 silhouette inside 32x32; very simple chunky shapes, big head, few details, readable at native sprite size. The entire silhouette should fill the target body aspect ratio, keep equipment tucked in. Use two prominent skin-tone and dark eye blocks above the scarf, two clearly separate silver blades held close on opposite sides, and large charcoal gray highlights to separate costume and black outline.

ONE single subject, centered, full body visible, nothing cropped.
Background: uniform solid flat pure magenta #FF00FF, no ground, no cast shadow on the background, no frame, no text, no watermark.
Flat colors, hard edges, no gradients, no blur, no dithering. Any magical light must be represented by hard-edged adjacent color blocks without atmospheric bloom.
```

## lobo-frente

- Sprite em `art/masmorra/monstros/lobo-frente.png`
- Original final em `lobo-frente.png`
- Conversão com `--largura 32 --altura 32 --corpo 28x20`
- 3 tentativas
- OK. Olhos puxam para o âmbar na grade final.

### Tentativa 1 — rejeitada

Olhos amarelos ilegíveis. Veja `art/rejeitadas/sprites/`.

```text
Pixel art sprite for a top-down 3/4 fantasy medieval action RPG (Diablo-like mood), same drawing style as the first attached village reference: same chunky shapes, same dark outline, same orthogonal top-down 3/4 camera (not isometric, not side view), same light from top-left. Mood and colors like the second attached image: earthy, grimy and dark, muted browns, moss greens, wet grey stone, old wood, mud; low saturation. Strong accents reserved for magic.

Subject: a lean gray wolf with yellow eyes, standing idle on all fours, seen head-on, ears pricked. Front-facing idle pose looking straight toward the camera. Both sides of the face are visible and stance reads head-on, slightly viewed from above.
Size feel: 28x20 silhouette inside 32x32; very simple chunky shapes, big head, few details, readable at native sprite size. The entire silhouette should fill the target body aspect ratio, keep equipment tucked in. The camera elevation shows a short run of grey back behind the head, a distinct narrow muzzle, two upright pointed ears and the complete outline including paws. Two clear mustard-yellow eyes in separate dark sockets. Use a low, wide 28-by-20 silhouette without forcing an unnaturally bulky body.

ONE single subject, centered, full body visible, nothing cropped.
Background: uniform solid flat pure magenta #FF00FF, no ground, no cast shadow on the background, no frame, no text, no watermark.
Flat colors, hard edges, no gradients, no blur, no dithering. Any magical light must be represented by hard-edged adjacent color blocks without atmospheric bloom.
```

### Tentativa 2 — rejeitada

Olhos apagados. Veja `art/rejeitadas/sprites/`.

```text
Pixel art sprite for a top-down 3/4 fantasy medieval action RPG (Diablo-like mood), same drawing style as the first attached village reference: same chunky shapes, same dark outline, same orthogonal top-down 3/4 camera (not isometric, not side view), same light from top-left. Mood and colors like the second attached image: earthy, grimy and dark, muted browns, moss greens, wet grey stone, old wood, mud; low saturation. Strong accents reserved for magic.

Subject: a lean cool grey wolf with two unmistakable yellow eyes and a small black nose, standing still on all fours facing the camera head-on. Front-facing idle pose looking straight toward the camera. Both sides of the face are visible and stance reads head-on, slightly viewed from above.
Size feel: 28x20 silhouette inside 32x32; very simple chunky shapes, big head, few details, readable at native sprite size. The entire silhouette should fill the target body aspect ratio, keep equipment tucked in. Use a very simple chunky sprite grid with a broad clear face of cool-grey shapes. Draw two yellow squares #E8B23A, at least two logical pixels each, on the front face on either side of the muzzle, low enough to be distinct from the ears. Use minimal fur texture and mostly flat neutral grays, visible torso and four paws; the slightly raised camera shows the shoulders and back.

ONE single subject, centered, full body visible, nothing cropped.
Background: uniform solid flat pure magenta #FF00FF, no ground, no cast shadow on the background, no frame, no text, no watermark.
Flat colors, hard edges, no gradients, no blur, no dithering. Any magical light must be represented by hard-edged adjacent color blocks without atmospheric bloom.
```

### Tentativa 3 — prompt final

```text
Pixel art sprite for a top-down 3/4 fantasy medieval action RPG (Diablo-like mood), same drawing style as the first attached village reference: same chunky shapes, same dark outline, same orthogonal top-down 3/4 camera (not isometric, not side view), same light from top-left. Mood and colors like the second attached image: earthy, grimy and dark, muted browns, moss greens, wet grey stone, old wood, mud; low saturation. Strong accents reserved for magic.

Subject: one lean charcoal-gray wolf monster staring straight at camera with enlarged vividly luminous yellow-gold magical eyes, rigid front-facing idle on four paws. Front-facing idle pose looking straight toward the camera. Both sides of the face are visible and stance reads head-on, slightly viewed from above.
Size feel: 28x20 silhouette inside 32x32; very simple chunky shapes, big head, few details, readable at native sprite size. The entire silhouette should fill the target body aspect ratio, keep equipment tucked in. The luminous eyes are the only magical accent: use two broad pure golden yellow (#F7DE7A and #E8B23A) rectangular eye blocks, separated by several gray nose-bridge pixels and surrounded by deep charcoal. No eye shading or outlines inside the yellow shapes. The yellow eye areas should fill about 15 percent of the face. Distinct large pointed triangular ears, narrow gray muzzle, tiny black nose, short torso visible behind the shoulders, four paws.

ONE single subject, centered, full body visible, nothing cropped.
Background: uniform solid flat pure magenta #FF00FF, no ground, no cast shadow on the background, no frame, no text, no watermark.
Flat colors, hard edges, no gradients, no blur, no dithering. Any magical light must be represented by hard-edged adjacent color blocks without atmospheric bloom.
```

## goblin-frente

- Sprite em `art/masmorra/monstros/goblin-frente.png`
- Original final em `goblin-frente.png`
- Conversão com `--largura 32 --altura 32 --corpo 16x20`
- 2 tentativas
- OK. Cabeça verde e lâmina destacadas da túnica.

### Tentativa 1 — rejeitada

Adaga fundida e rosto escuro. Veja `art/rejeitadas/sprites/`.

```text
Pixel art sprite for a top-down 3/4 fantasy medieval action RPG (Diablo-like mood), same drawing style as the first attached village reference: same chunky shapes, same dark outline, same orthogonal top-down 3/4 camera (not isometric, not side view), same light from top-left. Mood and colors like the second attached image: earthy, grimy and dark, muted browns, moss greens, wet grey stone, old wood, mud; low saturation. Strong accents reserved for magic.

Subject: a green goblin with wide pointed ears, short body, simple tattered brown tunic and a rusty iron dagger in one hand. Front-facing idle pose looking straight toward the camera. Both sides of the face are visible and stance reads head-on, slightly viewed from above.
Size feel: 16x20 silhouette inside 32x32; very simple chunky shapes, big head, few details, readable at native sprite size. The entire silhouette should fill the target body aspect ratio, keep equipment tucked in. Big olive-green face with two distinct dark eyes and a broad nose that contrast on the face. Keep ears within 16-column silhouette. The broad rusty dagger sits close and is clearly distinct from the arm; mix a grey blade with a burnt-orange rust patch.

ONE single subject, centered, full body visible, nothing cropped.
Background: uniform solid flat pure magenta #FF00FF, no ground, no cast shadow on the background, no frame, no text, no watermark.
Flat colors, hard edges, no gradients, no blur, no dithering. Any magical light must be represented by hard-edged adjacent color blocks without atmospheric bloom.
```

### Tentativa 2 — prompt final

```text
Pixel art sprite for a top-down 3/4 fantasy medieval action RPG (Diablo-like mood), same drawing style as the first attached village reference: same chunky shapes, same dark outline, same orthogonal top-down 3/4 camera (not isometric, not side view), same light from top-left. Mood and colors like the second attached image: earthy, grimy and dark, muted browns, moss greens, wet grey stone, old wood, mud; low saturation. Strong accents reserved for magic.

Subject: one front-facing small olive-green goblin with pointed ears and a rusty dagger held upright tightly beside its torso, in a plain dark brown tunic. Front-facing idle pose looking straight toward the camera. Both sides of the face are visible and stance reads head-on, slightly viewed from above.
Size feel: 16x20 silhouette inside 32x32; very simple chunky shapes, big head, few details, readable at native sprite size. The entire silhouette should fill the target body aspect ratio, keep equipment tucked in. Make its large head and ears visibly moss green (#518C29 and #518553) and slightly brighter than the body. Put two separate square near-black eyes on a flat green face, with one green pixel between. Use a clear four-step vertical silver-grey blade (#988D85) roughly two logical pixels wide, with exactly one red-brown rust cluster. A dark separator between the blade and tunic is essential.

ONE single subject, centered, full body visible, nothing cropped.
Background: uniform solid flat pure magenta #FF00FF, no ground, no cast shadow on the background, no frame, no text, no watermark.
Flat colors, hard edges, no gradients, no blur, no dithering. Any magical light must be represented by hard-edged adjacent color blocks without atmospheric bloom.
```

## esqueleto-frente

- Sprite em `art/masmorra/monstros/esqueleto-frente.png`
- Original final em `esqueleto-frente.png`
- Conversão com `--largura 32 --altura 32 --corpo 16x24`
- 1 tentativa
- OK. Crânio, costelas e espada em blocos legíveis.

### Tentativa 1 — prompt final

```text
Pixel art sprite for a top-down 3/4 fantasy medieval action RPG (Diablo-like mood), same drawing style as the first attached village reference: same chunky shapes, same dark outline, same orthogonal top-down 3/4 camera (not isometric, not side view), same light from top-left. Mood and colors like the second attached image: earthy, grimy and dark, muted browns, moss greens, wet grey stone, old wood, mud; low saturation. Strong accents reserved for magic.

Subject: one walking-dead skeleton standing still with an aged ivory skull and exposed rib cage, armed with a rusty sword. Front-facing idle pose looking straight toward the camera. Both sides of the face are visible and stance reads head-on, slightly viewed from above.
Size feel: 16x24 silhouette inside 32x32; very simple chunky shapes, big head, few details, readable at native sprite size. The entire silhouette should fill the target body aspect ratio, keep equipment tucked in. Show a large plain ivory skull with two dark square sockets, chunky rib cage with three large alternating bone and dark bands, and two bony legs and feet. Keep the sword upright close to one forearm, with distinct partly rusty blade and simple crossguard. The skull and bones contrast with dark warm shadows.

ONE single subject, centered, full body visible, nothing cropped.
Background: uniform solid flat pure magenta #FF00FF, no ground, no cast shadow on the background, no frame, no text, no watermark.
Flat colors, hard edges, no gradients, no blur, no dithering. Any magical light must be represented by hard-edged adjacent color blocks without atmospheric bloom.
```

## ogro-bastiao-frente

- Sprite em `art/masmorra/chefes/ogro-bastiao-frente.png`
- Original final em `ogro-bastiao-frente.png`
- Conversão com `--largura 64 --altura 64 --corpo 48x56`
- 1 tentativa
- OK. Clava espinhosa, ombreiras e fivela de caveira distinguíveis.

### Tentativa 1 — prompt final

```text
Pixel art sprite for a top-down 3/4 fantasy medieval action RPG (Diablo-like mood), same drawing style as the first attached village reference: same chunky shapes, same dark outline, same orthogonal top-down 3/4 camera (not isometric, not side view), same light from top-left. Mood and colors like the second attached image: earthy, grimy and dark, muted browns, moss greens, wet grey stone, old wood, mud; low saturation. Strong accents reserved for magic.

Subject: a huge muscular moss-green ogre bastion boss idle with both feet planted, a hefty spiked wooden club held upright close to his shoulder, brown leather pauldrons, and a heavy belt with an ivory skull buckle. Front-facing idle pose looking straight toward the camera. Both sides of the face are visible and stance reads head-on, slightly viewed from above.
Size feel: 48x56 silhouette inside 64x64; very simple chunky shapes, big head, few details, readable at native sprite size. The entire silhouette should fill the target body aspect ratio, keep equipment tucked in. Use a massive dark outlined upper body, distinct face with two eyes and lower tusks, thick leather on both shoulders, and a chunky pale skull at the waist. The club should clearly show several large metal spikes and fit inside the overall silhouette without shrinking the boss. High contrast within the restrained greens and warm browns.

ONE single subject, centered, full body visible, nothing cropped.
Background: uniform solid flat pure magenta #FF00FF, no ground, no cast shadow on the background, no frame, no text, no watermark.
Flat colors, hard edges, no gradients, no blur, no dithering. Any magical light must be represented by hard-edged adjacent color blocks without atmospheric bloom.
```


## necromante-frente-v3

- Original gerado com ImageGen em `necromante-frente-v3.png`.
- Referências: cavaleiro de frente ampliado em 8× para proporções e `art/referencia/vila-aprovada.jpg` para estilo.
- Conversão: `--largura 32 --altura 32 --corpo 16x24`.
- Veredito: aprovado na primeira tentativa. O manto roxo saturado e a chama violeta clara distinguem o necromante do cavaleiro vermelho e do mago azul na prancha sobre grama. O crânio e o contorno permanecem visíveis a 32×32.
- `check_art.py`: 70 arquivo(s), 0 erro(s).

### Prompt

```text
Generate one new pixel art sprite for a top-down 3/4 fantasy medieval RPG. Image 1 is the enlarged knight: use the same chibi proportions and head size as the attached knight, short compact body, forward-facing idle stance, both eyes visible, slightly viewed from above. Image 2 is the approved village: borrow its orthogonal camera, dark one-pixel-style outline, colorful chunky clusters and light from upper left. Subject: a skeleton necromancer standing idle, full body, large warm ivory bone-white skull with two dark sockets, a compact bright light-violet flame crest with hard-edged #B06EE8 clusters rising directly from the skull, and a short upright staff capped with a little ivory skull tucked immediately beside its body. The cloak is predominantly SATURATED PURPLE #7A3BB0 in broad clean areas across shoulders, chest and skirt, with #4E2378 shadows and #2A1640 deep folds, small gold edging and clasp. Keep its fabric visibly violet at a glance, with no blue or grey fabric. Fit the whole silhouette including staff and flames to a narrow 16:24 aspect ratio for downsampling to a 16x24 figure inside a 32x32 game sprite. Simple broad flat color clusters and a dark outline, clear stout chibi shape, feet visible, exactly one centered uncropped figure. Perfect uniform flat pure magenta #FF00FF background. No ground, cast shadow, gradient, glow bloom, blur, dithering, frame, text or watermark.
```

