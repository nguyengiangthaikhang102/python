def create_matrix(a,b):
    for i in range(1,a+1):
        for j in range(1,b+1):
            print(i*j,end="\t")
        print()
a=int(input("Nhap hang: "))
b=int(input("Nhap cot: "))
print(create_matrix(a,b))