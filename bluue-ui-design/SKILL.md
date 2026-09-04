---
name: bluue-ui-design
description: "Design, implement, revise, or audit product UI using Bluue's preferences: preserve the existing system and essential content, enforce alignment, minimize redundant explanatory copy and container noise, use icons purposefully, build real interactions, and verify the rendered result. Use for Figma or screenshot implementation, visual polish, content replacement, localization, responsive UI, and product-interface QA. Do not use for illustration-only or brand-identity work without a product interface."
---

# Bluue UI Design

Create product UI that is restrained, context-aware, faithful to the supplied material, genuinely interactive, and visibly verified.

The governing principle is:

> Understand the product and existing system first. Change only what the task authorizes, preserve essential information, remove redundant interface explanation, implement real behavior, and judge completion in the rendered interface.

## Classify the Task

Before changing anything, determine which mode applies. A task may combine modes, but do not silently expand one mode into another.

1. **Reference implementation**: Figma, screenshot, existing page, or a specifically named component is the authority.
2. **Visual refinement**: Preserve product meaning, required content, structure, and behavior; improve visual presentation and remove redundant interface explanation when authorized.
3. **Content replacement**: Preserve layout, components, interaction, and visual language; replace only the requested copy, assets, or product content.
4. **New UI design**: Establish a new visual direction only when no existing system or controlling reference applies.

Identify the authoritative reference, the existing design system, the allowed scope of change, the target language, required interactions, and desktop/mobile targets. If these can be inferred safely from the supplied project, inspect the project and proceed. Ask only when a missing choice would materially change the result.

## Non-Negotiable Rules

### Preserve scope, content, and context

- Reuse the existing components, layout logic, typography, spacing, visual language, assets, and interaction patterns whenever they exist.
- Make the requested change without redesigning unrelated areas.
- Keep real business content, user-created content, decision-critical details, warnings, and workflow instructions intact unless the user explicitly authorizes changing them.
- Minimize non-essential descriptive UI copy. Remove repeated headings, subtitles that restate the title, obvious helper text, decorative labels, and explanations already communicated by structure, icons, or state.
- Do not confuse concise UI with missing information. If removing text could change meaning, reduce confidence, or make an unfamiliar action ambiguous, keep it or request authorization.
- When asked to replace content, do not restructure the page unless the new content cannot function within the existing structure; explain that conflict before broadening the change.
- Do not invent product capabilities, assets, UI states, or claims and present them as implemented facts.

### Treat references as authoritative

- Use the exact supplied Figma selection, frame, screenshot, page, route, or named component rather than a merely similar section.
- Reproduce the reference's hierarchy, grouping, density, proportions, component relationships, and meaningful states.
- Do not add cards, thumbnails, sections, controls, or decorative elements absent from the reference unless required for real functionality.
- Do not mechanically copy a reference treatment that conflicts with the established product system. Integrate the reference while preserving product identity, and keep any necessary deviation narrow.
- If the reference or real product asset is unavailable, do not fabricate a replacement mockup that may be mistaken for the final design.

### Build real UI

- Use real interface components and state, not a flattened screenshot or image pretending to be UI.
- Buttons, tabs, cards, filters, toggles, dates, selectors, and CTAs must respond when they appear interactive.
- Keep selection, preview, output, status, loading, completion, and active indicators synchronized.
- Represent the actual product workflow and specific capabilities rather than substituting generic marketing cards.
- Use correct brand, platform, provider, or model icons when those identities matter. Do not use arbitrary placeholders or mismatched icons.

### Use motion deliberately

- Use animation to clarify state changes, hierarchy, progress, reordering, reveal, or completion—not as ambient decoration.
- Trigger staged demonstrations when the relevant section becomes visible or in response to an intentional user action. Do not let the meaningful sequence finish offscreen.
- Keep motion brief and legible, and support `prefers-reduced-motion`.
- Preserve interactive replay when the product demonstration requires users to revisit the current state.

## Visual Direction

Aim for a simple, polished, product-oriented interface with clear hierarchy and low visual noise.

### Alignment and spatial system

- Treat alignment as a primary design constraint. Major headings, toolbars, content grids, side panels, and footer actions should share deliberate edge and baseline relationships.
- Establish a small gutter and spacing system, then reuse it. Avoid near-matching padding values that create subtle drift between adjacent regions.
- Align icons optically with text, not only mathematically. Keep control heights, label baselines, column starts, and repeated row anatomy consistent.
- Check alignment in the rendered desktop and mobile interface; source-code symmetry is not proof of visual alignment.

### Color

- Do not enforce a universal hue or fixed color value. Derive color from the brand, product, content, and current design system.
- Keep the number of colors restrained within one UI. Establish a coherent primary, supporting, neutral, and semantic-state palette instead of assigning unrelated colors to individual modules.
- Use color to express hierarchy, identity, focus, and state; do not make every element compete for attention.
- Do not turn project-specific directions such as a particular blue, avoiding black, or a warm green palette into universal rules.

### Depth and effects

- Do not use shadows unless they communicate necessary elevation, overlay, drag state, or separation that borders, surfaces, spacing, and contrast cannot express clearly.
- When a shadow is necessary, keep it subtle and consistent.
- Use gradients sparingly. A gradient must serve brand expression, a controlled focal point, data meaning, or state communication; it is not the default way to make a design look polished.
- Avoid decorative glow, glass effects, heavy blur, excessive rounding, and ornamental layers when they do not improve comprehension.
- Reduce frame-within-frame composition. Prefer open surfaces, shared alignment, whitespace, tonal bands, dividers, and a single necessary boundary over nested cards and repeated bordered wrappers.
- Inputs, data tables, calendars, modals, and true grouped controls may retain boundaries when those boundaries improve scanning, editing, or interaction clarity.

