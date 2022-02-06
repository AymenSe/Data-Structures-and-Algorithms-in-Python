'''
Write a short Python function that takes a sequence of integer values 
and determines if there is a distinct pair of numbers in the sequence whose
product is odd.
'''

def product_odd(data):
    first = data[0]
    for i in range(len(data)):
        for j in range(len(data)):
            if (data[i] != data[j]) and (data[i] * data[j]) % 2 == 1:
                return data[i], data[j]
    return None

if __name__ == '__main__':
    data = list(range(50, 154))
    res = product_odd(data)
    assert res[0] * res[1] % 2 == 1, f'{res} product is not odd!'
