import typing
import types

# https://toolz.readthedocs.io/en/latest/api.html#toolz.functoolz.compose_left
def compose(*functions):
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

def identity(x): return x

def is_lambda(obj):
    return isinstance(obj, types.LambdaType) and obj.__name__ == '<lambda>'
