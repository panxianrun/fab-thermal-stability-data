"""Small consistency check for the staged manuscript data package."""
import csv
import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def rows(name):
    with (ROOT / name).open(encoding="utf-8-sig", newline="") as stream:
        return list(csv.DictReader(stream))


def main():
    fab = rows("processed/fab_binary_320.csv")
    external = rows("processed/igg_binary_129.csv")
    filtered = rows("processed/igg_binary_99_label_conflicts_removed.csv")
    audit = rows("processed/external_overlap_detail.csv")
    drop = {row["seq_key"] for row in audit if row["action_dedup403"] == "drop"}
    assert (len(fab), len(external), len(filtered), len(drop)) == (320, 129, 99, 30)
    assert [row["_seq_key"] for row in filtered] == [
        row["_seq_key"] for row in external if row["_seq_key"] not in drop
    ]
    assert sum(row["binary_class"] == "low" for row in filtered) == 45
    hashes = (ROOT / "SHA256SUMS.txt").read_text(encoding="utf-8").splitlines()
    for line in hashes:
        expected, name = line.split("  ", 1)
        assert hashlib.sha256((ROOT / name).read_bytes()).hexdigest() == expected, name
    print(f"OK: {len(hashes)} checksums; 320 Fab, 129 external, 99 filtered")


if __name__ == "__main__":
    main()
