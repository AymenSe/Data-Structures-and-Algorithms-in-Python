'''
Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the odd positive integers smaller than n.
'''

def square_odd_sum(n):
    k = 1
    res = 0
    while k < n:
        if k % 2 == 1:
            res += k**2
        k += 1
    return res

if __name__ == '__main__':
    res = square_odd_sum(5) # 1² + 3² = 10
    assert res == 10, f'{res} not equal 10'