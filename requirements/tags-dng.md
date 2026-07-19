# DNG tag registry summary

Generated from [tags-dng.yaml](tags-dng.yaml) by `tools/generate.py` — do not edit.
Tag codes are unique per `Location`; full details (values, descriptions,
notes) are in the YAML. Versions in brackets are the supplement's own
version that introduced the tag (e.g. DNG 1.4.0.0, Exif 2.3).

| Code | Hex | Name | Location | Versions | Type(s) | Count | Default | Required |
|-----:|-----|------|----------|----------|---------|-------|---------|----------|
| 50706 | 0xC612 | DNGVersion | ifd0 | 6.0– (DNG) [1.0.0.0] | BYTE | 4 | — | yes |
| 50707 | 0xC613 | DNGBackwardVersion | ifd0 | 6.0– (DNG) [1.0.0.0] | BYTE | 4 | DNGVersion with the last two bytes set to zero | no |
| 50708 | 0xC614 | UniqueCameraModel | ifd0 | 6.0– (DNG) [1.0.0.0] | ASCII | String length including null | — | yes |
| 50709 | 0xC615 | LocalizedCameraModel | ifd0 | 6.0– (DNG) [1.0.0.0] | ASCII,BYTE | Byte count including null | Same as UniqueCameraModel | no |
| 50710 | 0xC616 | CFAPlaneColor | raw-ifd | 6.0– (DNG) [1.0.0.0] | BYTE | ColorPlanes | 0, 1, 2 (red, green, blue) | conditional |
| 50711 | 0xC617 | CFALayout | raw-ifd | 6.0– (DNG) [1.0.0.0] | SHORT | 1 | 1 | no |
| 50712 | 0xC618 | LinearizationTable | raw-ifd | 6.0– (DNG) [1.0.0.0] | SHORT | N | Identity table (0, 1, 2, 3, ...) | no |
| 50713 | 0xC619 | BlackLevelRepeatDim | raw-ifd | 6.0– (DNG) [1.0.0.0] | SHORT | 2 | 1, 1 | no |
| 50714 | 0xC61A | BlackLevel | raw-ifd | 6.0– (DNG) [1.0.0.0] | SHORT,LONG,RATIONAL | BlackLevelRepeatRows * BlackLevelRepeatCo... | 0 | no |
| 50715 | 0xC61B | BlackLevelDeltaH | raw-ifd | 6.0– (DNG) [1.0.0.0] | SRATIONAL | ActiveArea width | All zeros | no |
| 50716 | 0xC61C | BlackLevelDeltaV | raw-ifd | 6.0– (DNG) [1.0.0.0] | SRATIONAL | ActiveArea length | All zeros | no |
| 50717 | 0xC61D | WhiteLevel | raw-ifd | 6.0– (DNG) [1.0.0.0] | SHORT,LONG | SamplesPerPixel | 2^BitsPerSample - 1 (unsigned int); 1.0 (floating point) | no |
| 50718 | 0xC61E | DefaultScale | raw-ifd | 6.0– (DNG) [1.0.0.0] | RATIONAL | 2 | 1.0, 1.0 | conditional |
| 50719 | 0xC61F | DefaultCropOrigin | raw-ifd | 6.0– (DNG) [1.0.0.0] | SHORT,LONG,RATIONAL | 2 | 0, 0 | no |
| 50720 | 0xC620 | DefaultCropSize | raw-ifd | 6.0– (DNG) [1.0.0.0] | SHORT,LONG,RATIONAL | 2 | ImageWidth, ImageLength | no |
| 50721 | 0xC621 | ColorMatrix1 | ifd0-or-camera-profile-ifd | 6.0– (DNG) [1.0.0.0] | SRATIONAL | ColorPlanes * 3 | — | conditional |
| 50722 | 0xC622 | ColorMatrix2 | ifd0-or-camera-profile-ifd | 6.0– (DNG) [1.0.0.0] | SRATIONAL | ColorPlanes * 3 | — | no |
| 50723 | 0xC623 | CameraCalibration1 | ifd0 | 6.0– (DNG) [1.0.0.0] | SRATIONAL | ColorPlanes * ColorPlanes | Identity matrix | no |
| 50724 | 0xC624 | CameraCalibration2 | ifd0 | 6.0– (DNG) [1.0.0.0] | SRATIONAL | ColorPlanes * ColorPlanes | Identity matrix | no |
| 50725 | 0xC625 | ReductionMatrix1 | ifd0-or-camera-profile-ifd | 6.0– (DNG) [1.0.0.0] | SRATIONAL | 3 * ColorPlanes | — | no |
| 50726 | 0xC626 | ReductionMatrix2 | ifd0-or-camera-profile-ifd | 6.0– (DNG) [1.0.0.0] | SRATIONAL | 3 * ColorPlanes | — | no |
| 50727 | 0xC627 | AnalogBalance | ifd0 | 6.0– (DNG) [1.0.0.0] | RATIONAL | ColorPlanes | All 1.0 | no |
| 50728 | 0xC628 | AsShotNeutral | ifd0 | 6.0– (DNG) [1.0.0.0] | SHORT,RATIONAL | ColorPlanes | — | no |
| 50729 | 0xC629 | AsShotWhiteXY | ifd0 | 6.0– (DNG) [1.0.0.0] | RATIONAL | 2 | — | no |
| 50730 | 0xC62A | BaselineExposure | ifd0 | 6.0– (DNG) [1.0.0.0] | SRATIONAL | 1 | 0.0 | no |
| 50731 | 0xC62B | BaselineNoise | ifd0 | 6.0– (DNG) [1.0.0.0] | RATIONAL | 1 | 1.0 | no |
| 50732 | 0xC62C | BaselineSharpness | ifd0 | 6.0– (DNG) [1.0.0.0] | RATIONAL | 1 | 1.0 | no |
| 50733 | 0xC62D | BayerGreenSplit | raw-ifd | 6.0– (DNG) [1.0.0.0] | LONG | 1 | 0 | no |
| 50734 | 0xC62E | LinearResponseLimit | ifd0 | 6.0– (DNG) [1.0.0.0] | RATIONAL | 1 | 1.0 | no |
| 50735 | 0xC62F | CameraSerialNumber | ifd0 | 6.0– (DNG) [1.0.0.0] | ASCII | String length including null | — | no |
| 50736 | 0xC630 | LensInfo | ifd0 | 6.0– (DNG) [1.0.0.0] | RATIONAL | 4 | — | no |
| 50737 | 0xC631 | ChromaBlurRadius | raw-ifd | 6.0– (DNG) [1.0.0.0] | RATIONAL | 1 | Reader default amount | no |
| 50738 | 0xC632 | AntiAliasStrength | raw-ifd | 6.0– (DNG) [1.0.0.0] | RATIONAL | 1 | 1.0 | no |
| 50739 | 0xC633 | ShadowScale | ifd0 | 6.0– (DNG) [1.0.0.0] | RATIONAL | 1 | 1.0 | no |
| 50740 | 0xC634 | DNGPrivateData | ifd0 | 6.0– (DNG) [1.0.0.0] | BYTE | Length of private data block in bytes | — | no |
| 50741 | 0xC635 | MakerNoteSafety | ifd0 | 6.0– (DNG) [1.0.0.0] | SHORT | 1 | 0 | no |
| 50778 | 0xC65A | CalibrationIlluminant1 | ifd0-or-camera-profile-ifd | 6.0– (DNG) [1.0.0.0] | SHORT | 1 | 0 (unknown) | no |
| 50779 | 0xC65B | CalibrationIlluminant2 | ifd0-or-camera-profile-ifd | 6.0– (DNG) [1.0.0.0] | SHORT | 1 | — | conditional |
| 50780 | 0xC65C | BestQualityScale | raw-ifd | 6.0– (DNG) [1.0.0.0] | RATIONAL | 1 | 1.0 | no |
| 50781 | 0xC65D | RawDataUniqueID | ifd0 | 6.0– (DNG) [1.0.0.0] | BYTE | 16 | — | no |
| 50827 | 0xC68B | OriginalRawFileName | ifd0 | 6.0– (DNG) [1.0.0.0] | ASCII,BYTE | Byte count including null | — | no |
| 50828 | 0xC68C | OriginalRawFileData | ifd0 | 6.0– (DNG) [1.0.0.0] | UNDEFINED | Byte count of embedded data | — | no |
| 50829 | 0xC68D | ActiveArea | raw-ifd | 6.0– (DNG) [1.1.0.0] | SHORT,LONG | 4 | 0, 0, ImageLength, ImageWidth | conditional |
| 50830 | 0xC68E | MaskedAreas | raw-ifd | 6.0– (DNG) [1.1.0.0] | SHORT,LONG | 4 * number of rectangles | — | no |
| 50831 | 0xC68F | AsShotICCProfile | ifd0 | 6.0– (DNG) [1.0.0.0] | UNDEFINED | Length of ICC profile in bytes | — | no |
| 50832 | 0xC690 | AsShotPreProfileMatrix | ifd0 | 6.0– (DNG) [1.0.0.0] | SRATIONAL | 3 * ColorPlanes or ColorPlanes * ColorPlanes | Identity matrix | no |
| 50833 | 0xC691 | CurrentICCProfile | ifd0 | 6.0– (DNG) [1.0.0.0] | UNDEFINED | Length of ICC profile in bytes | — | no |
| 50834 | 0xC692 | CurrentPreProfileMatrix | ifd0 | 6.0– (DNG) [1.0.0.0] | SRATIONAL | 3 * ColorPlanes or ColorPlanes * ColorPlanes | Identity matrix | no |
| 50879 | 0xC6BF | ColorimetricReference | ifd0 | 6.0– (DNG) [1.2.0.0] | SHORT | 1 | 0 | no |
| 50931 | 0xC6F3 | CameraCalibrationSignature | ifd0 | 6.0– (DNG) [1.2.0.0] | ASCII,BYTE | Length of string including null | Empty string | no |
| 50932 | 0xC6F4 | ProfileCalibrationSignature | ifd0-or-camera-profile-ifd | 6.0– (DNG) [1.2.0.0] | ASCII,BYTE | Length of string including null | Empty string | no |
| 50933 | 0xC6F5 | ExtraCameraProfiles | ifd0 | 6.0– (DNG) [1.2.0.0] | LONG | Number of extra camera profiles | Empty list | no |
| 50934 | 0xC6F6 | AsShotProfileName | ifd0 | 6.0– (DNG) [1.2.0.0] | ASCII,BYTE | Length of string including null | — | no |
| 50935 | 0xC6F7 | NoiseReductionApplied | raw-ifd | 6.0– (DNG) [1.2.0.0] | RATIONAL | 1 | 0/0 (unknown) | no |
| 50936 | 0xC6F8 | ProfileName | ifd0-or-camera-profile-ifd | 6.0– (DNG) [1.2.0.0] | ASCII,BYTE | Length of string including null | — | conditional |
| 50937 | 0xC6F9 | ProfileHueSatMapDims | ifd0-or-camera-profile-ifd | 6.0– (DNG) [1.2.0.0] | LONG | 3 | — | conditional |
| 50938 | 0xC6FA | ProfileHueSatMapData1 | ifd0-or-camera-profile-ifd | 6.0– (DNG) [1.2.0.0] | FLOAT | HueDivisions * SaturationDivisions * Valu... | — | no |
| 50939 | 0xC6FB | ProfileHueSatMapData2 | ifd0-or-camera-profile-ifd | 6.0– (DNG) [1.2.0.0] | FLOAT | HueDivisions * SaturationDivisions * Valu... | — | no |
| 50940 | 0xC6FC | ProfileToneCurve | ifd0-or-camera-profile-ifd | 6.0– (DNG) [1.2.0.0] | FLOAT | Samples * 2 | — | no |
| 50941 | 0xC6FD | ProfileEmbedPolicy | ifd0-or-camera-profile-ifd | 6.0– (DNG) [1.2.0.0] | LONG | 1 | 0 | no |
| 50942 | 0xC6FE | ProfileCopyright | ifd0-or-camera-profile-ifd | 6.0– (DNG) [1.2.0.0] | ASCII,BYTE | Length of string including null | — | no |
| 50964 | 0xC714 | ForwardMatrix1 | ifd0-or-camera-profile-ifd | 6.0– (DNG) [1.2.0.0] | SRATIONAL | 3 * ColorPlanes | — | no |
| 50965 | 0xC715 | ForwardMatrix2 | ifd0-or-camera-profile-ifd | 6.0– (DNG) [1.2.0.0] | SRATIONAL | 3 * ColorPlanes | — | no |
| 50966 | 0xC716 | PreviewApplicationName | preview-ifd | 6.0– (DNG) [1.2.0.0] | ASCII,BYTE | Length of string including null | — | no |
| 50967 | 0xC717 | PreviewApplicationVersion | preview-ifd | 6.0– (DNG) [1.2.0.0] | ASCII,BYTE | Length of string including null | — | no |
| 50968 | 0xC718 | PreviewSettingsName | preview-ifd | 6.0– (DNG) [1.2.0.0] | ASCII,BYTE | Length of string including null | — | no |
| 50969 | 0xC719 | PreviewSettingsDigest | preview-ifd | 6.0– (DNG) [1.2.0.0] | BYTE | 16 | — | no |
| 50970 | 0xC71A | PreviewColorSpace | preview-ifd | 6.0– (DNG) [1.2.0.0] | LONG | 1 | sRGB for color previews, Gray Gamma 2.2 for monochrome previews | no |
| 50971 | 0xC71B | PreviewDateTime | preview-ifd | 6.0– (DNG) [1.2.0.0] | ASCII | Length of string including null | — | no |
| 50972 | 0xC71C | RawImageDigest | ifd0 | 6.0– (DNG) [1.2.0.0] | BYTE | 16 | — | no |
| 50973 | 0xC71D | OriginalRawFileDigest | ifd0 | 6.0– (DNG) [1.2.0.0] | BYTE | 16 | — | no |
| 50974 | 0xC71E | SubTileBlockSize | raw-ifd | 6.0– (DNG) [1.2.0.0] | SHORT,LONG | 2 | 1, 1 | no |
| 50975 | 0xC71F | RowInterleaveFactor | raw-ifd | 6.0– (DNG) [1.2.0.0] | SHORT,LONG | 1 | 1 | no |
| 50981 | 0xC725 | ProfileLookTableDims | ifd0-or-camera-profile-ifd | 6.0– (DNG) [1.2.0.0] | LONG | 3 | — | no |
| 50982 | 0xC726 | ProfileLookTableData | ifd0-or-camera-profile-ifd | 6.0– (DNG) [1.2.0.0] | FLOAT | HueDivisions * SaturationDivisions * Valu... | — | no |
| 51008 | 0xC740 | OpcodeList1 | raw-ifd | 6.0– (DNG) [1.3.0.0] | UNDEFINED | Variable | Empty List | no |
| 51009 | 0xC741 | OpcodeList2 | raw-ifd | 6.0– (DNG) [1.3.0.0] | UNDEFINED | Variable | Empty List | no |
| 51022 | 0xC74E | OpcodeList3 | raw-ifd | 6.0– (DNG) [1.3.0.0] | UNDEFINED | Variable | Empty List | no |
| 51041 | 0xC761 | NoiseProfile | raw-ifd | 6.0– (DNG) [1.3.0.0] | DOUBLE | 2 or 2 * ColorPlanes | Estimated from BaselineNoise | no |
| 51089 | 0xC791 | OriginalDefaultFinalSize | ifd0 | 6.0– (DNG) [1.4.0.0] | SHORT,LONG | 2 | DefaultCropSize * DefaultScale of this file | no |
| 51090 | 0xC792 | OriginalBestQualityFinalSize | ifd0 | 6.0– (DNG) [1.4.0.0] | SHORT,LONG | 2 | OriginalDefaultFinalSize, else DefaultCropSize*DefaultScale*BestQualityScale | no |
| 51091 | 0xC793 | OriginalDefaultCropSize | ifd0 | 6.0– (DNG) [1.4.0.0] | SHORT,LONG,RATIONAL | 2 | OriginalDefaultFinalSize, else this file's DefaultCropSize | no |
| 51107 | 0xC7A3 | ProfileHueSatMapEncoding | ifd0-or-camera-profile-ifd | 6.0– (DNG) [1.4.0.0] | LONG | 1 | 0 | no |
| 51108 | 0xC7A4 | ProfileLookTableEncoding | ifd0-or-camera-profile-ifd | 6.0– (DNG) [1.4.0.0] | LONG | 1 | 0 | no |
| 51109 | 0xC7A5 | BaselineExposureOffset | ifd0-or-camera-profile-ifd | 6.0– (DNG) [1.4.0.0] | RATIONAL | 1 | 0.0 | no |
| 51110 | 0xC7A6 | DefaultBlackRender | ifd0-or-camera-profile-ifd | 6.0– (DNG) [1.4.0.0] | LONG | 1 | 0 | no |
| 51111 | 0xC7A7 | NewRawImageDigest | ifd0 | 6.0– (DNG) [1.4.0.0] | BYTE | 16 | — | no |
| 51112 | 0xC7A8 | RawToPreviewGain | preview-ifd | 6.0– (DNG) [1.4.0.0] | DOUBLE | 1 | 1.0 | no |
| 51125 | 0xC7B5 | DefaultUserCrop | raw-ifd | 6.0– (DNG) [1.4.0.0] | RATIONAL | 4 | 0.0, 0.0, 1.0, 1.0 | no |
| 51177 | 0xC7E9 | DepthFormat | ifd0 | 6.0– (DNG) [1.5.0.0] | SHORT | 1 | 0 | no |
| 51178 | 0xC7EA | DepthNear | ifd0 | 6.0– (DNG) [1.5.0.0] | RATIONAL | 1 | 0/0 (unknown) | no |
| 51179 | 0xC7EB | DepthFar | ifd0 | 6.0– (DNG) [1.5.0.0] | RATIONAL | 1 | 0/0 (unknown) | no |
| 51180 | 0xC7EC | DepthUnits | ifd0 | 6.0– (DNG) [1.5.0.0] | SHORT | 1 | 0 | no |
| 51181 | 0xC7ED | DepthMeasureType | ifd0 | 6.0– (DNG) [1.5.0.0] | SHORT | 1 | 0 | no |
| 51182 | 0xC7EE | EnhanceParams | enhanced-ifd | 6.0– (DNG) [1.5.0.0] | ASCII | String length including null | — | conditional |
| 52525 | 0xCD2D | ProfileGainTableMap | raw-ifd | 6.0– (DNG) [1.6.0.0] | UNDEFINED | 64 + (4 * MapPointsV * MapPointsH * MapPo... | — | no |
| 52526 | 0xCD2E | SemanticName | semantic-mask-ifd | 6.0– (DNG) [1.6.0.0] | ASCII | String length including null | — | yes |
| 52528 | 0xCD30 | SemanticInstanceID | semantic-mask-ifd | 6.0– (DNG) [1.6.0.0] | ASCII | String length including null | — | no |
| 52529 | 0xCD31 | CalibrationIlluminant3 | ifd0-or-camera-profile-ifd | 6.0– (DNG) [1.6.0.0] | SHORT | 1 | 0 (unknown) | no |
| 52530 | 0xCD32 | CameraCalibration3 | ifd0 | 6.0– (DNG) [1.6.0.0] | SRATIONAL | ColorPlanes * ColorPlanes | Identity matrix | no |
| 52531 | 0xCD33 | ColorMatrix3 | ifd0-or-camera-profile-ifd | 6.0– (DNG) [1.6.0.0] | SRATIONAL | ColorPlanes * 3 | — | conditional |
| 52532 | 0xCD34 | ForwardMatrix3 | ifd0-or-camera-profile-ifd | 6.0– (DNG) [1.6.0.0] | SRATIONAL | ColorPlanes * 3 | — | no |
| 52533 | 0xCD35 | IlluminantData1 | ifd0-or-camera-profile-ifd | 6.0– (DNG) [1.6.0.0] | UNDEFINED | See structure (x-y or spectral power dist... | — | conditional |
| 52534 | 0xCD36 | IlluminantData2 | ifd0-or-camera-profile-ifd | 6.0– (DNG) [1.6.0.0] | UNDEFINED | See structure (same as IlluminantData1) | — | conditional |
| 52535 | 0xCD37 | IlluminantData3 | ifd0-or-camera-profile-ifd | 6.0– (DNG) [1.6.0.0] | UNDEFINED | See structure (same as IlluminantData1) | — | conditional |
| 52536 | 0xCD38 | MaskSubArea | semantic-mask-ifd | 6.0– (DNG) [1.6.0.0] | LONG | 4 | 0, 0, MaskWidth, MaskHeight | no |
| 52537 | 0xCD39 | ProfileHueSatMapData3 | ifd0-or-camera-profile-ifd | 6.0– (DNG) [1.6.0.0] | FLOAT | HueDivisions * SaturationDivisions * Valu... | — | no |
| 52538 | 0xCD3A | ReductionMatrix3 | ifd0-or-camera-profile-ifd | 6.0– (DNG) [1.6.0.0] | SRATIONAL | ColorPlanes * 3 | — | no |
| 52543 | 0xCD3F | RGBTables | ifd0-or-camera-profile-ifd | 6.0– (DNG) [1.6.0.0] | UNDEFINED | See structure (NumTables, CompositeMethod... | — | no |
| 52544 | 0xCD40 | ProfileGainTableMap2 | ifd0-or-camera-profile-ifd | 6.0– (DNG) [1.7.0.0] | UNDEFINED | 80 + (B * MapPointsV * MapPointsH * MapPo... | — | no |
| 52547 | 0xCD43 | ColumnInterleaveFactor | raw-ifd | 6.0– (DNG) [1.7.1.0] | SHORT,LONG | 1 | 1 | no |
| 52548 | 0xCD44 | ImageSequenceInfo | ifd0 | 6.0– (DNG) [1.7.0.0] | UNDEFINED | Byte count of data | — | no |
| 52550 | 0xCD46 | ImageStats | raw-ifd | 6.0– (DNG) [1.7.0.0] | UNDEFINED | Byte count of data | — | no |
| 52551 | 0xCD47 | ProfileDynamicRange | ifd0-or-camera-profile-ifd | 6.0– (DNG) [1.7.0.0] | UNDEFINED | 8 | Optional (Standard Dynamic Range) | no |
| 52552 | 0xCD48 | ProfileGroupName | ifd0-or-camera-profile-ifd | 6.0– (DNG) [1.7.0.0] | ASCII,BYTE | Length of string including null | — | no |
| 52553 | 0xCD49 | JXLDistance | jxl-ifd | 6.0– (DNG) [1.7.1.0] | FLOAT | 1 | — | no |
| 52554 | 0xCD4A | JXLEffort | jxl-ifd | 6.0– (DNG) [1.7.1.0] | LONG | 1 | — | no |
| 52555 | 0xCD4B | JXLDecodeSpeed | jxl-ifd | 6.0– (DNG) [1.7.1.0] | LONG | 1 | — | no |
