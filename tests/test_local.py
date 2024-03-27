"""Tests for the carbide.local module."""

from carbide.local import LocalDataStore


def test_local_data_store():
    store: LocalDataStore = LocalDataStore()
