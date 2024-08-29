
import requests

""" Task 2 """

# def fetch_planet_data():
#     url = "https://api.le-systeme-solaire.net/rest/bodies/"
#     response = requests.get(url)
#     planets = response.json()['bodies']

#     #process each planet info
#     for planet in planets:
#         if planet['isPlanet']:
#             name = planet['englishName']
#             mass = planet['mass']['massValue']
#             orbit_period = planet['sideralOrbit']
#             print(f"\nPlanet: {name}\n- Mass: {mass}\n- Orbit Period: {orbit_period} days\n")

# fetch_planet_data()


""" Task 3 """

def fetch_planet_data():
    planet_list = []
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planets = response.json()['bodies']

    #process each planet info
    for planet in planets:
        if planet['isPlanet']:
            name = planet['englishName']
            mass = planet['mass']['massValue']
            orbit_period = planet['sideralOrbit']
            print(f"\nPlanet: {name}\n- Mass: {mass}\n- Orbit Period: {orbit_period} days\n")
            planet_list.append({name: mass})
    return planet_list

def find_heaviest_planet(planets):
    for planet in planets:
        flattened_data = {list(planet.keys())[0]: list(planet.values())[0]}
        heaviest_planet_name = max(flattened_data, key=flattened_data.get)
        heaviest_planet_mass = flattened_data[heaviest_planet_name]
        return heaviest_planet_name, heaviest_planet_mass


planets = fetch_planet_data()
name, mass = find_heaviest_planet(planets)
print(f"The heaviest planet is {name} with a mass of {mass} kg.\n")
