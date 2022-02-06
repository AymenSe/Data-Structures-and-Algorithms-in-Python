'''
Python allows negative integers to be used as indices into a sequence,
such as a string. If string s has length n, and expression s[k] is used
for index -n ≤ k < 0, what is the equivalent index j ≥ 0 such that s[j] references
the same element?
'''
# s = 'abcdef'
# s[-1] ==> 'd'
# s[len(s) - 1] ==> 'd'
# So j = len(s) - k

def check_indices(s):
    length = len(s)
    for k in range(1,length+1):
        print(f'{s[-k]} == {s[length - k]}')

if __name__ == '__main__':
    check_indices('Helloooo!!! how are ya!')