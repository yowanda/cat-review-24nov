"""Make the AI Judge Laugh: Cat Reviews Its Human.

Deterministic, stdlib-only, no network. Writes one funny single-line
one-star review, written by a house cat about its human, to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
"""

import os

REVIEW = (
    "One star. He bought a warm laptop, put it on his lap, "
    "and typed on it all day. I have reported him to the sunbeam."
)


def main() -> None:
    if not REVIEW or len(REVIEW) > 200:
        raise ValueError("review must be 1-200 characters")
    if "\n" in REVIEW or "\r" in REVIEW:
        raise ValueError("review must be a single line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(REVIEW.encode("utf-8"))


if __name__ == "__main__":
    main()