### Typography, icons, and density

- Preserve the product's existing font unless the task explicitly changes it. Resolve missing fonts rather than silently substituting a visibly different typeface.
- Keep type scale, weight, line height, casing, and alignment consistent.
- Avoid unnecessary all-caps English, especially inside Chinese interfaces; retain legitimate brands, acronyms, and model names.
- Prefer clear outline icons when no existing icon language overrides this preference. Keep stroke weight, optical size, alignment, and metaphor consistent.
- Use a familiar icon in place of a visible label when the meaning is conventional and context is sufficient. Use `icon + short label` for important or less familiar actions; do not replace clarity with icon guessing.
- Every icon-only interactive control needs an accessible name and, when useful, a tooltip. Icons must come from one coherent family unless real platform or brand marks are required.
- Maintain compact but readable information density. Do not create empty marketing layouts that weaken product substance, and do not compress core workspaces merely to fit a short viewport.

## Localization

When the task requests Chinese or global Chinese UI:

- Translate every user-visible layer, including navigation, controls, diagrams, cards, empty states, helper text, product mock UI, and visual components.
- Preserve legitimate brand names, platform names, model names, and required technical identifiers.
- Use natural, direct Chinese rather than literal translation.
- Route reusable product copy through the project's localization system when one exists; scan visual components for hard-coded language as well as body copy.

Do not force Chinese onto a different target locale unless requested.

## Responsive and Accessible Behavior

- Design mobile behavior intentionally rather than shrinking the desktop composition.
- Prevent page-level horizontal overflow. If horizontal browsing is appropriate, contain it within the relevant tab or card region.
- Preserve the readability and functional size of core product panels on short viewports.
- Provide visible focus states and appropriate semantics for interactive controls.
- Use real ARIA state such as `aria-selected` or `aria-pressed` when applicable.
- Do not rely on color alone for selection, success, warning, or error states.

## Working Method

1. Inspect the exact reference, target route, existing components, assets, design tokens, localization structure, and current behavior.
2. State or internally establish what must remain unchanged and what is allowed to change.
3. Establish the alignment grid, content priority, and allowed container layers before styling individual components.
4. Implement the smallest coherent change that fulfills the product and visual requirement.
5. Audit repeated descriptions, nested frames, icon consistency, and edge/baseline alignment.
6. Exercise all visible interactions and verify that related states remain synchronized.
7. Review the rendered UI against the authoritative reference at the intended desktop and mobile sizes.
8. Fix visual, interaction, accessibility, localization, routing, and console issues before declaring completion.

Research comparable products or reusable resources before coding when the task is exploratory or the user asks for a plan first. Research does not authorize copying another product's identity or replacing the supplied reference.

## Per-Version Design Summary

After completing every version that the user can review or test, send a concise design summary in the final response so the user can quickly request changes. Report only material decisions, not the implementation log.

Use three to five short lines and include the categories that apply:

- **Color**: primary, neutral, and semantic-color direction; include exact values only when useful.
- **Typography**: font, hierarchy, density, and important size or weight decisions.
- **Layout**: alignment grid, spacing rhythm, major regions, and responsive behavior.
- **Style**: container model, icon treatment, radius, shadow, gradient, and motion choices.
- **Adjustable next**: one or two high-impact variables the user can change next.

Keep the summary concise and user-editable. Do not bury it inside test results or a long change log.

## Completion Standard

Code completion, a passing build, or a generated screenshot is supporting evidence, not final acceptance.

Before reporting completion, verify as applicable:

- the exact route, locale, anchor, Figma node, or selected component;
- the rendered visual hierarchy and comparison with the source reference;
- real interaction for tabs, buttons, filters, toggles, dates, selectors, CTAs, and generated states;
- synchronized selection, preview, output, and completion state;
- desktop and mobile rendering, including overflow behavior;
- navigation destinations and other affected routes;
- missing fonts, incorrect icons, inconsistent casing, excess colors, unjustified shadows, and decorative gradients;
- drifting edges or baselines, excessive explanatory copy, repeated visible labels, and unnecessary nested frames;
- all visible language layers when localization is in scope;
- keyboard focus, semantic state, reduced motion, and browser console errors or warnings.

If the user says the design has not changed or does not match, return to the exact reference and rendered target. Do not answer with build results as a substitute for visible evidence.

## Prohibited Shortcuts

- Do not use a screenshot as the implemented interface.
- Do not create fake interaction or controls without meaningful state changes.
- Do not remove business content, warnings, or task-critical guidance under the guise of minimalism; reducing redundant interface explanation is encouraged.
- Do not redesign outside the authorized scope.
- Do not substitute an approximately similar component for the specified reference.
- Do not fabricate missing product visuals or unverified capabilities.
- Do not use unnecessary shadows, habitual gradients, or an uncontrolled number of colors.
- Do not stack cards, bordered panels, and rounded wrappers when alignment, spacing, dividers, or icons communicate the structure more clearly.
- Do not ship mismatched icons, missing fonts, hard-coded wrong-language text, or page-level mobile overflow.
- Do not declare the UI finished without inspecting and operating the rendered result.
