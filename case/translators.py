import typing

from . import models


def translator(hook: typing.Callable, /) -> models.Translator:
    return models.Translator(hook)


@translator
def lower(_: int, string: str, /) -> str:
    return string.lower()


@translator
def upper(_: int, string: str, /) -> str:
    return string.upper()


@translator
def title(_: int, string: str, /) -> str:
    return string.title()


@translator
def capitalize(index: int, string: str, /) -> str:
    return string.title() if index == 0 else string.lower()


@translator
def dromedary(index: int, string: str, /) -> str:
    return string.lower() if index == 0 else string.title()
