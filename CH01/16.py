'''
In our implementation of the scale function (page 25), the body of the loop
executes the command data[j] *= factor. We have discussed that numeric
types are immutable, and that use of the *= operator in this context causes
the creation of a new instance (not the mutation of an existing instance).
How is it still possible, then, that our implementation of scale changes the
actual parameter sent by the caller?
'''
'''
Answer: The reason why the actual parameter sent by the function caller is changed
is that the parameter is a list (array) and that particular element of the array
is assigned to a new numeric object.
'''

def scale(data, factor):
    # print(id(data))
    for j in range(len(data)):
        print(f'before: {id(data[j])}')
        data[j] *= factor
        print(f'After: {id(data[j])}')
    # print(id(data))
    print(data)

if __name__ == '__main__':
    data = [1, 2, 3]
    scale(data, 2)
