import typing
import pytest

from case import renderers


@pytest.fixture
def strings() -> typing.Iterable[str]:
    return ("foo", "bar")


def test_space(strings: typing.Iterable[str]) -> None:
    assert renderers.space(strings) == "foo bar"


def test_concatenate(strings: typing.Iterable[str]) -> None:
    assert renderers.concatenate(strings) == "foobar"


def test_underscore(strings: typing.Iterable[str]) -> None:
    assert renderers.underscore(strings) == "foo_bar"


def test_hyphen(strings: typing.Iterable[str]) -> None:
    assert renderers.hyphen(strings) == "foo-bar"


def test_period(strings: typing.Iterable[str]) -> None:
    assert renderers.period(strings) == "foo.bar"


def test_slash(strings: typing.Iterable[str]) -> None:
    assert renderers.slash(strings) == "foo/bar"
