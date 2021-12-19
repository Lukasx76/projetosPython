def is_anagram(test, original):
    lst1 = []
    lst2 = []

    temp_string1 = "" # string temporaria para armazenar a string caso ela esteja capitalizada, para o programa não diferenciar letras maisculas e minusculas
    temp_string2 = "" # string temporaria para armazenar a string caso ela esteja capitalizada, para o programa não diferenciar letras maisculas e minusculas

    for l in test:

        if l.isupper(): # caso letra do primeiro parametro esteja capitalizada ela será "descapitalizada"
            temp_string1 += l.lower()

        else:
            temp_string1 += l # caso contrário ela será adcionada a string temportária

    for l in original:

        if l.isupper():  # caso letra do primeiro parametro esteja capitalizada ela será "descapitalizada"
            temp_string2 += l.lower()

        else:
            temp_string2 += l # caso contrário ela será adcionada a string temportária

    for letter in temp_string1.encode(): # loop para encodificar a string temporaria

        lst1.append(letter) # armazena a string em uma lista
        lst1.sort() #organiza 

    for letter in temp_string2.encode():  # loop para encodificar a string temporaria

        lst2.append(letter) # armazena a string em uma lista
        lst2.sort() #organiza 

    return True if lst1 == lst2 else False 
