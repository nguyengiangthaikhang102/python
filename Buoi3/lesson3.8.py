def nguyento(n):
    xam=0
    for i in range(1,n+1):
        if n%i==0:
            xam+=1
    if xam == 2:
        return "La so nguyen to"
    return "Khong la so nguyen to"
def tong(n):
    sum=0
    for i in range(1,n+1):
        if nguyento(n):
            sum+=i
    print(sum)
n=int(input("Nhap so:"))
print(nguyento(n))
print(tong(n))


 

