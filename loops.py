def index_of_by_index(word, list, index):
    index = index
    while index < len(list):
        if word == list[index]:
            return index
        index += 1 
    return -1 


def index_of_empty(list):
     for index, element in enumerate(list):
        if element == "":
            return index
        else:
            index += 1
        return -1


def index_of(word, list):
    index = 0 
    for element in list:
        if word == element:
            return index
        index += 1
    return -1

def put(word, list):
    for indice, valor in enumerate(list):
        if valor == '':
            list[indice]=word
            return indice
    return -1


def remove(word, list):
    count = 0
    for index, element in enumerate(list):
        if element == word:
            list[index] = ""
            count += 1
            return count
        return -1
