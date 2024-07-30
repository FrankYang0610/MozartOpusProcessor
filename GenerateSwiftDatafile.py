import json

def escape_quotes(s):
    return s.replace('"', '\\"')

def dict_item_to_swift_string(single_opus):
    k = single_opus.get('K', '')
    k6 = single_opus.get('K6', '')

    if k6:
        if k and k != '—':
            number = f"KV {k6} ({k})"
        else:
            number = f"KV {k6}"
    elif k and k != '—':
        number = f"K. {k}"
    else:
        number = ""

    title = escape_quotes(single_opus.get('title', ''))
    key = single_opus.get('key', '')
    name = f"{title} ({key})"
    date = single_opus.get('date', '')
    swift_string = f'Composition(number: "{number}", name: "{name}", pieces: [], date: "{date}", mostFavorite: false, link: "")'
    return swift_string + ','

def load_array_from_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

mozart_opus = load_array_from_json('mozart_opus.json')

for single_opus in mozart_opus:
    print(dict_item_to_swift_string(single_opus))

