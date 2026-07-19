# Specification registry

Every requirement in this folder is traceable to one or more of the source documents
listed here, via the `Sources:` field on each requirement. Documents are cited as
`<SPEC-ID> §<section>` (with a page number where the document has printed page numbers,
e.g. `TIFF6 §8 p.34`).

## Core revisions

The core TIFF revisions form a linear version history. Revision numbers are the axis
used by the `Versions:` range on every requirement (see [README.md](README.md)).

| Spec ID | Revision | Document                          | File                                | Date       | Status   |
|---------|----------|-----------------------------------|-------------------------------------|------------|----------|
| TIFF4   | 4.0      | TIFF Revision 4.0 (Aldus/Microsoft) | `published/TIFF4.txt`             | 1987-04-30 | Obsolete — read support only, writing not required |
| TIFF5   | 5.0      | TIFF Revision 5.0 (Aldus/Microsoft) | `published/TIFF5.txt` (also `published/TIFF Revision 5.0.html`) | 1988-08-08 | Obsolete — read support only, writing not required |
| TIFF6   | 6.0      | TIFF 6.0 Specification (Adobe)    | `published/TIFF6.pdf`               | 1992-06-03 | Current  |

TIFF6 is internally divided into **Part 1: Baseline TIFF** and **Part 2: TIFF
Extensions**; requirements record this in their `Conformance:` field
(`baseline` / `extension`).

## Supplements to TIFF 6.0

Supplements extend TIFF 6.0 without revising it. Requirements originating in a
supplement carry `Versions: 6.0–` together with `Conformance: <supplement-id>`.

| Spec ID | Document                                             | File                       | Date       | Status |
|---------|------------------------------------------------------|----------------------------|------------|--------|
| TN2     | TIFF Technical Note #2 (replacement JPEG scheme)     | `published/TechNote2.txt`  | 1995-03-17 | Current — deprecates TIFF6 §22 |
| PM6     | Adobe PageMaker 6.0 TIFF Technical Notes             | `published/TIFFPM6.pdf`    | 1995-09-14 | Current |
| PS      | Adobe Photoshop TIFF Technical Notes                 | `published/TIFFphotoshop.pdf` | 2002-03-22 | Current |
| TN3D1   | Adobe Photoshop TIFF Technical Note 3, draft 1       | `published/TIFFTN3d1.pdf`  | 2005       | Superseded by TN3D2 |
| TN3D2   | Adobe Photoshop TIFF Technical Note 3, draft 2       | `published/TIFFTN3d2.pdf`  | 2005-04-08 | Current |
| BIGTIFF | BigTIFF Design (64-bit container variant)            | `published/BigTIFF.txt`    | 2007 (libtiff text) | Current |

Notes:

- **TN2** replaces the TIFF 6.0 Section 22 JPEG scheme (Compression = 6, tags
  512–521) with Compression = 7 and JPEGTables (347). The Section 22 scheme is
  retained in the requirements as read-only legacy material.
- **TN3** exists in two circulated drafts. Draft 2 is normative here; where draft 1
  differs, the affected requirement notes the difference so files written against
  draft 1 remain identifiable.
- **BIGTIFF** is not a revision of the TIFF semantics but an alternative file
  container (version 43 header, 64-bit offsets). It inherits all TIFF 6.0 tag
  semantics; requirements record container applicability in their `Container:`
  field (`classic`, `bigtiff`, or `both`).
- The PageMaker technote (PM6) internally contains its own "Tech Note 1" (TIFF
  trees / SubIFDs) and "Tech Note 2" (clip paths); citations use the PM6 document
  section names to avoid confusion with the free-standing TIFF Technical Note #2
  (TN2, JPEG).

## Related standards building on TIFF 6.0

These documents define TIFF-based formats or TIFF-carried metadata. Their
requirements carry `Versions: 6.0–` with the spec ID in `Conformance:`; their
rules bind only files that opt in to the standard (via DNGVersion, FaxProfile,
Exif pointers, or presence of the carrier tag).

