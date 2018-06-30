#                       Task 1

# [ ] assign a string 5 or more letters long to the variable: street_name
# [ ] print the 1st, 3rd and 5th characters

street_name="Aguilar"
print(street_name[0])
print(street_name[2])
print(street_name[4])

# [ ] Create an input variable: team_name - ask that second letter = "i", "o", or "u"
# [ ] Test if team_name 2nd character = "i", "o", or "u" and print a message
# note: use if, elif and else

team_name=input("introduce nombre de equipo: ")
if team_name[1] =="i":
    print("segundo caracter es:", team_name[1])
elif team_name[1]=="o":
    print("segundo caracter es:", team_name[1])
elif team_name[1]=="u":
    print("segundo caracter es:", team_name[1])