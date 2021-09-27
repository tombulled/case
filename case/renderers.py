from . import parsers

def lower(string: str) -> str:
    return ' '.join(parsers.parse(string)).lower()

def upper(string: str) -> str:
    return lower(string).upper()

def title(string: str) -> str:
    return lower(string).title()

def sentence(string: str) -> str:
    return lower(string).capitalize()

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
