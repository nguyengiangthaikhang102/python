def sohoanhao(n):
    if n<=1:
        return "không pải số hoàn hảo"
    else:
        sam=0   
        for i in range(1,n):
            if n%i==0:
                sam+=i
        if sam==n:
           return "La so hoan hao"
        else:
            return "khong pai so hoan hao"
n=int(input("Nhap:"))
print(sohoanhao(n))

            