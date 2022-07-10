import requests
import json


with open("./items.json") as data:
    items_json = json.load(data)
with open("./rarity.json") as data:
    rarity_json = json.load(data)


def pin_to_ipfs(path: str, name: str):

    url = "https://api.pinata.cloud/pinning/pinFileToIPFS"

    payload = {
        "pinataOptions": '{"cidVersion": 1}',
        "pinataMetadata": '{"name": "' + name + '"}',
    }
    files = [("file", ("image", open(f"{path}", "rb"), "application/octet-stream"))]
    headers = {
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySW5mb3JtYXRpb24iOnsiaWQiOiI5Mzk1NzFhOS0xMGM2LTQ5YmYtYmZhYy0wZDI5N2M4OGVkM2EiLCJlbWFpbCI6InNlYW5rb2hqdW5oYW9AZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsInBpbl9wb2xpY3kiOnsicmVnaW9ucyI6W3siaWQiOiJGUkExIiwiZGVzaXJlZFJlcGxpY2F0aW9uQ291bnQiOjF9XSwidmVyc2lvbiI6MX0sIm1mYV9lbmFibGVkIjpmYWxzZSwic3RhdHVzIjoiQUNUSVZFIn0sImF1dGhlbnRpY2F0aW9uVHlwZSI6InNjb3BlZEtleSIsInNjb3BlZEtleUtleSI6ImQ0MWViY2NhYTMyYjZkYjQwMjcxIiwic2NvcGVkS2V5U2VjcmV0IjoiODRjZjJkOWI0NDJiZmRlYTIwZjcyZWQzZjY1MjI0M2YyMDQ0MjY1NzIzZWM4ZDUwMmE2MTFmNTMyOTZlMGMwYSIsImlhdCI6MTY1NzIyNTU1N30.zv0QRPYFAY2bj-N5EcxhyJ6lA3R5TNZEl0jqYWBlsvM"
    }

    response = requests.post(url, headers=headers, data=payload, files=files).json()

    return response["IpfsHash"]


def process_dna(dna: list):
    skin = rarity_json["skin"][dna[0]]
    eyes = rarity_json["eye"][dna[1]]
    hair = rarity_json["hair"][dna[2]]
    clothes = rarity_json["clothes"][dna[3]]
    head = rarity_json["head"][dna[4]]
    accessory = rarity_json["accessory"][dna[5]]
    return {
        "skin": skin,
        "eyes": eyes,
        "hair": hair,
        "clothes": clothes,
        "head": head,
        "accessory": accessory,
    }


def build_metadata(hash: str, name: str, dna: dict):

    template = {
        f"{name}": {
            "skin": f"{dna['skin']}",
            "eye": f"{dna['eyes']}",
            "hair": f"{dna['hair']}",
            "clothes": f"{dna['clothes']}",
            "head": f"{dna['head']}",
            "accessory": f"{dna['accessory']}",
            "image": f"ipfs://{hash}",
        }
    }
    return template


for item in items_json["items"]:
    hash = pin_to_ipfs(item["path"], item["name"])
    dna = process_dna(item["dna"])
    metadata = build_metadata(hash, item["name"], dna)
    print(metadata)
