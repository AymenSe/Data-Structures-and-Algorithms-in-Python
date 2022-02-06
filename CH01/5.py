'''
ive a single command that computes the sum from Exercise R-1.4,
relying on Python comprehension syntax and the built-in sum function.
'''

def square_sum(n):
    return sum([r**2 for r in range(1, n)])

if __name__ == '__main__':
    res = square_sum(5)
    assert res == 30, f'{res} not equal 30'