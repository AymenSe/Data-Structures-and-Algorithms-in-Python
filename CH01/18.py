'''
Demonstrate how to use Python's list comprehension syntax to produce
the list [0, 2, 6, 12, 20, 30, 42, 56, 72, 90].
'''

def pronicNumbers(n):
    return [i * (i + 1) for i in range(n)]

if __name__ == '__main__':
    res = pronicNumbers(10)
    print(res)