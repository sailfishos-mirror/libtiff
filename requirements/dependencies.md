# Cross-tag dependency requirements (DEP-*) and class profiles

Generated from [constraints.yaml](constraints.yaml) by `tools/generate.py` — do not edit.
The YAML file carries the machine-readable conditions, severities, relaxation
flags and repair actions; this file is the readable index.

## Image-class profiles

### CLS-BILEVEL-6 — TIFF 6.0 baseline bilevel (Class B successor)
- Versions: 6.0- · Sources: T6B-044, T6B-DEP-003
- Required tags: 256, 257, 259, 262, 273, 278, 279, 282, 283, 296
- Constraint: `Compression in {1, 2, 32773}`
- Constraint: `PhotometricInterpretation in {0, 1}`

### CLS-GRAY-6 — TIFF 6.0 baseline grayscale
- Versions: 6.0- · Sources: T6B-047, T6B-DEP-004
- Required tags: 256, 257, 258, 259, 262, 273, 278, 279, 282, 283, 296
- Constraint: `Compression in {1, 32773}`
- Constraint: `PhotometricInterpretation in {0, 1}`
- Constraint: `BitsPerSample in {4, 8}`

### CLS-PALETTE-6 — TIFF 6.0 baseline palette-color
- Versions: 6.0- · Sources: T6B-050, T6B-DEP-005
- Required tags: 256, 257, 258, 259, 262, 273, 278, 279, 282, 283, 296, 320
- Constraint: `Compression in {1, 32773}`
- Constraint: `PhotometricInterpretation == 3`
- Constraint: `BitsPerSample in {4, 8}`
- Constraint: `SamplesPerPixel == 1`

### CLS-RGB-6 — TIFF 6.0 baseline RGB
- Versions: 6.0- · Sources: T6B-053, T6B-DEP-006
- Required tags: 256, 257, 258, 259, 262, 273, 277, 278, 279, 282, 283, 296
- Constraint: `Compression in {1, 32773}`
- Constraint: `PhotometricInterpretation == 2`
- Constraint: `SamplesPerPixel >= 3`
- Constraint: `BitsPerSample[0] == 8 && BitsPerSample[1] == 8 && BitsPerSample[2] == 8`

### CLS-B-5 — TIFF 5.0 Class B (bilevel)
- Versions: 5.0-5.0 · Sources: T5-115, T5-DEP-023
- Required tags: 256, 257, 259, 262, 273, 278, 279, 282, 283, 296
- Constraint: `SamplesPerPixel == 1 && BitsPerSample == 1`
- Constraint: `Compression in {1, 2, 32773}`
- Constraint: `PhotometricInterpretation in {0, 1}`

### CLS-G-5 — TIFF 5.0 Class G (grayscale)
- Versions: 5.0-5.0 · Sources: T5-116, T5-DEP-024
- Required tags: 256, 257, 258, 259, 262, 273, 278, 279, 282, 283, 296
- Constraint: `SamplesPerPixel == 1 && BitsPerSample in {4, 8}`
- Constraint: `Compression in {1, 5}`
- Constraint: `PhotometricInterpretation in {0, 1}`

### CLS-P-5 — TIFF 5.0 Class P (palette color)
- Versions: 5.0-5.0 · Sources: T5-117, T5-DEP-025
- Required tags: 256, 257, 258, 259, 262, 273, 278, 279, 282, 283, 296, 320
- Constraint: `SamplesPerPixel == 1 && BitsPerSample in {1, 2, 3, 4, 5, 6, 7, 8}`
- Constraint: `Compression in {1, 5}`
- Constraint: `PhotometricInterpretation == 3`

### CLS-R-5 — TIFF 5.0 Class R (RGB)
- Versions: 5.0-5.0 · Sources: T5-118, T5-DEP-026
- Required tags: 256, 257, 258, 259, 262, 273, 277, 278, 279, 282, 283, 296
- Constraint: `SamplesPerPixel == 3 && BitsPerSample[0] == 8 && BitsPerSample[1] == 8 && BitsPerSample[2] == 8`
- Constraint: `PlanarConfiguration in {1, 2}`
- Constraint: `Compression in {1, 5}`
- Constraint: `PhotometricInterpretation == 2`

### CLS-FAX-S — TIFF/FX Profile S (minimal black-and-white)
- Versions: 6.0- · Sources: TFX-049, TFX-050, TFX-051, TFX-053, TFX-060, TFX-069
- Required tags: 254, 256, 257, 258, 259, 262, 266, 273, 277, 278, 279, 282, 283, 292, 296, 297
- Constraint: `BitsPerSample == 1 && SamplesPerPixel == 1`
- Constraint: `Compression == 3 && (T4Options == 0 || T4Options == 4)`
- Constraint: `PhotometricInterpretation == 0`
- Constraint: `ImageWidth == 1728`
- Constraint: `one strip per page (RowsPerStrip >= ImageLength)`
- Constraint: `PageNumber starts at 0 and increments per page`

### CLS-FAX-F — TIFF/FX Profile F (extended black-and-white)
- Versions: 6.0- · Sources: TFX-071, TFX-072, TFX-073, TFX-074, TFX-081, TFX-082, TFX-083
- Required tags: 254, 256, 257, 258, 259, 262, 266, 273, 277, 278, 279, 282, 283, 296, 297
- Constraint: `BitsPerSample == 1`
- Constraint: `Compression in {3, 4}; T4Options in {0, 1, 4, 5} when 3; T6Options == 0 when 4`
- Constraint: `PhotometricInterpretation in {0, 1}`
- Constraint: `ImageWidth in {1728, 2048, 2432, 2592, 3072, 3456, 3648, 4096, 4864}`
- Constraint: `XResolution/YResolution/ImageWidth combinations per T.30 (see TFX-081)`

### CLS-FAX-J — TIFF/FX Profile J (lossless JBIG black-and-white)
- Versions: 6.0- · Sources: TFX-102, TFX-103, TFX-104
- Required tags: 254, 256, 257, 258, 259, 262, 266, 273, 277, 278, 279, 282, 283, 296, 297
- Constraint: `BitsPerSample == 1`
- Constraint: `Compression == 9 (T.85 profile of T.82); T82Options default 0 may be omitted`
- Constraint: `PhotometricInterpretation in {0, 1}`

### CLS-FAX-C — TIFF/FX Profile C (lossy color and grayscale)
- Versions: 6.0- · Sources: TFX-106, TFX-108, TFX-109, TFX-111, TFX-112, TFX-114, TFX-115, TFX-118
- Required tags: 254, 256, 257, 258, 259, 262, 266, 273, 277, 278, 279, 282, 283, 296, 297, 433
- Constraint: `BitsPerSample == 8 per sample`
- Constraint: `Compression == 7 (baseline JPEG per TN2)`
- Constraint: `PhotometricInterpretation == 10 (ITULAB); Decode (433) count = 2*SamplesPerPixel`
- Constraint: `ResolutionUnit == 2; XResolution in {100, 200, 300, 400}; YResolution == XResolution`
- Constraint: `ImageWidth in {864, 1024, 1216, 1728, 2048, 2432, 2592, 3072, 3456, 3648, 4096, 4864}; resolution/width combinations per T.30 (see TFX-115)`

### CLS-FAX-L — TIFF/FX Profile L (lossless color and grayscale)
- Versions: 6.0- · Sources: TFX-122, TFX-123, TFX-124, TFX-125, TFX-130
- Required tags: 254, 256, 257, 258, 259, 262, 266, 273, 277, 278, 279, 282, 283, 296, 297
- Constraint: `Compression == 10 (T.43 via T.82 JBIG)`
- Constraint: `PhotometricInterpretation/SamplesPerPixel/BitsPerSample/Indexed combinations per T.43 image type (see TFX-122)`
- Constraint: `ImageWidth as Profile C; NewSubfileType bit 1 set`
- Constraint: `XResolution in {100, 200, 300, 400}; YResolution == XResolution`

### CLS-FAX-M — TIFF/FX Profile M (Mixed Raster Content)
- Versions: 6.0- · Sources: TFX-133, TFX-141, TFX-142, TFX-144, TFX-146, TFX-148, TFX-150, TFX-151, TFX-155, TFX-158, TFX-171
- Required tags: 254, 256, 257, 258, 259, 262, 266, 273, 277, 278, 279, 282, 283, 296, 297, 330
- Constraint: `3-layer MRC model per T.44; primary (Mask) IFD has NewSubfileType 18, child IFDs 16`
- Constraint: `Compression per layer: Mask in {3, 4, 9}; Foreground/Background in {7, 9, 10}; 1 only for ImageBaseColor-only IFDs`
- Constraint: `StripRowCounts (559) supported; excludes RowsPerStrip in the same IFD`
- Constraint: `child IFDs via SubIFDs (330) require XPosition/YPosition; primary IFD must not use them`
- Constraint: `layer resolutions integer factors of the Mask resolution`

