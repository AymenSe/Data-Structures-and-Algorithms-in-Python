'''
 Write a short Python function, minmax(data), that takes a sequence of
one or more numbers, and returns the smallest and largest numbers, in the
form of a tuple of length two. Do not use the built-in functions min or
max in implementing your solution.
'''

from random import randrange


def minmax(data):
    min = data[0]
    max = data[0]
    for i in range(1, len(data)):
        min = data[i] if data[i] < min else min
        max = data[i] if data[i] > max else max
    return min, max


if __name__ == '__main__':
    data = [randrange(1, 1000, 1) for i in range(15)]
    t_max = max(data)
    t_min = min(data)
    min, max = minmax(data)
    assert t_max == max and t_min == min, f'max = {t_max} and min = {t_min} \n results: {min} and {max}'