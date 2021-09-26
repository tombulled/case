import re
import typing
import itertools

import humps

def parse(string: str) -> typing.List[str]:
    return list \
    (
        itertools.chain \
        (
            * \
            [
                humps.depascalize(segment).split('_')
                for segment in re.findall \
                (
                    pattern = r'[a-zA-Z0-9]+',
                    string  = string,
                )
            ]
        )
    )

def snake(string: str) -> str:
    return '_'.join(parse(string)).lower()

def macro(string: str) -> str:
    return snake(string).upper()

def kebab(string: str) -> str:
    return '-'.join(parse(string)).lower()

def train(string: str) -> str:
    return kebab(string).title()

def cobol(string: str) -> str:
    return kebab(string).upper()
