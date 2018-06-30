# [ ] review and run example
work_tip = "save your code"

print("number of characters in string")
print(len(work_tip),"\n")

print('letter "e" occurrences')
print(work_tip.count("e"),"\n")

print("find the index of the first space")
print(work_tip.find(" "),"\n")

print('find the index of "u" searching a slice work_tip[3:9] -', work_tip[3:9])
print(work_tip.find("u",3,9),"\n")

print('find the index of "e" searching a slice work_tip[4:] -', work_tip[4:])
print(work_tip.find("e",4))

print()
print()
# [ ] review and run example
work_tip = "good code is commented code"

print("The sentence: \"" + work_tip + "\" has character length = ", len(work_tip) )
# [ ] review and run example
# find the middle index
work_tip = "good code is commented code"
mid_pt = int(len(work_tip)/2)

# print 1st half of sentence
print(work_tip[:mid_pt])

# print the 2nd half of sentence
print(work_tip[mid_pt:])

print()
print()
# [ ] review and run example
print(work_tip)
print("how many w's? ", work_tip.count("w"))
print("how many o's? ", work_tip.count("o"))
print("uses 'code', how many times? ", work_tip.count("code"))
# [ ] review and run example
print(work_tip[:mid_pt])
print("# o's in first half")
print(work_tip[:mid_pt].count("o"))

print()
print(work_tip[mid_pt:])
print("# o's in second half")
print(work_tip[mid_pt:].count("o"))


print()
print()
# [ ] review and run example
work_tip = "good code has meaningful variable names"
print(work_tip)
# index where first instance of "code" starts
code_here = work_tip.find("code")
print(code_here, '= starting index for "code"')
# [ ] review and run example
# set start index = 13 and end index = 33
print('search for "meaning" in the sub-string:', work_tip[13:33],"\n")
meaning_here = work_tip.find("meaning",13,33)
print('"meaning" found in work_tip[13:33] sub-string search at index', meaning_here)
# [ ] review and run example
# if .find("o") has No Match, -1 is returned
print ("work_tip:" , work_tip)
location = work_tip.find("o")

# keeps looping until location = -1 (no "o" found)
while location >= 0:
    print("'o' at index =", location)
    # find("o", location + 1) looks for a "o" after index the first "o" was found
    location = work_tip.find("o", location + 1)
print("no more o's")