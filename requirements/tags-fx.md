# TIFF/FX tag registry summary

Generated from [tags-fx.yaml](tags-fx.yaml) by `tools/generate.py` — do not edit.
Tag codes are unique per `Location`; full details (values, descriptions,
notes) are in the YAML. Versions in brackets are the supplement's own
version that introduced the tag (e.g. DNG 1.4.0.0, Exif 2.3).

| Code | Hex | Name | Location | Versions | Type(s) | Count | Default | Required |
|-----:|-----|------|----------|----------|---------|-------|---------|----------|
| 326 | 0x0146 | BadFaxLines | ifd0 | 6.0– (TFX) | SHORT,LONG | 1 | — | no |
| 327 | 0x0147 | CleanFaxData | ifd0 | 6.0– (TFX) | SHORT | 1 | — | no |
| 328 | 0x0148 | ConsecutiveBadFaxLines | ifd0 | 6.0– (TFX) | LONG,SHORT | 1 | — | no |
| 400 | 0x0190 | GlobalParametersIFD | ifd0 | 6.0– (TFX) | IFD,LONG | 1 | — | no |
| 401 | 0x0191 | ProfileType | global-params-ifd | 6.0– (TFX) | LONG | 1 | — | no |
| 402 | 0x0192 | FaxProfile | global-params-ifd | 6.0– (TFX) | BYTE | 1 | — | no |
| 403 | 0x0193 | CodingMethods | global-params-ifd | 6.0– (TFX) | LONG | 1 | — | no |
| 404 | 0x0194 | VersionYear | global-params-ifd | 6.0– (TFX) | BYTE | 4 | — | no |
| 405 | 0x0195 | ModeNumber | global-params-ifd | 6.0– (TFX) | BYTE | 1 | — | no |
| 433 | 0x01B1 | Decode | ifd0 | 6.0– (TFX) | SRATIONAL | 2 * SamplesPerPixel | — | conditional |
| 434 | 0x01B2 | ImageBaseColor | sub-ifd | 6.0– (TFX) | SHORT | SamplesPerPixel | — | no |
| 435 | 0x01B3 | T82Options | ifd0 | 6.0– (TFX) | LONG | 1 | 0 | conditional |
| 559 | 0x022F | StripRowCounts | ifd0 | 6.0– (TFX) | LONG | number of strips | — | conditional |
| 34732 | 0x87AC | ImageLayer | sub-ifd | 6.0– (TFX) | LONG | 2 | — | conditional |
