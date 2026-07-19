# Container structure and general obligations

Requirement format and field meanings: see [README.md](README.md). Source citations
name per-document extraction entries in [sources/](sources/) (which carry the exact
document section and page), or a document section directly.

## STR — Classic TIFF container

### STR-001 — Byte order marker
- Level: MUST · Actor: file · Conformance: baseline
- Versions: 4.0– · Container: classic · Status: current
- Sources: T6B-014; T5 §1; T4 §3

Header bytes 0–1 hold the byte order: `II` (0x4949, little-endian) or `MM`
(0x4D4D, big-endian). The order applies to every 16-bit and 32-bit integer in the
file, including all field values.

### STR-002 — Magic number 42
- Level: MUST · Actor: file · Conformance: baseline
- Versions: 4.0– · Container: classic · Status: current
- Sources: T6B-015; T5 §1; T4 §3

Header bytes 2–3 contain 42 (0x2A), in the file's byte order. (BigTIFF uses 43;
see BTF-001.)

### STR-003 — First IFD offset
- Level: MUST · Actor: file · Conformance: baseline
- Versions: 4.0– · Container: classic · Status: current
- Sources: T6B-016, T6B-041, T6B-017

Header bytes 4–7 hold the byte offset of the first IFD, which must be an even
number ≥ 8. The IFD may be anywhere in the file after the header (including after
image data); readers must follow offsets wherever they lead.

### STR-004 — Maximum file size
- Level: MUST · Actor: file · Conformance: baseline
- Versions: 4.0– · Container: classic · Status: current
- Sources: T6B-012

A classic TIFF file is at most 2³² bytes; all offsets are 32-bit. (BigTIFF
removes this limit; see BTF-*.)

### STR-005 — IFD layout
- Level: MUST · Actor: file · Conformance: baseline
- Versions: 4.0– · Container: classic · Status: current
- Sources: T6B-018; T5 §1; T4 §3

An IFD is: a 2-byte entry count, then that many 12-byte entries, then the 4-byte
offset of the next IFD (0 if none).

### STR-006 — At least one IFD with at least one entry
- Level: MUST · Actor: file · Conformance: baseline
- Versions: 4.0– · Container: both · Status: current
- Sources: T6B-020

### STR-007 — IFD entry layout
- Level: MUST · Actor: file · Conformance: baseline
- Versions: 4.0– · Container: classic · Status: current
- Sources: T6B-021, T6B-027

Each 12-byte entry is: bytes 0–1 tag, bytes 2–3 field type, bytes 4–7 count
(number of values, not bytes), bytes 8–11 value offset. TIFF 4.0/5.0 called the
count "Length"; the semantics are identical.

### STR-008 — Value placement and alignment
- Level: MUST · Actor: file · Conformance: baseline
- Versions: 4.0– · Container: classic · Status: current
- Sources: T6B-022, T6B-025, T6B-026

A value is stored inline in the entry's last 4 bytes if and only if its total
size (type size × count) is ≤ 4 bytes, left-justified (lower-numbered bytes) if
shorter. Otherwise the entry holds an even (word-aligned) offset to the value,
which may be anywhere after the header, in any order relative to other values.
Vendor deviation: odd offsets occur in the wild — flag `tolerate.unaligned-values`
in [constraints.yaml](constraints.yaml).

### STR-009 — IFD entries sorted by tag
- Level: MUST · Actor: file · Conformance: baseline
- Versions: 4.0– · Container: both · Status: current
- Sources: T6B-024; BTF-024

Entries are sorted ascending by tag code. Vendor deviation: unsorted IFDs occur —
flag `tolerate.unsorted-ifd`.

### STR-010 — Baseline field types (codes 1–5)
- Level: MUST · Actor: file · Conformance: baseline
- Versions: 4.0– · Container: both · Status: current
- Sources: T6B-028; T4 §3; T5 §1

1 = BYTE (8-bit unsigned), 2 = ASCII (7-bit ASCII bytes, NUL-terminated),
3 = SHORT (16-bit unsigned), 4 = LONG (32-bit unsigned), 5 = RATIONAL (two LONGs:
numerator, denominator). Present in all revisions since 4.0.

