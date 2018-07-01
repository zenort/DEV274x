#Task 3 insert() input into a list
# [ ] insert a name from user input into the party_list in the second position (index 1)
party_list = ["Joana", "Alton", "Tobias"]
user_input=input("Introduce un nombre: ")
party_list.insert(1,user_input)
# [ ] print the updated list
print(party_list)


print("\n\n")

#Task 4 Fix The Error
# [ ] Fix the Error
tree_list = ["oak"]
print("tree_list before =", tree_list)
tree_list.insert(1,"pine")
print("tree_list after  =", tree_list)

