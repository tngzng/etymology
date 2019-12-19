from typing import Dict, List, Any
import multiprocessing as mp

import ety
from PyDictionary import PyDictionary


dictionary = PyDictionary()


class Word:
    def __init__(self, ety_word: ety.word.Word):
        self.word = ety_word._word
        self.language = ety_word._language.name
        self.language_code = ety_word._language.iso
        self.meaning = {}


def get_definition(word: str, language_code: str) -> Dict[str, List[str]]:
    try:
        definition = dictionary.meaning(word) or {}
    except IndexError:
        definition = {}
    return definition


def word_to_dict(word: Word) -> Dict[str, Any]:
    dictionary = word.__dict__
    dictionary['meaning'] = get_definition(word.word, word.language_code)
    return dictionary


def get_origins(word: str, language_code: str) -> List[Word]:
    origins = ety.origins(word, language=language_code, recursive=True)
    origins = [Word(origin) for origin in origins]
    # parallelize "lazy-loading" word_to_dict call, which makes an api fetch for each definition
    pool = mp.Pool(mp.cpu_count())
    serialized_origins = pool.map_async(word_to_dict, origins).get()
    pool.close
    return serialized_origins
