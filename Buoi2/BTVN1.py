import math
a=float(input("Nhap a:"))
b=float(input("Nhap b:"))
c=float(input("Nhap c:"))
if a==0:
    if b==0:
        print("PT Vo Nhiem")
    else:
        print("PT co 1 nghiem x=",(-c/b))
#deta
D=(b*b)-4*(a*c)
if D>0:
    x1=(float)((-b+ math.sqrt(D))/(2+a))
    x2=(float)((-b-math.sqrt(D))/(2*a))
    print(f"PT co 2 Nghiem x1={x1}x2={x2}")
elif D==0:
    x1=(-b/(2*a))
    print(f"PT co nghiem kep la : {x1}")
else:
    print("PT Vo Nghiem")



