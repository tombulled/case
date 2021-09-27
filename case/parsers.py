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
                humps.depascalize(segment).lower().split('_')
                for segment in re.findall \
                (
                    pattern = r'[a-zA-Z0-9]+',
                    string  = string,
                )
            ]
        )
    )
