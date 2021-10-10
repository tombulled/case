from . import enums
from . import types

space:       types.Renderer = enums.Separator.SPACE.join
concatenate: types.Renderer = enums.Separator.NONE.join
underscore:  types.Renderer = enums.Separator.UNDERSCORE.join
hyphen:      types.Renderer = enums.Separator.HYPHEN.join
period:      types.Renderer = enums.Separator.PERIOD.join
slash:       types.Renderer = enums.Separator.SLASH.join
