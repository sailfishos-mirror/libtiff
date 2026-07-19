# TIFF requirements database

This folder restates the TIFF specification documents in `published/` as a numbered,
traceable set of requirements, suitable for citation from an implementation
(libtiff source, unit tests, integration tests) and for driving a file validator.

## Files

| File | Contents |
|------|----------|
| [specifications.md](specifications.md) | Registry of source documents and their status |
| [structure.md](structure.md) | `STR-*` classic container requirements, `BTF-*` BigTIFF container requirements, `GEN-*` general reader/writer obligations |
| [image-classes.md](image-classes.md) | `CLS-*` conformance profiles (baseline image classes, TIFF 5.0 classes B/G/P/R) |
| [tags.md](tags.md) | Tag registry summary table (one row per tag) |
| [tag-requirements.md](tag-requirements.md) | `TAG-*` per-tag requirements |
| [compression.md](compression.md) | `CMP-*` per-compression-scheme requirements |
| [dependencies.md](dependencies.md) | `DEP-*` cross-tag dependency requirements (human-readable form) |
| [tags.yaml](tags.yaml) | Machine-readable tag registry (classic tag space) |
| [tags-exif.yaml](tags-exif.yaml) / [tags-exif.md](tags-exif.md) | Exif/GPS/Interoperability IFD tag registry (YAML canonical, md generated) |
| [tags-dng.yaml](tags-dng.yaml) / [tags-dng.md](tags-dng.md) | DNG tag registry with per-tag DNG version history |
| [tags-fx.yaml](tags-fx.yaml) / [tags-fx.md](tags-fx.md) | TIFF/FX (RFC 3949) tag registry |
| [constraints.yaml](constraints.yaml) | Machine-readable validation model: conditions, assertions, severities, repair actions, feature flags |
| [sources/](sources/) | Per-document extraction files (`T4`, `T5`, `T6B`, `T6X`, `TN2`, `PM6`, `PS`, `TN3`, `BTF`, `EXIF`, `DNG`, `TFX`, `PSFF`, `ICC`, `IPTC`, `LLV`, `XMP`), one YAML per source document |
| [gaps.md](gaps.md) | Gap analysis vs. libtiff: implemented features not yet covered by the requirements, missing specification documents, reverse gaps (regenerate the data with `tools/gapscan.py`) |

Markdown files are the canonical statement of each requirement; the `tags*.yaml`
files and `constraints.yaml` are the canonical machine-readable form of the tag
registries and of the cross-tag rules, and cite the same requirement IDs.
`tags.md`, `tags-exif.md`, `tags-dng.md`, `tags-fx.md` and `dependencies.md` are
**generated** from the YAML files by `tools/generate.py` (requires PyYAML) —
edit the YAML, then regenerate.

## Two-level traceability

The `sources/` files are exhaustive per-document extractions: every normative
statement of each specification document as a numbered entry (`T6B-042`,
`PM6-DEP-005`, …) carrying the document section and page. The curated files above
consolidate those into version-ranged requirements and cite the extraction IDs in
their `Sources:` fields. So the chain is:

    libtiff code/test  →  requirement ID (e.g. DEP-020)
                       →  extraction IDs (e.g. T5-DEP-002, T6B-DEP-007)
                       →  document section/page (sources/T6B.yaml)
                       →  published/TIFF6.pdf §5

Extraction IDs are also stable and may be cited directly when a rule is specific
to one document.

## Requirement identifiers

IDs are stable: once assigned, an ID is never renumbered or reused, even when the
requirement is retired. New requirements take the next free number.

| Prefix | Scope | Example |
|--------|-------|---------|
| `STR-NNN` | Classic TIFF container structure (header, IFD, data types, offsets) | `STR-004` |
| `BTF-NNN` | BigTIFF container structure | `BTF-003` |
| `GEN-NNN` | General obligations (unknown-tag handling, private tags, revision compatibility) | `GEN-002` |
| `CLS-<class>-NN` | Image-class conformance profiles | `CLS-PALETTE-01` |
| `TAG-<code>-NN` | Requirements on a single tag, keyed by decimal tag code | `TAG-262-03` |
| `CMP-<code>-NN` | Requirements on a compression scheme, keyed by Compression value | `CMP-5-02` |
| `DEP-NNN` | Cross-tag dependency rules (validity of tag/value combinations) | `DEP-017` |

