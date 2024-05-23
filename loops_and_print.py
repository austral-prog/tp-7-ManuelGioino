def enumerate_list(lista):
    lista_enumerada = []
    counter = 0
    for indice, valor in enumerate(lista):
        if valor:    
            lista_enumerada.append(f"{counter}. {valor.title()}")
            counter +=1
    return lista_enumerada


def enumerate_backwards(colors):
    new_list = []
    counter = 0
    for indice, valor in enumerate(colors):
        if valor:
            new_element = f"{counter}. {valor[::-1]}"
            new_list.append(new_element)
            counter += 1
    return new_list
colors = ["Red", "Green", "", "White", "Black", ""]
print(enumerate_list(colors))  
print(enumerate_backwards(colors)) 
