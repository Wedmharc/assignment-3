import numpy as np

#3 example arrays
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([[6, 7, 8], [9, 10, 11]])
arr3 = np.array([(1, 'mango'), (2, 'banana'), (3, 'langka')],
                dtype=[('id', int), ('fruit', 'U10')])

#Save the arrays to a single file using np.savez()
np.savez('data.npz', arr1=arr1, arr2=arr2, arr3=arr3)

#Load the arrays from the file using np.load()
loaded_data = np.load('data.npz')

#Print the loaded arrays
print("Loaded array 1:", loaded_data['arr1'])
print("Loaded array 2:", loaded_data['arr2'])
print("Loaded array 3:", loaded_data['arr3'])