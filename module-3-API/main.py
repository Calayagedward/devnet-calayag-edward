
import requests
import random

# List of at least five Pokemon
pokemon_list = [
    "pikachu",
    "charizard",
    "bulbasaur",
    "squirtle",
    "gengar",
    "eevee",
    "snorlax",
    "lucario"
]


def get_pokemon_data(pokemon_name):
    """Retrieve Pokemon information from PokeAPI."""
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"

    try:
        response = requests.get(url, timeout=10)

        # Check HTTP response status
        if response.status_code == 200:
            data = response.json()

            # Extract data from the JSON response
            name = data["name"]
            height = data["height"]
            weight = data["weight"]

            return {
                "name": name,
                "height": height,
                "weight": weight
            }

        elif response.status_code == 404:
            print(f"Pokemon '{pokemon_name}' was not found.")
            return None

        else:
            print(f"HTTP Error: {response.status_code}")
            return None

    except requests.exceptions.RequestException as error:
        print("Network error. Please check your internet connection.")
        print(f"Details: {error}")
        return None

    except (KeyError, ValueError) as error:
        print("Error processing the API response.")
        print(f"Details: {error}")
        return None


def guessing_game():
    print("===================================")
    print("       POKEMON GUESSING GAME")
    print("===================================")
    print("Guess the Pokemon using its height and weight!")
    print("You have 3 attempts.\n")

    # Randomly select a Pokemon
    selected_name = random.choice(pokemon_list)

    # Retrieve the selected Pokemon's data
    pokemon = get_pokemon_data(selected_name)

    if pokemon is None:
        print("Unable to start the game. Please try again.")
        return

    # Display clues without revealing the name
    print(f"Height: {pokemon['height']} decimeters")
    print(f"Weight: {pokemon['weight']} hectograms")

    attempts = 3

    while attempts > 0:
        guess = input("\nGuess the Pokemon: ").strip().lower()

        if not guess:
            print("Please enter a Pokemon name.")
            continue

        # Check the player's guess
        if guess == pokemon["name"]:
            print("\nCorrect! You guessed the Pokemon!")
            print(f"The Pokemon was {pokemon['name'].capitalize()}.")
            return

        attempts -= 1

        if attempts > 0:
            print(f"Wrong guess! You have {attempts} attempt(s) left.")
        else:
            print("\nGame over! You used all your attempts.")
            print(f"The correct Pokemon was {pokemon['name'].capitalize()}.")


if __name__ == "__main__":
    guessing_game()
