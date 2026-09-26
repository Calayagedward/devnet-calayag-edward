"""
Midterm Practical Exam — Pet Adoption Records Manager
Student: Calayag, Edward P.
"""

pets = []  # starts empty — the user adds pets as the program runs

add_pet = 1
view_pets = 2
count_available_adopted = 3
find_pet = 4
remove_pet = 5
exit = 6


print("=== Pet Adoption Records ===")
print("1. Add a pet")
print("2. View all pets")
print("3. Count Available vs adopted")
print("4. Find a pet by name")
print("5. Remove Pet")
print("6. Exit")

user = int(input("What you gonna do?(Choose 1 - 5:"))
for i in pets:
        if user == 1 :
            pet = input("Name of your new pet?: ")
            # result = add_pet + pet_list
            # print (result)

        elif user == 2 :
                print(view_pets)

        elif user == 3 :
                print(count_available_adopted)

        elif user == 4:
                print(find_pet)
                
        elif user == 5:
                print(remove_pet)

        else:
            print("Invalid Input")
        

    # def display_menu():
    # # print the menu, return the user's choice
            def add_pet(pet_list):
    # ask for name, animal type, status — build the string, add to the list
                pass

            def view_pets(pet_list):
    # loop through and print every pet — handle empty list
                pass
            def count_available_adopted(pet_list):
    # loop through, count Available vs Adopted, return both
                pass
            def find_pet(pet_list):
    # ask for a name, search the list, print result or "not found"
                pass
    # BONUS (optional)
            def remove_pet(pet_list):
    # your code here
                pass

            def main():
                running = True
                while running:
                    choice = display_menu()
        # use if/elif to call the right function based on choice
        # set running = False when the user picks Exit
