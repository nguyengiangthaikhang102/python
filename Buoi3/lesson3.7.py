def ktchinhphuong(n):
    if n <= 0:
        return False
    else:
        xam = False
        for i in range(1, n + 1):
            if i * i == n:
                xam = True
                break
        if xam == True:
            return True
        else:
            return False
n=int(input("Nhap:"))
print( ktchinhphuong(n))
            
