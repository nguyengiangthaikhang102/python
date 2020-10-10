import math
def body_mass_index(m,h):
    BMI=m/math.pow(h,2)
    return BMI
def bmi_information(m,h):
    bmi=body_mass_index(m,h)
    if bmi > 30:
        print("Beo phi")
    elif bmi >=25:
        print("Thua can")
    elif bmi >=18.5:
        print("Binh thuong")
    else:
        print("Gay")
m=float(input("Nhap can nang: "))
h=float(input("Nhap chieu cao: "))
while m<0 or h<0:
    print("Du lieu khong hop le\n Nhap lai")
    m=float(input("Nhap can nang: "))
    h=float(input("Nhap chieu cao"))
bmi_information(m,h)