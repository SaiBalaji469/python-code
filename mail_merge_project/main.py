PLACEHOLDER = "[name]"

with open("names.txt") as names_file:
    names = names_file.readlines()

with open("letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)