## Dependency rules

### DEP-001 — StripsPerImage arithmetic
- Kind: constrains-value · Versions: 4.0- · Conformance: baseline · Severity: error
- Tags: 257, 278
- When: `organization == 'strips'`
- Assert: `StripsPerImage == ceil_div(ImageLength, RowsPerStrip)`
- Sources: T4-DEP-003, T5-DEP-015, T6B-DEP-014

### DEP-002 — StripOffsets count matches strip organization
- Kind: constrains-value · Versions: 4.0- · Conformance: baseline · Severity: error
- Tags: 273, 284, 277
- When: `organization == 'strips'`
- Assert: `(PlanarConfiguration == 1 && count(StripOffsets) == StripsPerImage) || (PlanarConfiguration == 2 && count(StripOffsets) == SamplesPerPixel * StripsPerImage)`
- Repair (flag `repair.strip-count`): If count(StripOffsets) is exactly 1 and the data is uncompressed, treat the image as a single strip (RowsPerStrip = ImageLength). If more offsets are present than required, ignore the excess.
- Sources: T4-DEP-004, T4-DEP-005, T5-DEP-010, T6B-DEP-014

### DEP-003 — StripByteCounts count matches strip organization
- Kind: constrains-value · Versions: 4.0- · Conformance: baseline · Severity: error
- Tags: 279, 284, 277
- When: `organization == 'strips'`
- Assert: `count(StripByteCounts) == count(StripOffsets)`
- Repair (flag `repair.missing-stripbytecounts`): When StripByteCounts is absent or short: for Compression = 1 compute counts from the row-size formula (DEP-007); for a single-strip image assume the strip extends to end-of-file; otherwise unrecoverable.
- Sources: T4-DEP-006, T4-DEP-007, T5-DEP-011, T6B-DEP-015

### DEP-004 — Strip and tile organization are mutually exclusive
- Kind: forbids · Versions: 6.0- · Conformance: extension · Severity: warning
- Tags: 273, 278, 279, 322, 323, 324, 325
- When: `defined(TileWidth) || defined(TileLength) || defined(TileOffsets) || defined(TileByteCounts)`
- Assert: `!defined(StripOffsets) && !defined(StripByteCounts) && !defined(RowsPerStrip)`
- Relaxation: flag `tolerate.mixed-strip-tile` downgrades to info
- Repair (flag `repair.mixed-strip-tile`): When both are present, use the tile fields and ignore the strip fields.
- Sources: T6X-DEP-008

### DEP-005 — Every image needs exactly one data-location mechanism
- Kind: requires · Versions: 4.0- · Conformance: baseline · Severity: error
- Tags: 273, 279, 324, 325
- Assert: `(defined(StripOffsets) && defined(StripByteCounts)) || (defined(TileOffsets) && defined(TileByteCounts)) || (defined(JPEGInterchangeFormat) && JPEGInterchangeFormat != 0)`
- Sources: PM6-DEP-012, PM6-DEP-013, T6B-066, T4-030
- Notes: The old-style JPEG interchange stream (513) is accepted as a data location only for Compression = 6 legacy files.

### DEP-006 — Planar data plane ordering
- Kind: modifies-meaning · Versions: 4.0- · Conformance: baseline
- Tags: 284, 273, 279, 262
- When: `PlanarConfiguration == 2`
- Semantics: StripOffsets/StripByteCounts (or TileOffsets/TileByteCounts) form a 2D array of SamplesPerPixel rows by StripsPerImage (TilesPerImage) columns, plane-major; for RGB the planes are ordered R, G, B, and for chunky data the components within a pixel are ordered per PhotometricInterpretation (R,G,B for RGB).
- Sources: T4-DEP-009, T4-DEP-021, T4-DEP-022, T6B-DEP-025

### DEP-007 — Uncompressed row size and container type
- Kind: constrains-value · Versions: 4.0- · Conformance: baseline
- Tags: 259, 256, 277, 258, 284
- When: `Compression == 1`
- Semantics: Bytes per row = ceil_div(ImageWidth * SamplesPerPixel * BitsPerSample, 8) for chunky data, ceil_div(ImageWidth * BitsPerSample, 8) per plane for planar data; rows begin on byte boundaries. Data is stored as an array of SHORT when all BitsPerSample = 16, LONG when all = 32, BYTE otherwise, with rows padded to a multiple of that type's size.
- Sources: T4-DEP-014, T4-DEP-015, T4-DEP-016, T5-DEP-022, T6B-DEP-011
- Notes: Compression 32771 (4.0 only) pads each row to a 2-byte word boundary instead.

### DEP-008 — PlanarConfiguration irrelevant for single-sample images
- Kind: modifies-meaning · Versions: 4.0- · Conformance: baseline
- Tags: 277, 284
- When: `SamplesPerPixel == 1`
- Semantics: PlanarConfiguration 1 and 2 are equivalent; writers should omit the tag; readers must accept either value without effect.
- Sources: T4-DEP-008, T5-DEP-014, T6B-DEP-021

### DEP-010 — BitsPerSample count equals SamplesPerPixel
- Kind: constrains-value · Versions: 4.0- · Conformance: baseline · Severity: error
- Tags: 258, 277
- When: `defined(BitsPerSample)`
- Assert: `count(BitsPerSample) == SamplesPerPixel`
- Repair (flag `repair.bitspersample-count`): If count(BitsPerSample) == 1 and SamplesPerPixel > 1, replicate the single value across all samples (very common vendor deviation).
- Sources: T5-DEP-009, T6B-DEP-012
- Notes: Writers must write all values even when identical (6.0).

### DEP-011 — Min/MaxSampleValue count equals SamplesPerPixel
- Kind: constrains-value · Versions: 4.0- · Conformance: baseline · Severity: warning
- Tags: 280, 281, 277
- When: `defined(MinSampleValue) || defined(MaxSampleValue)`
- Assert: `count(MinSampleValue) == SamplesPerPixel && count(MaxSampleValue) == SamplesPerPixel`
- Relaxation: flag `tolerate.minmax-count` downgrades to info
- Sources: T5-DEP-013, T6B-DEP-019

### DEP-012 — MaxSampleValue default derives from BitsPerSample
- Kind: selects-default · Versions: 4.0- · Conformance: baseline
- Tags: 281, 258
- When: `!defined(MaxSampleValue)`
- Semantics: Effective MaxSampleValue = pow2(BitsPerSample) - 1 per sample.
- Sources: T4-DEP-018, T5-DEP-012, T6B-DEP-018

### DEP-013 — Padded BitsPerSample must not distort the stated sample range
- Kind: requires · Versions: 4.0-4.0 · Conformance: baseline
- Tags: 258, 280, 281
- When: `writer pads BitsPerSample up to a power of 2`
- Semantics: MinSampleValue/MaxSampleValue must state the true data range, not the padded range. Retired with the 5.0 redefinition of 280/281 as statistical-only.
- Sources: T4-DEP-017

### DEP-020 — Palette-color images require ColorMap and one sample
- Kind: requires · Versions: 5.0- · Conformance: baseline · Severity: error
- Tags: 262, 320, 277
- When: `PhotometricInterpretation == 3`
- Assert: `defined(ColorMap) && SamplesPerPixel == 1`
- Repair (flag `repair.missing-colormap`): Treat as grayscale (PhotometricInterpretation = 1) when ColorMap is absent; report the file as non-conformant.
- Sources: T5-DEP-002, T6B-DEP-007, PM6-DEP-017

### DEP-021 — ColorMap count is 3 * 2**BitsPerSample
- Kind: constrains-value · Versions: 5.0- · Conformance: baseline · Severity: error
- Tags: 320, 258
- When: `defined(ColorMap) && Indexed == 0`
- Assert: `count(ColorMap) == 3 * pow2(BitsPerSample)`
- Repair (flag `repair.colormap-count`): If the map is shorter, pad with zeros; if longer, ignore the excess.
- Sources: T5-DEP-006, T6B-DEP-013
- Notes: Vendor deviation handled separately: 8-bit-scaled ColorMap values (all values <= 255 in a nominally 16-bit map) should be detected and multiplied by 257 under flag repair.colormap-8bit.

