# Per-tag behavioral requirements (TAG-*)

IDs are `TAG-<code>-NN`. This file holds rules about a single tag's semantics
that a reader/writer must implement. Three requirement families are *implicit*
for every tag and need no entry here (cite them directly, they are defined in
the [tags.yaml](tags.yaml) header):

- `TAG-<code>-TYPE` — the stored field type must be in the registry `types`
  (plus `bigtiff_types` in a BigTIFF container), subject to GEN-004 integer
  flexibility and the `tolerate.type-mismatch` deviations.
- `TAG-<code>-COUNT` — the stored count must match the registry `count`.
- `TAG-<code>-VALUE` — enumerated values must be registry values valid for the
  file's version/conformance level.

Cross-tag rules are DEP-* ([constraints.yaml](constraints.yaml)); codec
contracts are CMP-* ([compression.md](compression.md)). Requirement format:
[README.md](README.md).

---

### TAG-254-01 — NewSubfileType is a bit mask
- MUST · file · baseline · Versions: 5.0– · both · current · Sources: T5-040, T6B-093

Bits 0 (reduced resolution), 1 (multi-page page, DEP-131), 2 (transparency
mask, DEP-024) are independent flags; undefined bits must be written 0 and
ignored on read.

### TAG-255-01 — SubfileType is superseded
- SHOULD-NOT · writer · baseline · Versions: 5.0– · both · deprecated · Sources: T5 ("No Longer Recommended"), T6B-108

Writers use NewSubfileType (254); readers map SubfileType 1/2/3 onto the
corresponding NewSubfileType bits when only 255 is present.

### TAG-256-01 — LONG required beyond 64K columns/rows
- MUST · writer · baseline · Versions: 5.0– · both · current · Sources: T6B-033, T6B-DEP-002

ImageWidth (256) and ImageLength (257) must use LONG when the value exceeds
65535. (In 4.0 the formal type was SHORT-only; see tags.yaml type_history.)

### TAG-258-01 — All BitsPerSample values written explicitly
- MUST · writer · baseline · Versions: 6.0– · both · current · Sources: T6B-076 (DEP-010)

The writer emits SamplesPerPixel values even when identical. Readers apply the
`repair.bitspersample-count` deviation for short counts.

### TAG-259-01 — Baseline reader compression support
- MUST · reader · baseline · Versions: 6.0– · both · current · Sources: T6B-039

A baseline reader must decode Compression 1, 2 and 32773. Every other value is
an extension the reader may refuse (GEN-005).

### TAG-262-01 — Photometric is authoritative and required
- MUST · both · baseline · Versions: 5.0– · both · current · Sources: T5-018, T6B-095

PhotometricInterpretation has no default and must be written for every image.
Readers must not infer it from other fields except as a repair action
(4.0-era CCITT files: DEP-032).

### TAG-266-01 — FillOrder support level
- MAY · reader · baseline · Versions: 6.0– · both · current · Sources: T6B-078, T6X-006..T6X-009

Baseline readers need only support FillOrder 1; FillOrder 2 is for transient
facsimile data. FillOrder governs bit order within bytes of uncompressed and
CCITT bilevel data only; LZW/JPEG/Deflate streams are byte-oriented (CMP-5-02).

### TAG-273-01 — Offsets reference real strip data
- MUST · writer · baseline · Versions: 4.0– · both · current · Sources: T4-038, T6B-065, T6B-066

Every StripOffsets value is a byte offset (from file start) to the first byte
of that strip's (possibly compressed) data; strips are self-contained for all
baseline and extension compressions (CMP-*-independence rules).

### TAG-274-01 — Orientation support level
- MAY · reader · baseline · Versions: 6.0– · both · current · Sources: T6B-094

Baseline readers need only implement Orientation 1; other values may be
treated as 1 with a warning (do not mis-rotate silently in validation mode).

### TAG-278-01 — Strip size guidance
- SHOULD · writer · baseline · Versions: 5.0– · both · current · Sources: T5-052, T6B-103

