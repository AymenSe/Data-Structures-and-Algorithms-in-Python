class SequenceIterator:
    """ An Iterator for any of python's sequence types """

    def __init__(self, sequence) -> None:
        """ Create an iterator for the given sequence """
        self._seq = sequence
        self._k = -1

    def __next__(self):
        """ Return the next element, else raise StopIteration error. """
        self._k += 1  # Advance to the next index
        if self._k < len(self._seq): 
            return self._seq[self._k] # Return the data element
        else:
            raise StopIteration() # There are no more element
    
    def __iter__(self):
        """ By Convention, an iterator must retrun itself as an iterator. """
        return self


if __name__ == '__main__':

    data = [10, 15, 20, 30, 25, 28, 45, 49]

    iterator = SequenceIterator(data)
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
