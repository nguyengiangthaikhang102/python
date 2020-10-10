i=0
def dem(n,i):
    if i==len(n) or n[i].isnumeric==False:
        return 0
    if int(n[i])%2!=0:
        return 1+dem(n,i+1)
    else:
        return 0+dem(n,i+1)
n=input("Nhap so : ")
print(dem(n,i))    