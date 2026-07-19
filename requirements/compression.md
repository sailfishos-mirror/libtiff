# Compression scheme requirements (CMP-*)

IDs are `CMP-<Compression value>-NN`. Cross-tag preconditions (which photometrics,
bit depths, or tags a scheme requires) are DEP-* rules in
[constraints.yaml](constraints.yaml); this file holds the codec contracts.
Requirement format: see [README.md](README.md).

## CMP-1 — No compression (Compression = 1)

### CMP-1-01 — Packed row layout
- Level: MUST · Actor: both · Conformance: baseline
- Versions: 4.0– · Container: both · Status: current
- Sources: T6B-079, T5-026, T4-046

Data is packed as tightly as possible into the container type given by DEP-007
(BYTE, or SHORT/LONG when all samples are 16/32-bit), with no unused bits except
row padding: each row begins on a boundary of the container type.

### CMP-1-02 — Word-aligned variant (32771)
- Level: MUST · Actor: reader · Conformance: baseline
- Versions: 4.0–4.0 · Container: classic · Status: retired
- Sources: T4 (Compression field entry, sources/T4.yaml)

Compression 32771 is identical to 1 except each row begins on a 2-byte word
boundary. Retired after 4.0; readers should still accept it in old files.

## CMP-2 — CCITT Group 3 1-D Modified Huffman (Compression = 2)

### CMP-2-01 — Code structure
- Level: MUST · Actor: both · Conformance: baseline
- Versions: 4.0– · Container: both · Status: current
- Sources: T6B-115, T6B-116, T6B-117; T5-091..T5-095; T4-081

Each row is coded independently as alternating white/black run lengths using the
CCITT T.4 terminating and make-up codes, beginning with a white run (length 0 if
the row starts black). Run lengths ≥ 64 use one or more make-up codes plus a
terminating code; runs up to 2560 use the extended make-up codes, and the
2624-pixel limit applies per T.4.

### CMP-2-02 — Row byte alignment, no EOL
- Level: MUST · Actor: both · Conformance: baseline
- Versions: 4.0– · Container: both · Status: current
- Sources: T6B-118, T6B-119; T5-096..T5-099

Each coded row begins on a byte boundary (pad with zero bits); no EOL codes,
fill bits, or RTC sequences are used. Decoded run lengths must sum to exactly
ImageWidth per row (DEP-041); any mismatch is an unrecoverable error.

### CMP-2-03 — Photometric reversal
- Level: MUST · Actor: reader · Conformance: baseline
- Versions: 5.0– · Container: both · Status: current
- Sources: T6B-120

With PhotometricInterpretation = 1, white and black runs are exchanged on
display (see DEP-033; in 4.0-era files see DEP-032 instead).

## CMP-3 — CCITT T.4 / Group 3 fax (Compression = 3)

### CMP-3-01 — T.4 conformance
- Level: MUST · Actor: both · Conformance: extension
- Versions: 4.0– · Container: both · Status: current
- Sources: T6X-010..T6X-017; T5-029, T5-081..T5-085

Data is encoded per CCITT Recommendation T.4, as selected by T4Options (292):
bit 0 chooses 1-D or 2-D coding, bit 1 uncompressed mode, bit 2 EOL byte
alignment (fill bits before EOL). Each strip/tile is an independent datastream
beginning on a byte boundary.

### CMP-3-02 — 2-D coding strip discipline
- Level: MUST · Actor: writer · Conformance: extension
- Versions: 6.0– · Container: both · Status: current
- Sources: T6X-013 (DEP-042)

With 2-D coding, each strip begins with a 1-D coded line, and RowsPerStrip
should be a multiple of the K parameter to keep strips independently decodable.

## CMP-4 — CCITT T.6 / Group 4 fax (Compression = 4)

### CMP-4-01 — T.6 conformance
- Level: MUST · Actor: both · Conformance: extension
- Versions: 4.0– · Container: both · Status: current
- Sources: T6X-018..T6X-029; T5-030

