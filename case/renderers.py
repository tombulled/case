from . import models

space: models.Renderer = models.Renderer(word_sep=" ")
concatenate: models.Renderer = models.Renderer(word_sep="")
underscore: models.Renderer = models.Renderer(word_sep="_")
hyphen: models.Renderer = models.Renderer(word_sep="-")
period: models.Renderer = models.Renderer(word_sep=".")
slash: models.Renderer = models.Renderer(word_sep="/")