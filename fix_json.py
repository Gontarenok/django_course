import json


with open('mainapp/fixtures/004_news.json', encoding='utf-16') as f:
    data = json.load(f)
    print(data)
with open('mainapp/fixtures/005_news.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False)