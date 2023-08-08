import numpy as np
"""we are creating a np ndarray(n - dimensional array)
the possible arithematic operations are are addition , subtraction , multiplication , division mod , e to the power and x to the power etc
"""
array = np.array([1,2,3,4])
# array is now np.ndarray
number = int(input("Please enter the number to be added"))
print("The addition of our array and given no ",number," is ",array+number)
number = int(input("Please enter the number to be subtracted"))
print("The subtraction of our array and given no ",number," is ",array-number)
number = int(input("Please enter the number to be multiplied"))
print("The multiplication of our array and given no ",number," is ",array*number)
number = int(input("Please enter the number to be divided"))
print("The division of our array and given no ",number," is ",array*number)
print("The exponential of all elements and given array is",np.exp(array))
number = int(input("Please enter the number to powered to"))
print("The power of our array and given no ",number," is ",array**number)

