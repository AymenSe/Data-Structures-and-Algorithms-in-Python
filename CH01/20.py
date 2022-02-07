'''
Python's random module includes a function shuffle(data) that accepts a
list of elements and randomly reorders the elements so that each possible
order occurs with equal probability. The random module includes a
more basic function randint(a, b) that returns a uniformly random integer
from a to b (including both endpoints). Using only the randint function,
implement your own version of the shuffle function.
'''

from random import randint
from re import A


def myShuffle(data): 
    random_list = []
    cond = 0
    while cond < len(data):
        random_value = randint(0, len(data) - 1)  
        if not random_value in random_list:
            random_list.append(random_value)
            data[cond], data[random_value] = data[random_value], data[cond]
            cond += 1


if __name__ == '__main__':
    data = list(range(100))
    print(data)
    myShuffle(data)
    print(data)