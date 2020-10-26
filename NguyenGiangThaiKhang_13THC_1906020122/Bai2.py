'''
Bài 2: Viết hàm với tham số truyền vào là một tháng và trả về mùa tương ứng trong năm. 
Sử dụng hàm vừa cài đặt, nhập vào một tháng và in ra màn hình mùa trong năm. 
Thí dụ: Người dùng nhập vào tháng 2, in ra màn hình là mùa Xuân. 
'''
def mua(a):
    if thang < 4: 
        print("Mùa Xuân")
    elif thang <7:
        print("Mùa Hè")
    elif thang <10:
        print("Mùa Thu")
    else:
        print("Mùa Đông")
if __name__ == "__main__":
    thang=int(input("Nhập Tháng:"))
    while thang<1 or thang>12:
        print("Tháng không đúng nhập lại")
        thang=int(input("Nhập Tháng: "))
    mua(thang)

    