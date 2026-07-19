#!/usr/bin/env python3
"""Generate the summary Markdown tables from the canonical YAML files:

    tags.yaml        -> tags.md
    tags-exif.yaml   -> tags-exif.md
    tags-dng.yaml    -> tags-dng.md
    tags-fx.yaml     -> tags-fx.md
    constraints.yaml -> dependencies.md

Usage: python3 tools/generate.py   (requires PyYAML)

The YAML files are canonical; do not edit the generated Markdown by hand.
"""
import os
import yaml

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
REQ = os.path.join(ROOT, "requirements")


def load(name):
    with open(os.path.join(REQ, name)) as f:
        return yaml.safe_load(f)


SUPPLEMENTS = {"PM6", "PS", "TN2", "TN3", "BIGTIFF",
               "EXIF", "DNG", "TFX", "PSFF", "ICC", "IPTC", "LLV", "XMP"}


def version_range(entry):
    since = str(entry.get("since", ""))
    last = entry.get("last")
    if since in SUPPLEMENTS:
        base = f"6.0– ({since})"
    else:
        base = f"{since}–{last if last else ''}"
    if entry.get("supplement_version"):
        base += f" [{entry['supplement_version']}]"
    return base


def gen_tags(tags_doc):
    out = []
    out.append("# Tag registry summary\n")
    out.append("Generated from [tags.yaml](tags.yaml) by `tools/generate.py` — do not edit.\n")
    out.append("Full details (enumerated values, histories, notes) are in the YAML;")
    out.append("per-tag behavioral rules are in [tag-requirements.md](tag-requirements.md).\n")
    out.append("| Code | Hex | Name | Versions | Status | Conformance | Type(s) | Count | Default | Required |")
    out.append("|-----:|-----|------|----------|--------|-------------|---------|-------|---------|----------|")
    for t in tags_doc["tags"]:
        types = ",".join(t["types"])
        if t.get("bigtiff_types"):
            types += " (+" + ",".join(t["bigtiff_types"]) + " in BigTIFF)"
        default = t.get("default")
        default = "—" if default is None else str(default)
        if len(default) > 40:
            default = default[:37] + "..."
        count = str(t.get("count", ""))
        if len(count) > 40:
            count = count[:37] + "..."
        required = t.get("required", "")
        required = {True: "yes", False: "no"}.get(required, str(required))
        out.append(
            f"| {t['code']} | 0x{t['code']:04X} | {t['name']} | {version_range(t)} "
            f"| {t['status']} | {t['conformance']} | {types} | {count} "
            f"| {default} | {required} |"
        )
    out.append("\n## Unadopted draft proposals (colliding codes)\n")
    out.append("| Code | Name | Proposed in | Notes |")
    out.append("|-----:|------|-------------|-------|")
    for t in tags_doc.get("draft_proposals", []):
        note = " ".join(str(t.get("notes", "")).split())
        out.append(f"| {t['code']} | {t['name']} | {t['proposed_in']} | {note} |")
    return "\n".join(out) + "\n"


DOMAIN_TITLES = {
    "tags-exif": ("Exif tag registry summary (Exif / GPS / Interoperability IFDs)",
                  "tags-exif.yaml"),
    "tags-dng": ("DNG tag registry summary", "tags-dng.yaml"),
    "tags-fx": ("TIFF/FX tag registry summary", "tags-fx.yaml"),
}


def gen_domain_tags(stem, tags_doc):
    title, src = DOMAIN_TITLES[stem]
    out = []
    out.append(f"# {title}\n")
    out.append(f"Generated from [{src}]({src}) by `tools/generate.py` — do not edit.")
    out.append("Tag codes are unique per `Location`; full details (values, descriptions,")
    out.append("notes) are in the YAML. Versions in brackets are the supplement's own")
    out.append("version that introduced the tag (e.g. DNG 1.4.0.0, Exif 2.3).\n")
    out.append("| Code | Hex | Name | Location | Versions | Type(s) | Count | Default | Required |")
    out.append("|-----:|-----|------|----------|----------|---------|-------|---------|----------|")
    for t in tags_doc["tags"]:
        types = ",".join(t.get("types") or []) or "—"
        default = t.get("default")
        default = "—" if default is None else str(default)
        count = str(t.get("count") or "")
        if len(count) > 44:
            count = count[:41] + "..."
        required = t.get("required", "")
        required = {True: "yes", False: "no"}.get(required, str(required))
        out.append(
            f"| {t['code']} | 0x{t['code']:04X} | {t['name']} | {t['location']} "
            f"| {version_range(t)} | {types} | {count} | {default} | {required} |"
        )
    return "\n".join(out) + "\n"


