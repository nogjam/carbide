"""Tests for CarbideException and its subclasses."""

import pytest

from carbide.exception import CarbideException


def test_default_message():
    class NoDefaultMessage(CarbideException): ...

    with pytest.raises(
        NotImplementedError, match="NoDefaultMessage does not specify a default message"
    ):
        NoDefaultMessage.with_default_message()

    class DefaultMessageNoFormatFields(CarbideException):
        _default_message = "Plain n simple!"

    with pytest.raises(DefaultMessageNoFormatFields, match="Plain n simple!"):
        raise DefaultMessageNoFormatFields.with_default_message()

    class DefaultMessageWithFormatFields(CarbideException):
        _default_message = "The word is: {word}"

    with pytest.raises(DefaultMessageWithFormatFields, match="The word is: yo"):
        raise DefaultMessageWithFormatFields.with_default_message(word="yo")

    with pytest.raises(DefaultMessageWithFormatFields, match="The word is: {word}"):
        raise DefaultMessageWithFormatFields.with_default_message()
