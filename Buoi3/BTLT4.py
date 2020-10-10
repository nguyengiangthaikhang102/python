def nguyento(n):
    xam=0
    for i in range(1,n+1):
        if n%i==0:
            xam+=1
    if xam == 2:
        return True
    return False
n=int(input("Nhap:"))
print(nguyento(n))