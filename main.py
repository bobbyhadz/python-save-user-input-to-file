# Save user input to a File in Python

# ✅ Save user input to file
file_name = 'example.txt'

with open(file_name, 'w', encoding='utf-8') as my_file:
    my_file.write(input('Your message: '))

# -------------------------------------------------

# ✅ Take a filename and contents of a file from user input

file_name = input('Filename with extension, e.g. example.txt: ')

with open(file_name, 'w', encoding='utf-8') as my_file:
    my_file.write(input('Your message: '))