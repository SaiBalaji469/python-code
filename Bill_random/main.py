import random
names_string = input("Give me everybody's names,seperated by a comma and space. : ")
names = names_string.split(", ")
# num_items = len(names)
# random_choice = random.randint(0,num_items - 1)
# person_who_will_pay = names[random_choice]
person_who_will_pay = random.choice(names)
print(f"{person_who_will_pay} is going to pay bill today.")