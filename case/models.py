import dataclasses
import typing
import parse

from typing import Optional

from . import protocols

@dataclasses.dataclass
class Character:
    value: str
    index: int = 0
    offset: int = 0

@dataclasses.dataclass
class Word:
    value: str
    index: int = 0
    offset: int = 0
    
    def __iter__(self) -> typing.Iterable[Character]:
        index: int
        character: str
        for index, character in enumerate(self.value):
            yield Character(
                value=character,
                index=index,
                offset=self.offset+index,
            )

@dataclasses.dataclass(frozen=True)
class Case:
    name: str
    renderer: protocols.Renderer = dataclasses.field(repr=False)
    translator: Optional[protocols.Translator] = dataclasses.field(default=None, repr=False)

    def __call__(self, string: str, /) -> str:
        return self.feed(parse.parse(string))

    def feed(self, strings: typing.Iterable[str], /) -> str:
        return self.renderer(self.translator(strings))

    def match(self, string: str, /) -> bool:
        return self(string) == string

@dataclasses.dataclass
class Renderer:
    prefix: str = ''
    suffix: str = ''
    word_prefix: str = ''
    word_suffix: str = ''
    word_sep: str = ''
    character_prefix: str = ''
    character_suffix: str = ''
    character_sep: str = ''

    def __call__(self, words: typing.Iterable[str], /) -> str:
        return ''.join((
            self.prefix,
            self.word_sep.join(
                ''.join((
                    self.word_prefix,
                    self.character_sep.join(
                        ''.join((
                            self.character_prefix,
                            character,
                            self.character_suffix,
                        ))
                        for character in word
                    ),
                    self.word_suffix,
                ))
                for word in words
            ),
            self.suffix,
        ))