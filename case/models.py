import dataclasses
import string
import typing

import parse

from . import abc, protocols


@dataclasses.dataclass
class Translator(protocols.Translator):
    hook: typing.Callable[[int, str], str]

    def __call__(self, strings: typing.Iterable[str], /) -> typing.Iterable[str]:
        return (self.hook(index, string) for index, string in enumerate(strings))


@dataclasses.dataclass(frozen=True)
class Case:
    name: str
    renderer: abc.RendererABC = dataclasses.field(repr=False)
    translator: typing.Optional[protocols.Translator] = dataclasses.field(
        default=None, repr=False
    )
    parser: protocols.Parser = parse.parse

    def __call__(self, string: str, /) -> str:
        return self.feed(self.parser(string))

    def feed(self, strings: typing.Iterable[str], /) -> typing.Iterable[str]:
        if self.translator is not None:
            strings = self.translator(strings)

        return self.renderer.render(strings)

    def style(self, strings: typing.Iterable[str], /) -> str:
        return "".join(self.feed(strings))

    def match(self, string: str, /) -> bool:
        return self(string) == string


@dataclasses.dataclass(repr=False)
class Renderer(abc.RendererABC):
    word_prefix: typing.Optional[str] = None
    word_suffix: typing.Optional[str] = None
    word_sep: typing.Optional[str] = None
    char_prefix: typing.Optional[str] = None
    char_suffix: typing.Optional[str] = None
    char_sep: typing.Optional[str] = None

    def __repr__(self) -> str:
        return "{cls}({attrs})".format(
            cls=type(self).__name__,
            attrs=", ".join(
                f"{key}={val!r}"
                for key, val in self.__dict__.items()
                if val is not None
            ),
        )

    def render(self, strings: typing.Iterable[str], /) -> typing.Iterable[str]:
        word_prefix: str = self.word_prefix or ""
        word_suffix: str = self.word_suffix or ""
        word_sep: str = self.word_sep or ""

        char_prefix: str = self.char_prefix or ""
        char_suffix: str = self.char_suffix or ""
        char_sep: str = self.char_sep or ""

        index: int
        string: str
        for index, string in enumerate(strings):
            word: str = "".join(
                (
                    word_prefix,
                    char_sep.join(
                        "".join(
                            (
                                char_prefix,
                                character,
                                char_suffix,
                            )
                        )
                        for character in string
                    ),
                    word_suffix,
                )
            )

            if index == 0:
                yield word

            else:
                yield f"{word_sep}{word}"

    # Throws RenderException('Cannot unrender')
    def unrender(self, s: str, /) -> typing.Iterable[str]:
        def lstrip(s: str, p: str, /) -> str:
            if not p:
                return s

            assert s.startswith(p)

            return s[len(p) :]

        def rstrip(s: str, p: str, /) -> str:
            if not p:
                return s

            assert s.endswith(p)

            return s[: -len(p)]

        words = iter(s) if not self.word_sep else s.split(self.word_sep)

        for word in words:
            word = lstrip(word, self.word_prefix)
            word = rstrip(word, self.word_suffix)

            characters = iter(word) if not self.char_sep else word.split(self.char_sep)

            unrendered_word = ""

            for character in characters:
                character = lstrip(character, self.char_prefix)
                character = rstrip(character, self.char_suffix)

                assert len(character) == 1 and character in string.ascii_letters

                unrendered_word += character

            assert len(unrendered_word) > 0

            # if not unrendered_word:
            #     continue

            yield unrendered_word
