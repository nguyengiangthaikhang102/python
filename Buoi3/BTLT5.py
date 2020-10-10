def KT(n):
    hoa=0
    thuong=0
    for i in n:
        if i.isupper():
            hoa+=1
        if i.islower():
            thuong +=1
    print("So chu hoa:",hoa)
    print("So chu thuong:",thuong)   
    return "OK"

n=str(input("Nhap:"))
print(KT(n))
