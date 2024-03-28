"""Defines the base class for carbide-originating exceptions."""


class CarbideException(Exception):
    """Base class for carbide-originating exceptions."""

    _default_message: str | None = None

    @classmethod
    def with_default_message(cls, **format_fields):
        if cls._default_message is None:
            raise NotImplementedError(
                f"{cls.__name__} does not specify a default message"
            )
        return cls(
            cls._default_message.format_map(format_fields)
            if format_fields
            else cls._default_message
        )
