'''
 Write a short Python function, is even(k), that takes an integer value and
returns True if k is even, and False otherwise. However, your function
cannot use the multiplication, modulo, or division operators.
'''

def is_even(k):
    while True:
        if k == 0:
            return True
        elif k == 1:
            return False
        else:  
            k -= 2

if __name__ == '__main__':
    for i in range(21):
        res = 'even' if is_even(i) else 'odd'
        print(f'{i} is {res}')
