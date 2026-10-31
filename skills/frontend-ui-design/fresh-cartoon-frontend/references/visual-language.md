# Visual language

Use this reference as a decision system, not a requirement to copy exact TripSeed branding.

## Character

The target balance is approximately 70% calm product clarity, 20% editorial personality, and 10% cartoon warmth. If the interface feels childish, reduce character before reducing usability. If it feels corporate, strengthen the illustration, display type, and tactile accent details rather than adding more effects.

## Starting tokens

Adapt hues to the product while preserving their roles.

```css
:root {
  --page: #f6fbfb;
  --page-strong: #eaf8ff;
  --surface: rgba(255, 255, 255, 0.90);
  --surface-solid: #ffffff;
  --surface-soft: #edf8f5;
  --ink: #17393f;
  --ink-soft: #557278;
  --line: #cfe3e0;
  --brand: #167c80;
  --brand-strong: #0f6267;
  --brand-soft: #d9f1ed;
  --accent-warm: #f6bc4b;
  --accent-coral: #ed806c;
  --shadow-panel: 0 22px 65px rgba(41, 109, 111, 0.13);
  --shadow-small: 0 10px 30px rgba(41, 109, 111, 0.10);
  --radius-panel: 22px;
  --radius-control: 14px;
}
```

Use one-pixel cool-tinted borders. Avoid pure black text and gray borders, which make the palette feel disconnected.

## Typography

- Display: Fredoka Variable or another softly rounded face with restrained weight.
- Body: Nunito Sans Variable, Manrope, or another open, readable sans.
- Chinese fallback: `"Microsoft YaHei UI", "PingFang SC", sans-serif`.
- Large titles may use `clamp()` but should usually fit within two or three deliberate lines.
- Use weight and size for hierarchy before changing color.

## Geometry and spacing

- Center content in one shared max-width container.
- Use a 4/8-based spacing rhythm, with 12, 20, 28, 40, 56, and 72 as useful larger steps.
- Keep text inputs and choice controls visually aligned, normally 52–60px tall on desktop.
- Use 14px controls, 18–24px cards, and fully rounded pills only for tags, badges, and compact status.
- Major sections need breathing room; internal groups should stay visibly tighter than the gap between sections.

## Illustration

Choose a single material language: paper-cut landscape, soft 3D clay, gouache map, or clean storybook vector. Favor natural scenery, routes, maps, clouds, transport, plants, and small mascot gestures when relevant.

Composition matters more than detail. Use transparent or softly blended edges so the illustration belongs to the page. Preserve text contrast and avoid placing essential controls on top of busy art.

## Components

### Guided form

Group origin/destination, start/end, min/max, or similar pairs into a visible relationship. Use icon + label + control + helper text in a consistent vertical stack. Choice cards should have equal heights and selected states that change border, surface, icon, and text together.

### Summary panel

Give one number or outcome clear dominance. Supporting categories may use a restrained grid, but all values must derive from the same data model. Use labels that explain scope precisely.

### Timeline or route

Create continuity with a line, repeated marker, or directional connector. Do not rely on a pile of unrelated cards. Keep metadata compact and place the narrative description near its associated day or step.

### Empty and error states

Explain what is missing and the next action. Preserve layout stability. Never insert invented production data as a visual fallback unless the product explicitly labels it as a demo.

## Responsive behavior

- Wide desktop: maintain one focal composition, avoid stretching content edge-to-edge.
- Small laptop: protect the main task above the fold; reduce decorative height before reducing type readability.
- Tablet: collapse complex grids by relationship, not simply every item to full width.
- Mobile: stack route pairs and choice cards, keep primary action reachable, and remove nonessential decorative labels.

Verify that native date inputs, long Chinese labels, currency values, validation messages, and selected-chip counts do not break alignment.
