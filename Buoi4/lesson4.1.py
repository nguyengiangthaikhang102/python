print("thay ki tu giong ki tu dau thanh '$'")
def thaythe(line):
    x=line[0]
    for i in range(1,len(line)):
        if line[i] == line[0]:
            x+="$"
        else:
            x+=line[i]
    return x
line=input("Nhap chuoi: ")
print(thaythe(line))




