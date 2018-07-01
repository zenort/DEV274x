#Parte 1
days_of_week=["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
print(days_of_week[0])
print(days_of_week[2])
print(days_of_week[4])
print(days_of_week[6])


print("\n\n")

#Parte 2
phone_letters=[" ", "", "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
print(phone_letters)

day=days_of_week[1]
print(day)

days_of_week[5]=day
print(days_of_week)

print("\n\n")

#Parte 3
days_of_week=["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
days_of_week.append("Vitaday")
print(days_of_week)

days_of_week.insert(3,"DiaIntermedio")
print(days_of_week)


# [ ] Challenge: write the code for "reverse a string" reversing some_numbers
some_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77]
nueva_lista=[]
print(some_numbers)
while some_numbers:
    reverso=0
    reverso=some_numbers.pop()
    nueva_lista.append(reverso)

reverso=nueva_lista.pop()
nueva_lista.insert(0,reverso)
print(nueva_lista)
