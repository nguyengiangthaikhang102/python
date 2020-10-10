def mua(thang):
    if thang < 4: 
        print("Mua xuan")
    elif thang <7:
        print("mua he")
    elif thang <10:
        print("mua thu")
    else:
        print("mua dong")
thang=int(input("Nhap thang: "))
while thang<1 or thang>12:
    print("thang khong hop le, nhap lai")
    thang=int(input("Nhap thang: "))
mua(thang)