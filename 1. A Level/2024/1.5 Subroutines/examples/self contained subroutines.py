# self contained means avoid using global variables
# using modular programming, create subroutines that will:
# create an empty list
# populate the list with 30 random numbers between 1 and 5
# print the list
# remove the number 5 from the list
# print the list
import random
list = []
def run():
    list = create_empty_list() # return empty list
    list = populate_list(list)
    print_list(list)
    list = remove_five(list)
    print_list(list)

def create_empty_list():
    return []

def print_list(l):
    print(l)

def populate_list(l):
    for i in range(30):
        l.append(random.randint(1,5))
    return l

def remove_five(l):
    while True:
        if 5 in l:
            l.remove(5)
        else:
            break
    return l

run()