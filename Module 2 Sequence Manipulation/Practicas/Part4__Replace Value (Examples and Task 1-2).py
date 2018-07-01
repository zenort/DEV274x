#----------------------------------------------Examples-------------------------------------------------------
# [ ] review and run example
# the list before Insert
party_list = ["Joana", "Alton", "Tobias"]
print("party_list before: ", party_list)

# the list after Insert
party_list[1] = "Colette"
print("party_list after:  ", party_list)
# [ ] review and run example
party_list = ["Joana", "Alton", "Tobias"]
print("before:",party_list)

# modify index value
party_list[1] = party_list[1] + " Derosa"
print("\nafter:", party_list)

# [ ] review and run example changes the data type of an element
# replace a string with a number (int)
single_digits = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
print("single_digits: ", single_digits)
print("single_digits[3]: ", single_digits[3], type(single_digits[3]),"\n")

# replace string with an int
single_digits[3] = 3
print("single_digits: ", single_digits)
print("single_digits[3]: ", single_digits[3], type(single_digits[3]))
print("\n\n\n\n")
#--------------------------------------------Fin Ejemplo--------------------------------------------------------

#Task 1.1 replace items in a list
three_num=[2, 7, 10]
print(three_num)

if three_num[0] <5:
    three_num[0]="small"
else:
    three_num[0]="large"

print(three_num,"\n\n\n")

#Task 1.2: Create a function, str_replace, that takes 2 arguments: int_list and index
#int_list is a list of single digit integers
#index is the index that will be checked - such as with int_list[index]
#Function replicates purpose of task "replace items in a list" above and replaces an
#integer with a string "small" or "large"
#return int_list

def str_replace(int_list, index):
    if int_list[index] < 5:
        int_list[index] = "small"
    else:
        int_list[index] = "large"
    return int_list

lista_a_enviar=[2, 6, 10, 12]

print(str_replace(lista_a_enviar, 2))


#Task 2
print("\n\nTask 2")
tres_palabras=["Gato", "Perro", "Mono"]
print(tres_palabras)

tres_palabras[0]=tres_palabras[0].upper()
tres_palabras[2]=tres_palabras[2].swapcase()
print(tres_palabras)


