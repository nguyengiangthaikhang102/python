print("chuyen chuoi hoa thanh chu thuong va nguoc lai")
def hoathuong(line):
    x = ""
    for i in line:
        if i.islower():
            x+=i.upper()
        else:
            x+=i.lower()
    print(x)
line=input("Nhap chuoi: ")
hoathuong(line)

