import numpy as np

a = np.array([1,5,10])

print(a)

b = np.array([[9.0, 8.0], [4.0, 2.0]])

print(b)

# get the dimension of any array
print(a.ndim)
print(b.ndim)
# get the shape of any array
print(a.shape)
print(b.shape)

# get data type , numpy typically support int 32 bits data types , which means 4 bytes
print(a.dtype)
print(b.dtype) #hari nm ekama eka enna one

# apita puluwan kochchr byte pramanayk da array ekk gnna one kiyla define krnna
c = np.array([1,2,3,4,5,6] , dtype='int16')
print(c.dtype)

#apita byte size ek blagnna one nm arrays wala
print(a.itemsize)   # meke item size eke awilla 8 i mokds 64 bit ne, ethkot 64/8 = 8 bytes
print(c.itemsize)   # meke item size ek awilla 2 mokd 16 bit ne , ethkot 16/8 = 2
print(b.itemsize)
# get total size
print(a.size)

