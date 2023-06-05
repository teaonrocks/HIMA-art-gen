from concurrent.futures import process
from readline import get_begidx
from PIL import Image
import os
import json
import random
import sqlite3
import requests
PINATA_API_TOKEN = os.getenv("PINATA_API_TOKEN")


def create_table():
    db = sqlite3.connect("test.db", isolation_level=None)
    cursor = db.cursor()
    cursor.execute("DROP TABLE dna")
    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS dna (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        bg INTEGER,
        aura INTEGER,
        skin INTEGER,
        eye INTEGER,
        hair INTEGER,
        clothes INTEGER,
        head INTEGER,
        face INTEGER
    )
    """
    )


def add_to_db(dna: list):
    db = sqlite3.connect("test.db", isolation_level=None)
    cursor = db.cursor()
    cursor.execute(
        f"""
    INSERT INTO dna (bg,aura,skin,eye,hair,clothes,head,face)
    VALUES ({dna[0]}, {dna[1]},{dna[2]},{dna[3]},{dna[4]},{dna[5]},{dna[6]},{dna[7]})
    """
    )


def get_db():
    db = sqlite3.connect("test.db", isolation_level=None)
    cursor = db.cursor()
    cursor.execute(
        """
    SELECT bg,aura,skin,eye,hair,clothes,head,face FROM dna
    """
    )
    return cursor.fetchall()


with open("./rarity.json") as rarity:
    rarity_json = json.load(rarity)
with open("./full_names.json") as data:
    full_names = json.load(data)["full_names"]


def generate_dna():
    def choose_bg():
        prob = rarity_json["bgprob"]
        chosen = random.randint(1, 10000)
        prob_sum = 0
        for index, item in enumerate(prob):
            prob_sum += item
            if prob_sum >= chosen:
                return index

    def choose_aura():
        prob = rarity_json["specialprob"]
        chosen = random.randint(1, 10000)
        prob_sum = 0
        for index, item in enumerate(prob):
            prob_sum += item
            if prob_sum >= chosen:
                return index

    def choose_skin():
        prob = rarity_json["skinprob"]
        chosen = random.randint(1, 10000)
        prob_sum = 0
        for index, item in enumerate(prob):
            prob_sum += item
            if prob_sum >= chosen:
                return index

    def choose_eye():
        prob = rarity_json["eyesprob"]
        chosen = random.randint(1, 10000)
        prob_sum = 0
        for index, item in enumerate(prob):
            prob_sum += item
            if prob_sum >= chosen:
                return index

    def choose_hair():
        prob = rarity_json["hairprob"]
        chosen = random.randint(1, 10000)
        prob_sum = 0
        for index, item in enumerate(prob):
            prob_sum += item
            if prob_sum >= chosen:
                return index

    def choose_clothes():
        prob = rarity_json["clothesprob"]
        chosen = random.randint(1, 10000)
        prob_sum = 0
        for index, item in enumerate(prob):
            prob_sum += item
            if prob_sum >= chosen:
                return index

    def choose_head():
        prob = rarity_json["headprob"]
        chosen = random.randint(1, 10000)
        prob_sum = 0
        for index, item in enumerate(prob):
            prob_sum += item
            if prob_sum >= chosen:
                return index

    def choose_face():
        prob = rarity_json["faceprob"]
        chosen = random.randint(1, 10000)
        prob_sum = 0
        for index, item in enumerate(prob):
            prob_sum += item
            if prob_sum >= chosen:
                return index

    dna = [
        choose_bg(),
        choose_aura(),
        choose_skin(),
        choose_eye(),
        choose_hair(),
        choose_clothes(),
        choose_head(),
        choose_face(),
    ]
    return dna


def generate_image(dna: list):
    bg_dir = sorted(os.listdir("./hima_assets_final/15_BG"))
    bg = Image.open(f"./hima_assets_final/15_BG/{bg_dir[dna[0]]}")
    back_aura_dir = sorted(os.listdir("./hima_assets_final/14_back aura"))
    back_aura = Image.open(f"./hima_assets_final/14_back aura/{back_aura_dir[dna[1]]}")
    bg_back_aura = Image.alpha_composite(bg, back_aura)
    skin_dir = sorted(os.listdir("./hima_assets_final/13_skin"))
    skin = Image.open(f"./hima_assets_final/13_skin/{skin_dir[dna[2]]}")
    back_aura_skin = Image.alpha_composite(bg_back_aura, skin)
    eye_dir = sorted(os.listdir("./hima_assets_final/12_eye"))
    if dna[3] > 17 or dna[3] == 12:
        eye = Image.open("./hima_assets_final/1_top aura/nothing.png")
    else:
        eye = Image.open(f"./hima_assets_final/12_eye/{eye_dir[dna[3]]}")
    skin_eye = Image.alpha_composite(back_aura_skin, eye)
    if dna[3] == 12 or dna[3] > 17:
        black_eye = Image.open(
            "./hima_assets_final/11_default/black eyes (DEFAULT EYES).png"
        )
    else:
        black_eye = Image.open("./hima_assets_final/1_top aura/nothing.png")
    eye_black = Image.alpha_composite(skin_eye, black_eye)
    default = Image.open("./hima_assets_final/11_default/default.png")
    default_black = Image.alpha_composite(eye_black, default)
    hair_back_dir = sorted(os.listdir("./hima_assets_final/10_hairBACK"))
    hair_back = Image.open(f"./hima_assets_final/10_hairBACK/{hair_back_dir[dna[4]]}")
    black_hair_back = Image.alpha_composite(default_black, hair_back)
    clothes_dir = sorted(os.listdir("./hima_assets_final/9_clothes"))
    clothes = Image.open(f"./hima_assets_final/9_clothes/{clothes_dir[dna[5]]}")
    hair_back_clothes = Image.alpha_composite(black_hair_back, clothes)
    hair_front_dir = sorted(os.listdir("./hima_assets_final/8_hairFRONT"))
    hair_front = Image.open(f"./hima_assets_final/8_hairFRONT/{hair_front_dir[dna[4]]}")
    clothes_hair_front = Image.alpha_composite(hair_back_clothes, hair_front)
    if dna[3] > 17:
        special_eye_dir = sorted(os.listdir("./hima_assets_final/7_specialeyes_back"))
        index = dna[3] - 18
        print(index)
        special_eye = Image.open(
            f"./hima_assets_final/7_specialeyes_back/{special_eye_dir[index]}"
        )
    else:
        special_eye = Image.open("./hima_assets_final/1_top aura/nothing.png")
    hair_front_special_eye = Image.alpha_composite(clothes_hair_front, special_eye)
    face_dir = sorted(os.listdir("./hima_assets_final/6_face accessories"))
    face = Image.open(f"./hima_assets_final/6_face accessories/{face_dir[dna[7]]}")
    special_eye_face = Image.alpha_composite(hair_front_special_eye, face)
    head_dir = sorted(os.listdir("./hima_assets_final/5_headwear"))
    head = Image.open(f"./hima_assets_final/5_headwear/{head_dir[dna[6]]}")
    face_head = Image.alpha_composite(special_eye_face, head)
    if dna[7] == 7:
        face_layer = Image.open(
            "./hima_assets_final/4_face_accessories_layer/cybernetic mask LAYER.png"
        )
    else:
        face_layer = Image.open("./hima_assets_final/1_top aura/nothing.png")
    head_face_layer = Image.alpha_composite(face_head, face_layer)
    if dna[6] == 4:
        head_layer = Image.open("./hima_assets_final/3_headwear_layer/bells LAYER.png")
    elif dna[6] == 13:
        head_layer = Image.open(
            "./hima_assets_final/3_headwear_layer/dragons breath LAYER.png"
        )
    elif dna[6] == 18:
        head_layer = Image.open("./hima_assets_final/3_headwear_layer/god LAYER.png")
    else:
        head_layer = Image.open("./hima_assets_final/1_top aura/nothing.png")
    face_layer_head_layer = Image.alpha_composite(head_face_layer, head_layer)
    if dna[3] > 17:
        special_eye_front_dir = sorted(
            os.listdir("./hima_assets_final/2_specialeyes_front")
        )
        index = dna[3] - 18
        special_eye_front = Image.open(
            f"./hima_assets_final/2_specialeyes_front/{special_eye_front_dir[index]}"
        )
    else:
        special_eye_front = Image.open("./hima_assets_final/1_top aura/nothing.png")
    head_layer_special_eye_front = Image.alpha_composite(
        face_layer_head_layer, special_eye_front
    )
    top_aura_dir = sorted(os.listdir("./hima_assets_final/1_top aura"))
    top_aura = Image.open(f"./hima_assets_final/1_top aura/{top_aura_dir[dna[1]]}")
    return Image.alpha_composite(head_layer_special_eye_front, top_aura)


def pin_to_ipfs(path: str, name: str):

    url = "https://api.pinata.cloud/pinning/pinFileToIPFS"

    payload = {
        "pinataOptions": '{"cidVersion": 1}',
        "pinataMetadata": '{"name": "' + name + '"}',
    }
    files = [("file", ("image", open(f"{path}", "rb"), "application/octet-stream"))]
    headers = {
        f"Authorization": "Bearer {PINATA_API_TOKEN}",
    }
    response = requests.post(url, headers=headers, data=payload, files=files)
    while response.status_code != 200:
        response = requests.post(url, headers=headers, data=payload, files=files)
    response_json = response.json()
    return response_json["IpfsHash"]


def process_dna(dna: list):
    bg = rarity_json["bg"][dna[0]]
    aura = rarity_json["special"][dna[1]]
    eyes = rarity_json["eyes"][dna[3]]
    hair = rarity_json["hair"][dna[4]]
    clothes = rarity_json["clothes"][dna[5]]
    head = rarity_json["head"][dna[6]]
    accessory = rarity_json["face"][dna[7]]
    return {
        "bg": bg,
        "aura": aura,
        "eyes": eyes,
        "hair": hair,
        "clothes": clothes,
        "head": head,
        "accessory": accessory,
    }


def build_metadata(hash: str, name: str, dna: dict):

    template = {
        f"{name}": {
            "name": name,
            "Background": f"{dna['bg']}",
            "Aura": f"{dna['aura']}",
            "Eye": f"{dna['eyes']}",
            "Hair": f"{dna['hair']}",
            "Clothes": f"{dna['clothes']}",
            "Head accessory": f"{dna['head']}",
            "Face accessory": f"{dna['accessory']}",
            "image": f"ipfs://{hash}",
            "discord": "https://discord.gg/hima",
            "twitter": "https://twitter.com/HimaHighSchool",
            "website": "https://himahighschool.io",
        }
    }
    return template


# create_table()
# for x in range(5000):
#     dna = generate_dna()
#     print(dna)
#     name = random.choice(full_names)
#     full_names.remove(name)
#     db_dnas = get_db()
#     if db_dnas is not None:
#         while tuple(db_dnas) in db_dnas:
#             dna = generate_dna()
#     add_to_db(dna)
#     image = generate_image(dna)
#     image.save(f"./output/{name}.png")
#     ipfs_hash = pin_to_ipfs(f"./output/{name}.png", name)
#     dna_dict = process_dna(dna)
#     metadata = build_metadata(ipfs_hash, name, dna_dict)
#     with open(f"./metadata/{name}.json", "w") as outfile:
#         outfile.write(json.dumps(metadata))
names = []
for file in os.listdir("./rejected/reroll"):
    names.append(file.split(".", 1)[0])
for file in os.listdir("./rejected/ribbon"):
    names.append(file.split(".", 1)[0])
for file in os.listdir("./rejected/special eyes"):
    names.append(file.split(".", 1)[0])
for file in os.listdir("./specialeye_regen_image"):
    name = file.split(".", 1)[0]
    names.remove(name)
db_dnas = get_db()
counter = 0
special_dna = []
for dna in db_dnas:
    if dna[3] > 17:
        special_dna.append(dna)
        counter += 1
print("special eyes:", counter)
print(special_dna)
counter = 0
ribbons_dna = []
for dna in db_dnas:
    if dna[6] == 29:
        ribbons_dna.append(dna)
        counter += 1
print("ribbons :", counter)
print(ribbons_dna)
counter = 0
for dna in db_dnas:
    if dna[6] == 3 and dna[7] == 7:
        counter += 1
print("reroll: ", counter)
for dna in ribbons_dna:
    print(dna)
    image = generate_image(list(dna))
    name = random.choice(names)
    image.save(f"./output/{name}.png")
    ipfs_hash = pin_to_ipfs(f"./output/{name}.png", name)
    dna_dict = process_dna(list(dna))
    metadata = build_metadata(ipfs_hash, name, dna_dict)
    with open(f"./metadata/{name}.json", "w") as outfile:
        outfile.write(json.dumps(metadata))
