# import request
import random

char = {
    "bulbasaur": 1,
    "ivysaur": 2,
    "venusaur": 3,
    "charmander": 4,
    "charmeleon": 5
}

bmi = {
        "bulbasaur": {"height": 7, "weight": 69},
        "ivysaur": {"height": 10, "weight": 130},
        "venusaur": {"height": 20, "weight": 1000},
        "charmander": {"height": 6, "weight": 85},
        "charmeleon": {"height": 11, "weight": 190},
    }

print("======WHO'S THAT POKEMON?=====")
print("")
ask  = input("Select a number from 1-5: ")
print("")

# for
if ask == "1":
    print(f"Bulbasaur: Height - {bmi['bulbasaur']['height']}, Weight - {bmi['bulbasaur']['weight']}")
elif ask == "2":
    print(f"Ivysaur: Height - {bmi['ivysaur']['height']}, Weight - {bmi['ivysaur']['weight']}")
elif ask == "3":
    print(f"Venusaur: Height - {bmi['venusaur']['height']}, Weight - {bmi['venusaur']['weight']}")
elif ask == "4":
    print(f"Charmander: Height - {bmi['charmander']['height']}, Weight - {bmi['charmander']['weight']}")
elif ask == "5":
    print(f"Charmeleon: Height - {bmi['charmeleon']['height']}, Weight - {bmi['charmeleon']['weight']}")
else:
    print("Please input a valid number!")