import json

with open('data.json') as in_file:
    data: dict = json.load(in_file)

# Очистить файл data
data.update({'groups': {}})
data.update({'students': {}})

with open('data.json', 'w') as outfile:
    json.dump(data, outfile, indent=4)
