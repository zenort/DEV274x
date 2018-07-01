#------------------------------------------------Examples---------------------------------------
# [ ] review and run example
# pop() gets the last item by default
party_list = ["Joana", "Alton", "Tobias"]
print(party_list)
print("Hello,", party_list.pop())

print("\n", party_list)
print("Hello,", party_list.pop())

print("\n", party_list)
print("Hello,", party_list.pop())

print("\n", party_list)
# [ ] review and run example
# can pop specific index like pop(3)
number_list = [11, 21, 13, 14, 51, 161, 117, 181]
print("before:", number_list)
number_list.pop(3)
print("after :", number_list)

# [ ] review and run example
# set a variable to a poped value
number_list = [11, 21, 13, 14, 51, 161, 117, 181]
print("list before:", number_list)
num_1 = number_list.pop()
num_2 = number_list.pop()
print("list after :", number_list)
print("add the popped values:", num_1, "+", num_2, "=", num_1 + num_2)
print("\n\n\n")
#-----------------------------------------------Fin  Ejemplo-------------------------------------


#Task 3 pop()
# [ ] pop() and print the first and last items from the ft_bones list
ft_bones = ["calcaneus", "talus", "cuboid", "navicular", "lateral cuneiform",
            "intermediate cuneiform", "medial cuneiform"]
print(ft_bones)
first=ft_bones.pop(0)
last=ft_bones.pop()
# [ ] print the remaining list
print("El primero borrado:",first, "y el ultimo borrado:",last)
print(ft_bones)


