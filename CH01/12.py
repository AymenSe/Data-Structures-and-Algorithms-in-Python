'''
Python's random module includes a function choice(data) that returns a
random element from a non-empty sequence. The random module includes a
more basic function randrange, with parameterization similar to
the built-in range function, that return a random choice from the given
range. Using only the randrange function, implement your own version
of the choice function.
'''

from random import randrange


def choice(data):
    l = len(data)
    idx = randrange(0, l)
    return data[idx]

if __name__ == '__main__':
    data = list(range(100))
    print(choice(data))