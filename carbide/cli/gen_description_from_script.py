"""For automatically getting help text from corresponding shell scripts, if
they exist.
"""

from pathlib import Path
import re
from warnings import warn

from carbide.config import REPO_ROOT_DIR


EXPECTED_VAR_NAME: str = "DESCRIPTION"


def gen_description_from_script(script: Path | str) -> str | None:
    """Returns the help text defined by the variable named "DESCRIPTION" in the
    specified shell script. Returns None if no corresponding script is found.

    Args:
        script: Name or path to the script.
    """
    if isinstance(script, str):
        script = REPO_ROOT_DIR / "scripts" / script

    if not script.exists():
        return

    description: str | None = None
    with open(script, encoding="utf-8") as f:
        for line in f.readlines():
            if re.match(rf"^{EXPECTED_VAR_NAME}=", line):
                description = line.split("=")[1].strip('\n "')
                break
        else:
            warn(f"Found no {EXPECTED_VAR_NAME} in {script}")

    return description
