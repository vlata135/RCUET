from unittest import result
import numpy as np

# Rows = int(input("Give the number of rows:"))  
# Columns = int(input("Give the number of columns:"))  

rows = 3
columns = 3

myMatrix1 = []
myMatrix2 = []

print("Nhap ma tran 1: ")

for i in range(rows):
    r = []
    for j in range(columns):
        r.append(int(input()))
    myMatrix1.append(r)
print("Nhap ma tran 2: ")
print(myMatrix1,myMatrix2)

for i in range(rows):
    r = []
    for j in range(columns):
        r.append(int(input()))
    myMatrix2.append(r)

# multiplication
print("Tich cua 2 ma tran la ")
output = np.dot(myMatrix1, myMatrix2)
print(output)

# determinant
print("định thức của ma trận 1 là:")
a = np.linalg.det(myMatrix1)
print(round(a))
print("định thức của ma trận 2 là:")
b = np.linalg.det(myMatrix1)
print(round(b))

#







# for i in range(rows):
#     for j in range(columns):
#         print(myMatrix[i][j], end =' ')
#     print()