#!/usr/bin/env python3
"""Scan a libtiff checkout for implemented tags/codecs and diff them against
requirements/tags.yaml. Data source for requirements/gaps.md.

Usage: python3 tools/gapscan.py [path-to-libtiff-checkout]
       (default: ~/CLionProjects/libtiff; requires PyYAML)
"""
import os
import re
import sys

import yaml

REQ = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "requirements")
LIBTIFF = os.path.expanduser(sys.argv[1] if len(sys.argv) > 1 else "~/CLionProjects/libtiff")
LT = os.path.join(LIBTIFF, "libtiff")


def read(path):
    with open(path, encoding="utf-8", errors="replace") as f:
        return f.read()


hdr = read(os.path.join(LT, "tiff.h"))
tagdef = {
    m.group(1): int(m.group(2))
    for m in re.finditer(r"#define\s+((?:TIFFTAG|EXIFTAG|GPSTAG)_[A-Z0-9_]+)\s+(\d+)", hdr)
}
compdef = {
    m.group(1): int(m.group(2))
    for m in re.finditer(r"#define\s+(COMPRESSION_[A-Z0-9_]+)\s+(\d+)", hdr)
}

src = read(os.path.join(LT, "tif_dirinfo.c"))


def array_body(name):
    i = src.index(f"TIFFField {name}[] = ")
    return src[i:src.index("};", i)]


def tags_in(body, prefix):
    out = {}
    for m in re.finditer(r"\{\s*(" + prefix + r"_[A-Z0-9_]+)\s*,", body):
        if m.group(1) in tagdef:
            out.setdefault(tagdef[m.group(1)], m.group(1))
    return out


tiff_tags = tags_in(array_body("tiffFields"), "TIFFTAG")
exif_tags = tags_in(array_body("exifFields"), "EXIFTAG")
gps_tags = tags_in(array_body("gpsFields"), "GPSTAG")

def registry(name):
    with open(os.path.join(REQ, name)) as f:
        return yaml.safe_load(f)["tags"]


known = {t["code"] for t in registry("tags.yaml")}
# domain registries: DNG/FX tags appear in libtiff's main table; Exif/GPS/
# Interop-IFD tags live in libtiff's separate exifFields/gpsFields tables
known |= {t["code"] for t in registry("tags-dng.yaml")}
known |= {t["code"] for t in registry("tags-fx.yaml")}
exif_known = {t["code"] for t in registry("tags-exif.yaml")
              if t["location"] in ("exif-ifd", "interop-ifd")}
gps_known = {t["code"] for t in registry("tags-exif.yaml")
             if t["location"] == "gps-ifd"}

FILE_TAG_LIMIT = 65535  # >= 65536 are libtiff pseudo-tags (API-only)
main_file_tags = {c: n for c, n in tiff_tags.items() if c <= FILE_TAG_LIMIT}
missing = sorted(set(main_file_tags) - known)

print(f"libtiff: {LIBTIFF}")
print(f"main table: {len(main_file_tags)} file tags; covered: "
      f"{len(set(main_file_tags) & known)}; not in registry: {len(missing)}")
for c in missing:
    print(f"  {c:6d} 0x{c:04X} {main_file_tags[c]}")

print(f"\nregistry-only (not in libtiff main table): {sorted(known - set(tiff_tags))}")
print("  (292/293/317/347/512-521 are registered by codec field arrays, not gaps)")
print(f"\nexif IFD table: {len(exif_tags)} tags; covered: "
      f"{len(set(exif_tags) & exif_known)}; not in registry: "
      f"{sorted(set(exif_tags) - exif_known)}")
print(f"gps IFD table: {len(gps_tags)} tags; covered: "
      f"{len(set(gps_tags) & gps_known)}; not in registry: "
      f"{sorted(set(gps_tags) - gps_known)}")

codec = read(os.path.join(LT, "tif_codec.c"))
body = codec[codec.index("_TIFFBuiltinCODECS[] = {"):]
body = body[: body.index("{NULL, 0, NULL}")]
print("\nbuilt-in codecs:")
implemented = set()
for m in re.finditer(r'\{"([^"]+)",\s*(COMPRESSION_[A-Z0-9_]+),\s*(\w+)\}', body):
    implemented.add(compdef.get(m.group(2)))
    print(f"  {compdef.get(m.group(2), '?'):>6} {m.group(1):16s} init={m.group(3)}")
print("\ndefined in tiff.h without built-in codec:")
for name, code in sorted(compdef.items(), key=lambda kv: kv[1]):
    if code not in implemented:
        print(f"  {code:>6} {name}")
