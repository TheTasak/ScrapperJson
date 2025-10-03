# ScrapperJson

### A simple automated scrapper with support for JSON structure of scrapping rules

## Installation:
```bash
pip install scrapper-json-jawron
```

## Usage:
```python
from scrapper-json-jawron import Scrapper
import json
from dataclasses import dataclass

# function to load rules from a file 
def load_rules(path: str) -> dict:
    with open(path, "r") as file:
        return json.load(file)

# example result dataclass
@dataclass
class Article:
    url: str
    title: str
    content: str
        
rules = load_rules("example.json")

# create templated scrapper
scr = Scrapper(rules, Article)

# scrap entity list
result = scr.scrap_list()

# scrap entity details
entity_rules = load_rules("example_entity.json")
for entity in result:
    entity_result = scr.scrap_entity(entity_rules, entity)
```

## JSON structure

### Main options
* **type:** Defines the type of scrapping data, can be either `xml` or `html`
* **url**: Defines the url of XML feed or HTML page that will be scrapped
* **root**: Defines the root element at which scrapping begins
* **entry**: Defines the particular entries elements which will be scrapped to separate objects
* **elements**: Defines the scrapped properties of an entity

### Elements options
* **selector:** Defines the CSS or XML selector for the element
* **item_type:** Defines the type of item, can be either `single` or `list`
* **attribute:** Defines the attribute of element which will be scrapped, if scrapping text use `text` else use the name of the attribute
* **prefix:** Defines the prefix which is added to the result property
* **suffix:** Defines the suffix which is added to the result property
* **remove:** Defines the text which to remove from the result property
* **replace:** Defines the text which to replace from the result property

### Example HTML
```json
{
  "type": "html",
  "url": "https://www.technewsworld.com/archive",
  "root": {
    "selector": "div.category-article-list",
    "attribute": "element"
  },
  "entry": {
    "selector": "div.search-item",
    "attribute": "element",
    "item_type": "list"
  },
  "elements": {
    "title": {
      "selector": "div.search-txt a h2",
      "attribute": "text"
    },
    "url": {
      "selector": "div.search-txt a",
      "attribute": "href"
    },
    "content": {
      "selector": null,
      "attribute": "text"
    }
  }
}
```

### Example XML
```json
{
  "type": "xml",
  "url": "https://www.cijeurope.com/rss/posts/en.xml",
  "root": "channel",
  "entry": "item",
  "elements": {
    "title": {
      "selector": "title",
      "attribute": "text"
    },
    "url": {
      "selector": "link",
      "attribute": "text"
    },
    "content": {
      "selector": null,
      "attribute": "text"
    }
  }
}
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change or add.