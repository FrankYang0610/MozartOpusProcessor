import json

def load_and_split_txt_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # 使用 '<td> —' 作为分隔符来分割文本
    parts = content.splitlines()

    # 删除空字符串，并去除每个部分首尾的空白字符
    parts = [part.strip() for part in parts if part.strip()]
    parts.pop(0)
    return parts

def split_content(line):
    parts = line.split('\t')

    if len(parts) < 7:
        return None  # 或者抛出一个异常

    if len(parts) == 7:
        K, K6, title, force, key, date, genre = parts[:7]
        notes = ""
    elif len(parts) == 8:
        K, K6, title, force, key, date, genre, notes = parts[:8]

    opus_dict = {
        'K': K.strip(),
        'K6': K6.strip(),
        'title': title.strip(),
        'force': force.strip(),
        'key': key.strip(),
        'date': date.strip(),
        'genre': genre.strip(),
        'notes': notes.strip()
    }

    return opus_dict

def save_array_to_json(array, file_path):
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(array, f, ensure_ascii=False, indent=4)

mozart_opus_lines = load_and_split_txt_file('Mozart_Opus_Raw_Table.txt')
mozart_opus = []

for opus_line in mozart_opus_lines:
    mozart_opus.append(split_content(opus_line))

print(mozart_opus)
save_array_to_json(mozart_opus, 'mozart_opus.json')
