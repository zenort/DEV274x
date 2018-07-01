#-------------------------------------------Examples--------------------------------------
# [ ] review and run example
# the list before delete
sample_list = [11, 21, 13, 14, 51, 161, 117, 181]
print("sample_list before: ", sample_list)

del sample_list[1]
# the list after delete
print("sample_list after:  ", sample_list)
# [ ] review and run example Multiple Times
# [ ] consider how to reset the list values?
print("sample_list before:", sample_list)
del sample_list[0]
print("sample_list after:", sample_list)
# [ ] review and run example
mixed_types = [1, "cat"]
# append number
mixed_types.append(3)
print("mixed_types list: ", mixed_types)

# append string
mixed_types.append("turtle")
print("mixed_types list: ", mixed_types)

#-----------------------------------------FIN Ejemplo---------------------------------------
print("\n\n\nTask 1")
#Task 1 del statement
# [ ] print ft_bones list
# [ ] delete "cuboid" from ft_bones
# [ ] reprint list
ft_bones = ["calcaneus", "talus", "cuboid", "navicular", "lateral cuneiform",
            "intermediate cuneiform", "medial cuneiform"]
print(ft_bones)
del ft_bones[2]
print(ft_bones)

print("\n\nTask 2")
#Task 2 multiple del statements
# [ ] print ft_bones list
# [ ] delete "cuboid" from ft_bones
# [ ] delete "navicular" from list
# [ ] reprint list
# [ ] check for deletion of "cuboid" and "navicular"
ft_bones = ["calcaneus", "talus", "cuboid", "navicular", "lateral cuneiform",
            "intermediate cuneiform", "medial cuneiform"]
print(ft_bones)
del ft_bones[2]
del ft_bones[2]
print(ft_bones)


