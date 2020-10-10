print("noi 2 ki tu dau va cuoi")
def noichuoidaucuoi(Line):
    if len(Line)<2:
        return ""
    else:
        return Line[0:2]+Line[-2:]

Line= input("Nhap chuoi:")
print(noichuoidaucuoi(Line))