Choose RowsPerStrip so each strip is roughly 8KB (uncompressed), enabling
random access; readers must nevertheless accept any value from 1 to 2³²−1,
including values exceeding ImageLength (single-strip images).

### TAG-280-01 / TAG-281-01 — Min/MaxSampleValue are statistical
- MUST-NOT · reader · baseline · Versions: 5.0– · both · current · Sources: T5-072, T6B-091, T6B-092

These fields must not affect the visual interpretation of the data (5.0
onward). In 4.0-era files they participate in photometric scaling (DEP-013).

### TAG-282-01 — Resolution semantics
- MUST · both · baseline · Versions: 4.0– · both · current · Sources: T4-DEP-024, T6B-101, T6B-110

XResolution/YResolution are pixels per ResolutionUnit; with ResolutionUnit = 1
they specify only the aspect ratio. Writers of images with no meaningful
absolute resolution should use unit 1 rather than fabricating a density.

### TAG-284-01 — Planar support level
- MAY · reader · baseline · Versions: 6.0– · both · current · Sources: T6B-099

PlanarConfiguration 2 is not required of baseline readers. If unsupported, the
reader must refuse the image, not interleave incorrectly.

### TAG-290-01 — Gray response semantics
- MUST · both · baseline · Versions: 4.0– · both · current · Sources: T4-DEP-025, T6B (290/291 entries)

GrayResponseCurve values are optical densities scaled by GrayResponseUnit
(default hundredths); value 0 of the curve corresponds to pixel value 0.
The 0th curve entry maps the darkest/lightest end per PhotometricInterpretation.

### TAG-297-01 — Page numbering convention
- MUST · file · extension · Versions: 6.0– · both · current · Sources: T6X (297 entry)

PageNumber[0] is 0-based; PageNumber[1] is the total page count or 0 when
unknown. Pages may appear in any IFD order.

### TAG-306-01 — DateTime format
- MUST · writer · baseline · Versions: 5.0– · both · current · Sources: T5 (306 entry), T6B (306 entry)

Exactly "YYYY:MM:DD HH:MM:SS" (24-hour, single space), 20 bytes with NUL.
Validators should accept and flag common deviations (wrong separators, missing
seconds) rather than fail the file (flag `tolerate.datetime-format`).

### TAG-317-01 — Horizontal differencing definition
- MUST · both · extension · Versions: 5.0– · both · current · Sources: T6X-047..049; T5-126..127

Predictor 2: each sample of each row (after the first pixel) stores the
difference from the same channel of the previous pixel; differencing is per
row (no carry across rows) and per channel (offset SamplesPerPixel for chunky
data). Applied before compression, reversed after decompression.

### TAG-317-02 — Floating point predictor definition
- MUST · both · TN3 · Versions: 6.0– · both · current · Sources: TN3-010..015

Predictor 3: per row, sample bytes are split into byte-significance planes
ordered most-significant first (independent of file byte order), then the
plane buffer is differenced byte-wise horizontally. Reversal order on read:
un-difference, then reassemble bytes. Row-reset behavior follows the reference
code in TN3 (flagged there as inferred, TN3-015).

### TAG-318-01 — Colorimetry usage
- SHOULD · writer · extension · Versions: 5.0– · both · current · Sources: T5 App H; T6X-083..T6X-087

WhitePoint and PrimaryChromaticities are CIE 1931 xy chromaticities; both are
needed for a colorimetric image (DEP-031). The 5.0 defaults (D65/SMPTE) were
dropped in 6.0 — treat 5.0-era files without these fields as D65/SMPTE, 6.0
files as uncalibrated. Beware the Appendix J tag-number collision
(tags.yaml `draft_proposals`).

### TAG-320-01 — ColorMap value scale and order
- MUST · file · baseline · Versions: 5.0– · both · current · Sources: T5-022/023, T6B-048/049

