import requests
import base64
import json
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
from time import sleep


def getMonkeytypeLogoJson():
    url = "https://monkeytype-readme.zeabur.app/mr-command/logo"

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)

        sleep(10)
        page.wait_for_load_state("networkidle")

        full_html = page.content()

        browser.close()

    soup = BeautifulSoup(full_html, "html.parser")
    monkeytypeLogoJson = soup.find(id="logoImageData").get_text()
    monkeytypeLogoJson = json.loads(monkeytypeLogoJson)
    monkeytypeLogoJson = json.dumps(monkeytypeLogoJson, indent=4)

    with open("./monkeytype-logo.json", "w") as json_file:
        json_file.write(monkeytypeLogoJson)

    print("Monkeytype logo json file generated successfully.")


def downloadMonkeytypeLogo():
    json_file_path = "./monkeytype-logo.json"

    with open(json_file_path, "r") as json_file:
        logoData = json.load(json_file)

    logoData = dict(logoData)

    for i in range(len(logoData)):
        png_binary_data = base64.b64decode(logoData[str(i)]["pngData"].split(",")[1])

        png_filename = f'{logoData[str(i)]["name"]}.png'

        with open(f"./monkeytype-logo/{png_filename}", "wb") as f:
            f.write(png_binary_data)

        print(f"Image '{png_filename}' downloaded successfully.")


getMonkeytypeLogoJson()
downloadMonkeytypeLogo()
