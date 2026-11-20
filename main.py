"""Copy the pre-rendered news image to the output directory.

Standard library only, no network. The image is deterministic: every run
writes the exact same bytes.
"""

import os
import shutil
from pathlib import Path


def main() -> None:
    here = Path(__file__).resolve().parent
    source = here / "entry.png"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.png"
    shutil.copyfile(source, target)
    # Guard: the copy must be byte-identical to the source.
    if target.stat().st_size != source.stat().st_size:
        raise SystemExit("entry.png copy size mismatch")
    print(f"Wrote {target} ({target.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
