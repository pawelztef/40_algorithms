import random

def create_nums_list(length):
    list_to_sort =  list(range(1, length+1))
    random.shuffle(list_to_sort)
    
    return list_to_sort