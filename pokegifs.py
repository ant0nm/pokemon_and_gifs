import json
import requests
import os

# Pokemon API
print("Pokemon API:")
base_path = "http://pokeapi.co/api/v2/"
name_token = "pokemon"
type_token = "type"

# request 1
# get pikachu
pokemon_name = "pikachu"
final_path_1 = f"{base_path}{name_token}/{pokemon_name}/"
response1 = requests.get(final_path_1)
body1 = json.loads(response1.content)
print(f"Pokemon Name: {body1['name']}")

# request 2
# get haunter
pokemon_id = 93
final_path_2 = f"{base_path}{name_token}/{pokemon_id}/"
response2 = requests.get(final_path_2)
body2 = json.loads(response2.content)
print()
print(f"Pokemon Name: {body2['name']}")

# request 3
# get all pokemons of type fire
type = "fire"
final_path_3 = f"{base_path}{type_token}/{type}/"
response3 = requests.get(final_path_3)
body3 = json.loads(response3.content)
print()
print("All pokemons of type fire:")
for pokemon in body3["pokemon"]:
    print("*", pokemon["pokemon"]["name"])

# GIPHY API
print()
print("GIPHY API:")
giphy_key = os.environ.get("GIPHY_KEY")
url = f"https://api.giphy.com/v1/gifs/search?api_key={giphy_key}&q=pikachu&rating=g"
response4 = requests.get(url)
body4 = json.loads(response4.content)
all_gifs = body4["data"]
for gif in all_gifs:
    print(gif["url"])

print()
print("Ketchup + Pikachu GIF:")
pikachu_ketchup_gif = all_gifs[18]["url"]
print(pikachu_ketchup_gif)
