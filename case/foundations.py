import abc
import random
import typing
import dataclasses

from . import base

# Note: Rename -> components, blocks, mixins

### Separators, Delimiters

@dataclasses.dataclass(repr=False, frozen=True)
class Separated(base.Case):
    sep: str

    def render(self, segments: typing.Iterable[str]):
        return self.sep.join(segments)

@dataclasses.dataclass(repr=False, frozen=True)
class SpaceSeparated(Separated):
    sep: str = ' '

@dataclasses.dataclass(repr=False, frozen=True)
class UnderscoreSeparated(Separated):
    sep: str = '_'

@dataclasses.dataclass(repr=False, frozen=True)
class HyphenSeparated(Separated):
    sep: str = '-'

@dataclasses.dataclass(repr=False, frozen=True)
class DotSeparated(Separated):
    sep: str = '.'

@dataclasses.dataclass(repr=False, frozen=True)
class SlashSeparated(Separated):
    sep: str = '/'

@dataclasses.dataclass(repr=False, frozen=True)
class NotSeparated(Separated):
    sep: str = ''

### Translators

class Translatable(base.Case):
    @staticmethod
    @abc.abstractmethod
    def translate(string: str) -> str:
        raise NotImplementedError

    @classmethod
    def prepare(cls, segments: typing.Iterable[str]) -> typing.Iterable[str]:
        return [cls.translate(segment) for segment in segments]

class Lower(Translatable):
    @staticmethod
    def translate(string: str) -> str:
        return string.lower()

class Upper(Translatable):
    @staticmethod
    def translate(string: str) -> str:
        return string.upper()

class Title(Translatable):
    @staticmethod
    def translate(string: str) -> str:
        return string.title()

class Inverse(Translatable):
    @staticmethod
    def translate(string: str) -> str:
        return string.swapcase()

### Preparators

class Capitalize(base.Case):
    @staticmethod
    def prepare(segments: typing.Iterable[str]) -> typing.Iterable[str]:
        first_segment, *remaining_segments = segments

        return \
        [
            first_segment.title(),
            * \
            [
                segment.lower()
                for segment in remaining_segments
            ],
        ]

class Alternating(base.Case):
    @staticmethod
    def prepare(segments: typing.Iterable[str]) -> typing.Iterable[str]:
        return \
        [
            ''.join \
            (
                (
                    str.lower,
                    str.upper,
                ) \
                [
                    (
                        sum \
                        (
                            len(previous_segment)
                            for previous_segment in segments[:segment_index]
                        )
                        + character_index
                    )
                    % 2
                ](character)
                for character_index, character in enumerate(segment)
            )
            for segment_index, segment in enumerate(segments)
        ]

class Random(base.Case):
    @staticmethod
    def prepare(segments: typing.Iterable[str]) -> typing.Iterable[str]:
        return \
        [
            ''.join \
            (
                random.choice \
                (
                    (
                        str.lower,
                        str.upper,
                    ),
                )(character)
                for character in segment
            )
            for segment in segments
        ]

class Dromedary(base.Case):
    @staticmethod
    def prepare(segments: typing.Iterable[str]) -> typing.Iterable[str]:
        first_segment, *remaining_segments = segments

        return \
        [
            first_segment.lower(),
            * \
            [
                segment.title()
                for segment in remaining_segments
            ],
        ]
