
import requests

""" Task 2 """

# def fetch_pokemon_data():
#     abilities = []
#     url = "https://pokeapi.co/api/v2/pokemon/pikachu"
#     try:
#         response = requests.get(url)
#         details = response.json()

#         if isinstance(details, dict):
#             name = details['name']
#             print(f"\nName: {name.capitalize()}\nAbilities:")
#             for info in details['abilities']:
#                 ability = info.get('ability')
#                 abilities.append(ability['name'])
#                 for i in range(len(abilities)):
#                     print(f"\t- {abilities[i].capitalize()}")
#         else:
#             status = details.get("status")
#             reason = details.get("reason")
#             print(f"Error: {status}: {reason}")
#     except requests.exceptions.RequestException as e:
#         print(f"Error: {e}")

# fetch_pokemon_data()

""" Task 3 """

def fetch_pokemon_data(pokemon_name):
    abilities = []
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    try:
        response = requests.get(url)
        details = response.json()

        if isinstance(details, dict):
            name = details['name']
            weight = details['weight']
            print(f"\nName: {name.capitalize()}\nWeight: {weight}\nAbilities:")
            for info in details['abilities']:
                ability = info.get('ability')
                abilities.append(ability['name'])
                for i in range(len(abilities)):
                    print(f"\t- {abilities[i].capitalize()}")
            return weight
        else:
            status = details.get("status")
            reason = details.get("reason")
            print(f"Error: {status}: {reason}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


def calculate_average_weight(weight, num_of_pokemon):
    total_weight = sum(weight)
    return total_weight / num_of_pokemon


def catch_em_all(pokemon_names):
    weight = []
    num_of_pokemon = len(pokemon_names)
    for pokemon_name in pokemon_names:
        weight.append(fetch_pokemon_data(pokemon_name))
    average_weight = calculate_average_weight(weight, num_of_pokemon)
    print(f"\nAverage Weight: {average_weight}\n")


pokemon_names = ["pikachu", "bulbasaur", "charmander"]
catch_em_all(pokemon_names)