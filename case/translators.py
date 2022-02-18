import dataclasses
import random
import typing

from . import api, models, protocols

class WordTranslatorHook(typing.Protocol):
    def __call__(self, word: models.Word, /) -> str:
        ...

class CharacterTranslatorHook(typing.Protocol):
    def __call__(self, character: models.Character, /) -> str:
        ...

@dataclasses.dataclass
class WordTranslator(protocols.Translator):
    hook: WordTranslatorHook

    def __call__(self, strings: typing.Iterable[str], /) -> typing.Iterable[str]:
        word: models.Word
        for word in api.tokenize(strings):
            yield self.hook(word)

@dataclasses.dataclass
class CharacterTranslator(protocols.Translator):
    hook: CharacterTranslatorHook

    def __call__(self, strings: typing.Iterable[str], /) -> typing.Iterable[str]:
        word: models.Word
        for word in api.tokenize(strings):
            translated: str = ''

            character: models.Character
            for character in word:
                translated += self.hook(character)

            yield translated

def character_translator(hook: CharacterTranslatorHook) -> CharacterTranslator:
    return CharacterTranslator(hook)

def word_translator(hook: WordTranslatorHook) -> WordTranslator:
    return WordTranslator(hook)

@word_translator
def lower(word: models.Word, /) -> str:
    return word.value.lower()

@word_translator
def upper(word: models.Word, /) -> str:
    return word.value.upper()

@word_translator
def title(word: models.Word, /) -> str:
    return word.value.title()

@word_translator
def swapcase(word: models.Word, /) -> str:
    return word.value.swapcase()

@word_translator
def capitalize(word: models.Word, /) -> str:
    if word.index == 0:
        return word.value.title()

    return word.value.lower()

@word_translator
def dromedary(word: models.Word, /) -> str:
    if word.index == 0:
        return word.value.lower()

    return word.value.title()

@character_translator
def alternating(character: models.Character, /) -> str:
    if character.offset % 2 == 0:
        return character.value.lower()

    return character.value.upper()

@character_translator
def sponge(character: models.Character, /) -> str:
    if random.getrandbits(1):
        return character.value.upper()

    return character.value.lower()