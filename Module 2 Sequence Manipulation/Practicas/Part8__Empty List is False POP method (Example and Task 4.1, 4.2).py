#Example
dog_types = ["Lab", "Pug", "Poodle"]

while dog_types:
    print(dog_types.pop())

print("\n\n\n")

#Task 4.1
purchase_amount=[]

while True:
    lista_compra=input("Introduce la lista de compra, para acabar con la lista escibir \"done\": ")
    if lista_compra=="done":
        break
    purchase_amount.append(lista_compra)

print("Las lista de compra es: ", purchase_amount)

print("\n\n")
#Task 4.2
subtotal=0
while purchase_amount:
    subtotal+=float(purchase_amount.pop())

print(subtotal)


