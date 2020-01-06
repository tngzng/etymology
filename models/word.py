import re
from typing import Dict, List, Any
import multiprocessing as mp

from pydantic import BaseModel
import ety
from wiktionaryparser import WiktionaryParser


parser = WiktionaryParser()
origin_descendants = {}


for word in ety.data.etyms['eng'].keys():
    origins = ety.origins(word, recursive=True)
    for origin in origins:
        # tuple of the form ('gata', 'Old Norse')
        origin = (origin._word, origin._language.iso)
        if origin_descendants.get(origin):
            origin_descendants[origin].append(word)
        else:
            origin_descendants[origin] = [word]


class Word(BaseModel):
    word: str
    language: str = 'English'
    language_code: str = 'eng'
    meaning: List[Dict[str, Any]] = []


def camel_to_snake(text: str) -> str:
    text = re.sub(r'(?<!^)(?=[A-Z])', '_', text).lower()
    return text


def format_definition(definition: Dict[str, Any]) -> Dict[str, Any]:
    return {camel_to_snake(k): v for k, v in definition.items()}


def get_definition(word: str, language_code: str) -> List[str]:
    try:
        # TODO add non-english support
        entries = parser.fetch(word)
        definitions = [format_definition(d) for d in entries[0]['definitions']]
    except IndexError:
        definitions = []
    return definitions


def ety_to_word(ety_word: ety.word.Word) -> Word:
    data = {
        'word': ety_word._word,
        'language': ety_word._language.name,
        'language_code': ety_word._language.iso,
    }
    return Word(**data)


def word_to_dict(word: Word) -> Dict[str, Any]:
    word_dict = word.__dict__
    word_dict['meaning'] = get_definition(word.word, word.language_code)
    return word_dict


def get_origins(word: str, language_code: str) -> List[Word]:
    origins = ety.origins(word, language=language_code, recursive=True)
    origins = [ety_to_word(origin) for origin in origins]
    # parallelize "lazy-loading" word_to_dict call, which makes an api fetch for each definition
    pool = mp.Pool(mp.cpu_count())
    serialized_origins = pool.map_async(word_to_dict, origins).get()
    pool.close
    return serialized_origins


def get_descendants(word: str, language_code: str) -> List[Word]:
    descendants = origin_descendants.get((word, language_code), [])
    descendants = [Word(word=descendant) for descendant in descendants]
    # parallelize "lazy-loading" word_to_dict call, which makes an api fetch for each definition
    pool = mp.Pool(mp.cpu_count())
    serialized_descendants = pool.map_async(word_to_dict, descendants).get()
    pool.close
    return serialized_descendants
