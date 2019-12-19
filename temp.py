import ety
from PyDictionary import PyDictionary


d = PyDictionary()
origin_descendants = {}


for word in ety.data.etyms['eng'].keys():
    origins = ety.origins(word, recursive=True)
    for origin in origins:
        # tuple of the form ('gata', 'Old Norse')
        origin = (origin._word, origin._language.name)
        if origin_descendants.get(origin):
            origin_descendants[origin].append(word)
        else:
            origin_descendants[origin] = [word]


def get_origins(word):
    origins = ety.origins(word, recursive=True)
    return [(origin._word, origin._language.name) for origin in origins]


def get_descendants(origin):
    return origin_descendants.get(origin)


def get_definition(word):
    try:
        definition = d.meaning(word)
    except IndexError:
        definition = {}
    return definition
