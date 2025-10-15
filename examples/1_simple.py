from src.scrapper_json_jawron.scrapper import Scrapper, get_rules_from_file
from dataclasses import dataclass
# example result dataclass
@dataclass
class Article:
    url: str
    title: str
    content: str = ""

rules = get_rules_from_file("1_list_rules.json")

# create templated scrapper
scr = Scrapper(rules, Article)

# scrap entity list
result = scr.scrap_list()
flat_list = []
for item in result:
    flat_list.extend(item)

# export to csv, json
scr.export_to_csv("test.csv", flat_list)
scr.export_to_json("test.json", flat_list)

print(flat_list)
print(len(flat_list))