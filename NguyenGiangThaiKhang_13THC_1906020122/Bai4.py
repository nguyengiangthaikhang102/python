'''
Bài 4: Giả sử có một chuỗi như sau: “0001;10:18:25;0983876207;0918295063”, tách chuỗi trên thành từng phần riêng biệt 
Cho biết vị trí thứ 2 trong chuỗi trên là thời gian cuộc gọi từ số thứ 1 “0983876207” sang số thứ 2 “0918295063”.
Biết rằng 1 phút cho mỗi cuộc gọi là 2500đ, tính giá cước cuộc gọi trên. 

'''
def tinh_tien():
    a=input("Nhap:")
    b=a.split(";")
    time=b[1].split(":")
    tong_time =float(time[0])*60 + float(time[1])+round(float(time[2])/60) 
    money=tong_time*2500
    return money

if __name__ == "__main__":
    kq=tinh_tien()
    print("So tien can phai tra:",kq)




