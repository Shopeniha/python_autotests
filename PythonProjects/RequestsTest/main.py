import requests

URL = 'https://api.pokemonbattle.me/v2/'
HEADERS = {'Content-Type' : 'application/json', 'trainer_token' : 'вставьте свой токен'}

body = {
    "name": "Собаня",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}

body_change = {
    "pokemon_id": "15711",
    "name": "Котява",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}

body_add = {
    "pokemon_id": "15711"
}

response = requests.post(url = f'{URL}pokemons', headers = HEADERS, json = body)

print(response.text)

response_change = requests.put(url = f'{URL}pokemons', headers = HEADERS, json = body_change)

print(response_change.text)

response_add = requests.post(url = f'{URL}trainers/add_pokeball', headers = HEADERS, json = body_add)

print(response_add.text)