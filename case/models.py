import dataclasses
import typing
import parse
import string

from . import abc
from . import protocols


@dataclasses.dataclass
class Translator(protocols.Translator):
    hook: typing.Callable[[int, str], str]

    def __call__(self, strings: typing.Iterable[str], /) -> typing.Iterable[str]:
        return (self.hook(index, string) for index, string in enumerate(strings))


@dataclasses.dataclass(frozen=True)
class Case:
    name: str
    renderer: abc.RendererABC = dataclasses.field(repr=False)
    translators: typing.List[protocols.Translator] = dataclasses.field(
        default_factory=list, repr=False
    )

    def __call__(self, string: str, /) -> str:
        return self.feed(parse.parse(string))

    def style(self, strings: typing.Iterable[str], /) -> str:
        return self.renderer.render(self.translate(strings))

    def match(self, string: str, /) -> bool:
        return self(string) == string

    def translate(self, strings: typing.Iterable[str], /) -> typing.Iterable[str]:
        for translator in self.translators:
            strings = translator(strings)

        return strings


@dataclasses.dataclass(repr=False)
class Renderer(abc.RendererABC):
    prefix: typing.Optional[str] = None
    suffix: typing.Optional[str] = None
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

    def render(self, strings: typing.Iterable[str], /) -> str:
        return "".join(
            (
                self.prefix,
                self.word_sep.join(
                    "".join(
                        (
                            self.word_prefix,
                            self.char_sep.join(
                                "".join(
                                    (
                                        self.char_prefix,
                                        character,
                                        self.char_suffix,
                                    )
                                )
                                for character in string
                            ),
                            self.word_suffix,
                        )
                    )
                    for string in strings
                ),
                self.suffix,
            )
        )

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

        s = lstrip(s, self.prefix)
        s = rstrip(s, self.suffix)

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