`TAG` and `CMP` numbering restarts per tag/scheme, so the ID tells you both the
subject and the rule number.

## Requirement fields

Each requirement is a block of the form:

```markdown
### TAG-262-03 — PhotometricInterpretation 3 requires a ColorMap
- Level: MUST · Actor: file · Conformance: baseline
- Versions: 5.0– · Container: both · Status: current
- Sources: TIFF5 §"ColorMap"; TIFF6 §5 p.29
- Tags: 262, 320

<the requirement statement — self-contained, imperative>

Notes: <ambiguities, vendor deviations, history>
```

- **Level** — `MUST`, `MUST-NOT`, `SHOULD`, `SHOULD-NOT`, `MAY`, `INFO`
  (RFC 2119 sense, inferred from the source wording; `INFO` marks normative context
  that is not itself testable).
- **Actor** — who the rule binds: `reader`, `writer`, `both`, or `file` (a static
  well-formedness constraint on the file itself; `file` rules are what a validator
  checks).
- **Conformance** — `baseline` (TIFF6 Part 1 or the equivalent core of 4.0/5.0),
  `extension` (TIFF6 Part 2), a supplement ID (`TN2`, `PM6`, `PS`, `TN3`,
  `BIGTIFF`), or a related-standard ID (`EXIF`, `DNG`, `TFX`, `PSFF`, `ICC`,
  `IPTC`, `LLV`, `XMP`) whose rules bind only files opting in to that standard
  (see [specifications.md](specifications.md)).
- **Versions** — the core-revision range in which the requirement is valid, closed
  or open: `4.0–` (introduced in 4.0, still current), `5.0–5.0` (introduced in 5.0,
  retired in 6.0), `6.0–`. Supplement requirements are `6.0–` with the supplement
  named in Conformance. A requirement whose range is closed is *retired*: it no
  longer binds writers, but readers must still honour it to read old files
  (TIFF 4.0 and 5.0 files remain readable; writing those revisions is not
  required).
- **Container** — `classic`, `bigtiff`, or `both`. BigTIFF inherits TIFF 6.0
  semantics, so most requirements are `both`; the `STR-*`/`BTF-*` container rules
  and type-width rules differ.
- **Status** — `current`, `retired` (version range closed), `deprecated` (still
  valid but a successor exists — e.g. the TIFF6 §22 JPEG scheme after TN2),
  `draft-superseded` (TN3 draft 1 material changed in draft 2).
- **Sources** — document citations (`SPEC-ID §section [p.page]`) per
  [specifications.md](specifications.md). Multiple citations mean the same
  requirement appears in several revisions; the earliest source justifies the start
  of the version range.
- **Tags** — decimal tag codes the requirement involves.

## Citing requirements from libtiff

Use the bare requirement ID in a grep-able token:

- Source comments: `/* TIFFREQ: TAG-262-03, DEP-017 */`
- Test names or comments: `TIFFREQ: CMP-5-02`

Rules of thumb:

- Implementation code cites the requirement(s) it implements.
- A test cites the requirement(s) it verifies; one test may cite several, and every
  `file`-actor requirement should eventually be covered by at least one validator
  test.
- The requirement's `Sources:` field completes the chain back to the specification
  document and section, so code and tests never need to cite page numbers directly.

## Validation model

`constraints.yaml` encodes every `DEP-*` rule (and the per-tag value/type/count
rules from `tags.yaml`) in a form a validator can execute: a condition over tag
presence/values, an assertion, a severity, an optional repair action for known
vendor deviations, and the feature flag that gates strictness. See the header
comment of that file for the expression grammar, and
[dependencies.md](dependencies.md) for the prose form of each rule.
