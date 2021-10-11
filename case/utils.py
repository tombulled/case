import typing
import types

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

# Note: Use <TypeVar> of 'T' ?
def identity(x: typing.Any) -> typing.Any:
    return x

def is_lambda(obj: typing.Any):
    return isinstance(obj, types.LambdaType) and obj.__name__ == '<lambda>'
