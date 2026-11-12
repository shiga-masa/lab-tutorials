#!/usr/bin/env python3
"""Build the release zips (one per course folder, plus one with everything).

Course folders are the top-level directories whose names do not start with ".".
Zip names are fixed because the README links to
https://github.com/shiga-masa/lab-tutorials/releases/latest/download/<name>.

  lab-tutorials_<course>.zip : lab-tutorials_<course>/ + course contents + common files
  lab-tutorials_all.zip      : lab-tutorials/ + all course folders + common files

Reproducible: entries are sorted, timestamps are the HEAD commit time (or
SOURCE_DATE_EPOCH), permissions are fixed. File names are stored as UTF-8 with
the language-encoding flag (bit 11) set, which Python's zipfile does
automatically for non-ASCII names.

Usage: python3 .github/scripts/build_release_zips.py --out dist/
"""
import argparse
import os
import subprocess
import sys
import time
import unicodedata
import zipfile
from pathlib import Path

COMMON_FILES = ["README.md", "LICENSE", "LICENSE-CC-BY-4.0"]
REPO_ROOT = Path(__file__).resolve().parents[2]


def commit_time() -> int:
    env = os.environ.get("SOURCE_DATE_EPOCH")
    if env:
        return int(env)
    try:
        out = subprocess.run(
            ["git", "-C", str(REPO_ROOT), "log", "-1", "--format=%ct"],
            check=True, capture_output=True, text=True,
        ).stdout.strip()
        return int(out)
    except (subprocess.CalledProcessError, FileNotFoundError, ValueError) as e:
        sys.exit(f"ERROR: cannot determine commit time (set SOURCE_DATE_EPOCH): {e}")


def list_files(folder: Path) -> list[Path]:
    """All regular files under folder, sorted by relative path."""
    files = []
    for dirpath, dirnames, filenames in os.walk(folder):
        dirnames.sort()
        for name in sorted(filenames):
            p = Path(dirpath) / name
            if p.is_symlink() or not p.is_file():
                sys.exit(f"ERROR: unsupported entry (symlink or special file): {p}")
            files.append(p)
    return sorted(files, key=lambda p: p.relative_to(folder).as_posix())


def write_zip(zip_path: Path, entries: list[tuple[Path, str]], ts: int) -> None:
    """entries: (source file, archive name). Names must be unique."""
    names = [a for _, a in entries]
    assert len(names) == len(set(names)), f"duplicate archive names in {zip_path}"
    date_time = time.gmtime(max(ts, 315532800))[:6]  # zip cannot store < 1980
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for src, arcname in entries:
            zi = zipfile.ZipInfo(arcname, date_time)  # sets 0x800 for non-ASCII names
            zi.compress_type = zipfile.ZIP_DEFLATED
            zi.create_system = 3  # Unix
            zi.external_attr = (0o100644 & 0xFFFF) << 16
            zf.writestr(zi, src.read_bytes(), compresslevel=9)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--out", required=True, help="output directory (e.g. dist/)")
    args = ap.parse_args()

    out = Path(args.out).resolve()
    out.mkdir(parents=True, exist_ok=True)
    ts = commit_time()

    for f in COMMON_FILES:
        if not (REPO_ROOT / f).is_file():
            sys.exit(f"ERROR: common file missing: {f}")

    courses = sorted(
        p.name for p in REPO_ROOT.iterdir()
        if p.is_dir() and not p.name.startswith(".") and p.resolve() != out
    )
    if not courses:
        sys.exit("ERROR: no course folders found")
    print(f"course folders ({len(courses)}): {', '.join(courses)}")
    print(f"timestamp: {time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(ts))} UTC")

    common = [(REPO_ROOT / f, f) for f in COMMON_FILES]
    jobs = []  # (zip name, entries, expected file count)
    all_entries = []
    for c in courses:
        files = list_files(REPO_ROOT / c)
        course_entries = [(p, f"{c}/{p.relative_to(REPO_ROOT / c).as_posix()}") for p in files]
        all_entries += course_entries
        top = f"lab-tutorials_{c}"
        # Contents of the course folder sit directly under the top-level folder.
        entries = [(p, f"{top}/{p.relative_to(REPO_ROOT / c).as_posix()}") for p in files]
        # The course folder has its own README.md, which would collide with the
        # repository README.md; the course README keeps its name and the
        # repository one is stored as README_repository.md.
        taken = {a for _, a in entries}
        for p, a in common:
            arc = f"{top}/{a}"
            if arc in taken:
                if a != "README.md":
                    sys.exit(f"ERROR: {c}/{a} collides with the common file {a}")
                arc = f"{top}/README_repository.md"
                print(f"note: {c}/README.md exists; repository README.md stored as README_repository.md")
            entries.append((p, arc))
        jobs.append((f"{top}.zip", entries, len(files) + len(common)))
    entries = [(p, f"lab-tutorials/{a}") for p, a in all_entries + common]
    jobs.append(("lab-tutorials_all.zip", entries, len(all_entries) + len(common)))

    # A course file named like a common file would collide; write_zip asserts uniqueness.
    failed = 0
    for name, entries, expected in jobs:
        zip_path = out / name
        write_zip(zip_path, sorted(entries, key=lambda e: e[1]), ts)
        with zipfile.ZipFile(zip_path) as zf:
            infos = zf.infolist()
            n = len(infos)
            bad_flag = [i.filename for i in infos
                        if not i.filename.isascii() and not i.flag_bits & 0x800]
            if zf.testzip() is not None:
                print(f"ERROR: corrupt zip {name}")
                failed += 1
        size = zip_path.stat().st_size
        status = "OK" if n == expected and not bad_flag else "MISMATCH"
        print(f"{name}: {n} files (expected {expected}), {size:,} bytes [{status}]")
        if n != expected:
            failed += 1
        if bad_flag:
            print(f"ERROR: {len(bad_flag)} names lack the UTF-8 flag in {name}")
            failed += 1

    print(f"done: {len(jobs)} zips, {failed} failure(s)")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