### DEP-022 — Generalized indexed ColorMap entry width (PM6)
- Kind: constrains-value · Versions: 6.0- · Conformance: PM6
- Tags: 320, 346, 334, 262
- When: `Indexed == 1`
- Semantics: Components per ColorMap entry = 3 for RGB and CIELab base color spaces, 4 for CMYK, NumberOfInks for other separated spaces; total count = components * pow2(BitsPerSample).
- Sources: PM6-DEP-008

### DEP-023 — Transparency mask constraints
- Kind: requires · Versions: 5.0- · Conformance: baseline · Severity: error
- Tags: 262, 277, 258, 256, 257
- When: `PhotometricInterpretation == 4`
- Assert: `SamplesPerPixel == 1 && BitsPerSample == 1`
- Sources: T5-DEP-003, T6B-DEP-008
- Notes: ImageWidth/ImageLength must additionally equal those of the image being masked (not checkable within a single IFD). PackBits compression is recommended for masks.

### DEP-024 — NewSubfileType mask bit implies transparency-mask photometric
- Kind: requires · Versions: 5.0- · Conformance: baseline · Severity: error
- Tags: 254, 262
- When: `bit(NewSubfileType, 2) == 1`
- Assert: `PhotometricInterpretation == 4`
- Sources: T5-DEP-004, T6B-DEP-009

### DEP-025 — GrayResponseCurve count is 2**BitsPerSample
- Kind: constrains-value · Versions: 4.0- · Conformance: baseline · Severity: error
- Tags: 291, 258
- When: `defined(GrayResponseCurve)`
- Assert: `count(GrayResponseCurve) == pow2(BitsPerSample)`
- Sources: T4-DEP-019, T5-DEP-008

### DEP-026 — GrayResponseCurve values are in GrayResponseUnit units
- Kind: modifies-meaning · Versions: 4.0- · Conformance: baseline
- Tags: 291, 290
- When: `defined(GrayResponseCurve)`
- Semantics: Curve values are optical densities in units of GrayResponseUnit (default hundredths). In 5.0 a present curve overrides PhotometricInterpretation for interpretation purposes.
- Sources: T4-DEP-025, T5-DEP-005

### DEP-027 — TransferFunction count and table sharing
- Kind: constrains-value · Versions: 4.0- · Conformance: extension · Severity: error
- Tags: 301, 258
- When: `defined(TransferFunction)`
- Assert: `count(TransferFunction) == pow2(BitsPerSample) || count(TransferFunction) == 3 * pow2(BitsPerSample)`
- Sources: T6X-DEP-020, T4-DEP-020, T5-DEP-007
- Notes: The single-table (shared) form requires equal BitsPerSample across channels and is valid from 6.0 only; 4.0/5.0 always used three concatenated R,G,B curves (in 4.0 scaled by ColorResponseUnit 300).

### DEP-028 — TransferFunction photometric applicability
- Kind: forbids · Versions: 6.0- · Conformance: extension · Severity: warning
- Tags: 301, 262
- When: `defined(TransferFunction)`
- Assert: `PhotometricInterpretation in {0, 1, 2, 3, 6}`
- Sources: T6X-DEP-021

### DEP-029 — TransferRange only for RGB and YCbCr
- Kind: forbids · Versions: 6.0- · Conformance: extension · Severity: warning
- Tags: 342, 262
- When: `defined(TransferRange)`
- Assert: `PhotometricInterpretation in {2, 6}`
- Sources: T6X-DEP-022

### DEP-030 — ReferenceBlackWhite only for RGB and YCbCr
- Kind: forbids · Versions: 6.0- · Conformance: extension · Severity: warning
- Tags: 532, 262
- When: `defined(ReferenceBlackWhite)`
- Assert: `PhotometricInterpretation in {2, 6}`
- Sources: T6X-DEP-023

### DEP-031 — Colorimetric interpretation requires WhitePoint and primaries
- Kind: modifies-meaning · Versions: 6.0- · Conformance: extension
- Tags: 318, 319
- When: `defined(WhitePoint) && defined(PrimaryChromaticities)`
- Semantics: Only with both fields present does the image have a full colorimetric interpretation; otherwise rendering is application/hardware dependent.
- Sources: T6X-DEP-024

### DEP-032 — CCITT compression implies photometric interpretation (4.0)
- Kind: modifies-meaning · Versions: 4.0-4.0 · Conformance: baseline
- Tags: 259, 262
- When: `Compression in {2, 3, 4}`
- Semantics: In 4.0-era files readers should ignore PhotometricInterpretation for CCITT-compressed images (the scheme implies WhiteIsZero). From 5.0, PhotometricInterpretation is authoritative; see DEP-033.
- Sources: T4-DEP-023

### DEP-033 — BlackIsZero reverses CCITT run colors
- Kind: modifies-meaning · Versions: 5.0- · Conformance: baseline
- Tags: 259, 262
- When: `Compression in {2, 3, 4} && PhotometricInterpretation == 1`
- Semantics: The reader must reverse the meaning of the CCITT white/black runs when decoding for display or print.
- Sources: T6B-DEP-022, T6X-DEP-001

### DEP-034 — Non-default gamma must be declared
- Kind: requires · Versions: 6.0- · Conformance: extension
- Tags: 262, 291, 301
- When: `image data deviates from the photometric's implied transfer characteristic`
- Semantics: Data other than the implied linear (bilevel/gray) or NTSC gamma-2.2 (RGB) characteristic requires GrayResponseCurve or TransferFunction to describe the deviation.
- Sources: T6X-DEP-040

### DEP-035 — Bilevel Threshholding values require 1-bit data (4.0)
- Kind: requires · Versions: 4.0-4.0 · Conformance: baseline · Severity: warning
- Tags: 263, 258
- When: `Threshholding in {1, 2}`
- Assert: `BitsPerSample == 1`
- Sources: T4-DEP-012

### DEP-036 — Cell dimensions only meaningful for ordered dither
- Kind: forbids · Versions: 4.0- · Conformance: baseline · Severity: info
- Tags: 263, 264, 265
- When: `defined(CellWidth) || defined(CellLength)`
- Assert: `Threshholding == 2`
- Sources: T4-DEP-013, T5-DEP-017, T6B-DEP-020

### DEP-040 — Modified Huffman requires bilevel data
- Kind: requires · Versions: 4.0- · Conformance: baseline · Severity: error
- Tags: 259, 258
- When: `Compression == 2`
- Assert: `BitsPerSample == 1 && SamplesPerPixel == 1`
- Sources: T4-DEP-011, T5-DEP-001, T6B-DEP-010

### DEP-041 — Decoded run lengths must sum to ImageWidth
- Kind: constrains-value · Versions: 4.0- · Conformance: baseline
- Tags: 259, 256
- When: `Compression == 2`
- Semantics: In each decoded row the run lengths must total exactly ImageWidth; any other total is an unrecoverable decode error. Rows begin with a white run (possibly of length 0); each row decodes independently and begins on a byte boundary; no EOL/RTC codes are used.
- Sources: T4-DEP-027, T6B-117

### DEP-042 — T4Options governs Group 3 coding
- Kind: constrains-value · Versions: 4.0- · Conformance: extension
- Tags: 259, 292, 278
- When: `Compression == 3`
- Semantics: T4Options (292) selects 1-D vs 2-D coding, uncompressed mode, and EOL byte alignment. With 2-D coding (bit 0 set) each strip must begin with a 1-D coded line and RowsPerStrip should be a multiple of the K parameter. T4Options is meaningless for other compressions.
- Sources: T5-DEP-018, T6X-DEP-002

### DEP-043 — T6Options governs Group 4 coding
- Kind: constrains-value · Versions: 4.0- · Conformance: extension
- Tags: 259, 293
- When: `Compression == 4`
- Semantics: T6Options (293) is the only option field readers should honour for T.6; writers unable to guarantee absence of uncompressed-mode material must set bit 1.
- Sources: T5-DEP-019, T6X-DEP-003, T6X-DEP-004

### DEP-044 — T.6 encoding requires exact line width
- Kind: requires · Versions: 6.0- · Conformance: extension · Severity: error
- Tags: 259, 256, 322
- When: `Compression == 4`
- Assert: `ImageWidth states the exact pixel count per line (TileWidth when tiled)`
- Sources: T6X-DEP-005

