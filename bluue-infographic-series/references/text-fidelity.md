# Text Fidelity

Use this reference whenever visible text accuracy matters, especially for non-English output, finance, legal, compliance, scientific, medical, policy, product, or data-heavy infographics.

## Principle

The visual may be stylized. Critical text may not drift.

## Exact-text manifest

Before generation, separate strings into two groups.

### Critical
Must appear exactly as resolved:

- primary numbers
- percentages
- dates
- units
- names
- legal or technical terms
- product names
- jurisdiction names
- short citations
- stage labels
- user-specified wording

### Flexible
May be compressed while preserving meaning:

- subtitle
- explanatory phrases
- supporting captions
- non-essential transitions

## Language rules

1. Explicit user language wins.
2. Otherwise preserve the dominant language of supplied content.
3. If the user provides no substantial source language, default to English.
4. Preserve established proper nouns and official terms in their standard form.
5. Do not introduce a translation merely because the visual style reference is in another language.

## Image-generation text strategy

When using an image generator directly:

- keep visible copy short
- put critical strings in a dedicated exact-text block in the prompt
- avoid long paragraphs
- avoid many similar numerical labels in one frame unless necessary
- prefer 2–5 major text clusters over dozens of small labels
- repeat critical numbers with their units in the prompt
- use short section names and simple typography hierarchy

## Deterministic typography preference

When a task contains substantial text or when exact spelling is essential, prefer deterministic typesetting if the environment supports it.

Recommended pipeline:

```text
1. resolve content and exact text
2. generate / construct background, diagrams, illustration, shapes, and image treatment
3. typeset exact text with HTML/SVG/Canvas or another deterministic renderer
4. render final image
5. visually inspect
```

This is especially preferred for:

- Chinese, Japanese, Korean or multilingual posters with many labels
- compliance and legal terminology
- tables and matrices
- more than ~8 critical strings
- exact citations
- dense quantitative labels

## Review checklist

Before delivery verify:

- every number matches the source
- `%`, currency symbols, units, ×, +/− signs are correct
- no digit is dropped, added, or swapped
- dates and ranges are correct
- names are spelled correctly
- capitalization is intentional
- acronyms are correct
- CJK characters are not malformed
- line breaks do not change meaning
- labels are attached to the correct chart mark or object
- no accidental filler text, pseudo-language, watermark, or invented logo appears

## Recovery sequence

If critical text is wrong:

1. keep the successful composition and style
2. reduce visible text
3. shorten only flexible copy
4. explicitly repeat the exact string
5. regenerate the affected frame
6. if errors persist, switch to deterministic typography

Do not approve an image with a visible critical text error solely because the visual design is strong.
