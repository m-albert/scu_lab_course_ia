#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
tmp_dir="$(mktemp -d)"
out_dir="$repo_root/_build/html/myst"

cleanup() {
  rm -rf "$tmp_dir"
}
trap cleanup EXIT

mkdir -p "$tmp_dir/notebooks/lite"
cp "$repo_root/myst.yml" "$tmp_dir/myst.yml"
cp "$repo_root/.logo.svg" "$tmp_dir/.logo.svg"
cp "$repo_root/notebooks/lite/python_basics_lite.md" "$tmp_dir/notebooks/lite/python_basics_lite.md"

python - "$tmp_dir/favicon.ico" <<'PY'
import struct
import sys

path = sys.argv[1]
size = 16
bgra = bytearray()

for y in range(size - 1, -1, -1):
    for x in range(size):
        on_diagonal = x == y or x == size - y - 1
        in_center = 4 <= x <= 11 and 4 <= y <= 11
        if on_diagonal or in_center:
            r, g, b, a = 30, 90, 150, 255
        else:
            r, g, b, a = 255, 255, 255, 0
        bgra.extend((b, g, r, a))

and_mask = b"\x00\x00\x00\x00" * size
bitmap_info_header = struct.pack(
    "<IIIHHIIIIII",
    40,
    size,
    size * 2,
    1,
    32,
    0,
    len(bgra),
    0,
    0,
    0,
    0,
)
image = bitmap_info_header + bgra + and_mask
header = struct.pack("<HHH", 0, 1, 1)
entry = struct.pack("<BBBBHHII", size, size, 0, 0, 1, 32, len(image), 22)

with open(path, "wb") as handle:
    handle.write(header + entry + image)
PY

base_url="${MYST_BASE_URL:-/myst}"
(
  cd "$tmp_dir"
  BASE_URL="$base_url" myst build --html
)

rm -rf "$out_dir"
mkdir -p "$out_dir"
cp -R "$tmp_dir/_build/html/." "$out_dir/"