### DEP-045 — LZW strips are independent bitstreams
- Kind: constrains-value · Versions: 5.0- · Conformance: extension
- Tags: 259, 266
- When: `Compression == 5`
- Semantics: Each strip/tile is compressed independently, begins on a byte boundary with a ClearCode, ends with an EndOfInformation code, and is interpreted with FillOrder = 1 regardless of the FillOrder tag.
- Sources: T6X-DEP-041, T5-102

### DEP-046 — Readers must honour Predictor before LZW/Deflate data
- Kind: requires · Versions: 5.0- · Conformance: extension
- Tags: 259, 317
- When: `Compression in {5, 8}`
- Semantics: The reader must inspect Predictor (317); an unrecognized value is fatal for the image.
- Sources: T5-DEP-020

### DEP-047 — Predictor 2 preconditions
- Kind: constrains-value · Versions: 5.0- · Conformance: extension · Severity: warning
- Tags: 317, 259, 258, 284, 277
- When: `Predictor == 2`
- Assert: `Compression in {5, 8} && BitsPerSample uniform across samples`
- Relaxation: flag `tolerate.predictor-any-compression` downgrades to info
- Sources: T5-DEP-021, T6X-DEP-006, T6X-DEP-007, PM6-DEP-016, PS-DEP-001
- Notes: 6.0 defines Predictor 2 for LZW only; the PS technote extends it to Deflate (8). For chunky data differencing runs per-channel with an offset of SamplesPerPixel. Vendors also combine Predictor 2 with other compressions; readers may accept under the relax flag.

### DEP-048 — Predictor 3 (floating point) preconditions and semantics
- Kind: constrains-value · Versions: 6.0- · Conformance: TN3 · Severity: warning
- Tags: 317, 258, 259, 339
- When: `Predictor == 3`
- Assert: `BitsPerSample % 8 == 0`
- Semantics: Sample bytes are reordered into big-endian byte-significance planes per row, then differenced horizontally per channel, independent of the file byte order; readers reverse both steps. Intended for use with LZW (5) and Deflate (8) and floating point data (SampleFormat 3).
- Sources: TN3-DEP-003, TN3-DEP-004, TN3-DEP-005

### DEP-049 — PackBits output is interpreted as uncompressed
- Kind: modifies-meaning · Versions: 4.0- · Conformance: baseline
- Tags: 259, 277, 258, 284
- When: `Compression == 32773`
- Semantics: After decompression the data is laid out exactly as Compression = 1 (DEP-007). Each row is coded separately: the expected decoded byte count per row is the DEP-007 row size, and encoding state must not cross row boundaries.
- Sources: T4-DEP-028, T6B-113

### DEP-050 — Old-style JPEG requires JPEGProc
- Kind: requires · Versions: 6.0- · Conformance: extension · Severity: error
- Tags: 259, 512
- When: `Compression == 6`
- Assert: `defined(JPEGProc)`
- Relaxation: flag `tolerate.ojpeg-missing-fields` downgrades to warning
- Repair (flag `repair.ojpeg`): Many vendors wrote broken Compression=6 files. When JPEGProc or the table tags are missing but a JPEGInterchangeFormat stream exists, decode that stream directly; assume JPEGProc=1.
- Sources: T6X-DEP-031

### DEP-051 — Old-style JPEG mandatory table fields
- Kind: requires · Versions: 6.0- · Conformance: extension · Severity: error
- Tags: 512, 519, 520, 521
- When: `Compression == 6`
- Assert: `defined(JPEGDCTables) && (JPEGProc == 14 || (defined(JPEGQTables) && defined(JPEGACTables)))`
- Relaxation: flag `tolerate.ojpeg-missing-fields` downgrades to warning
- Sources: T6X-DEP-034, T6X-DEP-035, T6X-DEP-032

### DEP-052 — Lossless old-style JPEG requires predictors
- Kind: requires · Versions: 6.0- · Conformance: extension · Severity: error
- Tags: 512, 517, 518
- When: `Compression == 6 && JPEGProc == 14`
- Assert: `defined(JPEGLosslessPredictors)`
- Sources: T6X-DEP-033
- Notes: JPEGACTables and JPEGQTables do not apply to lossless; JPEGPointTransforms defaults to 0.

### DEP-053 — Old-style JPEG restart interval alignment
- Kind: constrains-value · Versions: 6.0- · Conformance: extension
- Tags: 259, 273, 324, 515
- When: `Compression == 6 && multiple strips or tiles`
- Semantics: Each strip/tile offset must point to the start of a restart interval and contain an integral number of restart intervals.
- Sources: T6X-DEP-037

### DEP-054 — Old-style JPEG interchange-format tile height
- Kind: constrains-value · Versions: 6.0- · Conformance: extension · Severity: error
- Tags: 259, 513, 322, 323, 256
- When: `Compression == 6 && defined(JPEGInterchangeFormat) && JPEGInterchangeFormat != 0 && TileWidth < ImageWidth`
- Assert: `TileLength == height of one JPEG MCU`
- Sources: T6X-DEP-036

### DEP-055 — Compression 6 and tags 512-521 are deprecated
- Kind: modifies-meaning · Versions: 6.0- · Conformance: TN2
- Tags: 259, 512, 513, 514, 515, 517, 518, 519, 520, 521
- Semantics: Writers must not produce new Compression = 6 files (use 7 with JPEGTables 347). Readers may continue to interpret them per TIFF 6.0 Section 22. The tag numbers remain reserved indefinitely.
- Sources: TN2-DEP-018, TN2-002

### DEP-060 — JPEG 7 forbids palette and mask photometrics
- Kind: forbids · Versions: 6.0- · Conformance: TN2 · Severity: error
- Tags: 259, 262
- When: `Compression == 7`
- Assert: `PhotometricInterpretation != 3 && PhotometricInterpretation != 4`
- Sources: TN2-DEP-001, PS-DEP-003

### DEP-061 — JPEG 7 segment structure
- Kind: constrains-value · Versions: 6.0- · Conformance: TN2 · Severity: error
- Tags: 259, 284, 277
- When: `Compression == 7`
- Assert: `Each strip/tile is a complete ISO/IEC 10918-1 datastream whose component count equals SamplesPerPixel for PlanarConfiguration 1 and equals 1 for PlanarConfiguration 2`
- Sources: TN2-DEP-002, TN2-DEP-003, PS-DEP-008, PS-DEP-009

### DEP-062 — JPEG 7 chunky data requires uniform BitsPerSample
- Kind: constrains-value · Versions: 6.0- · Conformance: TN2 · Severity: error
- Tags: 284, 258
- When: `Compression == 7 && PlanarConfiguration == 1`
- Assert: `BitsPerSample uniform across all samples`
- Sources: TN2-DEP-004, PS-DEP-007
- Notes: Planar components may differ in depth (each has its own SOFn).

### DEP-063 — JPEG 7 SOFn precision must match BitsPerSample
- Kind: constrains-value · Versions: 6.0- · Conformance: TN2 · Severity: error
- Tags: 259, 258
- When: `Compression == 7`
- Assert: `SOFn precision == BitsPerSample, and: SOF0 implies precision 8; SOF1 implies precision in {8, 12}; SOF3 implies 2 <= precision <= 16`
- Sources: TN2-DEP-006, TN2-DEP-007, TN2-DEP-008, PS-DEP-006

### DEP-064 — JPEG 7 strip height must cover whole MCUs
- Kind: constrains-value · Versions: 6.0- · Conformance: TN2 · Severity: error
- Tags: 259, 278, 257, 530
- When: `Compression == 7 && organization == 'strips' && RowsPerStrip < ImageLength && SOFn is DCT-based`
- Assert: `RowsPerStrip % (8 * max vertical sampling factor) == 0`
- Relaxation: flag `tolerate.jpeg-strip-height` downgrades to warning
- Sources: TN2-DEP-009, TN2-DEP-010, PS-DEP-012
- Notes: Single-strip images (RowsPerStrip >= ImageLength) are exempt. For YCbCrSubSampling [2,2] this means a multiple of 16. Lossless SOF3 files are exempt (DEP-066).

### DEP-065 — JPEG 7 tile dimensions must cover whole MCUs
- Kind: constrains-value · Versions: 6.0- · Conformance: TN2 · Severity: error
- Tags: 259, 322, 323, 530
- When: `Compression == 7 && organization == 'tiles' && SOFn is DCT-based`
- Assert: `TileWidth % (8 * max horizontal sampling factor) == 0 && TileLength % (8 * max vertical sampling factor) == 0`
- Sources: TN2-DEP-024, PS-DEP-013

