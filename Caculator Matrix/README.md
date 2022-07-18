# Các phép toán trong ma trận 3x3
 
## 1. Ma trận trong Numpy

- Ma trận trong Numpy là một bảng dữ liệu gồm m hàng và n cột
- Cú pháp khai báo ma trận:

   ` arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])`

## 2. Các phép toán đối với ma trận 3x3

### *2.1 Tổng/Hiệu ma trận 3x3*
- Ta có thể tiến hành cộng trừ ma trận  bằng cách dưới đây

`A = np.array([[1, 3, 4], [-2, 6, 0], [-5, 7, 2]])`
`B = np.array([[2, 3, 4], [-1, -2, -3], [0, 4, -4]])`
`print("A + B = \n", A + B)`
`print("A - B = \n", A - B)`

- Kết quả nhận lại được sẽ có dạng dưới đây
`A + B = `
 `[[ 3  6  8]`
 `[-3  4 -3]`
` [-5 11 -2]]`
`A - B = `
 `[[-1  0  0]`
 `[-1  8  3]`
 `[-5  3  6]]`

### *2.2 Tích của hai ma trận*
- Numpy cung cấp một hàm để thực hiện tích vô hướng của hai mảng 
            `np.dot(matrix1, matrix2, out)`
    **CÁC THAM SỐ**
        matrix1, matrix2: ma trận cần nhân
        out: mặc định là None, em chưa hiểu rõ cái tham số này muốn nói gì 
### *2.3 Định thức của ma trận*
- Để tính định thức của một ma trận, Numpy cung cấp cú pháp như sau:
   ` numpy.linalg.det(matrix)`
   với matrix là ma trận cần tính det

### *2.4 Hạng của ma trận*
- Cú pháp:
    `np.linalg.matrix_rank(matrix)`
    Bên cạnh matrix, hàm này còn 2 thông số nữa là tol với hermitian, phần này em chưa hiểu lắm
### *2.5 Ma trận nghịch đảo*
- Cú pháp:
    `np.linalg.inv(matrixc)`
    Kết quả chỉ trả về là ma trận nghịch đảo nếu như định thức bằng 0

### *2.6 Ma trận chuyển vị*
- Cú pháp:
    ` np.transpose()`

## 3. Một số cú pháp bổ sung

1. `np.diag()`: tạo ma trận đường chéo hoặc lấy cách giá trị ở đường chéo của ma trận
2. `np.eye(a)`: tạo một ma trận đơn vị cấp a 

    




