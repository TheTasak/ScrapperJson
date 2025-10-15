from src.scrapper_json_jawron.scrapper import Scrapper, get_rules_from_file
from dataclasses import dataclass
# example result dataclass
@dataclass
class JobOffer:
    title: str
    url: str

rules = get_rules_from_file("2_playwright.json")

# create templated scrapper
scr = Scrapper(rules, JobOffer)

# scrap entity list
result = scr.scrap_list()
for item in result:
    print(item)