print("in ra max min trong chuoi")
def minmaxchuoi(line):
    max=min=line[0]
    for i in line:
        if min>i:
            min=i
        if max<i:
            max=i
    print("Ki tu lon nhat la",max)
    print("ki tu nho nhat la",min)
line=input("Nhap chuoi:")
minmaxchuoi(line)

            

