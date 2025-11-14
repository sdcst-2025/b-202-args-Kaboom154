"""
Sum of numbers
Create a function called addNumbers() that makes use of *args to receive a variable number of inputs.  
The return value should be the sum of the numbers.  
Use the assertion statements below to test your results:
```
assert addNumbers(1,2,3,4,5) == 15
assert addNumbers(2,5,6,10,12,20) == 55
```
"""

def addNumbers(*args):
    totalSum = 0
    for i in args:
        totalSum += i

    return totalSum

assert addNumbers(1,2,3,4,5) == 15
assert addNumbers(2,5,6,10,12,20) == 55