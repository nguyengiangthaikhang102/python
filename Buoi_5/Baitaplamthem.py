def khonglaplai(arr):
    a=[]
    for i in arr:
        if i not in a:
            a.append(i)
    return a


def mang(n):
    i=0
    while True:
        k=input(f"Phan tu thu {i}:")
        try:
            arr.append(int(k))
            i+=1
            if i>=n:
                break
        except:
            print("Nhap lai")
    return arr
arr=[]
n=int(input("Nhap mang:"))
print(mang(n))
print(khonglaplai(arr))