# Gap analysis: libtiff features vs. requirements coverage

Comparison of what libtiff implements against what the requirements database
(and the documents in `published/`) covers. Baseline: libtiff **4.7.2**
(d6217f35, 2026-07-19); scanned `libtiff/tif_dirinfo.c` (tag tables
`tiffFields`, `exifFields`, `gpsFields`), `libtiff/tif_codec.c` (built-in
codecs), the codec-private field arrays (`tif_fax3.c`, `tif_jpeg.c`,
`tif_ojpeg.c`, `tif_predict.c`, `tif_luv.c`, …) and `libtiff/tiff.h`.
Regenerate the data with `tools/gapscan.py <libtiff-path>`.

**Second-wave update (2026-07-19):** the EXIF, DNG, TFX, PSFF, ICC, IPTC, LLV
and XMP documents were vendored and extracted (`sources/*.yaml`), closing the
largest gaps below. Coverage after the merge:

| Population | Count | Covered by requirements | Gap |
|---|---:|---:|---:|
| libtiff main tag table (`tiffFields`) | 248 file tags | 194 | 54 |
| libtiff EXIF IFD table (`exifFields`) | 81 | 69 | 12 (Exif 2.31/2.32 additions) |
| libtiff GPS IFD table (`gpsFields`) | 32 | 32 | 0 |
| Built-in codecs (`tif_codec.c`) | 21 registrations / 19 schemes | 13 schemes | 6 |

Registries: `tags.yaml` (92 classic tags), `tags-exif.yaml` (103),
`tags-dng.yaml` (118), `tags-fx.yaml` (14). Every remaining gap comes from a
specification that is still not in `published/` (sections 1 and 4), plus the
reverse gaps in section 3.

Pseudo-tags (codes ≥ 65535: FaxMode, JPEGQuality, ZipQuality, the DCS 655xx
block, PerSample 65563, codec tuning tags) are libtiff API artifacts, never
written to files, and are out of scope for the requirements database.

## 1. Remaining tag gaps by originating specification

### CLOSED in the second wave

- **TIFF/FX** (RFC 3949 → `TFX`): tags 400–405, 433–435, 559, 34732, 326–328;
  Compression 9/10; ITULAB photometric 10; fax profiles `CLS-FAX-*`.
- **Exif/GPS** (CIPA DC-008-2010 → `EXIF`): pointer tags 34665/34853/40965 and
  the Exif/GPS/Interop IFD registries (`tags-exif.yaml`).
- **DNG** (1.7.1 → `DNG`): the 50706–52555 blocks (`tags-dng.yaml`), new
  photometrics 32803/34892/51177/52527, Compression 34892/52546, Predictor
  34892–34895.
- **LogLuv** (`LLV`): photometrics 32844/32845, Compression 34676/34677,
  StoNits 37439.
- **Metadata carriers** (`PSFF`, `ICC`, `IPTC`, `XMP`): tags 700, 33723, 34377,
  34675, 37724 (PSB variant), 50255.

### TIFFEP — TIFF/EP (ISO 12234-2) — still open

Tags: the `TIFFTAG_EP_*` block — CFARepeatPatternDim (33421), CFAPattern
(33422), BatteryLevel (33423), ExposureTime (33434), FNumber (33437),
ExposureProgram (34850), SpectralSensitivity (34852), ISOSpeedRatings (34855),
OECF (34856), Interlace (34857), TimeZoneOffset (34858), SelfTimerMode
(34859), DateTimeOriginal (36867), CompressedBitsPerPixel (37122), and
37377–37399 (ShutterSpeed…SensingMethod): **37 of the 54 remaining main-table
gaps**. These are IFD0-resident twins of Exif-IFD tags (same codes for
33421/33422 which DNG covers in the raw IFD; the rest shadow Exif tags of the
same meaning). ISO 12234-2 is paywalled; DNG's TIFF/EP summary plus
`tags-exif.yaml` entries may substitute — the open question is registering the
IFD0 location variants.

