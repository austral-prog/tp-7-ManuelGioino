def index_of_by_index(word, list, index):
    index = index
    while index < len(list):
        if word == list[index]:
            return index
        index += 1 
    return -1 

def index_of_empty(list):
    index = 0
    while index < len(list):
        if list[index] == "":
            return index
        index += 1 
    return -1   

def index_of(word, list):
    index = 0
    while index < len(list):
        if word == list[index]:
            return index
        index += 1 
    return -1   
def put(word, list):
    index = 0
    while index < len(list):
        if list[index] == "":
            list[index] = word
            return index
        index += 1
    return -1




def remove(word, list):
    index = 0
    eliminations = 0
    while index < len(list):
        if word == list[index]:
            list[index] = ""
            eliminations += 1
        index += 1
    return eliminations
