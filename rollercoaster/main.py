print("---welcome to roller coaster---")
height = int(input("What is your height in cm : "))
bill = 0
if height >= 120:
    print("You can ride the roller coaster")
    age = int(input("What is your age : "))
    if age <= 12:
        bill = 25
        print("Child tickets are Rs 25")
    elif age <= 18:
        bill = 50
        print("youth tickets are Rs 50")
    else:
        bill = 100
        print("adult tickets are Rs 100")
    wants_photo = input("Do you want a photo? Y or N : ")
    if wants_photo == "Y":
        bill += 10
    print(f"Your final bill is {bill} ")
else:
    print("Sorry ! you have to grow taller before you can ride")
