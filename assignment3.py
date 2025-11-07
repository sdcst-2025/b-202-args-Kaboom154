'''
Median, Mode, Midpoint
Create a function called centralTendency() that makes use of *args to receive a variable number of inputs.  The function will return 3 values, the median, mode and midpoints.  
You will need to google what these mean.

You will need to make use of list.sort() to help you with some of these

Use the assertion statments below to test your results:
```
assert CentralTendency(8, 6, 6, 4, 6, 7, 10, 3, 1, 3, 9, 7, 9, 6, 5, 6, 5, 1, 6, 3) == (4.5,6,5.5)
assert centralTendency(5, 5, 8, 10, 4, 7, 5, 6, 9, 9, 5, 4, 7, 7, 3, 8, 2, 3, 5, 9) == (5,5,6)
```
'''

#median = middle value of a list
#mode = most common value in a list
#midpoint = average of two extremes

import math

def centralTendency(*args):
    args = list(args)
    args.sort()
    count = -1
    for i in args:
        count += 1
    medianHigh = args[ math.floor(count/2) ]
    medianLow = args[ math.ceil(count/2) ]
    median = (medianHigh+medianLow) / 2

    mode = #put counts into a seperate list, reverse sort list 2

    midpoint = (args[0] + args[count]) / 2


    print(median,mode,midpoint)
    return median,mode,midpoint


centralTendency(1,2,3,4,5,6)
centralTendency(8, 6, 6, 4, 6, 7, 10, 3, 1, 3, 9, 7, 9, 6, 5, 6, 5, 1, 6, 3)
centralTendency(5, 5, 8, 10, 4, 7, 5, 6, 9, 9, 5, 4, 7, 7, 3, 8, 2, 3, 5, 9)



abcd = [8, 6, 6, 4, 6, 7, 10, 3, 1, 3, 9, 7, 9, 6, 5, 6, 5, 1, 6, 3]
abcd.sort()
abcd1 = [5, 5, 8, 10, 4, 7, 5, 6, 9, 9, 5, 4, 7, 7, 3, 8, 2, 3, 5, 9]
abcd1.sort()
print(f'\n{abcd}\n\n{abcd1}')


'''
assert centralTendency(8, 6, 6, 4, 6, 7, 10, 3, 1, 3, 9, 7, 9, 6, 5, 6, 5, 1, 6, 3) == (4.5,6,5.5)
assert centralTendency(5, 5, 8, 10, 4, 7, 5, 6, 9, 9, 5, 4, 7, 7, 3, 8, 2, 3, 5, 9) == (5.5,5,6)
'''