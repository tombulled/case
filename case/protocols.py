import typing


class Parser(typing.Protocol):
    def parse(self, string: str, /) -> typing.Iterable[str]:
        ...

class Renderer(typing.Protocol):
    def render(self, strings: typing.Iterable[str], /) -> str:
        ...

class Translator(typing.Protocol):
    def translate(self, strings: typing.Iterable[str], /) -> typing.Iterable[str]:
        ...