#Task 1 len()
# [ ] use len() to find the midpoint of the string
# [ ] print the halves on separate lines
print("Task 1")
random_tip = "wear a hat when it rains"
mid_point =int(len(random_tip)/2)
print(random_tip[:mid_point])
print(random_tip[mid_point:])

print()
print()
#Task 2 .count()
# for letters: "e" and "a" in random_tip
# [ ] print letter counts
# [ ] BONUS: print which letter is most frequent
print("Task 2")
random_tip = "wear a hat when it rains"
print(random_tip.count("e"))
print(random_tip.count("a"))
if random_tip.count("e")>random_tip.count("a"):
    print("\"e\" es más frecuente")
else:
    print("\"a\" es más frecuente")

print()
print()
#Task 3 .find()
# [ ] print long_word from the location of the first and second "t"
print("Task 3")
long_word = "juxtaposition"
location =long_word.find("t")
while location >=0:
    print(location)
    location = long_word.find("t", location + 1)


print()
print()
#Task 4 Program: print each word in a quote
# code to print word (index slice start:space_index): Output should look like below: they   stumble who run fast
    # [ ] Print each word in the quote on a new line
print("Task 4")
quote = " they stumble who run fast"
print(quote)
start = 0
space_index = quote.find(" ")
while space_index != -1:
    print(quote[start:space_index])
    start=space_index
    space_index=quote.find(" ", space_index+1)