### STR-011 — TIFF 6.0 field types (codes 6–12)
- Level: MUST · Actor: file · Conformance: baseline
- Versions: 6.0– · Container: both · Status: current
- Sources: T6B-029

6 = SBYTE, 7 = UNDEFINED (opaque byte), 8 = SSHORT, 9 = SLONG, 10 = SRATIONAL
(two SLONGs), 11 = FLOAT (IEEE single), 12 = DOUBLE (IEEE double). All governed
by the header byte order.

### STR-012 — IFD field type (code 13)
- Level: MUST · Actor: file · Conformance: PM6
- Versions: 6.0– · Container: both · Status: current
- Sources: PM6 (Tech Note 1, SubIFDs); tags.yaml entry 330

13 = IFD: a LONG offset whose value is the position of a child IFD. Defined by
the PM6 technote for SubIFDs (330). Codes 14–15 are not assigned by any document
in this registry; codes 16–18 are BigTIFF (BTF-009).

### STR-013 — ASCII field termination
- Level: MUST · Actor: file · Conformance: baseline
- Versions: 4.0– · Container: both · Status: current
- Sources: T6B-030, T6B-031

The last byte of an ASCII field is NUL, included in the count (no pad byte is
counted). Multiple NUL-terminated strings in one field are allowed but a single
string is preferred; exactly one NUL separates strings. Vendor deviation:
missing final NUL — flag `tolerate.missing-nul`.

### STR-014 — IFD chain termination
- Level: MUST · Actor: writer · Conformance: baseline
- Versions: 4.0– · Container: both · Status: current
- Sources: T6B-019, T6B-060

Every IFD ends with the offset of the next IFD; the writer must write 0 after
the last IFD. Readers traverse the chain to enumerate subfiles (STR-015).
A cycle in the chain is malformed (validators must detect it).

### STR-015 — Multiple subfiles
- Level: MAY · Actor: file · Conformance: baseline
- Versions: 4.0– · Container: both · Status: current
- Sources: T6B-037; T5 §1

A file may contain any number of IFDs, each defining an independent subfile
(page, reduced resolution, mask — see NewSubfileType 254).

### STR-016 — Pointer hygiene
- Level: MUST · Actor: writer · Conformance: baseline
- Versions: 6.0– · Container: both · Status: current
- Sources: T6B-065, T6B-066

Offsets must point at real data of the stated size within the file (no
out-of-bounds, no truncated values); an offset of 0 is never a valid "not
present" marker. No data should be referenced from more than one place,
although readers and editors are under no obligation to detect duplicates.

## BTF — BigTIFF container

BigTIFF is the 64-bit container variant; it changes only what is listed here and
otherwise inherits every classic TIFF 6.0 rule (BTF-013).

### BTF-001 — Version number 43
- Level: MUST · Actor: file · Conformance: BIGTIFF
- Versions: 6.0– · Container: bigtiff · Status: current
- Sources: BTF-002, BTF-021

Header bytes 2–3 contain 43. Byte order in bytes 0–1 works exactly as in classic
TIFF (STR-001).

### BTF-002 — Offset size field
- Level: MUST · Actor: file · Conformance: BIGTIFF
- Versions: 6.0– · Container: bigtiff · Status: current
- Sources: BTF-003, BTF-004

Header bytes 4–5 contain 8 (the byte size of offsets). A reader encountering any
other value must refuse the file (the field exists so a future revision can move
to 16-byte pointers).

### BTF-003 — Reserved header bytes
- Level: MUST · Actor: file · Conformance: BIGTIFF
- Versions: 6.0– · Container: bigtiff · Status: current
- Sources: BTF-006, BTF-007

Header bytes 6–7 must be 0; a reader encountering any other value must refuse
the file.

### BTF-004 — First IFD offset (64-bit)
- Level: MUST · Actor: file · Conformance: BIGTIFF
- Versions: 6.0– · Container: bigtiff · Status: current
- Sources: BTF-008, BTF-022

