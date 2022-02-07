'''
Had we implemented the scale function (page 25) as follows, does it work
properly?
'''
'''
Answer:
It does not work because the values inside the data 
are numerical values so they are immutable so what happend is 
that new instances (alias for data's elements) are created and assinged with the new values
- and these instances have nothing to do with data - So the actual 
values inside data will not change.
'''
def scale(data, factor):
    print(data)
    for val in data:
        val *= factor
    print(data)



if __name__ == '__main__':
    data = [1, 2, 3]
    scale(data, 2)
