#Task 1
#iterate a String
#one character at a time
# [ ] Get user input for first_name
# [ ] iterate through letters in first_name
#    - print each letter on a new line

first_name=input("Introduce tu nombre: ")

for letra in first_name:
    print(letra)

print()
#Task 2: Program: capitalize-io, get user input for first_name,
# create an empty string variable: new_name, iterate through
# letters in first_name add each letter in new_name, capitalize
# if letter is an "i" or "o" *(hint: if, elif, else), print new_name
first_name="vitaliy"
new_name=""
for ltr in first_name:
    if ltr=="i":
        new_name += ltr.capitalize()
    elif ltr=="o":
        new_name += ltr.capitalize()
    else:
        new_name+=ltr

print(first_name, " vs ", new_name)