### DEP-066 — Lossless JPEG exempts size multiples
- Kind: modifies-meaning · Versions: 6.0- · Conformance: TN2
- Tags: 259, 278, 322, 323
- When: `Compression == 7 && SOFn == SOF3`
- Semantics: The MCU-multiple constraints DEP-064/DEP-065 do not apply.
- Sources: TN2-DEP-011, PS-DEP-014

### DEP-067 — JPEGTables presence semantics
- Kind: constrains-value · Versions: 6.0- · Conformance: TN2 · Severity: error
- Tags: 347, 259
- When: `Compression == 7`
- Assert: `defined(JPEGTables) implies (JPEGTables is a valid abbreviated table-specification datastream; segments may omit tables it defines, must not redefine them, and must not reference tables defined nowhere). !defined(JPEGTables) implies every segment defines every table it references.`
- Sources: TN2-DEP-012, TN2-DEP-013, TN2-DEP-019, PS-DEP-004, PS-DEP-005
- Notes: Readers must load JPEGTables before processing any segment.

### DEP-068 — JPEG subsampling only for YCbCr
- Kind: constrains-value · Versions: 6.0- · Conformance: TN2 · Severity: error
- Tags: 262, 530
- When: `Compression == 7 && PhotometricInterpretation != 6`
- Assert: `all JPEG sampling factors == 1`
- Sources: TN2-DEP-016

### DEP-069 — JPEG 7 interleave limits
- Kind: requires · Versions: 6.0- · Conformance: TN2 · Severity: error
- Tags: 277
- When: `Compression == 7 && (SamplesPerPixel > 4 || MCU would exceed 10 blocks)`
- Assert: `one scan per component instead of a single interleaved scan`
- Sources: TN2-DEP-017

### DEP-070 — JPEG 7 stored color description must match the datastream
- Kind: requires · Versions: 6.0- · Conformance: PS · Severity: error
- Tags: 259, 262, 530
- When: `Compression == 7 && color conversion or downsampling applied before compression`
- Assert: `PhotometricInterpretation and YCbCrSubSampling describe the data as stored in the file, not the pre-conversion source`
- Sources: PS-DEP-002

### DEP-071 — YCbCr pixel structure and compression set
- Kind: constrains-value · Versions: 6.0- · Conformance: extension · Severity: error
- Tags: 262, 277, 258, 259
- When: `PhotometricInterpretation == 6`
- Assert: `SamplesPerPixel == 3 && BitsPerSample == [8, 8, 8] && Compression in {1, 5, 6, 7}`
- Sources: T6X-DEP-026
- Notes: 6.0 lists {1, 5, 6}; Compression 7 added by TN2/PS.

### DEP-072 — Subsampling factor ordering
- Kind: constrains-value · Versions: 6.0- · Conformance: extension · Severity: error
- Tags: 530
- When: `defined(YCbCrSubSampling)`
- Assert: `YCbCrSubSampling[0] in {1, 2, 4} && YCbCrSubSampling[1] in {1, 2, 4} && YCbCrSubSampling[1] <= YCbCrSubSampling[0]`
- Sources: T6X-DEP-028

### DEP-073 — Image and segment dimensions must be subsampling multiples
- Kind: constrains-value · Versions: 6.0- · Conformance: extension · Severity: error
- Tags: 530, 256, 257, 278, 322, 323
- When: `PhotometricInterpretation == 6`
- Assert: `ImageWidth % ChromaSubsampleHoriz == 0 && ImageLength % ChromaSubsampleVert == 0 && (organization == 'tiles' ? (TileWidth % ChromaSubsampleHoriz == 0 && TileLength % ChromaSubsampleVert == 0) : (RowsPerStrip >= ImageLength || RowsPerStrip % ChromaSubsampleVert == 0))`
- Relaxation: flag `tolerate.ycbcr-dims` downgrades to warning
- Repair (flag `repair.ycbcr-dims`): Round the affected dimension up to the next multiple when decoding (writers were told to pad; the last samples are padding).
- Sources: T6X-DEP-029, TN2-DEP-023, TN2-DEP-024, TN2-DEP-025
- Notes: TN2 exempts single-strip images from the RowsPerStrip multiple. Dimensions are always measured in luma samples (TN2).

### DEP-074 — YCbCr requires explicit ReferenceBlackWhite
- Kind: requires · Versions: 6.0- · Conformance: extension · Severity: warning
- Tags: 262, 532
- When: `PhotometricInterpretation == 6`
- Assert: `defined(ReferenceBlackWhite)`
- Relaxation: flag `tolerate.missing-refblackwhite` downgrades to info
- Repair (flag `repair.missing-refblackwhite`): Assume CCIR 601-1 video range [15, 235, 128, 240, 128, 240] or full range [0, 255, 128, 255, 128, 255] per a caller-selected policy; full range matches JFIF-style data.
- Sources: T6X-DEP-025, TN2-DEP-014
- Notes: The generic default (DEP-030 family) is inappropriate for YCbCr.

### DEP-075 — Non-601 conversion requires explicit coefficients
- Kind: requires · Versions: 6.0- · Conformance: extension · Severity: warning
- Tags: 262, 529
- When: `PhotometricInterpretation == 6 && conversion differs from CCIR 601-1`
- Assert: `defined(YCbCrCoefficients)`
- Sources: T6X-DEP-027

### DEP-076 — Chunky YCbCr data unit ordering
- Kind: modifies-meaning · Versions: 6.0- · Conformance: extension
- Tags: 262, 284, 530
- When: `PhotometricInterpretation == 6 && PlanarConfiguration == 1`
- Semantics: Samples are stored as data units of ChromaSubsampleVert x ChromaSubsampleHoriz Y samples followed by one Cb and one Cr sample; rows of data units are traversed left-to-right, top-to-bottom.
- Sources: T6X-DEP-030

### DEP-077 — Planar subsampled YCbCr strip/tile geometry
- Kind: modifies-meaning · Versions: 6.0- · Conformance: TN2
- Tags: 284, 530, 338
- When: `PhotometricInterpretation == 6 && PlanarConfiguration == 2`
- Semantics: All components have the same strip/tile count, but chroma segments contain fewer samples per the subsampling factors. Extra sample channels are never subsampled (they match the luma sample count).
- Sources: TN2-DEP-021, TN2-DEP-022, TN2-DEP-015

### DEP-080 — Separated pixel structure
- Kind: constrains-value · Versions: 6.0- · Conformance: extension · Severity: error
- Tags: 262, 277, 258, 334, 338
- When: `PhotometricInterpretation == 5`
- Assert: `SamplesPerPixel - count(ExtraSamples) == NumberOfInks && BitsPerSample == 8 per ink`
- Relaxation: flag `tolerate.separated-depth` downgrades to warning
- Sources: T6X-DEP-014, T6X-DEP-042
- Notes: 6.0 defines only 8-bit separated data; 16-bit exists in the wild.

### DEP-081 — CMYK ink set forbids InkNames
- Kind: forbids · Versions: 6.0- · Conformance: extension · Severity: info
- Tags: 332, 333
- When: `InkSet == 1`
- Assert: `!defined(InkNames)`
- Sources: T6X-DEP-015

### DEP-082 — Non-CMYK ink sets require names and count
- Kind: requires · Versions: 6.0- · Conformance: extension · Severity: warning
- Tags: 332, 333, 334
- When: `InkSet == 2`
- Assert: `defined(InkNames) && defined(NumberOfInks)`
- Sources: PM6-DEP-010

### DEP-083 — InkNames string count equals NumberOfInks
- Kind: constrains-value · Versions: 6.0- · Conformance: extension · Severity: error
- Tags: 333, 334
- When: `defined(InkNames)`
- Assert: `number of NUL-terminated strings in InkNames == NumberOfInks`
- Sources: T6X-DEP-016

### DEP-084 — DotRange bounds
- Kind: constrains-value · Versions: 6.0- · Conformance: extension · Severity: warning
- Tags: 336, 258
- When: `defined(DotRange)`
- Assert: `DotRange[0] >= 0 && DotRange[1] <= pow2(BitsPerSample) - 1 && DotRange[0] < DotRange[1]`
- Sources: T6X-DEP-017

### DEP-090 — Extra components require ExtraSamples
- Kind: requires · Versions: 6.0- · Conformance: baseline · Severity: error
- Tags: 338, 277, 262
- When: `SamplesPerPixel > components implied by PhotometricInterpretation`
- Assert: `count(ExtraSamples) == SamplesPerPixel - implied components`
- Repair (flag `repair.missing-extrasamples`): Treat surplus channels as ExtraSamples value 0 (unspecified); for the common RGBA case (PhotometricInterpretation 2, SamplesPerPixel 4, no ExtraSamples) optionally assume unassociated alpha.
- Sources: T6B-DEP-016, PM6-DEP-015

