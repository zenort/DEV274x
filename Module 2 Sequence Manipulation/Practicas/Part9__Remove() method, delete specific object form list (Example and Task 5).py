#--------------------------------------------Examples--------------------------------------
# [ ] review and run example
dog_types = ["Lab", "Pug", "Poodle"]

if "Pug" in dog_types:
    dog_types.remove("Pug")
else:
    print("no Pug found")
print(dog_types)
# [ ] review and run example
dogs = ["Lab", "Pug", "Poodle", "Poodle", "Pug", "Poodle"]

print(dogs)
while "Poodle" in dogs:
    dogs.remove("Poodle")
    print(dogs)

print("\n\n\n")
#-------------------------------------------Fin Ejemplo-------------------------------------


#Task 5 .remove()
# [ ] remove one "Poodle" from the list: dogs , or print "no Poodle found"
# [ ] print list before and after
dogs = ["Lab", "Pug", "Poodle", "Poodle", "Pug", "Poodle"]
print(dogs)
while "Poodle" in dogs: # if "Poodle" in dogs: (entonces solo removería uno de los Poodle)
    dogs.remove("Poodle")
else:
    print("No \"Poodle\" found")

print(dogs)

