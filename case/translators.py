import random
import typing

def enumerate_words(translator):
    def wrapper(words):
        return \
        [
            translator(index, word)
            for index, word in enumerate(words)
        ]

    return wrapper

def enumerate_characters(translator):
    def wrapper(words):
        index: int = 0

        translated_words: typing.List[str] = []

        word: str
        for word in words:
            translated_word: str = ''

            character: str
            for character in word:
                translated_word += translator(index, character)

                index += 1

            translated_words.append(translated_word)

        return translated_words

    return wrapper

@enumerate_words
def lower(index: int, word: str) -> str:
    return word.lower()

@enumerate_words
def upper(index: int, word: str) -> str:
    return word.upper()

@enumerate_words
def title(index: int, word: str) -> str:
    return word.title()

@enumerate_words
def swapcase(index: int, word: str) -> str:
    return word.swapcase()

@enumerate_words
def capitalize(index: int, word: str) -> str:
    return word.title() if index == 0 else word.lower()

@enumerate_words
def dromedary(index: int, word: str) -> str:
    return word.lower() if index == 0 else word.title()

@enumerate_characters
def alternating(index: int, character: int) -> str:
    return (str.lower, str.upper)[index % 2](character)

# TODO: Find a way to rename to 'random'
@enumerate_characters
def sponge(index: int, character: int) -> str:
    return random.choice((str.lower, str.upper))(character)
