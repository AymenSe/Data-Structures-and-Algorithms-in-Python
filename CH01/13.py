'''
Write a pseudo-code description of a function that reverses a list of n
integers, so that the numbers are listed in the opposite order than they
were before, and compare this method to an equivalent Python function
for doing the same thing.
'''

def reverse_list(data):
    return data[::-1]

if __name__ == '__main__':
    data = list(range(15))
    data.reverse()
    assert data == reverse_list(list(range(15))), 'Error!'