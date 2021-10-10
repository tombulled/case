from . import models
from . import translators
from . import renderers
from . import types
from . import style

__all__ = ['Lower', 'Upper'] # And the others...

@style.style
class Lower(models.Case):
    prepare: types.Translator = translators.lower
    render:  types.Renderer   = renderers.space

@style.style
class Upper(models.Case):
    prepare: types.Translator = translators.upper
    render:  types.Renderer   = renderers.space

@style.style
class Title(models.Case):
    prepare: types.Translator = translators.title
    render:  types.Renderer   = renderers.space

@style.style
class Sentence(models.Case):
    prepare: types.Translator = translators.capitalize
    render:  types.Renderer   = renderers.space

@style.style
class Snake(models.Case):
    prepare: types.Translator = translators.lower
    render:  types.Renderer   = renderers.underscore

@style.style
class Helter(models.Case):
    prepare: types.Translator = translators.title
    render:  types.Renderer   = renderers.underscore

@style.style
class Macro(models.Case):
    prepare: types.Translator = translators.upper
    render:  types.Renderer   = renderers.underscore

@style.style
class Kebab(models.Case):
    prepare: types.Translator = translators.lower
    render:  types.Renderer   = renderers.hyphen

@style.style
class Train(models.Case):
    prepare: types.Translator = translators.title
    render:  types.Renderer   = renderers.hyphen

@style.style
class Cobol(models.Case):
    prepare: types.Translator = translators.upper
    render:  types.Renderer   = renderers.hyphen

@style.style
class Flat(models.Case):
    prepare: types.Translator = translators.lower
    render:  types.Renderer   = renderers.concatenate

@style.style
class Flush(models.Case):
    prepare: types.Translator = translators.upper
    render:  types.Renderer   = renderers.concatenate

@style.style
class Pascal(models.Case):
    prepare: types.Translator = translators.title
    render:  types.Renderer   = renderers.concatenate

@style.style
class Camel(models.Case):
    prepare: types.Translator = translators.dromedary
    render:  types.Renderer   = renderers.concatenate

@style.style
class Dot(models.Case):
    prepare: types.Translator = translators.lower
    render:  types.Renderer   = renderers.period

@style.style
class Path(models.Case):
    prepare: types.Translator = translators.lower
    render:  types.Renderer   = renderers.slash
