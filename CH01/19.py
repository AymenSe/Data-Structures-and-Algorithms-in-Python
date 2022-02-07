'''
Demonstrate how to use Python's list comprehension syntax to produce
the list [ a , b , c , ..., z ], but without having to type all 26 such
characters literally.
'''

def charList():
    return [chr(i) for i in range(97, 97+26)]

if __name__ == '__main__':
    res = charList()
    print(res)