### DEP-091 — Readers must not infer SamplesPerPixel from photometric
- Kind: modifies-meaning · Versions: 6.0- · Conformance: baseline
- Tags: 338, 277, 262
- Semantics: SamplesPerPixel is authoritative; extra components are stored last within each pixel and sized by their BitsPerSample entries.
- Sources: T6X-DEP-019, T6B-DEP-016, T6B-DEP-024

### DEP-092 — Associated alpha is premultiplied and unique
- Kind: constrains-value · Versions: 6.0- · Conformance: extension · Severity: error
- Tags: 338, 262, 277
- When: `1 in ExtraSamples`
- Assert: `2 not in ExtraSamples && color components are stored premultiplied by the alpha in component SamplesPerPixel-1`
- Sources: T6X-DEP-018, T6B-DEP-017
- Notes: Mixing associated (1) and unassociated (2) alpha in one image is undefined.

### DEP-100 — Tiled images require the full tile tag set
- Kind: requires · Versions: 6.0- · Conformance: extension · Severity: error
- Tags: 322, 323, 324, 325
- When: `organization == 'tiles'`
- Assert: `defined(TileWidth) && defined(TileLength) && defined(TileOffsets) && defined(TileByteCounts)`
- Sources: T6X-DEP-009, PM6-DEP-014

### DEP-101 — Tile dimensions are multiples of 16
- Kind: constrains-value · Versions: 6.0- · Conformance: extension · Severity: warning
- Tags: 322, 323
- When: `organization == 'tiles'`
- Assert: `TileWidth % 16 == 0 && TileLength % 16 == 0`
- Relaxation: flag `tolerate.tile-size` downgrades to info
- Sources: T6X-DEP-010, T6X-DEP-011
- Notes: TIFF 6.0 internal inconsistency: the Section 22 JPEG minimum requirements table says "multiple of 8". Validate multiples of 16; accept multiples of 8 for legacy Compression 6 files.

### DEP-102 — Tile offset/count array sizes
- Kind: constrains-value · Versions: 6.0- · Conformance: extension · Severity: error
- Tags: 324, 325, 284, 277
- When: `organization == 'tiles'`
- Assert: `(PlanarConfiguration == 1 && count(TileOffsets) == TilesPerImage && count(TileByteCounts) == TilesPerImage) || (PlanarConfiguration == 2 && count(TileOffsets) == SamplesPerPixel * TilesPerImage && count(TileByteCounts) == SamplesPerPixel * TilesPerImage)`
- Sources: T6X-DEP-012, T6X-DEP-013

### DEP-110 — Unhandled SampleFormat must terminate gracefully
- Kind: modifies-meaning · Versions: 6.0- · Conformance: baseline
- Tags: 339
- When: `SampleFormat != 1`
- Semantics: A reader that cannot process the sample format must fail the image gracefully rather than misinterpret the data.
- Sources: T6B-DEP-023

### DEP-111 — Reduced-precision floating point layouts (TN3)
- Kind: modifies-meaning · Versions: 6.0- · Conformance: TN3
- Tags: 339, 258
- When: `SampleFormat == 3 && BitsPerSample in {16, 24}`
- Semantics: BitsPerSample 16: 1 sign bit, 5 exponent bits (bias 15), 10 mantissa bits (IEEE 754 half / OpenEXR HALF). BitsPerSample 24: 1 sign bit, 7 exponent bits (bias 63), 16 mantissa bits. Draft 1 of TN3 printed incorrect biases (16 and 64); draft 2 corrected them.
- Sources: TN3-DEP-001, TN3-DEP-002

### DEP-115 — L*a*b* pixel structure
- Kind: constrains-value · Versions: 6.0- · Conformance: extension · Severity: error
- Tags: 262, 258, 277, 338
- When: `PhotometricInterpretation in {8, 9}`
- Assert: `SamplesPerPixel - count(ExtraSamples) in {1, 3} && BitsPerSample in {8, 16} per component`
- Sources: T6X-DEP-038, PS-DEP-017, PS-DEP-016
- Notes: 6.0 defines 8-bit; the PS technote adds 16-bit encodings. Difference of 1 = monochrome L*-only, 3 = full L*a*b*.

### DEP-116 — L*a*b* excludes colorimetry tags
- Kind: forbids · Versions: 6.0- · Conformance: extension · Severity: warning
- Tags: 262, 318, 319, 301
- When: `PhotometricInterpretation == 8`
- Assert: `!defined(WhitePoint) && !defined(PrimaryChromaticities) && !defined(TransferFunction)`
- Sources: T6X-DEP-039
- Notes: PS technote later re-purposes WhitePoint for Lab images with default D50 (DEP-117); apply this rule only to strict 6.0 validation.

### DEP-117 — Lab white point defaults to D50
- Kind: selects-default · Versions: 6.0- · Conformance: PS
- Tags: 318, 262
- When: `PhotometricInterpretation in {8, 9} && !defined(WhitePoint)`
- Semantics: The effective white point is CIE D50.
- Sources: PS-DEP-018

### DEP-118 — ICCLab encoding offset
- Kind: modifies-meaning · Versions: 6.0- · Conformance: PM6
- Tags: 262
- When: `PhotometricInterpretation == 9`
- Semantics: a*/b* are stored offset by +128 relative to PhotometricInterpretation 8 (range 0..255 for 8-bit); L* is unchanged. For 16-bit data see the PS technote value ranges.
- Sources: PM6-DEP-009, PS-DEP-016

### DEP-120 — SubIFD chaining
- Kind: constrains-value · Versions: 6.0- · Conformance: PM6
- Tags: 330
- When: `defined(SubIFDs) && count(SubIFDs) references multiple children via one offset`
- Semantics: Child IFDs beyond the first are chained through the children's own NextIFD links; the last child's NextIFD is 0. Alternatively each child may be referenced directly by a separate SubIFDs value.
- Sources: PM6-DEP-001

### DEP-121 — SubIFDs ignored at unusual bit depths (PS warning)
- Kind: modifies-meaning · Versions: 6.0- · Conformance: PS
- Tags: 330, 258
- When: `defined(SubIFDs) && BitsPerSample != 8`
- Semantics: Readers should ignore the SubIFDs found in the file.
- Sources: PS-DEP-015
- Notes: The PS technote does not specify whose bit depth; libtiff should document its choice.

### DEP-122 — ClipPath requires XClipPathUnits
- Kind: requires · Versions: 6.0- · Conformance: PM6 · Severity: error
- Tags: 343, 344
- When: `defined(ClipPath)`
- Assert: `defined(XClipPathUnits)`
- Sources: PM6-DEP-002

### DEP-123 — YClipPathUnits defaults to XClipPathUnits
- Kind: selects-default · Versions: 6.0- · Conformance: PM6
- Tags: 344, 345
- When: `!defined(YClipPathUnits)`
- Semantics: Effective YClipPathUnits = XClipPathUnits.
- Sources: PM6-DEP-003

### DEP-124 — Indexed images require ColorMap and exclude photometric 3
- Kind: requires · Versions: 6.0- · Conformance: PM6 · Severity: error
- Tags: 346, 320, 262
- When: `Indexed == 1`
- Assert: `defined(ColorMap) && PhotometricInterpretation != 3`
- Sources: PM6-DEP-005, PM6-DEP-006, PM6-DEP-007
- Notes: PhotometricInterpretation 3 already means (RGB base + indexed); the combination would be circular.

### DEP-125 — OPI proxy requires ImageID
- Kind: requires · Versions: 6.0- · Conformance: PM6 · Severity: warning
- Tags: 351, 32781
- When: `OPIProxy == 1`
- Assert: `defined(ImageID)`
- Sources: PM6-DEP-011

### DEP-130 — SubfileType 1/2 required-field rule (4.0)
- Kind: requires · Versions: 4.0-4.0 · Conformance: baseline · Severity: error
- Tags: 255, 256, 257, 273
- When: `SubfileType in {1, 2}`
- Assert: `defined(ImageWidth) && defined(ImageLength) && defined(StripOffsets)`
- Sources: T4-DEP-001, T4-DEP-002

### DEP-131 — Multi-page bit points to PageNumber
- Kind: modifies-meaning · Versions: 5.0- · Conformance: baseline
- Tags: 254, 297
- When: `bit(NewSubfileType, 1) == 1`
- Semantics: The image is one page of a multi-page document; see PageNumber (297).
- Sources: T5-DEP-027

