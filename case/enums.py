import enum

# TODO: Add `registry` as sibling dependency
import registry

export = __all__ = registry.Record(lambda cls: cls.__name__)

class NoValue(str, enum.Enum):
    _generate_next_value_ = lambda name, *_: name.lower()

    def __repr__(self) -> str:
        return f'<{self.__class__.__name__}.{self.name}>'

@export
class Case(NoValue):
    LOWER:    str = enum.auto()
    UPPER:    str = enum.auto()
    TITLE:    str = enum.auto()
    SENTENCE: str = enum.auto()
    SNAKE:    str = enum.auto()
    HELTER:   str = enum.auto()
    MACRO:    str = enum.auto()
    FLAT:     str = enum.auto()
    FLUSH:    str = enum.auto()
    CAMEL:    str = enum.auto()
    PASCAL:   str = enum.auto()
    KEBAB:    str = enum.auto()
    TRAIN:    str = enum.auto()
    COBOL:    str = enum.auto()
    DOT:      str = enum.auto()
    PATH:     str = enum.auto()
