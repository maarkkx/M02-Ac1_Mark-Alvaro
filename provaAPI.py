import requests

url = "https://pokeapi.co/api/v2/pokemon/pikachu"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("Nom:", data["name"])
    print("Pes:", data["weight"])
    print("Alçada:", data["height"])
    print("Tipus:", [t["type"]["name"] for t in data["types"]])
else:
    print("Error en la consulta")
