'''
Write a Python function that takes a sequence of numbers and determines
if all the numbers are different from each other (that is, they are distinct).
'''


def are_distinct(data): 
    starter = 0
    while starter < len(data): 
        first = data[starter]
        i = starter + 1
        while i < len(data):
            if first == data[i]:
                return False
            i += 1
        starter += 1
    return True


if __name__ == '__main__':
    data = [1, 2, 3, 4, 5]
    data2 = [1, 2, 3, 4, 4]

    assert are_distinct(data) == True, 'Error!'
    assert are_distinct(data2) == False, 'Error!'
    