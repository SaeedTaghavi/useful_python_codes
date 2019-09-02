import numpy as np

def test(A):
    A = 3*A
    return A

A= [1,2]
B= test(A)
print(B)

A = np.array([1,2])
B=test(A)
print (B)

exit()