Data is encoded per CCITT Recommendation T.6 (2-D coding throughout), governed
solely by T6Options (293). Each strip/tile is an independent datastream ending
with EOFB; the line width is exactly ImageWidth (TileWidth if tiled, DEP-044).

### CMP-4-02 — Uncompressed-mode declaration
- Level: MUST · Actor: writer · Conformance: extension
- Versions: 6.0– · Container: both · Status: current
- Sources: T6X-026 (DEP-043)

A writer that cannot guarantee the absence of uncompressed-mode segments must
set T6Options bit 1; readers may refuse files with bit 1 set if they do not
implement uncompressed mode.

## CMP-5 — LZW (Compression = 5)

### CMP-5-01 — Algorithm contract
- Level: MUST · Actor: both · Conformance: extension
- Versions: 5.0– · Container: both · Status: current
- Sources: T6X-038..T6X-046; T5-081(App F), T5-086..T5-089

LZW with variable code width 9–12 bits, MSB-first packing, initial dictionary of
256 literals plus ClearCode (256) and EndOfInformation (257); the code width
increases at dictionary sizes 511/1023/2047 (early change, "off by one" per the
6.0 text as implemented in practice); the dictionary resets on ClearCode, and the
writer must emit ClearCode whenever the dictionary is full.

### CMP-5-02 — Strip independence
- Level: MUST · Actor: both · Conformance: extension
- Versions: 5.0– · Container: both · Status: current
- Sources: T6X-041 (DEP-045)

Each strip/tile is compressed independently, begins with ClearCode, ends with
EndOfInformation, and is bit-packed MSB-first regardless of FillOrder.

### CMP-5-03 — Predictor interaction
- Level: MUST · Actor: both · Conformance: extension
- Versions: 5.0– · Container: both · Status: current
- Sources: T5-102 (DEP-046), DEP-047, DEP-048

Readers must consult Predictor (317) before interpreting decompressed LZW data;
unknown predictor values are fatal for the image.

### CMP-5-04 — Patent note
- Level: INFO · Actor: both · Conformance: extension
- Versions: 6.0–6.0 · Container: both · Status: retired
- Sources: T6X-037

The 6.0 document carries an LZW licensing notice (Unisys). The patents expired
in 2003–2004; the note is historical only.

## CMP-6 — Old-style JPEG, TIFF 6.0 §22 (Compression = 6)

Deprecated by TN2 (DEP-055): read-only legacy. Field rules for tags 512–521 are
DEP-050..DEP-054; see also tags.yaml.

### CMP-6-01 — Scheme outline
- Level: INFO · Actor: reader · Conformance: extension
- Versions: 6.0– · Container: both · Status: deprecated
- Sources: T6X-102..T6X-119

Image data is JPEG-compressed per JPEGProc (1 = baseline DCT, 14 = lossless
Huffman), with tables stored in the tag set 519–521 or a complete interchange
stream located by JPEGInterchangeFormat/Length (513/514). Strips/tiles align to
restart intervals when both are used (DEP-053).

### CMP-6-02 — Known defects and reader guidance
- Level: INFO · Actor: reader · Conformance: TN2
- Versions: 6.0– · Container: both · Status: deprecated
- Sources: TN2-001..TN2-030 (design-flaw discussion)

TN2 documents the §22 design as internally inconsistent and incompletely
specified (component-to-tag mapping, subsampling interaction, restart
semantics); vendor files vary widely. Readers should implement the pragmatic
recovery in DEP-050's repair action rather than strict §22 conformance.

## CMP-7 — JPEG per TechNote 2 (Compression = 7)

Cross-tag rules: DEP-060..DEP-070.

### CMP-7-01 — Independent interchange datastreams
- Level: MUST · Actor: both · Conformance: TN2
- Versions: 6.0– · Container: both · Status: current
- Sources: TN2-031..TN2-050

