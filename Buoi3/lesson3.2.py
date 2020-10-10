def giaithua(n):
    thua=1
    if n==0 or n==1:
        return thua
    else:
        for i in range(2,n+1):
            thua*=i
        return thua
n=int(input("Nhap:"))
print(giaithua(n))

