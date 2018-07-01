def list_o_matic(list, input_pasado):
    while list:
        if input_pasado in list:
            list.remove(input_pasado)
            return print("look at the animals:",list)
        else:
            list.append(input_pasado)
            return print("look at the animals:",list)
    list.pop()
    return print(list)

animals=['cat', 'goat', 'cat']
print(animals)
print("\n")

while animals:
    input_animal=input("Introduce el nombre de un animal: ")
    if input_animal=="quit":
        print("Goodbye!")
        break

    list_o_matic(animals,input_animal)




