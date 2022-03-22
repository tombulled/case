import typing


class Parser(typing.Protocol):
    def parse(self, string: str, /) -> typing.Iterable[str]:
        ...

# class Renderer(typing.Protocol):
#     def render(self, strings: typing.Iterable[str], /) -> str:
#         ...

#     def unrender(self, string: str, /) -> typing.Iterable[str]:
#         ...

#     def match(self, string: str, /) -> bool:
#         ...

class Translator(typing.Protocol):
    def translate(self, strings: typing.Iterable[str], /) -> typing.Iterable[str]:
        ...