Header bytes 8–15 hold the 8-byte offset of the first IFD.

### BTF-005 — 64-bit IFD layout
- Level: MUST · Actor: file · Conformance: BIGTIFF
- Versions: 6.0– · Container: bigtiff · Status: current
- Sources: BTF-011, BTF-012, BTF-013, BTF-023

An IFD is: an 8-byte entry count, then that many 20-byte entries, then the
8-byte offset of the next IFD (0 if none).

### BTF-006 — 20-byte IFD entry layout
- Level: MUST · Actor: file · Conformance: BIGTIFF
- Versions: 6.0– · Container: bigtiff · Status: current
- Sources: BTF-025 (see note), BTF-009

Bytes 0–1 tag, bytes 2–3 type, bytes 4–11 count (8 bytes), bytes 12–19 value or
value offset (8 bytes). Note: the BigTIFF document's overview text says the
value field occupies "bytes 8–15" of an entry; the normative tag-structure table
(offset 12) is correct and is what all implementations use.

### BTF-007 — 8-byte inline threshold
- Level: MUST · Actor: file · Conformance: BIGTIFF
- Versions: 6.0– · Container: bigtiff · Status: current
- Sources: BTF-026

A value is stored inline in the entry's 8-byte value field if and only if its
total size is ≤ 8 bytes; otherwise the field holds an 8-byte offset.

### BTF-008 — 8-byte alignment
- Level: MUST · Actor: file · Conformance: BIGTIFF
- Versions: 6.0– · Container: bigtiff · Status: current
- Sources: BTF-010

All out-of-line values must begin at an 8-byte-aligned file offset.

### BTF-009 — New field types (codes 16–18)
- Level: MUST · Actor: file · Conformance: BIGTIFF
- Versions: 6.0– · Container: bigtiff · Status: current
- Sources: BTF-014, BTF-015, BTF-016

16 = LONG8 (64-bit unsigned), 17 = SLONG8 (64-bit signed), 18 = IFD8 (64-bit IFD
offset). These types are invalid in a classic (42) file.

### BTF-010 — 64-bit offset/count tags
- Level: MAY · Actor: file · Conformance: BIGTIFF
- Versions: 6.0– · Container: bigtiff · Status: current
- Sources: BTF-017, BTF-028

StripOffsets (273), StripByteCounts (279), TileOffsets (324) and TileByteCounts
(325) may use LONG8 in addition to their classic types (see tags.yaml; note that
classic TileOffsets is LONG-only despite the BigTIFF document's looser wording).

### BTF-011 — 64-bit IFD-pointer tags
- Level: MAY · Actor: file · Conformance: BIGTIFF
- Versions: 6.0– · Container: bigtiff · Status: current
- Sources: BTF-029, BTF-030

Tags whose values are IFD offsets (e.g. SubIFDs 330) may use IFD8 in addition to
IFD; plain LONG remains valid but writers should not use it.

### BTF-012 — Inherited TIFF 6.0 semantics
- Level: MUST · Actor: both · Conformance: BIGTIFF
- Versions: 6.0– · Container: bigtiff · Status: current
- Sources: BTF-019, BTF-001

Apart from the rules above, a BigTIFF file follows the classic TIFF 6.0
specification in full: all tag semantics, dependencies (DEP-*), image classes,
and compression rules apply unchanged.

### BTF-013 — File extensions
- Level: INFO · Actor: both · Conformance: BIGTIFF
- Versions: 6.0– · Container: bigtiff · Status: current
- Sources: BTF-018, BTF-027

Suggested extensions: `.tif`, `.tf8`, `.btf`. (The document proposes both
`.tf8`/`.btf` only and `.tif`/`.tf8`/`.btf` in different sections; do not reject
a BigTIFF file on the basis of its extension.)

## GEN — General reader, writer and administrative obligations

### GEN-001 — Readers accept both byte orders
- Level: MUST · Actor: reader · Conformance: baseline
- Versions: 4.0– · Container: both · Status: current
- Sources: T6B-058; T5-004, T5-105

TIFF 5.0 said "should" in the body and "must" for Class X readers; 6.0 says
must. Writers may use either order.

### GEN-002 — Defaults apply when a field is absent
- Level: MUST · Actor: reader · Conformance: baseline
- Versions: 4.0– · Container: both · Status: current
- Sources: T6B-075, T6B-056

Readers must assume the default value (tags.yaml `default`) for absent fields;
writers may omit fields whose desired value is the default, and readers must
handle both presence and absence.

### GEN-003 — Unknown fields are skipped
- Level: MUST · Actor: reader · Conformance: baseline
- Versions: 4.0– · Container: both · Status: current
- Sources: T6B-042, T6B-057, T6B-035, T6B-068

Readers must skip gracefully over: optional fields they do not use, fields with
unknown tags (including private tags ≥ 32768), and fields with unexpected or
unknown field types. Readers must never require optional fields to be present.

### GEN-004 — Type checking and integer-type flexibility
- Level: MUST · Actor: reader · Conformance: baseline
- Versions: 6.0– · Container: both · Status: current
- Sources: T6B-032, T6B-034

Readers must verify each field's type against the expected set (tags.yaml
`types`), and should accept any of BYTE/SHORT/LONG for unsigned-integer fields.

