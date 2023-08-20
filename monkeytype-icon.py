import base64
import json

json_file_path = "./monkeytype-icon.json"

with open(json_file_path, "r") as json_file:
    faviconData = json.load(json_file)

faviconData = dict(faviconData)

for i in range(len(faviconData)):
    binary_data = base64.b64decode(faviconData[str(i)]['data'].split(',')[1])

    filename = f'{faviconData[str(i)]["name"]}.png'


    with open(f'./monkeytype-icon/{filename}', 'wb') as f:
        f.write(binary_data)

    print(f"Image '{filename}' downloaded successfully.")
