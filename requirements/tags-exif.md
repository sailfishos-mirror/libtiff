# Exif tag registry summary (Exif / GPS / Interoperability IFDs)

Generated from [tags-exif.yaml](tags-exif.yaml) by `tools/generate.py` — do not edit.
Tag codes are unique per `Location`; full details (values, descriptions,
notes) are in the YAML. Versions in brackets are the supplement's own
version that introduced the tag (e.g. DNG 1.4.0.0, Exif 2.3).

| Code | Hex | Name | Location | Versions | Type(s) | Count | Default | Required |
|-----:|-----|------|----------|----------|---------|-------|---------|----------|
| 0 | 0x0000 | GPSVersionID | gps-ifd | 6.0– (EXIF) | BYTE | 4 | 2.3.0.0 | conditional |
| 1 | 0x0001 | GPSLatitudeRef | gps-ifd | 6.0– (EXIF) | ASCII | 2 | — | no |
| 1 | 0x0001 | InteroperabilityIndex | interop-ifd | 6.0– (EXIF) | ASCII | Any | — | conditional |
| 2 | 0x0002 | GPSLatitude | gps-ifd | 6.0– (EXIF) | RATIONAL | 3 | — | no |
| 3 | 0x0003 | GPSLongitudeRef | gps-ifd | 6.0– (EXIF) | ASCII | 2 | — | no |
| 4 | 0x0004 | GPSLongitude | gps-ifd | 6.0– (EXIF) | RATIONAL | 3 | — | no |
| 5 | 0x0005 | GPSAltitudeRef | gps-ifd | 6.0– (EXIF) | BYTE | 1 | 0 | no |
| 6 | 0x0006 | GPSAltitude | gps-ifd | 6.0– (EXIF) | RATIONAL | 1 | — | no |
| 7 | 0x0007 | GPSTimeStamp | gps-ifd | 6.0– (EXIF) | RATIONAL | 3 | — | no |
| 8 | 0x0008 | GPSSatellites | gps-ifd | 6.0– (EXIF) | ASCII | Any | — | no |
| 9 | 0x0009 | GPSStatus | gps-ifd | 6.0– (EXIF) | ASCII | 2 | — | no |
| 10 | 0x000A | GPSMeasureMode | gps-ifd | 6.0– (EXIF) | ASCII | 2 | — | no |
| 11 | 0x000B | GPSDOP | gps-ifd | 6.0– (EXIF) | RATIONAL | 1 | — | no |
| 12 | 0x000C | GPSSpeedRef | gps-ifd | 6.0– (EXIF) | ASCII | 2 | K | no |
| 13 | 0x000D | GPSSpeed | gps-ifd | 6.0– (EXIF) | RATIONAL | 1 | — | no |
| 14 | 0x000E | GPSTrackRef | gps-ifd | 6.0– (EXIF) | ASCII | 2 | T | no |
| 15 | 0x000F | GPSTrack | gps-ifd | 6.0– (EXIF) | RATIONAL | 1 | — | no |
| 16 | 0x0010 | GPSImgDirectionRef | gps-ifd | 6.0– (EXIF) | ASCII | 2 | T | no |
| 17 | 0x0011 | GPSImgDirection | gps-ifd | 6.0– (EXIF) | RATIONAL | 1 | — | no |
| 18 | 0x0012 | GPSMapDatum | gps-ifd | 6.0– (EXIF) | ASCII | Any | — | no |
| 19 | 0x0013 | GPSDestLatitudeRef | gps-ifd | 6.0– (EXIF) | ASCII | 2 | — | no |
| 20 | 0x0014 | GPSDestLatitude | gps-ifd | 6.0– (EXIF) | RATIONAL | 3 | — | no |
| 21 | 0x0015 | GPSDestLongitudeRef | gps-ifd | 6.0– (EXIF) | ASCII | 2 | — | no |
| 22 | 0x0016 | GPSDestLongitude | gps-ifd | 6.0– (EXIF) | RATIONAL | 3 | — | no |
| 23 | 0x0017 | GPSDestBearingRef | gps-ifd | 6.0– (EXIF) | ASCII | 2 | T | no |
| 24 | 0x0018 | GPSDestBearing | gps-ifd | 6.0– (EXIF) | RATIONAL | 1 | — | no |
| 25 | 0x0019 | GPSDestDistanceRef | gps-ifd | 6.0– (EXIF) | ASCII | 2 | K | no |
| 26 | 0x001A | GPSDestDistance | gps-ifd | 6.0– (EXIF) | RATIONAL | 1 | — | no |
| 27 | 0x001B | GPSProcessingMethod | gps-ifd | 6.0– (EXIF) | UNDEFINED | Any | — | no |
| 28 | 0x001C | GPSAreaInformation | gps-ifd | 6.0– (EXIF) | UNDEFINED | Any | — | no |
| 29 | 0x001D | GPSDateStamp | gps-ifd | 6.0– (EXIF) | ASCII | 11 | — | no |
| 30 | 0x001E | GPSDifferential | gps-ifd | 6.0– (EXIF) | SHORT | 1 | — | no |
| 31 | 0x001F | GPSHPositioningError | gps-ifd | 6.0– (EXIF) [2.3] | RATIONAL | 1 | — | no |
| 33434 | 0x829A | ExposureTime | exif-ifd | 6.0– (EXIF) | RATIONAL | 1 | — | no |
| 33437 | 0x829D | FNumber | exif-ifd | 6.0– (EXIF) | RATIONAL | 1 | — | no |
| 34850 | 0x8822 | ExposureProgram | exif-ifd | 6.0– (EXIF) | SHORT | 1 | 0 | no |
| 34852 | 0x8824 | SpectralSensitivity | exif-ifd | 6.0– (EXIF) | ASCII | Any | — | no |
| 34855 | 0x8827 | PhotographicSensitivity | exif-ifd | 6.0– (EXIF) | SHORT | Any | — | no |
| 34856 | 0x8828 | OECF | exif-ifd | 6.0– (EXIF) | UNDEFINED | Any | — | no |
| 34864 | 0x8830 | SensitivityType | exif-ifd | 6.0– (EXIF) [2.3] | SHORT | 1 | — | no |
| 34865 | 0x8831 | StandardOutputSensitivity | exif-ifd | 6.0– (EXIF) [2.3] | LONG | 1 | — | no |
| 34866 | 0x8832 | RecommendedExposureIndex | exif-ifd | 6.0– (EXIF) [2.3] | LONG | 1 | — | no |
| 34867 | 0x8833 | ISOSpeed | exif-ifd | 6.0– (EXIF) [2.3] | LONG | 1 | — | no |
| 34868 | 0x8834 | ISOSpeedLatitudeyyy | exif-ifd | 6.0– (EXIF) [2.3] | LONG | 1 | — | conditional |
| 34869 | 0x8835 | ISOSpeedLatitudezzz | exif-ifd | 6.0– (EXIF) [2.3] | LONG | 1 | — | conditional |
| 36864 | 0x9000 | ExifVersion | exif-ifd | 6.0– (EXIF) | UNDEFINED | 4 | 0230 | yes |
| 36867 | 0x9003 | DateTimeOriginal | exif-ifd | 6.0– (EXIF) | ASCII | 20 | — | no |
| 36868 | 0x9004 | DateTimeDigitized | exif-ifd | 6.0– (EXIF) | ASCII | 20 | — | no |
| 37121 | 0x9101 | ComponentsConfiguration | exif-ifd | 6.0– (EXIF) | UNDEFINED | 4 | 4 5 6 0 (RGB uncompressed) or 1 2 3 0 (other) | conditional |
| 37122 | 0x9102 | CompressedBitsPerPixel | exif-ifd | 6.0– (EXIF) | RATIONAL | 1 | — | conditional |
| 37377 | 0x9201 | ShutterSpeedValue | exif-ifd | 6.0– (EXIF) | SRATIONAL | 1 | — | no |
| 37378 | 0x9202 | ApertureValue | exif-ifd | 6.0– (EXIF) | RATIONAL | 1 | — | no |
| 37379 | 0x9203 | BrightnessValue | exif-ifd | 6.0– (EXIF) | SRATIONAL | 1 | — | no |
| 37380 | 0x9204 | ExposureBiasValue | exif-ifd | 6.0– (EXIF) | SRATIONAL | 1 | — | no |
| 37381 | 0x9205 | MaxApertureValue | exif-ifd | 6.0– (EXIF) | RATIONAL | 1 | — | no |
| 37382 | 0x9206 | SubjectDistance | exif-ifd | 6.0– (EXIF) | RATIONAL | 1 | — | no |
| 37383 | 0x9207 | MeteringMode | exif-ifd | 6.0– (EXIF) | SHORT | 1 | 0 | no |
| 37384 | 0x9208 | LightSource | exif-ifd | 6.0– (EXIF) | SHORT | 1 | 0 | no |
| 37385 | 0x9209 | Flash | exif-ifd | 6.0– (EXIF) | SHORT | 1 | — | no |
| 37386 | 0x920A | FocalLength | exif-ifd | 6.0– (EXIF) | RATIONAL | 1 | — | no |
| 37396 | 0x9214 | SubjectArea | exif-ifd | 6.0– (EXIF) | SHORT | 2 or 3 or 4 | — | no |
| 37500 | 0x927C | MakerNote | exif-ifd | 6.0– (EXIF) | UNDEFINED | Any | — | no |
| 37510 | 0x9286 | UserComment | exif-ifd | 6.0– (EXIF) | UNDEFINED | Any | — | no |
| 37520 | 0x9290 | SubSecTime | exif-ifd | 6.0– (EXIF) | ASCII | Any | — | no |
| 37521 | 0x9291 | SubSecTimeOriginal | exif-ifd | 6.0– (EXIF) | ASCII | Any | — | no |
| 37522 | 0x9292 | SubSecTimeDigitized | exif-ifd | 6.0– (EXIF) | ASCII | Any | — | no |
| 40960 | 0xA000 | FlashpixVersion | exif-ifd | 6.0– (EXIF) | UNDEFINED | 4 | 0100 | yes |
| 40961 | 0xA001 | ColorSpace | exif-ifd | 6.0– (EXIF) | SHORT | 1 | — | yes |
| 40962 | 0xA002 | PixelXDimension | exif-ifd | 6.0– (EXIF) | SHORT,LONG | 1 | — | conditional |
| 40963 | 0xA003 | PixelYDimension | exif-ifd | 6.0– (EXIF) | SHORT,LONG | 1 | — | conditional |
| 40964 | 0xA004 | RelatedSoundFile | exif-ifd | 6.0– (EXIF) | ASCII | 13 | — | no |
| 40965 | 0xA005 | InteroperabilityIFDPointer | exif-ifd | 6.0– (EXIF) | LONG | 1 | — | conditional |
| 41483 | 0xA20B | FlashEnergy | exif-ifd | 6.0– (EXIF) | RATIONAL | 1 | — | no |
| 41484 | 0xA20C | SpatialFrequencyResponse | exif-ifd | 6.0– (EXIF) | UNDEFINED | Any | — | no |
| 41486 | 0xA20E | FocalPlaneXResolution | exif-ifd | 6.0– (EXIF) | RATIONAL | 1 | — | no |
| 41487 | 0xA20F | FocalPlaneYResolution | exif-ifd | 6.0– (EXIF) | RATIONAL | 1 | — | no |
| 41488 | 0xA210 | FocalPlaneResolutionUnit | exif-ifd | 6.0– (EXIF) | SHORT | 1 | 2 | no |
| 41492 | 0xA214 | SubjectLocation | exif-ifd | 6.0– (EXIF) | SHORT | 2 | — | no |
| 41493 | 0xA215 | ExposureIndex | exif-ifd | 6.0– (EXIF) | RATIONAL | 1 | — | no |
| 41495 | 0xA217 | SensingMethod | exif-ifd | 6.0– (EXIF) | SHORT | 1 | — | no |
| 41728 | 0xA300 | FileSource | exif-ifd | 6.0– (EXIF) | UNDEFINED | 1 | 3 | no |
| 41729 | 0xA301 | SceneType | exif-ifd | 6.0– (EXIF) | UNDEFINED | 1 | 1 | no |
| 41730 | 0xA302 | CFAPattern | exif-ifd | 6.0– (EXIF) | UNDEFINED | Any | — | no |
| 41985 | 0xA401 | CustomRendered | exif-ifd | 6.0– (EXIF) | SHORT | 1 | 0 | no |
| 41986 | 0xA402 | ExposureMode | exif-ifd | 6.0– (EXIF) | SHORT | 1 | — | no |
| 41987 | 0xA403 | WhiteBalance | exif-ifd | 6.0– (EXIF) | SHORT | 1 | — | no |
| 41988 | 0xA404 | DigitalZoomRatio | exif-ifd | 6.0– (EXIF) | RATIONAL | 1 | — | no |
| 41989 | 0xA405 | FocalLengthIn35mmFilm | exif-ifd | 6.0– (EXIF) | SHORT | 1 | — | no |
| 41990 | 0xA406 | SceneCaptureType | exif-ifd | 6.0– (EXIF) | SHORT | 1 | 0 | no |
| 41991 | 0xA407 | GainControl | exif-ifd | 6.0– (EXIF) | RATIONAL | 1 | — | no |
| 41992 | 0xA408 | Contrast | exif-ifd | 6.0– (EXIF) | SHORT | 1 | 0 | no |
| 41993 | 0xA409 | Saturation | exif-ifd | 6.0– (EXIF) | SHORT | 1 | 0 | no |
| 41994 | 0xA40A | Sharpness | exif-ifd | 6.0– (EXIF) | SHORT | 1 | 0 | no |
| 41995 | 0xA40B | DeviceSettingDescription | exif-ifd | 6.0– (EXIF) | UNDEFINED | Any | — | no |
| 41996 | 0xA40C | SubjectDistanceRange | exif-ifd | 6.0– (EXIF) | SHORT | 1 | — | no |
| 42016 | 0xA420 | ImageUniqueID | exif-ifd | 6.0– (EXIF) | ASCII | 33 | — | no |
| 42032 | 0xA430 | CameraOwnerName | exif-ifd | 6.0– (EXIF) [2.3] | ASCII | Any | — | no |
| 42033 | 0xA431 | BodySerialNumber | exif-ifd | 6.0– (EXIF) [2.3] | ASCII | Any | — | no |
| 42034 | 0xA432 | LensSpecification | exif-ifd | 6.0– (EXIF) [2.3] | RATIONAL | 4 | — | no |
| 42035 | 0xA433 | LensMake | exif-ifd | 6.0– (EXIF) [2.3] | ASCII | Any | — | no |
| 42036 | 0xA434 | LensModel | exif-ifd | 6.0– (EXIF) [2.3] | ASCII | Any | — | no |
| 42037 | 0xA435 | LensSerialNumber | exif-ifd | 6.0– (EXIF) [2.3] | ASCII | Any | — | no |
| 42240 | 0xA500 | Gamma | exif-ifd | 6.0– (EXIF) [2.3] | RATIONAL | 1 | — | no |
