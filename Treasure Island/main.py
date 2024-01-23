print("----Welcome to to Treasure Island----")
print("Your mission is to find the treasure.")
choice1 = input('You are at the crossroad , Where do you want to go?'
                'Type "left" or "right" : ').lower()
if choice1 == "left":
    choice2 = input('You have come to lake . There is an island in the middle of the lake. '
          'Type "wait" to wait for the boat.Type "swim" to swim.:').lower()
    if choice2 == "wait":
        choice3 = input("You arrived at the island unharmed. There is a house with 3 doors."
              "One red ,one is yellow and one door is blue choose one :").lower()
        if choice3 == "red":
            print("It is room of fire .Game Over")
        elif choice3 == "yellow":
            print("You won")
        elif choice3 == "blue":
            print("You enter a room of beasts .Game Over")
        else:
            print("You choose a door that doesn't exist.Game Over")

    else:
        print("You got attacked by an angry trout.Game Over")

else:
    print("You fell into a hole .Game Over")

