import numpy as np
a = 0
n = 0
rows, columns = 3,3
matrixc = []

def inputMatrix():
    global n
    i = int(input("Nhập số lượng ma trận 3x3: "))
    n = i
    for m in range(i):
        myMatrix1 =[]
        print("Nhập ma trận số",m+1, "Nhập ma trận từ trái sang phải, từ trên xuống dưới")
        for i in range(rows):
            r = []
            for j in range(columns):
                r.append(int(input()))
            myMatrix1.append(r)
        matrixc.append(myMatrix1)    
inputMatrix()
x = np.array(matrixc)
a = x[0]-x[1]
print(a)