| Spec ID | Document                                                    | File                                | Date       | Status |
|---------|-------------------------------------------------------------|-------------------------------------|------------|--------|
| EXIF    | Exif 2.3 — CIPA DC-008-2010 / JEITA CP-3451                  | `published/CIPA-DC-008-2010_E.pdf`  | 2010       | Current edition vendored; libtiff also tracks 2.31/2.32 additions not in this edition |
| DNG     | Adobe Digital Negative (DNG) Specification 1.7.1.0           | `published/DNG_Spec_1_7_1_0.pdf`    | 2023       | Current — `supplement_version` records the 1.0–1.7.1 tag history |
| TFX     | RFC 3949, File Format for Internet Fax (TIFF/FX)             | `published/rfc3949.txt`             | 2005-02    | Current — obsoletes RFC 2301 (`published/rfc2301.txt`, reference only) |
| PSFF    | Adobe Photoshop File Formats Specification (TIFF sections)   | `published/Adobe Photoshop File Formats Specification.html` | 2023 (web) | Current |
| ICC     | ICC.1:2022-05 profile specification                          | `published/ICC.1-2022-05.pdf`       | 2022-05    | Current — embedding annex replaced by a pointer to ICC TN 10-2021 (not vendored) |
| IPTC    | IPTC Photo Metadata User Guide                               | `published/IPTC Photo Metadata User Guide.html` | 2023 (web) | Current — carries almost no TIFF-container-normative content (see sources/IPTC.yaml) |
| LLV     | G. Ward Larson, "LogLuv Encoding for Full-Gamut HDR Images" (JGT) | `published/jgtpap1.pdf`         | 1998       | Current — academic paper; numeric tag/compression codes are libtiff-registered, not printed in the paper |
| XMP     | Adobe XMP Specification Part 3, Storage in Files             | `published/XMPSpecificationPart3.pdf` | 2020-01  | Current (Parts 1 & 2 vendored for reference: `XMPSpecificationPart1.pdf` 2012, `XMPSpecificationPart2.pdf` 2022) |

Notes:

- **EXIF** tags resident in the Exif/GPS/Interoperability IFDs are registered in
  `tags-exif.yaml`; the pointer tags (34665, 34853, 40965) and placement rules
  are in `tags.yaml` / DEP-140..143.
- **DNG** tags are registered in `tags-dng.yaml` with the DNG version that
  introduced each; DNG-defined values for classic tags are merged into
  `tags.yaml`. DNG is the practical substitute for ISO 12234-2 (TIFF/EP), which
  is paywalled and not vendored.
- **TFX** tags are registered in `tags-fx.yaml`; the six fax profiles are the
  `CLS-FAX-*` entries in `constraints.yaml`.
- **ICC** 2022-05 no longer defines file embedding; the ICCProfile (34675) tag
  definition rests on the historical Annex B via PSFF and ecosystem practice.
  Acquiring ICC Technical Note 10-2021 would restore a first-party source.

## Referenced standards not vendored here

| Standard | Relationship |
|----------|--------------|
| ITU-T T.4 / T.6 (CCITT Group 3/4) | Encodings referenced by Compression values 2, 3, 4 |
| ISO/IEC 10918-1 (JPEG), ITU-T T.81 | Datastream format referenced by Compression 6 and 7 |
| RFC 1950/1951 (zlib/deflate) | Datastream format referenced by Compression 8 (and 32946) |
| IEEE 754 | Floating point formats referenced by SampleFormat 3 and TN3 |
| CCIR/ITU-R BT.601 | YCbCr coefficients and reference black/white defaults |
| ITU-T T.82 / T.85 (JBIG), T.43, T.42, T.44 (MRC), T.30 | Encodings and constraints referenced by TIFF/FX (Compression 9, 10; ITULAB; fax profiles) |
| ISO/IEC 18181-1 (JPEG XL) | Datastream format referenced by DNG Compression 52546 |
| ISO 12234-2 (TIFF/EP) | Raw-camera TIFF profile; paywalled, superseded in practice by DNG |
| ICC Technical Note 10-2021 | Current first-party definition of ICC profile embedding (ICCProfile 34675) |
| IPTC-NAA IIM v4 | The datastream carried by tag 33723 |