### GEN-005 — Graceful failure on unsupported extensions
- Level: MUST · Actor: reader · Conformance: baseline
- Versions: 6.0– · Container: both · Status: current
- Sources: T6B-002, T6B-069

A reader encountering an extension it cannot process (compression scheme, color
space, sample format) must refuse the image with an informative error rather
than misrender it.

### GEN-006 — Private tags and values
- Level: MUST-NOT · Actor: writer · Conformance: baseline
- Versions: 4.0– · Container: both · Status: current
- Sources: T6B-003, T6B-004, T6B-005, T6B-006

Tag codes ≥ 32768 and enumeration values ≥ 32768 are private; writers must not
invent tag numbers outside the registered private range. Large private schemas
should use one registered tag pointing to a private IFD.

### GEN-007 — Multi-subfile obligations
- Level: MUST · Actor: reader · Conformance: baseline
- Versions: 4.0– · Container: both · Status: current
- Sources: T6B-038, T6B-059, T6B-062

Readers must tolerate multiple IFDs but a baseline reader need only process the
first. A reader that uses later subfiles must scan their IFDs before deciding
how to proceed.

### GEN-008 — Baseline options are the reader's burden
- Level: MUST · Actor: reader · Conformance: baseline
- Versions: 6.0– · Container: both · Status: current
- Sources: T6B-055

Wherever baseline TIFF offers a choice (byte order, bit fill order, compression
1/2/32773, etc.), writers choose freely and baseline readers must handle every
option.

### GEN-009 — Editor obligations
- Level: MUST · Actor: writer · Conformance: baseline
- Versions: 6.0– · Container: both · Status: current
- Sources: T6B-063, T6B-064

An editor modifying a full-resolution subfile must regenerate or delete derived
subfiles (e.g. reduced-resolution previews) it does not update. Editors should
not blindly copy fields they do not understand, as those fields may be
invalidated by the edit.

### GEN-010 — Extended TIFF designation
- Level: SHOULD · Actor: writer · Conformance: extension
- Versions: 6.0– · Container: both · Status: current
- Sources: T6B-009, T6B-010

Files using non-baseline features are "Extended TIFF 6.0" files and the
extensions used should be documented; baseline readers are not required to
support any extension.

### GEN-011 — Obsolete revisions remain readable
- Level: MUST · Actor: reader · Conformance: baseline
- Versions: 4.0– · Container: classic · Status: current
- Sources: T6B-001; T5 §Abstract; project policy (README.md)

TIFF 4.0 and 5.0 are obsolete: implementations must still read conforming
4.0/5.0-era files (including retired constructs flagged `Versions: 4.0–4.0` or
`5.0–5.0`), but are not required to write them. Requirements with a closed
version range bind readers only.