All red values, then all green, then all blue; 0 = minimum intensity, 65535 =
maximum. Black is (0,0,0), white (65535,65535,65535). 8-bit-scaled maps are a
known deviation (`repair.colormap-8bit`).

### TAG-321-01 — Halftone hints semantics
- SHOULD · both · extension · Versions: 6.0– · both · current · Sources: T6X-069..T6X-073 (§17)

HalftoneHints[0] is the highlight gray level to print at the lightest
reproducible tint, HalftoneHints[1] the shadow level at the darkest; applies
to continuous-tone data intended for halftone reproduction.

### TAG-322-01 — Tile geometry and padding
- MUST · both · extension · Versions: 6.0– · both · current · Sources: T6X-050..T6X-060

Tiles are TileWidth × TileLength pixels; TilesAcross = ceil(ImageWidth /
TileWidth), TilesDown = ceil(ImageLength / TileLength). Edge tiles are padded
to full tile size before compression; readers clip padding. Tiles are stored
left-to-right, top-to-bottom (planes consecutive when planar).

### TAG-330-01 — TIFF tree semantics
- MUST · both · PM6 · Versions: 6.0– · both · current · Sources: PM6-001..PM6-007; PS-001

SubIFDs values are offsets to child IFDs (type IFD or LONG; IFD8 in BigTIFF).
Children hold auxiliary images of the parent (previews, alternate resolutions,
masks); NewSubfileType in the child describes its role. Children of one parent
chain through NextIFD (DEP-120); child IFDs must not appear in the main
top-level IFD chain.

### TAG-338-01 — Alpha interpretation
- MUST · both · baseline/extension · Versions: 6.0– · both · current · Sources: T6B-084/085, T6X-074..T6X-078

ExtraSamples value 1 (associated): color is premultiplied; compositing uses
the stored values directly; value 2 (unassociated): color is not premultiplied.
Extra samples occupy the trailing components of each pixel. See DEP-090..092.

### TAG-339-01 — SampleFormat does not size samples
- MUST · both · extension · Versions: 6.0– · both · current · Sources: T6X (339 entry)

SampleFormat describes interpretation only; BitsPerSample always gives the
width. Format 4 (undefined) data must be passed through without numeric
interpretation.

### TAG-343-01 — ClipPath encoding
- MUST · both · PM6 · Versions: 6.0– · both · current · Sources: PM6-008..PM6-039

The ClipPath byte stream is: fixed header (byte-order marker, version,
reserved words), then commands, each an operator byte (see tags.yaml values)
with a data-type byte and operands; coordinates are normalized by
XClipPathUnits/YClipPathUnits into [0,1] across the image width/height
(values outside [0,1] are legal and lie outside the image). Operand integer
width (SBYTE/SSHORT/SLONG) must be large enough for the units values
(PM6-DEP-004).

### TAG-346-01 — Indexed generalizes palettes
- MUST · both · PM6 · Versions: 6.0– · both · current · Sources: PM6-040..PM6-045

Indexed = 1 means pixel values index into ColorMap for the base color space
given by PhotometricInterpretation. PhotometricInterpretation 3 ≡ RGB base +
Indexed 1 (DEP-124); the extended ColorMap width rule is DEP-022.

### TAG-529-01 — YCbCr transform equations
- MUST · both · extension · Versions: 6.0– · both · current · Sources: T6X-093..T6X-101

Y = R·LumaRed + G·LumaGreen + B·LumaBlue; Cb = (B − Y) / (2 − 2·LumaBlue);
Cr = (R − Y) / (2 − 2·LumaRed), followed by ReferenceBlackWhite (532)
headroom/footroom coding. Defaults are CCIR 601-1 coefficients; positioning
per YCbCrPositioning (531).

### TAG-532-01 — ReferenceBlackWhite coding
- MUST · both · extension · Versions: 6.0– · both · current · Sources: T6X-088..T6X-092

