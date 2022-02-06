'''
Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the positive integers smaller than n.
'''

def square_sum(n):
    k = 1
    res = 0
    while k < n:
        res += k**2
        k += 1
    return res

if __name__ == '__main__':
    res = square_sum(5) # 1² + 2² + 3² + 4² 
    t_res = sum([r**2 for r in range(1,5)])
    assert t_res == res, f'{t_res} not equal to {res}'