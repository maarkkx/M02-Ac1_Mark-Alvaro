import requests

pokemonNom = "bulbasaur"
url = "https://pokeapi.co/api/v2/pokemon/" + pokemonNom

pokemonIDEvolucio = "1"
urlEvolution = "https://pokeapi.co/api/v2/evolution-chain/" + pokemonIDEvolucio

pokemonRegio = "Kanto"
urlRegio = "https://pokeapi.co/api/v2/region/" + pokemonRegio

response = requests.get(url)
responseEvolution = requests.get(urlEvolution)
responseRegio = requests.get(urlRegio)

if response.status_code == 200 and responseEvolution.status_code == 200 and responseRegio.status_code == 200:
    data = response.json()
    dataEvolution = responseEvolution.json()
    dataRegio = responseRegio.json()

    #Informació bàsica del pokemon
    print("Nom:", data["name"])
    print("Altura:", data["height"])
    print("Pes:", data["weight"])
    print("Experiencia Base:", data["base_experience"])
    print("Tipus:", [t["type"]["name"] for t in data["types"]])
    print("Habilitats:", [a["ability"]["name"] for a in data["abilities"]])


    print("Cadena evolutiva:")
    evolution_chain = dataEvolution["chain"]
    while evolution_chain:
        print(" -", evolution_chain["species"]["name"])

        if evolution_chain["evolves_to"]:
            evolution_chain = evolution_chain["evolves_to"][0]
        else:
            break

    print("Regió principal:", dataRegio["name"])
    print("Joc principal:", data["game_inci"])
else:
    print("Error en la consulta")
