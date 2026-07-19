# Tag registry summary

Generated from [tags.yaml](tags.yaml) by `tools/generate.py` — do not edit.

Full details (enumerated values, histories, notes) are in the YAML;
per-tag behavioral rules are in [tag-requirements.md](tag-requirements.md).

| Code | Hex | Name | Versions | Status | Conformance | Type(s) | Count | Default | Required |
|-----:|-----|------|----------|--------|-------------|---------|-------|---------|----------|
| 254 | 0x00FE | NewSubfileType | 5.0– | current | baseline | LONG | 1 | 0 | no |
| 255 | 0x00FF | SubfileType | 4.0– | deprecated | baseline | SHORT | 1 | — | no |
| 256 | 0x0100 | ImageWidth | 4.0– | current | baseline | SHORT,LONG | 1 | — | yes |
| 257 | 0x0101 | ImageLength | 4.0– | current | baseline | SHORT,LONG | 1 | — | yes |
| 258 | 0x0102 | BitsPerSample | 4.0– | current | baseline | SHORT | SPP | 1 | conditional |
| 259 | 0x0103 | Compression | 4.0– | current | baseline | SHORT | 1 | 1 | no |
| 262 | 0x0106 | PhotometricInterpretation | 4.0– | current | baseline | SHORT | 1 | — | yes |
| 263 | 0x0107 | Threshholding | 4.0– | current | baseline | SHORT | 1 | 1 | no |
| 264 | 0x0108 | CellWidth | 4.0– | current | baseline | SHORT | 1 | — | no |
| 265 | 0x0109 | CellLength | 4.0– | current | baseline | SHORT | 1 | — | no |
| 266 | 0x010A | FillOrder | 4.0– | current | baseline | SHORT | 1 | 1 | no |
| 269 | 0x010D | DocumentName | 4.0– | current | extension | ASCII | N | — | no |
| 270 | 0x010E | ImageDescription | 4.0– | current | baseline | ASCII | N | — | no |
| 271 | 0x010F | Make | 4.0– | current | baseline | ASCII | N | — | no |
| 272 | 0x0110 | Model | 4.0– | current | baseline | ASCII | N | — | no |
| 273 | 0x0111 | StripOffsets | 4.0– | current | baseline | SHORT,LONG (+LONG8 in BigTIFF) | StripsPerImage (PlanarConfiguration=1... | — | conditional |
| 274 | 0x0112 | Orientation | 4.0– | current | baseline | SHORT | 1 | 1 | no |
| 277 | 0x0115 | SamplesPerPixel | 4.0– | current | baseline | SHORT | 1 | 1 | conditional |
| 278 | 0x0116 | RowsPerStrip | 4.0– | current | baseline | SHORT,LONG | 1 | 4294967295 | conditional |
| 279 | 0x0117 | StripByteCounts | 4.0– | current | baseline | SHORT,LONG (+LONG8 in BigTIFF) | StripsPerImage (PlanarConfiguration=1... | — | conditional |
| 280 | 0x0118 | MinSampleValue | 4.0– | current | baseline | SHORT | SPP | 0 | no |
| 281 | 0x0119 | MaxSampleValue | 4.0– | current | baseline | SHORT | SPP | 2**BitsPerSample - 1 | no |
| 282 | 0x011A | XResolution | 4.0– | current | baseline | RATIONAL | 1 | — | yes |
| 283 | 0x011B | YResolution | 4.0– | current | baseline | RATIONAL | 1 | — | yes |
| 284 | 0x011C | PlanarConfiguration | 4.0– | current | baseline | SHORT | 1 | 1 | no |
| 285 | 0x011D | PageName | 4.0– | current | extension | ASCII | N | — | no |
| 286 | 0x011E | XPosition | 4.0– | current | extension | RATIONAL | 1 | — | no |
| 287 | 0x011F | YPosition | 4.0– | current | extension | RATIONAL | 1 | — | no |
| 288 | 0x0120 | FreeOffsets | 4.0– | deprecated | extension | LONG | N | — | no |
| 289 | 0x0121 | FreeByteCounts | 4.0– | deprecated | extension | LONG | N | — | no |
| 290 | 0x0122 | GrayResponseUnit | 4.0– | current | baseline | SHORT | 1 | 2 | no |
| 291 | 0x0123 | GrayResponseCurve | 4.0– | current | baseline | SHORT | 2**BitsPerSample | — | no |
| 292 | 0x0124 | T4Options | 4.0– | current | extension | LONG | 1 | 0 | no |
| 293 | 0x0125 | T6Options | 4.0– | current | extension | LONG | 1 | 0 | no |
| 296 | 0x0128 | ResolutionUnit | 4.0– | current | baseline | SHORT | 1 | 2 | no |
| 297 | 0x0129 | PageNumber | 4.0– | current | extension | SHORT | 2 | — | no |
| 300 | 0x012C | ColorResponseUnit | 4.0–4.0 | retired | baseline | SHORT | 1 | 2 | no |
| 301 | 0x012D | TransferFunction | 4.0– | current | extension | SHORT | {1|3} * 2**BitsPerSample | A single table matching NTSC gamma 2.2 | no |
| 305 | 0x0131 | Software | 5.0– | current | baseline | ASCII | N | — | no |
| 306 | 0x0132 | DateTime | 5.0– | current | baseline | ASCII | 20 | — | no |
| 315 | 0x013B | Artist | 5.0– | current | baseline | ASCII | N | — | no |
| 316 | 0x013C | HostComputer | 5.0– | current | baseline | ASCII | N | — | no |
| 317 | 0x013D | Predictor | 5.0– | current | extension | SHORT | 1 | 1 | no |
| 318 | 0x013E | WhitePoint | 5.0– | current | extension | RATIONAL | 2 | — | conditional |
| 319 | 0x013F | PrimaryChromaticities | 5.0– | current | extension | RATIONAL | 6 | — | conditional |
| 320 | 0x0140 | ColorMap | 5.0– | current | baseline | SHORT | 3 * 2**BitsPerSample | — | conditional |
| 321 | 0x0141 | HalftoneHints | 6.0– | current | extension | SHORT | 2 | — | no |
| 322 | 0x0142 | TileWidth | 6.0– | current | extension | SHORT,LONG | 1 | — | conditional |
| 323 | 0x0143 | TileLength | 6.0– | current | extension | SHORT,LONG | 1 | — | conditional |
| 324 | 0x0144 | TileOffsets | 6.0– | current | extension | LONG (+LONG8 in BigTIFF) | TilesPerImage (PlanarConfiguration=1)... | — | conditional |
| 325 | 0x0145 | TileByteCounts | 6.0– | current | extension | SHORT,LONG (+LONG8 in BigTIFF) | TilesPerImage (PlanarConfiguration=1)... | — | conditional |
| 330 | 0x014A | SubIFDs | 6.0– (PM6) | current | PM6 | LONG,IFD (+IFD8 in BigTIFF) | N (number of child IFDs) | — | no |
| 332 | 0x014C | InkSet | 6.0– | current | extension | SHORT | 1 | 1 | no |
| 333 | 0x014D | InkNames | 6.0– | current | extension | ASCII | Total bytes of all NUL-terminated ink... | — | conditional |
| 334 | 0x014E | NumberOfInks | 6.0– | current | extension | SHORT | 1 | 4 | no |
| 336 | 0x0150 | DotRange | 6.0– | current | extension | BYTE,SHORT | 2 | 2*SPP | [0, 2**BitsPerSample - 1] | no |
| 337 | 0x0151 | TargetPrinter | 6.0– | current | extension | ASCII | N | — | no |
| 338 | 0x0152 | ExtraSamples | 6.0– | current | baseline | SHORT | Number of extra components per pixel | — | conditional |
| 339 | 0x0153 | SampleFormat | 6.0– | current | extension | SHORT | SPP | 1 | no |
| 340 | 0x0154 | SMinSampleValue | 6.0– | current | extension | BYTE,ASCII,SHORT,LONG,RATIONAL,SBYTE,UNDEFINED,SSHORT,SLONG,SRATIONAL,FLOAT,DOUBLE | SPP | Full range of the sample data type | no |
| 341 | 0x0155 | SMaxSampleValue | 6.0– | current | extension | BYTE,ASCII,SHORT,LONG,RATIONAL,SBYTE,UNDEFINED,SSHORT,SLONG,SRATIONAL,FLOAT,DOUBLE | SPP | Full range of the sample data type | no |
| 342 | 0x0156 | TransferRange | 6.0– | current | extension | SHORT | 6 | [0, NV, 0, NV, 0, NV] where NV = 2**B... | no |
| 343 | 0x0157 | ClipPath | 6.0– (PM6) | current | PM6 | BYTE | N (bytes in the clip path data stream) | — | no |
| 344 | 0x0158 | XClipPathUnits | 6.0– (PM6) | current | PM6 | LONG | 1 | — | conditional |
| 345 | 0x0159 | YClipPathUnits | 6.0– (PM6) | current | PM6 | LONG | 1 | Equal to XClipPathUnits (344) | no |
| 346 | 0x015A | Indexed | 6.0– (PM6) | current | PM6 | SHORT | 1 | 0 | no |
| 347 | 0x015B | JPEGTables | 6.0– (TN2) | current | TN2 | UNDEFINED | N (bytes in the tables datastream) | — | conditional |
| 351 | 0x015F | OPIProxy | 6.0– (PM6) | current | PM6 | SHORT | 1 | 0 | no |
| 512 | 0x0200 | JPEGProc | 6.0– | deprecated | extension | SHORT | 1 | — | conditional |
| 513 | 0x0201 | JPEGInterchangeFormat | 6.0– | deprecated | extension | LONG | 1 | — | no |
| 514 | 0x0202 | JPEGInterchangeFormatLength | 6.0– | deprecated | extension | LONG | 1 | — | no |
| 515 | 0x0203 | JPEGRestartInterval | 6.0– | deprecated | extension | SHORT | 1 | — | no |
| 517 | 0x0205 | JPEGLosslessPredictors | 6.0– | deprecated | extension | SHORT | SPP | — | conditional |
| 518 | 0x0206 | JPEGPointTransforms | 6.0– | deprecated | extension | SHORT | SPP | 0 | no |
| 519 | 0x0207 | JPEGQTables | 6.0– | deprecated | extension | LONG | SPP | — | conditional |
| 520 | 0x0208 | JPEGDCTables | 6.0– | deprecated | extension | LONG | SPP | — | conditional |
| 521 | 0x0209 | JPEGACTables | 6.0– | deprecated | extension | LONG | SPP | — | conditional |
| 529 | 0x0211 | YCbCrCoefficients | 6.0– | current | extension | RATIONAL | 3 | [299/1000, 587/1000, 114/1000] (CCIR ... | no |
| 530 | 0x0212 | YCbCrSubSampling | 6.0– | current | extension | SHORT | 2 | [2, 2] | no |
| 531 | 0x0213 | YCbCrPositioning | 6.0– | current | extension | SHORT | 1 | 1 | no |
| 532 | 0x0214 | ReferenceBlackWhite | 6.0– | current | extension | RATIONAL | 6 | [0, NV, 0, NV, 0, NV] where NV = 2**B... | conditional |
| 700 | 0x02BC | XMP | 6.0– (XMP) | current | XMP | BYTE,UNDEFINED | N (byte length of the serialized XMP ... | — | no |
| 32781 | 0x800D | ImageID | 6.0– (PM6) | current | PM6 | ASCII | N | — | conditional |
| 33432 | 0x8298 | Copyright | 6.0– | current | baseline | ASCII | N | — | no |
| 33723 | 0x83BB | IPTC | 6.0– (XMP) | current | XMP | UNDEFINED,BYTE | N (byte length of the IPTC-IIM DataSe... | — | no |
| 34377 | 0x8649 | Photoshop | 6.0– (PSFF) | current | PSFF | BYTE,UNDEFINED | N | — | no |
| 34665 | 0x8769 | ExifIFDPointer | 6.0– (EXIF) | current | EXIF | LONG (+IFD8 in BigTIFF) | 1 | — | conditional |
| 34675 | 0x8773 | ICCProfile | 6.0– (ICC) | current | ICC | UNDEFINED | N (profile size in bytes) | — | no |
| 34853 | 0x8825 | GPSInfoIFDPointer | 6.0– (EXIF) | current | EXIF | LONG (+IFD8 in BigTIFF) | 1 | — | no |
| 37439 | 0x923F | StoNits | 6.0– (LLV) | current | LLV | DOUBLE | 1 | — | no |
| 37724 | 0x935C | ImageSourceData | 6.0– (PS) | current | PS | UNDEFINED | N | — | no |
| 50255 | 0xC44F | PhotoshopAnnotations | 6.0– (PSFF) | current | PSFF | BYTE,UNDEFINED | N | — | no |

## Unadopted draft proposals (colliding codes)

| Code | Name | Proposed in | Notes |
|-----:|------|-------------|-------|
| 318 | ColorImageType | T5 | TIFF 5.0 Appendix J draft; collides with the adopted WhitePoint (318). Distinguishable by field type (SHORT vs RATIONAL) and count. |
| 319 | ColorList | T5 | TIFF 5.0 Appendix J draft; collides with the adopted PrimaryChromaticities (319). Distinguishable by field type. |
