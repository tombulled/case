import abc
import parse
import typing


class Case(abc.ABC):
    style: typing.Optional[str] = None

    def __init__(self, style: typing.Optional[str] = None) -> None:
        if style is not None:
            self.style = style
        elif self.style is None:
            self.style = type(self).__name__.lower()

    def __repr__(self) -> str:
        return f"Case(style={self.style!r})"

    def __call__(self, string: str, /) -> str:
        return self.feed(self.parse(string))

    @abc.abstractmethod
    def render(self, strings: typing.Iterable[str], /) -> str:
        raise NotImplementedError

    @staticmethod
    def translate(strings: typing.Iterable[str], /) -> typing.Iterable[str]:
        return strings

    @staticmethod
    def parse(string: str, /) -> typing.Iterable[str]:
        return parse.parse(string)

    def feed(self, strings: typing.Iterable[str], /) -> str:
        return self.render(self.translate(strings))

    def match(self, string: str, /) -> bool:
        return self(string) == string
