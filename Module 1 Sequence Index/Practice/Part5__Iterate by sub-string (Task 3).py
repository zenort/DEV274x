#Task 3
#String slicing and iteration
# [ ] create & print a variable, other_word, made of every other letter in long_word
long_word = "juxtaposition"
other_word=""
for letra in long_word:
    other_word+=letra
print(other_word)

print()
# Mirror Color
# [ ] get user input, fav_color
# [ ] print fav_color backwards + fav_color
# example: "Red" prints "deRRed"
modif_color=""

fav_color=input("introduce color en ingles: ")
for letra in fav_color[::-1]:
    modif_color+=letra
for letra in fav_color[::]:
    modif_color += letra

print(modif_color)





