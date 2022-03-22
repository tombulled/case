import dataclasses
import re
import typing
import parse
import string

from typing import Optional

from . import abc
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
    renderer: abc.Renderer = dataclasses.field(repr=False)
    translator: Optional[protocols.Translator] = dataclasses.field(default=None, repr=False)

    def __call__(self, string: str, /) -> str:
        return self.feed(parse.parse(string))

    def feed(self, strings: typing.Iterable[str], /) -> str:
        return self.renderer(self.translator(strings))

    def match(self, string: str, /) -> bool:
        return self(string) == string

@dataclasses.dataclass
class SimpleRenderer(abc.Renderer):
    prefix: str = ''
    suffix: str = ''
    word_prefix: str = ''
    word_suffix: str = ''
    word_sep: str = ''
    character_prefix: str = ''
    character_suffix: str = ''
    character_sep: str = ''

    def render(self, strings: typing.Iterable[str], /) -> str:
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
                        for character in string
                    ),
                    self.word_suffix,
                ))
                for string in strings
            ),
            self.suffix,
        ))

    # Throws RenderException('Cannot unrender')
    def unrender(self, s: str, /) -> typing.Iterable[str]:
        def lstrip(s: str, p: str, /) -> str:
            if not p:
                return s

            assert s.startswith(p)
            
            return s[len(p):]

        def rstrip(s: str, p: str, /) -> str:
            if not p:
                return s

            assert s.endswith(p)
            
            return s[:-len(p)]

        s = lstrip(s, self.prefix)
        s = rstrip(s, self.suffix)

        words = (
            iter(s)
            if not self.word_sep
            else s.split(self.word_sep)
        )

        for word in words:
            word = lstrip(word, self.word_prefix)
            word = rstrip(word, self.word_suffix)

            characters = (
                iter(word)
                if not self.character_sep
                else word.split(self.character_sep)
            )

            unrendered_word = ''

            for character in characters:
                character = lstrip(character, self.character_prefix)
                character = rstrip(character, self.character_suffix)

                assert len(character) == 1 and character in string.ascii_letters

                unrendered_word += character

            # assert len(unrendered_word) > 0
            
            if not unrendered_word:
                continue

            yield unrendered_word