### EXIF231 — Exif 2.31/2.32 additions — still open

The 12 uncovered `exifFields` entries: OffsetTime/OffsetTimeOriginal/
OffsetTimeDigitized (36880–36882), Temperature/Humidity/Pressure/WaterDepth/
Acceleration/CameraElevationAngle (37888–37893), CompositeImage group
(42080–42082). Vendored edition is Exif 2.3 (2010); acquiring CIPA
DC-008-2019 or later closes these.

### SGI — SGI extensions (3D volumes, matting) — still open

Tags: Matteing (32995), DataType (32996), **ImageDepth (32997)** and
**TileDepth (32998)** — the z-dimension for volumetric data; libtiff is the
de-facto defining implementation. Needs the written-from-implementation
`LIBTIFF` supplement (ImageDepth/TileDepth add a depth factor to DEP-001/
DEP-102 arithmetic).

### PIXAR — Pixar film/texture extensions — still open

Tags: 33300–33306. Compression 32908 (PIXARFILM, define-only), 32909
(PIXARLOG, implemented). No public spec → `LIBTIFF` supplement.

### HylaFAX private tags — still open

FaxRecvParams (34908), FaxSubAddress (34909), FaxRecvTime (34910), FaxDcs
(34911) — HylaFAX documentation → `LIBTIFF` supplement.

### Miscellaneous vendor codes (implemented or defined)

- ThunderScan RLE (32809), NeXT 2-bit RLE (32766) — implemented; libtiff
  source is the spec → `LIBTIFF`.
- ISO JBIG (34661) — implemented via libjbig; ITU-T T.82 not vendored.
- LZMA2 (34925), ZSTD (50000), WEBP (50001), LERC (34887) — implemented;
  50000/50001/50002 are *not* registered with the Adobe registry — interchange
  risk worth a requirements note.
- Defined in `tiff.h` with **no** built-in codec: IT8 family (32895–32898),
  Kodak DCS (32947), JP2000 (34712), JXL (50002), PIXARFILM (32908).

## 2. Codec coverage summary

| Compression | Scheme | libtiff | Requirements coverage |
|---:|---|---|---|
| 1, 2, 3, 4, 5, 6, 7, 8/32946, 32771, 32773 | classic set | implemented | **covered** (CMP-*) |
| 9, 10 | TIFF/FX JBIG T.85 / T.43 | defined only | **covered** (CMP-9, CMP-10) |
| 34676, 34677 | SGILog, SGILog24 | implemented | **covered** (CMP-34676/7) |
| 34892, 52546 | DNG lossy JPEG, JPEG XL | 52546 via JXL plugin path; 34892 absent from tiff.h | **covered** (CMP-34892, CMP-52546) |
| 32766, 32809 | NeXT, ThunderScan | implemented | gap → LIBTIFF supplement |
| 32895–32898 | IT8 CT/LW/MP/BL | defined only | gap (TIFF/IT, ISO 12639) |
| 32908, 32909 | PixarFilm, PixarLog | 32909 implemented | gap → PIXAR/LIBTIFF |
| 32947 | Kodak DCS | defined only | gap (no public spec) |
| 34661 | JBIG | implemented | gap → ITU-T T.82 |
| 34712 | JP2000 | defined only | gap (ISO 15444) |
| 34887 | LERC | implemented | gap (Esri LERC spec) |
| 34925 | LZMA2 | implemented | gap (libtiff-defined) |
| 50000, 50001, 50002 | ZSTD, WebP, JXL | implemented/defined | gap (libtiff-defined, unregistered codes) |

## 3. Reverse gaps: in the requirements, not (or wrongly) in libtiff