### DEP-140 — Metadata and pointer tags are IFD0-only
- Kind: constrains-value · Versions: 6.0- · Conformance: XMP · Severity: error
- Tags: 700, 33723, 34377, 34665, 34853
- When: `defined(XMP) || defined(IPTC) || defined(Photoshop) || defined(ExifIFDPointer) || defined(GPSInfoIFDPointer)`
- Assert: `each such tag appears only in the 0th (primary) IFD`
- Relaxation: flag `tolerate.metadata-outside-ifd0` downgrades to warning
- Sources: XMP-DEP-001
- Notes: XMP Part 3 states these tags are not valid in thumbnail or other IFDs. Exif itself permits 34665 in IFD1 (thumbnail Exif); the relax flag accepts such files while reporting them.

### DEP-141 — Exif IFD pointer well-formedness
- Kind: requires · Versions: 6.0- · Conformance: EXIF · Severity: error
- Tags: 34665
- When: `defined(ExifIFDPointer)`
- Assert: `type(ExifIFDPointer) == LONG && count(ExifIFDPointer) == 1 && the offset resolves to a structurally valid IFD containing no image data`
- Sources: EXIF-DEP-001
- Notes: BigTIFF containers may use type IFD8. Resident tags are registered in tags-exif.yaml (location exif-ifd).

### DEP-142 — GPS IFD pointer well-formedness and GPSVersionID
- Kind: requires · Versions: 6.0- · Conformance: EXIF · Severity: error
- Tags: 34853
- When: `defined(GPSInfoIFDPointer)`
- Assert: `the offset resolves to a structurally valid IFD with no image data, containing GPSVersionID (gps-ifd tag 0, value 2.3.0.0)`
- Relaxation: flag `tolerate.missing-gpsversionid` downgrades to warning
- Sources: EXIF-DEP-002, EXIF-DEP-021

### DEP-143 — Interoperability IFD pointer resides in the Exif IFD
- Kind: constrains-value · Versions: 6.0- · Conformance: EXIF · Severity: error
- Tags: 40965
- When: `defined(InteroperabilityIFDPointer)`
- Assert: `the tag is located in the Exif IFD (not IFD0) and points to a structurally valid IFD with no image data`
- Sources: EXIF-DEP-003
- Notes: Exif 2.3 additionally marks the Interoperability IFD as not-allowed for uncompressed (TIFF) primary images (EXIF-DEP-029/030).

### DEP-144 — ICC profile size consistency
- Kind: constrains-value · Versions: 6.0- · Conformance: ICC · Severity: error
- Tags: 34675
- When: `defined(ICCProfile)`
- Assert: `count(ICCProfile) == profile header size field (bytes 0-3, big-endian)`
- Sources: ICC-007, ICC-008

### DEP-145 — ICC profile signature and byte order
- Kind: constrains-value · Versions: 6.0- · Conformance: ICC · Severity: error
- Tags: 34675
- When: `defined(ICCProfile)`
- Assert: `profile bytes 36-39 == 'acsp' and all profile fields are big-endian regardless of TIFF byte order`
- Sources: ICC-004, ICC-013

### DEP-146 — Photoshop image resource block structure
- Kind: constrains-value · Versions: 6.0- · Conformance: PSFF · Severity: error
- Tags: 34377
- When: `defined(Photoshop)`
- Assert: `the value parses as a sequence of Image Resource Blocks: '8BIM' signature, 2-byte resource ID, even-padded Pascal-string name, 4-byte size, even-padded data, ending exactly at count(Photoshop) bytes`
- Sources: PSFF-001, PSFF-002, PSFF-003, PSFF-004, PSFF-005, PSFF-042

### DEP-147 — No XMP image resource inside the Photoshop tag
- Kind: forbids · Versions: 6.0- · Conformance: XMP · Severity: warning
- Tags: 34377, 700
- When: `defined(Photoshop)`
- Assert: `the resource block sequence contains no resource 1060 (XMP); XMP belongs in tag 700`
- Sources: XMP-DEP-003, PSFF-009
- Notes: Resource 1058 (nested Exif) may be present only in files written by Photoshop 6 (documented quirk); readers may recover Exif metadata from it when tag 34665 is absent.

### DEP-148 — XMP packet type, count and encoding
- Kind: constrains-value · Versions: 6.0- · Conformance: XMP · Severity: warning
- Tags: 700
- When: `defined(XMP)`
- Assert: `type(XMP) in {UNDEFINED, BYTE} && count(XMP) == byte length of the packet, which is UTF-8 serialized RDF/XML`
- Sources: XMP-DEP-002
- Notes: SHOULD-level in the source ("should be UNDEFINED or BYTE"), hence warning.

### DEP-149 — Duplicated metadata copies must stay synchronised
- Kind: modifies-meaning · Versions: 6.0- · Conformance: XMP
- Tags: 700, 33723, 34377, 34675
- When: `the same metadata exists in more than one carrier (33723 vs resource 0x0404 in 34377; 34675 vs resource 0x040F; XMP properties vs native TIFF/Exif tags)`
- Semantics: Writers must keep all copies identical. On conflict, native TIFF/Exif tag values take precedence over mirrored XMP properties (single documented exception: exif:ISOSpeedRating when the native tag saturates at 65535). No vendored document states a precedence between 33723/34675/700 and their Photoshop-resource copies inside 34377; validators should report divergence.
- Sources: IPTC-DEP-001, IPTC-DEP-002, XMP-DEP-006, PSFF-007, PSFF-008

### DEP-150 — ExifVersion expected in the Exif IFD
- Kind: requires · Versions: 6.0- · Conformance: EXIF · Severity: warning
- Tags: 34665
- When: `defined(ExifIFDPointer)`
- Assert: `ExifVersion (exif-ifd tag 36864) is present`
- Sources: EXIF-DEP-025
- Notes: Absence makes the file non-conformant to Exif, not malformed TIFF.

### DEP-151 — GPS coordinate values require their reference tags
- Kind: requires · Versions: 6.0- · Conformance: EXIF · Severity: warning
- Tags: 34853
- When: `GPSLatitude (gps-ifd 2) or GPSLongitude (gps-ifd 4) is present`
- Assert: `the matching GPSLatitudeRef (1) / GPSLongitudeRef (3) is present`
- Sources: EXIF-DEP-022

### DEP-152 — Sensitivity tag group co-requirements
- Kind: requires · Versions: 6.0- · Conformance: EXIF · Severity: warning
- Tags: 34665
- When: `StandardOutputSensitivity (34865), RecommendedExposureIndex (34866) or ISOSpeed (34867) is present in the Exif IFD`
- Assert: `PhotographicSensitivity (34855) and SensitivityType (34864) are also present; ISOSpeedLatitudeyyy (34868) additionally requires ISOSpeed (34867) and ISOSpeedLatitudezzz (34869)`
- Sources: EXIF-DEP-017, EXIF-DEP-018

### DEP-153 — JPEG-only Exif tags forbidden in uncompressed Exif TIFF
- Kind: forbids · Versions: 6.0- · Conformance: EXIF · Severity: warning
- Tags: 513, 514, 34665, 40965
- When: `Exif-compliant file with uncompressed (TIFF) primary image`
- Assert: `JPEGInterchangeFormat (513), JPEGInterchangeFormatLength (514), CompressedBitsPerPixel (37122) and the Interoperability IFD are not used for the primary image`
- Sources: EXIF-DEP-016, EXIF-DEP-029, EXIF-DEP-030

### DEP-160 — DNGVersion marks a DNG file and gates DNG rules
- Kind: modifies-meaning · Versions: 6.0- · Conformance: DNG
- Tags: 50706
- When: `defined(DNGVersion)`
- Semantics: The file is a DNG; IFD roles (raw/preview/enhanced/depth/semantic mask) are assigned via NewSubfileType and the SubIFDs tree, and the DEP-161..167 rules apply. SubIFD trees (SubIFDs 330) are used; SubIFD chains are not supported. DNGBackwardVersion (50707) states the oldest compatible reader version.
- Sources: DNG-003

### DEP-161 — CFA photometric requires the CFA pattern tags
- Kind: requires · Versions: 6.0- · Conformance: DNG · Severity: error
- Tags: 262, 33421, 33422
- When: `PhotometricInterpretation == 32803`
- Assert: `defined(CFARepeatPatternDim) && defined(CFAPattern)`
- Sources: DNG-DEP-002

