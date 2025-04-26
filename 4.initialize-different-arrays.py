import numpy as np

a = np.array([[1,2,3,4,5,6,7], [8,9,10,11,12,13,14]])

#all 0 matrix
print(np.zeros(5)) #meke number ek denna one apita on array shape ek
print(np.zeros((2,3)))
#print(np.zeros((2,3,6,1,5)))    #more complex one
print()

#all one matrix or arrays
print(np.ones((4,2)))
print()

#any other number 
print(np.full((2,2), 99, dtype='float32'))
print()

#thwa array ekaka shape ek wage eka number ekakin array or matrix hdnna one unama:
print(np.full_like(a, 4))
print()

#generating random decimal numbers into a matrix or array
print(np.random.rand(4,2))
print(np.random.sample(a.shape))    #mekath thwa thiyna ekaka shape ekk use krnna one nm hoda ekk
print()

#generate random int values
print(np.random.randint(9, size=(3,3))) #Pick random integers starting from 0 up to but not including 9.
print()
print(np.random.randint(-90,23, size=(10,2)))   #range ekk athulatha int random agayan laba denne mehm
print()

#creating a identity matrix: identity matirx is a square matrix with main diagonal is contained with 1 s and other all values are 0
print(np.identity(5))
print()

#repeat a array
arr = np.array([1,2,3])
r1 = np.repeat(arr,3,axis=0)
print(r1)