Coded = (full-range value) × (white − black) / range + black, per component
pair (black, white); decoding is the inverse, clamping to the sample range.
The RGB default (0, 2^bps −1 per component) is a no-op; YCbCr requires
explicit values (DEP-074).

### TAG-32781-01 — ImageID naming
- SHOULD · writer · PM6 · Versions: 6.0– · both · current · Sources: PM6-055..PM6-057

ImageID carries the OPI identifier (conventionally a full pathname) of the
high-resolution original; it must uniquely identify that image and is
meaningful primarily when OPIProxy = 1 (DEP-125).

### TAG-37724-01 — ImageSourceData structure
- MAY · both · PS · Versions: 6.0– · both · current · Sources: PS-087..PS-090

Begins with the NUL-terminated signature "Adobe Photoshop Document Data
Block", followed by Photoshop resource records (layer/mask data as in the PSD
format). Opaque to TIFF processing; editors must drop or regenerate it when
pixel data changes (GEN-009).

### TAG-700-01 — XMP packet content
- MUST · file · XMP · Versions: 6.0– · both · current · Sources: XMP-DEP-002, XMP-007

The value is a self-contained, UTF-8 encoded, serialized RDF/XML XMP packet;
count equals the packet byte length. IFD0-only placement per DEP-140; type
and reconciliation rules per DEP-148/DEP-149.

### TAG-33723-01 — IPTC datastream content
- MUST · file · XMP · Versions: 6.0– · both · current · Sources: XMP-025, IPTC-003, PSFF-007

The value is an IPTC-IIM datastream: a sequence of DataSets, each introduced
by the 0x1C record marker with record:dataset numbering. No vendored document
defines the TIFF field type; accept LONG-typed variants via
`tolerate.iptc-as-long`. IFD0-only placement per DEP-140; synchronization
with XMP and Photoshop resource 0x0404 per DEP-149.

### TAG-34377-01 — Photoshop image resources structure
- MUST · file · PSFF · Versions: 6.0– · both · current · Sources: PSFF-001..PSFF-005, PSFF-042

A sequence of Image Resource Blocks ('8BIM', resource ID, even-padded Pascal
name, 4-byte size, even-padded data), big-endian throughout regardless of the
TIFF byte order. Structure check DEP-146; resource 1060 prohibition DEP-147.

### TAG-34665-01 — Exif IFD pointer semantics
- MUST · both · EXIF · Versions: 6.0– · both · current · Sources: EXIF-025, EXIF-DEP-001, XMP-011

Points to the Exif IFD (tags registered in tags-exif.yaml). The link is
implicit — type LONG carries no IFD marking in classic TIFF — so editors
rewriting the file must relocate the target IFD and update the pointer
together (whole-file rewrite or append-only update, XMP-DEP-010).
Well-formedness per DEP-141.

### TAG-34675-01 — ICC profile content
- MUST · file · ICC · Versions: 6.0– · both · current · Sources: ICC-004, ICC-007, ICC-008, ICC-013

The value is a complete ICC profile: 128-byte header + tag table + tagged
element data, big-endian regardless of TIFF byte order. Size and signature
consistency per DEP-144/DEP-145. One profile per IFD; the profile describes
the color space of that IFD's image data.

### TAG-34853-01 — GPS IFD pointer semantics
- MUST · both · EXIF · Versions: 6.0– · both · current · Sources: EXIF-026, EXIF-DEP-002

Points to the GPS Info IFD (tags registered in tags-exif.yaml with location
gps-ifd). GPSVersionID (gps-ifd tag 0) is mandatory in the pointed-to IFD.
Same implicit-link editing rules as TAG-34665-01. Well-formedness per
DEP-142.

### TAG-37439-01 — StoNits calibration semantics
- MAY · both · LLV · Versions: 6.0– · both · current · Sources: LLV-014, LLV-016

Present only when the writer knows the absolute calibration of the source
data: decoded Y × StoNits = luminance in cd/m². Readers must not assume
calibration when the tag is absent (DEP-182).
