''' 
This code is to calculate the frequency of the sequence.
First, provide a sequence as the input.
Second, create an empty dictionary, b.
Second, check each base in the sequence, set the count as 1 in the first step.
Third, increment 1 to the count.

'''
def function1(a):
# a is the sequence
    b = dict()
    for c in a:
        if c not in b:
            b[c] = 1
        else:
            b[c] += 1
    return b

def function2(a):
    print('freqsfind ')
    total = float(sum([a[b] for b in a.keys()]))
    for b in a.keys():
        print(b + ':' + str(a[b]/total))

function2(function1('ATCTGACGCGCGCCGC'))
