import json


def generateReadme():
    md = """
![](https://github.com/ridemountainpig/monkeytype-icon/blob/master/asset/image/monkeytype-icon-banner-rounded.png?raw=true)

# MonkeyType Icon
Add monkeytype icon to your Profile and Projects.

## Usage:
- Press `Ctrl + f` on your keyboard, to bring out the search modal.
- Enter the monkeytype theme of the icon you need, if the theme name have space, please replace it with `_`.<br/>
  example : (`nord light` => `nord_light`)
- Copy the link or download icon to use.

## MonkeyType Favicons
    """

    with open("./asset/docs/icon-table.md", "r") as icon_table:
        md += icon_table.read()

    md += """
## MonkeyType Logo Icons
    """

    with open("./asset/docs/logo-icon-table.md", "r") as icon_table:
        md += icon_table.read()

    with open("./README.md", "w") as readme:
        readme.write(md)


def generateIconTable():
    json_file_path = "./monkeytype-icon.json"

    with open(json_file_path, "r") as json_file:
        faviconData = json.load(json_file)

    faviconData = dict(faviconData)

    for i in range(len(faviconData)):
        for j in range(i + 1, len(faviconData)):
            if faviconData[str(i)]['name'] > faviconData[str(j)]['name']:
                faviconData[str(i)], faviconData[str(
                    j)] = faviconData[str(j)], faviconData[str(i)]

    iconTable = """
| Theme | Icon | Link |
| --- | --- | --- |
"""

    for i in range(len(faviconData)):
        iconTable += f"| {faviconData[str(i)]['name']} | ![{faviconData[str(i)]['name']}-favicon](https://raw.githubusercontent.com/ridemountainpig/monkeytype-icon/master/monkeytype-icon/svg/{faviconData[str(i)]['name']}.svg) | `https://raw.githubusercontent.com/ridemountainpig/monkeytype-icon/master/monkeytype-icon/svg/{faviconData[str(i)]['name']}.svg` |\n"

    with open("./asset/docs/icon-table.md", "w") as icon_table:
        icon_table.write(iconTable)