| Tag | Registry status | libtiff status |
|---|---|---|
| **IlluminantData3 (52535)** | current, DNG 1.6 (`tags-dng.yaml`) | **wrong code**: `tiff.h` defines `TIFFTAG_ILLUMINANTDATA3` as **53535** — a transposition typo for 52535 (0xCD37, DNG 1.7.1 p.85). libtiff reads/writes the tag under a code no other DNG implementation uses. Fix candidate with a `TIFFREQ:` citation. |
| TransferRange (342) | current, TIFF6 §20 | absent entirely (no define, no field entry) |
| OPIProxy (351) | current, PM6 | defined in `tiff.h`, not in any field table |
| ImageID (32781) | current, PM6 | same as OPIProxy |
| ColorResponseUnit (300) | retired 4.0 | absent (harmless: readers may ignore, GEN-003) |
| PhotoshopAnnotations (50255) | current, PSFF | absent from `tiff.h` and field tables |
| DNG 1.7 blocks 52544/52547–52555 | current, DNG 1.7 (`tags-dng.yaml`) | absent (libtiff tracks DNG through ~1.6 plus 53535 above) |
| ColorImageType / ColorList (318/319 draft proposals) | never adopted | absent (correct) |

Also worth noting:

- Tags 292/293 (T4/T6Options), 317 (Predictor), 347 (JPEGTables), 512–521
  (old JPEG) and 326–328 (fax page quality) are registered dynamically by
  codec field arrays (`tif_fax3.c`, `tif_predict.c`, `tif_jpeg.c`,
  `tif_ojpeg.c`), not the main table — their API availability depends on the
  configured codec set.
- InteroperabilityIFD (40965) appears in libtiff's *main* table, but Exif 2.3
  places it in the Exif IFD (registered in `tags-exif.yaml`, DEP-143); libtiff
  accepts it in any IFD.

## 4. Missing specification documents — acquisition list

| Proposed Spec ID | Document | Availability | Unlocks |
|---|---|---|---|
| EXIF231 | CIPA DC-008-2019+ (Exif 2.31/2.32) | free download | 12 exifFields tags |
| TIFFEP | ISO 12234-2 (TIFF/EP) | paywalled (DNG substitute possible) | 37 EP tags |
| ICCTN10 | ICC Technical Note 10-2021 (Embedding ICC profiles) | free (color.org) | first-party source for tag 34675 (ICC.1:2022-05 dropped its embedding annex) |
| CLASSF | "TIFF Class F" fax spec (Cygnet 1990) | archived copies | historical source for 326–328 (RFC 3949 now covers them) |
| T82 | ITU-T T.82 (JBIG) | free (ITU) | Compression 34661 datastream |
| IIM | IPTC-NAA IIM v4 | free download | 33723 datastream internals (the vendored IPTC guide has no container rules) |
| LIBTIFF | new supplement written from libtiff behavior | to be written | SGI depth/matting tags, Pixar tags, NeXT/ThunderScan/PixarLog/LZMA/ZSTD/WebP/LERC codecs, HylaFAX tags |

The `LIBTIFF` supplement is the interesting one: for features whose only
specification *is* libtiff, the requirements flow reverses — we document the
implementation, and the extraction source becomes a new
`sources/LIBTIFF.yaml` maintained by hand.

## 5. Model extensions

Implemented in the second wave:

- **IFD location attribute** — `location:` on tag entries; per-registry
  vocabularies (exif-ifd/gps-ifd/interop-ifd; DNG IFD roles;
  global-params-ifd/sub-ifd) plus placement rules DEP-140..143.
- **Conformance IDs** — EXIF/DNG/TFX/PSFF/ICC/IPTC/LLV/XMP slot into the
  `conformance:` vocabulary; `supplement_version` records document-internal
  versions (DNG 1.x, Exif editions).

Still pending:

- **Depth dimension**: ImageDepth/TileDepth (LIBTIFF supplement) add a z term
  to DEP-001/DEP-102 strip/tile arithmetic and a context variable.
- **Registered vs unregistered codes**: a boolean on compression values
  (ZSTD/WebP/JXL private codes) so validators can warn about interchange risk.