### DEP-162 — BlackLevel count follows BlackLevelRepeatDim
- Kind: constrains-value · Versions: 6.0- · Conformance: DNG · Severity: error
- Tags: 50713, 50714, 277
- When: `defined(BlackLevel)`
- Assert: `count(BlackLevel) == BlackLevelRepeatDim[0] * BlackLevelRepeatDim[1] * SamplesPerPixel`
- Sources: DNG-DEP-014

### DEP-163 — Calibration illuminant/matrix chains are complete
- Kind: requires · Versions: 6.0- · Conformance: DNG · Severity: error
- Tags: 50778, 50779, 52529, 52531, 52533, 52534, 52535
- When: `defined(CalibrationIlluminant3)`
- Assert: `defined(CalibrationIlluminant1) && defined(CalibrationIlluminant2) && defined(ColorMatrix3); illuminant white points must be distinct. CalibrationIlluminantN == 255 requires IlluminantDataN`
- Sources: DNG-DEP-007, DNG-DEP-008, DNG-DEP-009, DNG-DEP-010

### DEP-164 — Floating-point raw data bit depths
- Kind: constrains-value · Versions: 6.0- · Conformance: DNG · Severity: error
- Tags: 339, 258
- When: `SampleFormat == 3`
- Assert: `BitsPerSample in {16, 24, 32}`
- Sources: DNG-DEP-022
- Notes: DNG 1.4+; earlier DNG versions always use unsigned integer samples.

### DEP-165 — Enhanced-image IFD photometric constraint
- Kind: requires · Versions: 6.0- · Conformance: DNG · Severity: error
- Tags: 254, 262, 51182
- When: `defined(DNGVersion) && NewSubfileType == 16`
- Assert: `PhotometricInterpretation == 34892`
- Sources: DNG-DEP-031

### DEP-166 — DNGBackwardVersion floor for 1.4 features
- Kind: constrains-value · Versions: 6.0- · Conformance: DNG · Severity: warning
- Tags: 50707, 339, 254, 259
- When: `SampleFormat == 3 || NewSubfileType == 4 || Compression in {8, 34892}`
- Assert: `DNGBackwardVersion >= 1.4.0.0`
- Sources: DNG-DEP-042

### DEP-167 — Uniform BitsPerSample across DNG samples
- Kind: constrains-value · Versions: 6.0- · Conformance: DNG · Severity: error
- Tags: 258, 277
- When: `defined(DNGVersion) && SamplesPerPixel != 1`
- Assert: `all BitsPerSample values are equal`
- Sources: DNG-DEP-021

### DEP-170 — Fax T.4 coding requires T4Options
- Kind: requires · Versions: 6.0- · Conformance: TFX · Severity: error
- Tags: 259, 292
- When: `fax file && Compression == 3`
- Assert: `defined(T4Options)`
- Sources: TFX-DEP-005
- Notes: Classic TIFF gives T4Options a default of 0; RFC 3949 requires the field to be written explicitly in fax profiles.

### DEP-171 — Fax T.6 coding requires T6Options == 0
- Kind: requires · Versions: 6.0- · Conformance: TFX · Severity: error
- Tags: 259, 293
- When: `fax file && Compression == 4`
- Assert: `defined(T6Options) && T6Options == 0`
- Sources: TFX-DEP-006
- Notes: Uncompressed mode (bit 1) is not allowed in fax use.

### DEP-172 — ITULAB requires Decode semantics
- Kind: requires · Versions: 6.0- · Conformance: TFX · Severity: error
- Tags: 262, 433, 277
- When: `PhotometricInterpretation == 10`
- Assert: `Decode is present with count == 2 * SamplesPerPixel, or the T.42 default ranges apply`
- Sources: TFX-DEP-011, TFX-118
- Notes: Decode gives (min, max) pairs mapping unsigned ITULAB samples to signed L*a*b*; defaults per ITU-T T.42 when absent (see sources/TFX.yaml for the default table).

### DEP-173 — StripRowCounts excludes RowsPerStrip
- Kind: forbids · Versions: 6.0- · Conformance: TFX · Severity: error
- Tags: 559, 278
- When: `defined(StripRowCounts)`
- Assert: `!defined(RowsPerStrip)`
- Sources: TFX-DEP-022

### DEP-174 — MRC IFDs carry NewSubfileType bit 4
- Kind: constrains-value · Versions: 6.0- · Conformance: TFX · Severity: error
- Tags: 254, 330, 286, 287, 34732
- When: `Profile M (MRC) file`
- Assert: `primary IFD has NewSubfileType 18 and child IFDs 16; child IFDs are reached via SubIFDs (330), carry ImageLayer (34732) and XPosition/YPosition; the primary IFD must not use XPosition/YPosition`
- Sources: TFX-DEP-017, TFX-DEP-018, TFX-DEP-019, TFX-DEP-030, TFX-146

### DEP-175 — GlobalParametersIFD placement and content
- Kind: constrains-value · Versions: 6.0- · Conformance: TFX · Severity: error
- Tags: 400, 401, 402, 403, 404, 405
- When: `defined(GlobalParametersIFD)`
- Assert: `the tag resides in the first page IFD and points to a structurally valid IFD holding file-global parameters (ProfileType, FaxProfile, CodingMethods, VersionYear, ModeNumber)`
- Sources: TFX-DEP-028, TFX-040
- Notes: Values in the GlobalParametersIFD describe the whole file; per-page IFD values prevail on conflict for their page.

### DEP-176 — Page-quality tags only from real fax hardware
- Kind: forbids · Versions: 6.0- · Conformance: TFX · Severity: info
- Tags: 326, 327, 328
- When: `the producing system has no page-quality information (not a fax receiver)`
- Assert: `!defined(BadFaxLines) && !defined(CleanFaxData) && !defined(ConsecutiveBadFaxLines)`
- Sources: TFX-DEP-029

### DEP-180 — LOGLUV photometric pairs with SGILOG compression
- Kind: constrains-value · Versions: 6.0- · Conformance: LLV · Severity: error
- Tags: 262, 259
- When: `PhotometricInterpretation == 32845`
- Assert: `Compression in {34676, 34677}`
- Sources: LLV-DEP-001
- Notes: 34676 carries the 32-bit encoding, 34677 the 24-bit packing.

### DEP-181 — LOGL photometric pairs with SGILOG compression
- Kind: constrains-value · Versions: 6.0- · Conformance: LLV · Severity: error
- Tags: 262, 259
- When: `PhotometricInterpretation == 32844`
- Assert: `Compression == 34676`
- Sources: LLV-DEP-002

### DEP-182 — StoNits calibrates absolute luminance
- Kind: modifies-meaning · Versions: 6.0- · Conformance: LLV
- Tags: 37439, 262
- When: `PhotometricInterpretation in {32844, 32845}`
- Semantics: When StoNits (37439) is present, decoded Y values multiplied by it yield absolute luminance in cd/m^2; absence means the data is uncalibrated (relative luminance).
- Sources: LLV-DEP-004, LLV-DEP-005

## Standalone vendor-deviation flags

| Flag | Concerns | Behavior |
|------|----------|----------|
| `tolerate.unsorted-ifd` | STR sort-order requirement | Accept IFDs whose entries are not sorted ascending by tag; sort in memory. |
| `tolerate.unaligned-values` | STR word-alignment requirement | Accept value offsets that are not 2-byte (classic) / 8-byte (BigTIFF) aligned. |
| `tolerate.missing-nul` | ASCII field termination | Accept ASCII values lacking the final NUL; treat count as the string length. |
| `tolerate.type-mismatch` | per-tag `types` in tags.yaml | Accept documented wild-type variants (ExtraSamples as BYTE, ReferenceBlackWhite as LONG, SubIFDs as LONG where IFD/IFD8 expected) and convert; both cases stem from spec inconsistencies noted in tags.yaml. |
| `tolerate.deflate-32946` | Compression enumerated values | Treat Compression 32946 as a synonym for 8 (Deflate). |
| `tolerate.iptc-as-long` | IPTC (33723) field type | Accept IPTC data stored as type LONG (count N/4, historical libtiff and NAA practice) and reinterpret the raw bytes as the IIM datastream; no vendored document defines the tag's type (see tags.yaml notes for 33723). |
| `repair.rowsperstrip-zero` | RowsPerStrip (278) | Treat RowsPerStrip 0 (invalid) as "entire image in one strip". |
| `repair.colormap-8bit` | ColorMap (320) value scale | When every ColorMap value is <= 255 in a 16-bit map, assume 8-bit vendor scaling and multiply values by 257. |
