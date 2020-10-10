def reverse_string(n):
    a=""
    for i in n:
        a=i+a
    return a
n=str(input("Nhap:"))
print(reverse_string(n))