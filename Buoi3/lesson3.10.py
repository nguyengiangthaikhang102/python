def fibonacci(n):
    fi0=0
    fi1=1
    fin=1
    if n<0:
        return -1
    elif n==0 or n==1:
        return n
    else:
        for i in range(2,n):
            fi0=fi1
            fi1=fin
            fin=fi0+fi1
        return fin
n=int(input("Nhap:"))
day=""
for i in range(0,n+1):
    day+= str(fibonacci(i))+"  "
print(day)
