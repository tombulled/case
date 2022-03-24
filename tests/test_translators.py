import pytest
import typing

from case import translators


@pytest.fixture
def strings() -> typing.Iterable[str]:
    return ("fOO", "BaR")


def test_lower(strings: typing.Iterable[str]) -> None:
    assert list(translators.lower(strings)) == ["foo", "bar"]


def test_upper(strings: typing.Iterable[str]) -> None:
    assert list(translators.upper(strings)) == ["FOO", "BAR"]


def test_title(strings: typing.Iterable[str]) -> None:
    assert list(translators.title(strings)) == ["Foo", "Bar"]


def test_capitalize(strings: typing.Iterable[str]) -> None:
    assert list(translators.capitalize(strings)) == ["Foo", "bar"]


def test_dromedary(strings: typing.Iterable[str]) -> None:
    assert list(translators.dromedary(strings)) == ["foo", "Bar"]