Each strip/tile contains a complete ISO/IEC 10918-1 datastream (SOI…EOI),
independently decodable, optionally abbreviated (tables from JPEGTables 347).
Any process the ISO standard allows may be used (baseline, extended sequential,
progressive, lossless), subject to SOFn/BitsPerSample agreement (DEP-063).

### CMP-7-02 — Marker restrictions
- Level: MUST · Actor: writer · Conformance: TN2
- Versions: 6.0– · Container: both · Status: current
- Sources: TN2-051..TN2-058

Segments must not contain markers that contradict the TIFF field description of
the image (dimensions, components); DNL markers are not used (dimensions come
from SOFn); restart markers are permitted but not required; APPn/COM markers
should be ignored by readers.

### CMP-7-03 — Table management
- Level: MUST · Actor: both · Conformance: TN2
- Versions: 6.0– · Container: both · Status: current
- Sources: TN2-045, TN2-046, TN2-073 (DEP-067)

With JPEGTables present, readers load its tables before any segment; segments
may omit but must not redefine those tables, and must not reference undefined
tables. Without JPEGTables, every segment is fully self-contained. No table
state carries over between segments.

### CMP-7-04 — Photoshop usage profile
- Level: INFO · Actor: both · Conformance: PS
- Versions: 6.0– · Container: both · Status: current
- Sources: PS-018..PS-086

The PS technote restates the TN2 rules as Photoshop writes them (always
JPEGTables, YCbCr or grayscale or RGB/CMYK without subsampling) and is the
de-facto interoperability profile for Compression 7.

## CMP-8 — Deflate (Compression = 8)

### CMP-8-01 — zlib datastream
- Level: MUST · Actor: both · Conformance: PS
- Versions: 6.0– · Container: both · Status: current
- Sources: PS-002..PS-017

Each strip/tile is an independent zlib-format (RFC 1950) stream containing
deflate (RFC 1951) data, applied to the same byte layout as Compression 1.
Applicable to any bit depth and photometric; Predictor 2/3 may be applied first
(DEP-047, DEP-048).

### CMP-8-02 — Legacy code 32946
- Level: INFO · Actor: reader · Conformance: PS
- Versions: 6.0– · Container: both · Status: current
- Sources: deviation flag `tolerate.deflate-32946`

Compression 32946 is a pre-standard synonym for 8 used by early implementations
(including libtiff); readers should accept it, writers must emit 8.

## CMP-9 — JBIG, T.85 profile (Compression = 9)

### CMP-9-01 — T.85 datastream
- Level: MUST · Actor: both · Conformance: TFX
- Versions: 6.0– · Container: both · Status: current
- Sources: TFX-101, TFX-102, TFX-104
- Tags: 259, 435

Bilevel image data coded with ITU-T T.82 JBIG in the single-progression
sequential mode constrained by the ITU-T T.85 fax application profile
(fax Profile J). T82Options (435) declares the JBIG profile in use; the
all-bits-zero value means T.85 and may then be omitted. Strips follow the
TN2 discipline: each strip is an independently decodable datastream.

## CMP-10 — T.43 color via JBIG (Compression = 10)

### CMP-10-01 — T.43 datastream
- Level: MUST · Actor: both · Conformance: TFX
- Versions: 6.0– · Container: both · Status: current
- Sources: TFX-120, TFX-121, TFX-122, TFX-125
- Tags: 259, 262, 346

Color/grayscale data coded per ITU-T T.43 (which internally uses T.82 JBIG
plane coding) for fax Profile L. The color table for palette images is the one
embedded in the T.43 datastream — not the TIFF ColorMap (320); the
PhotometricInterpretation / SamplesPerPixel / BitsPerSample / Indexed (346)
combination must match the T.43 image type (see CLS-FAX-L and DEP-172).

## CMP-32773 — PackBits

### CMP-32773-01 — Algorithm contract
- Level: MUST · Actor: both · Conformance: baseline
- Versions: 4.0– · Container: both · Status: current
- Sources: T6B-111..T6B-114; T5 App C; T4-085..T4-089

