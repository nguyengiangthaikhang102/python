#Theo de quy
def dequy(n):
    if n==1 or n==2:
        return 1
    return dequy(n-1) + dequy(n-2)
#KKhong de quy
def thuong(n):
    n1=0
    n2=1
    for i in range(n-1):
        temp=n1+n2
        n1=n2
        n2=temp
    return temp
n=int(input("Nhap so: "))
while n<=0:
    print("So khong hop le\n Nhap lai")
    n=int(input("Nhap so: "))
print(f"De quy: {dequy(n)}")
print(f"Khong de quy: {thuong(n)}")