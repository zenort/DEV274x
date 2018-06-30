quote=input("Introduce una frase: ")
quote=quote+" "
word=""
for character in quote:
    if character.isalpha():
        word+=character
    else:
        word+=" "
        if word.lower()>="h":
            print(word.upper())
            word=""
        else:
            word=""

#Texto to input: Wherever you go, go with all your heart

#Expected Result :
    # WHEREVER 
    # YOU 
    # WITH 
    # YOUR 
    # HEART

