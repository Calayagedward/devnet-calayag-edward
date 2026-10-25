import random
import requests

char = {
    "bulbasaur": 1,
    "ivysaur": 2,
    "venusaur": 3,
    "charmander": 4,
    "charmeleon": 5
}

# randomly select a Pokemon
ask = random.choice(list(char.keys()))

print("====== WHO'S THAT POKEMON? ======")
print("Guess the Pokemon using its height and weight!")
print("You have 3 attempts.\n")


url = f"https://pokeapi.co/api/v2/pokemon/{ask}"

try:
    response = requests.get(url, timeout=10)

    if response.status_code == 200:
        data = response.json()


        bmi = {
            ask: {
                "height": data["height"],
                "weight": data["weight"]
            }
        }

        print(f"Height: {bmi[ask]['height']} decimeters")
        print(f"Weight: {bmi[ask]['weight']} hectograms")

        attempts = 3

        while attempts > 0:
            guess = input("\nGuess the Pokemon: ").strip().lower()

            if guess not in char:
                print("Please input a valid Pokemon name!")
                continue

            if guess == ask:
                print("Correct! You guessed the Pokemon!")
                print(f"The Pokemon is {ask.capitalize()}!")
                break

            else:
                attempts -= 1

                if attempts > 0:
                    print(f"Wrong guess! You have {attempts} attempts left.")
                else:
                    print("Game over!")
                    print(f"The correct Pokemon was {ask.capitalize()}.")

    else:
        print("Unable to retrieve Pokemon data.")
        print("HTTP Status Code:", response.status_code)

except requests.exceptions.RequestException:
    print("Network error! Please check your internet connection.")
