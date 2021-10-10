import random
import typing

def enumerate_words(translator):
    def wrapper(words):
        for index, word in enumerate(words):
            yield translator(index, word)

    return wrapper

def enumerate_characters(translator):
    def wrapper(words):
        index: int = 0

        word: str
        for word in words:
            character: str
            for character in word:
                yield translator(index, character)

                index += 1

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

@enumerate_characters
def sponge(index: int, character: int) -> str:
    return random.choice((str.lower, str.upper))(character)
