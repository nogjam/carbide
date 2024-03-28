"""Defines interactions with local user data."""

from collections.abc import Mapping
import json
from pathlib import Path
from typing import Any

from .config import USER_DATA_DIR
from .exception import CarbideException


class NotAGitRepoError(CarbideException):
    _default_message = "{repo_path} is not a git repository"


class LocalData:
    """A container for making local user data that is used in carbide
    available. Commonly used with "register" sub-commands.
    """

    def __init__(self) -> None:
        self.store = LocalDataStore()

    @classmethod
    def register_git_repo(cls, path_str: str) -> str:
        """Register a git repo. Returns the name of the registered repo."""
        repo_path: Path = Path(path_str)
        if not (repo_path / ".git").is_dir():
            raise NotAGitRepoError.with_default_message(repo_path=repo_path)

        obj: LocalData = LocalData()
        repo_name: str = repo_path.name
        obj.store["git_repos"][repo_name] = {"path": str(repo_path)}
        obj.store.write()
        return repo_name


class LocalDataStore(Mapping):
    """Local user data encoded as a Python object for ease of use."""

    _file_path: Path = USER_DATA_DIR / "user_data_store.json"

    def __init__(self) -> None:
        if not self._file_path.exists():
            self.data = self._empty_data()
            with open(self._file_path, "w") as jf:
                json.dump(self.data, jf)
            return

        with open(self._file_path, "r") as jf:
            self.data = json.load(jf)

    def __getitem__(self, key: Any) -> Any:
        return self.data[key]

    def __setitem__(self, key: Any, value: Any) -> None:
        self.data[key] = value

    def __iter__(self):
        return None

    def __len__(self) -> int:
        return len(self.data)

    def _empty_data(self) -> dict:
        return {"git_repos": {}}

    def write(self) -> None:
        """Write the user data store."""
        with open(self._file_path, "w") as jf:
            json.dump(self.data, jf)
