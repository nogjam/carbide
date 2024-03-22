"""The Python implementation of copy_all_files_with_name.sh."""

from pathlib import Path
import shutil
from typing import Generator


def copy_all_files_with_name(
    name: str, source: str, dest: str
) -> Generator[str, None, None]:
    """Copy all files with the given NAME from SOURCE to DEST as specified."""
    source_path: Path = Path(source)
    dest_path: Path = Path(dest)
    for path in source_path.rglob(name):
        target_path = dest_path / path.relative_to(source_path)
        target_path.parent.mkdir(parents=True, exist_ok=True)
        yield f"Copying {path} -> {target_path}"
        shutil.copy(path, target_path)
