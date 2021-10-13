import io
import typing
import types
# import itertools

def compose(*functions: typing.Callable):
    def wrapper(*args, **kwargs):
        response: typing.Any = None

        for index, function in enumerate(functions):
            response = \
            (
                function(*args, **kwargs)
                if not index
                else function(response)
            )

        return response

    return wrapper

def identity(x: typing.Any) -> typing.Any:
    return x

def is_lambda(obj: typing.Any) -> bool:
    return isinstance(obj, types.LambdaType) and obj.__name__ == '<lambda>'

def chunk(string: str, sizes):
    buffer = io.StringIO(string)

    return \
    [
        buffer.read(size)
        for size in sizes
    ]

def concatenate(strings):
    return ''.join(strings)
