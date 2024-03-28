"""Application configuration."""

import getpass
from pathlib import Path

import platformdirs


REPO_ROOT_DIR: Path = Path(__file__).parents[1]
REPO_TEST_DIR: Path  = REPO_ROOT_DIR / "tests"

current_user: str = getpass.getuser()

USER_DATA_DIR: Path = Path(platformdirs.user_data_dir(current_user))
