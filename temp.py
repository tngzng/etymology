import ety

origin_map = {}

for word in ety.data.etyms['eng'].keys():
    origins = ety.origins(word, recursive=True)
    for origin in origins:
        # tuple of the form ('gata', 'Old Norse')
        origin = (origin._word, origin._language.name)
        if origin_map.get(origin):
            origin_map[origin].append(word)
        else:
            origin_map[origin] = [word]

for origin in origin_map.keys():
    if len(origin_map[origin]) > 5 and len(origin_map[origin]) < 15:
        print(f'descendants of {origin}:')
        for descendant in origin_map[origin]:
            print(f'- {descendant}')
        print('-------------')