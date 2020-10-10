def max_min(n):
    list=[]
    for i in range(1,n+1):
        list.append(int(input(f"Phan tu thứ {i}:")))
    print("Số Lớn Nhất Là :",max(list))
    print("Số Nhỏ Nhất Là :",min(list))
    return"Đúng"
n=int(input("Nhap so phan tu :"))
print(max_min(n))




