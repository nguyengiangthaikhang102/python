'''
Bài 1: Tạo mảng a = [1, 1, 2, 5, 7, 9] 
Thay thế phần tử đầu tiên là 0. (Kết quả:  a = [0, 1, 2, 5, 7, 9]) 
Thay thế phần tử thứ 3 đến thứ 5 là 4,6,8. (Kết quả:  a = [0, 1, 4, 6, 8, 9]) 

'''

def mang(a):
    a[0]=0
    a[2:5]=4,6,8
    return a
 
if __name__ == "__main__":
    a=[1,1,2,5,7,9]
    print( mang(a))



