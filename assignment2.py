"""
Mean Value
Create a function called myAverage() that makes use of an *args argument to receive a variable number of inputs.  
There should be 2 return values: the average and the number of terms.  
Use the assertion statements below to test your results:
```
assert myAverage(3,4,5) == (4,3)
assert myAverage(1,2,5,6,10) == (4.6,5)
```

"""

def myAverage(*args):
    total = 0
    sum = 0
    for i in args:
        total += 1
    for i in args:
        sum += i
    average = sum / total
    print(average,total)
    return average,total



assert myAverage(3,4,5) == (4,3)
assert myAverage(1,2,5,6,10) == (4.8,5)
