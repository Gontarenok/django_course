import json


with open('mainapp/fixtures/001_user.json', encoding='utf-16') as f:
    data = json.load(f)
with open('mainapp/fixtures/001_user.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False)

