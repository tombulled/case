import re
import typing

# TODO: Implement
class Parser:
    ...

# TODO: Switch to class-based approach for configuration changes

# TODO: Strip unwanted characters? Make a `strip` function to do this? (sanitise?)
def unflatten(string: str) -> typing.List[str]:
    words: typing.List[str] = []

    current: str
    for current in re.split(r'([A-Z][a-z0-9]*)', string):
        if not current: continue

        if not words or not all(item[-1].isupper() for item in (current, words[-1]) if item):
            words.append(str())

        words[-1] += current

    return words

def parse(string: str) -> typing.List[str]:
    return \
    [
        word
        for segment in re.findall \
        (
            pattern = r'[a-zA-Z0-9]+',
            string  = string,
        )
        for word in unflatten(segment)
    ]
