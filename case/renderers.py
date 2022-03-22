from . import models

space: models.SimpleRenderer = models.SimpleRenderer(word_sep=" ")
concatenate: models.SimpleRenderer = models.SimpleRenderer(word_sep="")
underscore: models.SimpleRenderer = models.SimpleRenderer(word_sep="_")
hyphen: models.SimpleRenderer = models.SimpleRenderer(word_sep="-")
period: models.SimpleRenderer = models.SimpleRenderer(word_sep=".")
slash: models.SimpleRenderer = models.SimpleRenderer(word_sep="/")