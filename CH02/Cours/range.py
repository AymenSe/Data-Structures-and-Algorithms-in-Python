class Range:
    """ a class that mimic's the built-in range class """

    def __init__(self, start, stop=None, step=1) -> None:
        
        if step == 0:
            raise ValueError('step cannot be 0')
        
        if stop == None:
            start, stop = 0, start
        
        # Calculate the effective length once
        self._length = max(0, (stop - start + step - 1) // step)

        self._start = start
        self._step = step

    def __len__(self):
        """ Return the number of enteries in the range """
        return self._length
    
    def __getitem__(self, k):
        """ Return Entery at index k """

        if k < 0:
            k += len(self)
        
        if not 0 <= k < self._length:
            raise IndexError('index out of range')
        
        return self._start + k * self._step

if __name__ == '__main__':
    for i in Range(5):
        print(i)
    
    print('---------------------')

    for i in Range(1, 10, 2):
        print(i)
    
    

