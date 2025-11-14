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

    myList = []
    for i in range(0,count+1):
        myList.append(args.count(args[i]))
    myList.sort(reverse=True)
    if myList.count(myList[0]) > myList[0]:
        mode = "multiple possible modes"
    elif myList.count(myList[0]) == myList[0]:
        mode = args[args.index(myList[0])]

    midpoint = (args[0] + args[count]) / 2

    return median,mode,midpoint



assert centralTendency(8, 6, 6, 4, 6, 7, 10, 3, 1, 3, 9, 7, 9, 6, 5, 6, 5, 1, 6, 3) == (6,6,5.5)
assert centralTendency(5, 5, 8, 10, 4, 7, 5, 6, 9, 9, 5, 4, 7, 7, 3, 8, 2, 3, 5, 9) == (5.5,5,6)
