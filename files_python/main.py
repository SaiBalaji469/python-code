# a file named "data", will be opened with the reading mode.
file = open('data.txt', 'r')

# This will print every line one by one in the file
contents = file.read()
print(contents)
file.close()

