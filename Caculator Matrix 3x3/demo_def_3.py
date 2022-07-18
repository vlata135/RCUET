
import numpy as np
a = 0
n = 0
Status = True # dự định cho chương trình chạy được nhiều lần 
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

def calDeterminant(matrixc, n):
    for i in range(n):
        print("Định thức của ma trận ", i + 1)
        print(round(np.linalg.det(matrixc[i])))

def calMutip(matrixc, n):
    b = np.eye(3)
    for i in range(n):
        a = matrixc[i]
        b = np.dot(b,a)
    print("Tích của các ma trận là ")
    print(b)

def calInverse(matrixc,n):
    for i in range(n):
        if(np.linalg.det(matrixc[i]) == 0):
            print("Không có ma trận nghịch đảo vì định thức bằng 0")
        else:
            print("Ma trận nghịch đảo của ma trận thứ", i+1)
            print(np.linalg.inv(matrixc[i]))

def calTranspose(matrixc, n):
    for i in range(n):
        print("Ma trận chuyển vị của ma trận thứ", i+1, "là")
        print(np.transpose(matrixc[i]))

def calMatrix_rank(matrixc,n):
    for i in range(n):
        print("Hạng của ma trận thứ", i+1)
        print(np.linalg.matrix_rank(matrixc[i]))

def calSum(matrixc,n):
    for i in range(n):
        global a
        a = a + matrixc[i]
    print(a)

def calSub(matrixc,n):
    global a
    a = matrixc[0]-matrixc[1]
    print(a)
    

def main():
    inputMatrix()
    x = np.array(matrixc)
    print("Nhấn phím 1 để tăng tương tác")
    print("Nhấn phím 2 để tính GIÁ TRỊ RIÊNG")
    print("Nhấn phím 3 để tính MA TRẬN CHUYỂN VỊ")
    print("Nhấn phím 4 để tính HẠNG CỦA MA TRẬN")
    print("Nhấn phím 5 để tính MA TRẬN NGHỊCH ĐẢO")
    print("Nhấn phím 6 để tính TỔNG CÁC MA TRẬN")
    print("Nhấn phím 7 để tính HIỆU HAI MA TRẬN")
    i = int(input("Lựa chọn của bạn là: "))
    
    if(i==1): print("Mua ngay tài khoản Netflix, Spotify,... chỉ từ 15k facebôk.com/vlata.d <3") 
    if(i==2): calDeterminant(x,n)
    if(i==3): calTranspose(x,n)
    if(i==4): calMatrix_rank(x,n)
    if(i==5): calInverse(x,n)
    if(i==6): calSum(x,n)
    if(i==7): calSub(x,n)

main()










