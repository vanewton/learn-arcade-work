import random
def main():
    print()
    print("Welcome to Camel!")
    print("You have stolen a camel to make your way across the great Mobi desert.")
    print("The natives want their camel back and are chasing you down!")
    print("Survive your desert trek and outrun the natives!")

miles_traveled = 0
thirst = 0
camel_tiredness = 0
natives_distance = -20
canteen = 3


done = False
while not done:
    print()
    print("A. Drink from canteen.")
    print("B. Ahead moderate speed.")
    print("C. Ahead full speed.")
    print("D. Stop for the night.")
    print("E. Status check.")
    print("Q. Quit.")


user_choice = input("What is your choice? ")
if user_choice == "Q":
    print ("Get outta here!")
    done = True
elif user_choice == "E":
    print("You have traveled " + str(miles_traveled) + " miles.")
    print("You have " + str(canteen) + " drinks left.")
    print("The natives are " + str(miles_traveled - natives_distance) + " miles away.")
elif user_choice == "D":
    print("You have decided to rest for the night.")
    print("Your camel is resting and happy! :)")
    print("The natives are " + str(random.randrange(7,14) + "miles away."))
elif user_choice == "C":
    print("You have chosen to continue at full speed.")
    print("You have traveled " + str(random.randrange(10,20) + " miles."))
    thirst = thirst + 1
    camel_tiredness = camel_tiredness + random.randrange(1,3)
    natives_distance = natives_distance + random.randrange(7,14)
elif user_choice == "B":
    print("You go ahead at moderate speed.")
    print("You have traveled " + str(miles_traveled + random.randrange(5,12) + " miles."))
    thirst = thirst + 1
    camel_tiredness = camel_tiredness + 1
elif user_choice == "A":
    print("You chose to drink from your canteen.")







main()