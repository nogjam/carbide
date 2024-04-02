from pathlib import Path

import pytest

from carbide.cli.gen_description_from_script import (
    EXPECTED_VAR_NAME,
    gen_description_from_script,
)
from carbide.config import REPO_ROOT_DIR, REPO_TEST_DIR


def test_named_script_parameter():
    # This should be something we're sure exists in the actual scripts/ dir.
    name: str = "copy_all_files_with_name.sh"
    result = gen_description_from_script(name)
    expected = (
        "Copy all files with the given name from source to destination as specified."
    )
    assert result == expected


def test_path_script_parameter():
    script_path: Path = REPO_TEST_DIR / "data" / "script_with_description.sh"
    result = gen_description_from_script(script_path)
    expected = "This is my description, y'all."
    assert result == expected


def test_warns_of_no_description():
    script = REPO_TEST_DIR / "data" / "empty_script.sh"
    with pytest.warns(UserWarning, match=f"Found no {EXPECTED_VAR_NAME} in "):
        result = gen_description_from_script(script)
    assert result is None
