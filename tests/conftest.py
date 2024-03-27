"""Pytest configuration. Ref.
https://docs.pytest.org/en/7.1.x/reference/fixtures.html#conftest-py-sharing-fixtures-across-multiple-files
"""

from carbide import config

# Patch the user data directory to point to a test location instead of the real
# one.
config.USER_DATA_DIR = config.REPO_ROOT_DIR / "tests" / "temp"
config.USER_DATA_DIR.mkdir(exist_ok=True)
