---
name: fresh-cartoon-frontend
description: Design or refine consumer-facing web interfaces in a fresh, calm, lightly cartooned visual language with disciplined alignment, soft teal surfaces, friendly typography, restrained illustration, and production-ready responsive behavior. Use for landing pages, guided forms, itinerary or lifestyle products, result pages, and redesigns that should feel warm and polished rather than corporate or childish.
---

# Fresh Cartoon Frontend

Create interfaces that feel clear, optimistic, and human: editorial hierarchy and rigorous grids softened by friendly type, pale natural color, rounded geometry, and one purposeful illustrated world.

## Before designing

For an existing project, inspect its framework, layout primitives, design tokens, component library, routes, and screenshots before editing. Preserve behavior, data flow, accessibility, and established product content. Fix alignment and hierarchy at the layout-system level instead of adding isolated offsets.

For a new page, identify the primary user journey and choose one visual story. Do not begin from a generic dashboard, SaaS card grid, or stock gradient template.

Read [references/visual-language.md](references/visual-language.md) when choosing tokens, layout, illustration, components, or responsive rules.

## Design decisions

- Use an airy off-white or mist-tinted page with deep blue-green text and a restrained teal brand color. Warm yellow or coral may appear only as small semantic accents.
- Pair a softly rounded display face with a highly readable body face. Headlines should be confident and compact; body copy should remain sober enough to protect trust.
- Build alignment from a shared container, explicit grid tracks, consistent control heights, and a small spacing scale. Labels, fields, helper text, and repeated cards must share baselines and edges.
- Use rounded corners in a hierarchy: controls smaller than cards, cards smaller than major feature panels. Avoid making every element a pill.
- Use borders before shadows. Shadows should be broad, pale, and low-contrast; reserve stronger depth for one or two focal surfaces.
- Introduce cartoon character through one coherent illustration, a mascot detail, map-like line work, or tactile icon treatment. Do not scatter unrelated emoji, stickers, blobs, or decorative stars across the page.
- Let the illustration support the product story and composition. It must not make the form harder to scan or push the primary action below a small laptop viewport.
- Keep copy concise, warm, and specific. Avoid exaggerated claims, placeholder-sounding headings, and repetitive explanatory text.
- Motion should clarify state: subtle hover lift, selection feedback, progress, and gentle entrance. Respect reduced-motion preferences.
- Implement both light and dark themes only when the product already needs them. Dark mode should retain the same hierarchy rather than invert colors mechanically.

## Page composition

Use a strong opening composition with one dominant message and one visual counterweight. Follow it with the primary task surface, then evidence, output, or reassurance in the order users need it. Vary section composition; do not repeat identical cards across the entire page.

Forms should read as a guided sentence or journey. Group related fields visually, distinguish required decisions from preferences, and keep helper text attached to the field it explains. Results should prioritize summary, key totals, timeline or route, then supporting detail.

## Implementation standard

- Prefer semantic HTML and existing project components.
- Centralize colors, type, radii, shadows, container width, and spacing as tokens.
- Test the exact widths where grids change, not only generic desktop and mobile sizes.
- Prevent text wrapping, icon size, browser-native inputs, and error messages from shifting neighboring alignment unexpectedly.
- Retain visible focus states, keyboard navigation, sufficient contrast, touch targets, and meaningful labels.
- After implementation, run the project's type check/build and inspect the rendered page at desktop, small-laptop, tablet, and mobile widths when browser tooling is available.

## Avoid

- Purple-blue gradients, glass panels everywhere, neon glows, or generic AI-SaaS styling.
- Excessive card nesting, equal visual weight for every block, or a page made entirely of bento tiles.
- Arbitrary rotations on functional UI, uneven field heights, drifting helper text, or local negative margins used to fake alignment.
- Oversized cartoon decoration that competes with the task.
- Hard-coded content or fallback data added merely to make a screen look populated.

For a reusable one-shot request without installing this skill, adapt [references/prompt-template.md](references/prompt-template.md).
