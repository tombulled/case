import typing
import abc

from . import enums

# TODO: Add `registry` as sibling dependency
import registry

cases = registry.Record()

class BaseCase(abc.ABC):
    case: enums.Case

    # TODO: Register methods as *abstract* methods

    @staticmethod
    def parse(self, string: str) -> typing.List[str]:
        raise NotImplementedError

    @staticmethod
    def render(segments: typing.Iterable[str]) -> str:
        raise NotImplementedError

    @staticmethod
    def match(self, string: str) -> bool:
        raise NotImplementedError

@cases
class Lower(BaseCase):
    case: enums.Case = enums.Case.LOWER

    @staticmethod
    def render(segments: typing.Iterable[str]) -> str:
        return ' '.join(segments).lower()

@cases
class Upper(BaseCase):
    case: enums.Case = enums.Case.UPPER

    @staticmethod
    def render(segments: typing.Iterable[str]) -> str:
        return ' '.join(segments).upper()

@cases
class Title(BaseCase):
    case: enums.Case = enums.Case.TITLE

    @staticmethod
    def render(segments: typing.Iterable[str]) -> str:
        return ' '.join(segments).title()

@cases
class Sentence(BaseCase):
    case: enums.Case = enums.Case.SENTENCE

    @staticmethod
    def render(segments: typing.Iterable[str]) -> str:
        return ' '.join(segments).capitalize()

@cases
class Snake(BaseCase):
    case: enums.Case = enums.Case.SNAKE

    @staticmethod
    def render(segments: typing.Iterable[str]) -> str:
        return '_'.join(segments).lower()

'''
def snake(string: str) -> str:
    return '_'.join(parsers.parse(string)).lower()

def helter(string: str) -> str:
    return snake(string).title()

def macro(string: str) -> str:
    return snake(string).upper()

def kebab(string: str) -> str:
    return '-'.join(parsers.parse(string)).lower()

def train(string: str) -> str:
    return kebab(string).title()

def cobol(string: str) -> str:
    return kebab(string).upper()

def flat(string: str) -> str:
    return ''.join(parsers.parse(string)).lower()

def flush(string: str) -> str:
    return flat(string).upper()

def pascal(string: str) -> str:
    return ''.join(segment.capitalize() for segment in parsers.parse(string))

def camel(string: str) -> str:
    return ''.join \
    (
        segment
        for first_segment, *segments in (parsers.parse(string),)
        for segment in \
        (
            first_segment,
            * map(str.capitalize, segments),
        )
    )

def dot(string: str) -> str:
    return '.'.join(parsers.parse(string)).lower()

def path(string: str) -> str:
    return '/'.join(parsers.parse(string)).lower()
'''
