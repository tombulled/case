import enum

class StrEnum(str, enum.Enum):
    def __repr__(self) -> str:
        return super().__repr__()

class Separator(StrEnum):
    SPACE:      str = ' '
    NONE:       str = ''
    UNDERSCORE: str = '_'
    HYPHEN:     str = '-'
    PERIOD:     str = '.'
    SLASH:      str = '/'