Byte-oriented run-length coding: control byte n in [0,127] means copy n+1
literal bytes; n in [-127,-1] (two's complement) means repeat the next byte
1−n times; −128 is a no-op. Each row is coded separately (encoding state and
runs must not cross row boundaries); the decoded output is interpreted exactly
as Compression 1 (DEP-049).

### CMP-32773-02 — Encoding recommendations
- Level: SHOULD · Actor: writer · Conformance: baseline
- Versions: 5.0– · Container: both · Status: current
- Sources: T6B-113

Prefer the representation that decodes correctly under the "runs may not cross
row boundaries" rule; a two-byte repeated run is better coded as a replicate
run except when it interrupts a literal run.

## CMP-34676 — SGILOG (Compression = 34676)

### CMP-34676-01 — Adaptive run-length scheme
- Level: MUST · Actor: both · Conformance: LLV
- Versions: 6.0– · Container: both · Status: current
- Sources: LLV-008, LLV-017, LLV-018, LLV-019
- Tags: 259, 262

Adaptive run-length encoding for 32-bit LogLuv and 16-bit LogL pixel data
(PhotometricInterpretation 32845/32844). Each scanline's pixel bytes are
separated into four byte streams by byte position (two for 16-bit LogL) and
each stream is run-length coded; the scheme never expands data beyond its
uncompressed size. The exact bitstream op-codes are defined by the
implementation (libtiff `tif_luv.c`); the paper describes the strategy only —
see sources/LLV.yaml notes.

### CMP-34676-02 — Codec I/O contract
- Level: INFO · Actor: both · Conformance: LLV
- Versions: 6.0– · Container: both · Status: current
- Sources: LLV-009, LLV-010, LLV-011

The reference codec encodes from and decodes to floating-point CIE XYZ
scanlines (optionally raw encoded values or tone-mapped RGB); StoNits (37439)
scales decoded luminance to absolute cd/m² (DEP-182).

## CMP-34677 — SGILOG24 (Compression = 34677)

### CMP-34677-01 — 24-bit LogLuv packing
- Level: MUST · Actor: both · Conformance: LLV
- Versions: 6.0– · Container: both · Status: current
- Sources: LLV-001, LLV-DEP-001
- Tags: 259, 262

Carries the 24-bit LogLuv encoding (10-bit log luminance + 14-bit CIE (u',v')
lookup index) for PhotometricInterpretation 32845. The paper does not define a
separate run-length scheme for this packing (the 24-bit form is already
near-incompressible); see sources/LLV.yaml.

## CMP-34892 — Lossy JPEG for DNG (Compression = 34892)

### CMP-34892-01 — Baseline DCT for linear raw
- Level: MUST · Actor: both · Conformance: DNG
- Versions: 6.0– · Container: both · Status: current
- Sources: DNG-022, DNG-029
- Tags: 259, 262

Baseline ISO/IEC 10918-1 DCT JPEG applied to 8-bit data in DNG files
(DNG 1.4+); permitted for PhotometricInterpretation 34892 (LinearRaw) and
52527 (PhotometricMask) IFDs. Distinct code from 7 because the classic
value implies lossless-capable interchange in DNG's usage. Requires
DNGBackwardVersion ≥ 1.4.0.0 (DEP-166).

## CMP-52546 — JPEG XL (Compression = 52546)

### CMP-52546-01 — JPEG XL datastream
- Level: MUST · Actor: both · Conformance: DNG
- Versions: 6.0– · Container: both · Status: current
- Sources: DNG-030, DNG-031
- Tags: 259

ISO/IEC 18181-1:2022 JPEG XL codestream, introduced by DNG 1.7 for integer
image data (8–16 bit). Both bare codestreams and ISO BMFF container form are
permitted; with multiple tiles the bare form is used. JXL-specific parameters
live in the jxl-ifd tags (52549–52551, see tags-dng.yaml).
