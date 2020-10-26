'''
Bài 3: Tính tổng giá trị từ 1 đến n (n>13, n nhập từ bàn phím, xử lý điều kiện n>13), 
nếu chạy đến số 13 thì không chạy nữa (không cộng số 13) và xuất kết quả  
 	Ví dụ: input: n = 20 
    Output: S = 78 

'''
def tinhtong(a):
    tong=0
    for i in range(a+1):
        if i==13:
            break
        tong+=i
    return tong
if __name__ == "__main__":
    a=int(input("Nhập số cần tính:"))
    print("Tong (tru:13):",tinhtong(a))