def gen_deps(cons_doc):
    out = []
    out.append("# Cross-tag dependency requirements (DEP-*) and class profiles\n")
    out.append("Generated from [constraints.yaml](constraints.yaml) by `tools/generate.py` — do not edit.")
    out.append("The YAML file carries the machine-readable conditions, severities, relaxation")
    out.append("flags and repair actions; this file is the readable index.\n")

    out.append("## Image-class profiles\n")
    for p in cons_doc.get("profiles", []):
        out.append(f"### {p['id']} — {p['title']}")
        out.append(f"- Versions: {p['versions']} · Sources: {', '.join(p['sources'])}")
        out.append(f"- Required tags: {', '.join(str(t) for t in p['required_tags'])}")
        for c in p.get("constraints", []):
            out.append(f"- Constraint: `{c}`")
        out.append("")

    out.append("## Dependency rules\n")
    for r in cons_doc.get("rules", []):
        out.append(f"### {r['id']} — {r['title']}")
        line = (
            f"- Kind: {r['kind']} · Versions: {r['versions']} · "
            f"Conformance: {r['conformance']}"
        )
        if "severity" in r:
            line += f" · Severity: {r['severity']}"
        out.append(line)
        out.append(f"- Tags: {', '.join(str(t) for t in r.get('tags', [])) or '—'}")
        if r.get("when"):
            out.append(f"- When: `{' '.join(str(r['when']).split())}`")
        if r.get("assert"):
            out.append(f"- Assert: `{' '.join(str(r['assert']).split())}`")
        if r.get("semantics"):
            out.append(f"- Semantics: {' '.join(str(r['semantics']).split())}")
        if r.get("relax"):
            out.append(f"- Relaxation: flag `{r['relax']['flag']}` downgrades to {r['relax']['severity']}")
        if r.get("repair"):
            out.append(
                f"- Repair (flag `{r['repair']['flag']}`): "
                + " ".join(str(r["repair"]["action"]).split())
            )
        out.append(f"- Sources: {', '.join(r['sources'])}")
        if r.get("notes"):
            out.append(f"- Notes: {' '.join(str(r['notes']).split())}")
        out.append("")

    out.append("## Standalone vendor-deviation flags\n")
    out.append("| Flag | Concerns | Behavior |")
    out.append("|------|----------|----------|")
    for d in cons_doc.get("deviations", []):
        out.append(
            f"| `{d['flag']}` | {d['concerns']} | "
            + " ".join(str(d["behavior"]).split())
            + " |"
        )
    return "\n".join(out) + "\n"


def main():
    tags_doc = load("tags.yaml")
    cons_doc = load("constraints.yaml")
    with open(os.path.join(REQ, "tags.md"), "w") as f:
        f.write(gen_tags(tags_doc))
    counts = [f"tags.md: {len(tags_doc['tags'])} tags"]
    for stem in DOMAIN_TITLES:
        doc = load(f"{stem}.yaml")
        with open(os.path.join(REQ, f"{stem}.md"), "w") as f:
            f.write(gen_domain_tags(stem, doc))
        counts.append(f"{stem}.md: {len(doc['tags'])}")
    with open(os.path.join(REQ, "dependencies.md"), "w") as f:
        f.write(gen_deps(cons_doc))
    counts.append(f"dependencies.md: {len(cons_doc['profiles'])} profiles, "
                  f"{len(cons_doc['rules'])} rules, {len(cons_doc['deviations'])} deviation flags")
    print("; ".join(counts))


if __name__ == "__main__":
    main()
