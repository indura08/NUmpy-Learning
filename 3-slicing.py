import numpy as np

a = np.array([[1,2,3,4,5,6,7], [8,9,10,11,12,13,14]])
print(a.shape)

#get specific element
print(a[1, -2]) # mekedi me minus ganan kiynne aga idla 2 element ek , ethkot aga palweni eka ganinna poatna gnne 0 idl newei 1 idla , 0 idla ganinne muladi withri
print(a[0,4])

#get a specific row - mekn krnne 0 weni row eke okkoma tika denwa apita
print(a[0, :])
print(a[1, :])


#get a specific column
print(a[:, 3])  #mekn krnne 3 column ekt adlawa okkoma data tika denwa

# [startIndex:endIndex:stepSize]
print(a[0, 1:6:2])

# 3d example:
b = np.array([
    [
        [1,2],
        [3,4]
    ] ,

    [
        [5,6],
        [7,8]
    ]
])
print("printing new shaped b arrays info and other stuff")
print(b.shape)
print(b)

#get sepcific element (work outside in)
print(b[0,0,1])

#replacings
b[:,1,:] = [[9,9], [8,8]]
print(b)