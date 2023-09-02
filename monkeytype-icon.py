import base64
import json
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
from time import sleep

from script import generate_readme as generateReadme


def getMonkeytypeIconJson():

    url = "https://monkeytype-readme.zeabur.app/mr-command/favicon"

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)

        sleep(10)
        page.wait_for_load_state("networkidle")

        full_html = page.content()

        browser.close()

    soup = BeautifulSoup(full_html, 'html.parser')
    monkeytypeIconJson = soup.find(id="faviconImageData").get_text()
    monkeytypeIconJson = json.loads(monkeytypeIconJson)
    monkeytypeIconJson = json.dumps(monkeytypeIconJson, indent=4)

    with open("./monkeytype-icon.json", "w") as json_file:
        json_file.write(monkeytypeIconJson)


def downloadMonkeytypeIcon():
    json_file_path = "./monkeytype-icon.json"

    with open(json_file_path, "r") as json_file:
        faviconData = json.load(json_file)

    faviconData = dict(faviconData)

    for i in range(len(faviconData)):
        binary_data = base64.b64decode(
            faviconData[str(i)]['data'].split(',')[1])

        filename = f'{faviconData[str(i)]["name"]}.png'

        with open(f'./monkeytype-icon/{filename}', 'wb') as f:
            f.write(binary_data)

        print(f"Image '{filename}' downloaded successfully.")


getMonkeytypeIconJson()
downloadMonkeytypeIcon()
generateReadme.generateReadme()