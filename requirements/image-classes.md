# Image-class conformance profiles (CLS-*)

A *class* (TIFF 5.0 terminology) or *baseline image type* (TIFF 6.0) is a
writer-side profile: the set of fields a conforming writer must emit, plus value
restrictions, for a given kind of image. Readers use profiles to classify files
and to know the minimum they must implement. The machine-readable form of each
profile (required tags and constraints) is the `profiles:` section of
[constraints.yaml](constraints.yaml); this file is the requirement text.

In all profiles, "required" means the field must be present *unless its default
gives the desired value* — the defaulted-field exemption of GEN-002 applies
(TIFF 6.0 §7 states required fields "must be" present but simultaneously blesses
default omission for fields with defaults; libtiff validation should treat a
missing required-with-default field as satisfied by its default).

## TIFF 6.0 baseline image types

### CLS-BILEVEL-6 — Bilevel
- Level: MUST · Actor: writer · Conformance: baseline
- Versions: 6.0– · Container: both · Status: current
- Sources: T6B-044, T6B-DEP-003 (TIFF6 §3)

Required: ImageWidth (256), ImageLength (257), Compression (259) ∈ {1, 2,
32773}, PhotometricInterpretation (262) ∈ {0, 1}, StripOffsets (273),
RowsPerStrip (278), StripByteCounts (279), XResolution (282), YResolution
(283), ResolutionUnit (296). BitsPerSample defaults to 1.

### CLS-GRAY-6 — Grayscale
- Level: MUST · Actor: writer · Conformance: baseline
- Versions: 6.0– · Container: both · Status: current
- Sources: T6B-047, T6B-DEP-004 (TIFF6 §4)

As bilevel, plus BitsPerSample (258) ∈ {4, 8}; Compression restricted to
{1, 32773} (Modified Huffman is bilevel-only, DEP-040).

### CLS-PALETTE-6 — Palette color
- Level: MUST · Actor: writer · Conformance: baseline
- Versions: 6.0– · Container: both · Status: current
- Sources: T6B-050, T6B-DEP-005 (TIFF6 §5)

As grayscale, plus PhotometricInterpretation = 3 and ColorMap (320);
SamplesPerPixel = 1 (DEP-020, DEP-021).

### CLS-RGB-6 — RGB full color
- Level: MUST · Actor: writer · Conformance: baseline
- Versions: 6.0– · Container: both · Status: current
- Sources: T6B-053, T6B-DEP-006 (TIFF6 §6)

As grayscale, plus SamplesPerPixel (277) ≥ 3, BitsPerSample = 8,8,8 (plus an
entry per extra sample, T6B-DEP-024), PhotometricInterpretation = 2; no
ColorMap.

## TIFF 5.0 classes (retired: read-only)

The 5.0 classes are the direct ancestors of the 6.0 baseline types; the notable
differences are that LZW (Compression 5) was part of Class G/P/R conformance
and PackBits was only required for Class B, and that Class P allowed any
BitsPerSample 1–8.

### CLS-B-5 — Class B (bilevel)
- Level: MUST · Actor: writer · Conformance: baseline
- Versions: 5.0–5.0 · Container: classic · Status: retired
- Sources: T5-115, T5-DEP-023 (TIFF5 App. G)

SamplesPerPixel = 1, BitsPerSample = 1, Compression ∈ {1, 2, 32773},
PhotometricInterpretation ∈ {0, 1}; required tag set as CLS-BILEVEL-6.

### CLS-G-5 — Class G (grayscale)
- Level: MUST · Actor: writer · Conformance: baseline
- Versions: 5.0–5.0 · Container: classic · Status: retired
- Sources: T5-116, T5-DEP-024

SamplesPerPixel = 1, BitsPerSample ∈ {4, 8}, Compression ∈ {1, 5},
PhotometricInterpretation ∈ {0, 1}.

### CLS-P-5 — Class P (palette color)
- Level: MUST · Actor: writer · Conformance: baseline
- Versions: 5.0–5.0 · Container: classic · Status: retired
- Sources: T5-117, T5-DEP-025

SamplesPerPixel = 1, BitsPerSample 1–8, Compression ∈ {1, 5},
PhotometricInterpretation = 3, ColorMap present.

### CLS-R-5 — Class R (RGB)
- Level: MUST · Actor: writer · Conformance: baseline
- Versions: 5.0–5.0 · Container: classic · Status: retired
- Sources: T5-118, T5-DEP-026

SamplesPerPixel = 3, BitsPerSample = 8,8,8, PlanarConfiguration ∈ {1, 2},
Compression ∈ {1, 5}, PhotometricInterpretation = 2.

## TIFF 4.0

TIFF 4.0 predates the class system; its per-image requirements are keyed off
SubfileType (DEP-130): when SubfileType ∈ {1, 2}, ImageWidth, ImageLength and
StripOffsets are required, everything else is optional with defaults. Validate
4.0-era files against the tag registry version ranges rather than a profile.
