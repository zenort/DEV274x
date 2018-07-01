#Task 1 .append()
# Currency Values
# [ ] create a list of 3 or more currency denomination values, cur_values
# cur_values, contains values of coins and paper bills (.01, .05, etc.)
# [ ] print the list
cur_values=[.01, 0.5, 0.10, 0.2, 0.7]
print(cur_values)

# [ ] append an item to the list and print the list
cur_values.append(0.50)
print(cur_values)

# Currency Names
# [ ] create a list of 3 or more currency denomination NAMES, cur_names
# cur_names contains the NAMES of coins and paper bills (penny, etc.)
cur_names=["Bitcoin", "Siacoin", "Cardano", "Ethereum", "IOTA"]
# [ ] print the list
print(cur_names)
# [ ] append an item to the list and print the list
cur_names.append("Ripple")
print(cur_names, "\n\n")


#Task 2 Append items to a list with input()
# [ ] append additional values to the Currency Names list using input()
add_names=input("Introduce otro nombre de moneda: ")
cur_names.append(add_names)
# [ ] print the appended list
print(cur_names)

#Task 3 while loop .append()
#define an empty list: bday_survey
#get user input, bday, asking for the day of the month they were born (1-31) or "q" to finish
#using a while loop (while user not entering "quit")
#append the bday input to the bday_survey list
#get user input, bday, asking for the day of the month they were born (1-31) or "q" to finish
#print bday_survey list
# [ ] complete the Birthday Survey task above
print("\n\n\n")
bday_survey=[]
while True:
    diadenacimiento=input("Introduce tu dia de nacimiento (1-31) o \"q\" para salir: ")
    if diadenacimiento=="q":
        break
    bday_survey.append(diadenacimiento)
print("Lista de Cumpleaños:", bday_survey, "\n\n")

#Task 4 Fix The Error
# [ ] Fix the Error
three_numbers = [1, 1, 2]
print("an item in the list is: ", three_numbers[0])


