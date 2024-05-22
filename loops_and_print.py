def enumerate_list(colors):
	lista_enumerada = []
	for indice, valor in enumerate(colors):
		if valor: 
			lista_enumerada.append(f"{len(lista_enumerada)}. {valor.title()}")
			return lista_enumerada
colors = ["Red","Green","","White","Black",""]
lista_enumerada = enumerate_list(colors)
print(lista_enumerada)


def enumerate_backwards(colors):
    newlist2 = []
    index2 = 0
    for element in colors:
        if len(element) > 0:
            newlist2.append(f"{index2}. {element [::-1]}")
            index2 += 1
    return newlist2
print(enumerate_backwards(colors))
