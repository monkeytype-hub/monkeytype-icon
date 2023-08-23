import json

json_file_path = "./monkeytype-icon.json"

with open(json_file_path, "r") as json_file:
    faviconData = json.load(json_file)

faviconData = dict(faviconData)

for i in range(len(faviconData)):
    for j in range(i + 1, len(faviconData)):
        if faviconData[str(i)]['name'] > faviconData[str(j)]['name']:
            faviconData[str(i)], faviconData[str(j)] = faviconData[str(j)], faviconData[str(i)]

md = """
| Theme | Icon | Link |
| --- | --- | --- |
"""

for i in range(len(faviconData)):
    md += f"| {faviconData[str(i)]['name']} | ![{faviconData[str(i)]['name']}-favicon](https://raw.githubusercontent.com/ridemountainpig/monkeytype-icon/master/monkeytype-icon/{faviconData[str(i)]['name']}.png) | `https://raw.githubusercontent.com/ridemountainpig/monkeytype-icon/master/monkeytype-icon/{faviconData[str(i)]['name']}.png` |\n"

with open("./asset/docs/icon-table.md", "w") as icon_table:
    icon_table.write(md)
