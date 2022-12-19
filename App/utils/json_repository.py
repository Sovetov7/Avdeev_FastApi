import json

# Реализация хранилища в файле json
with open('data.json') as json_file:
    data: dict = json.load(json_file)

data_students = data.get("students")
data_groups = data.get("groups")


def save_dict_to_json():
    # Сохранение словаря в файл json
    with open('data.json', 'w') as outfile:
        json.dump(data, outfile, indent=4)