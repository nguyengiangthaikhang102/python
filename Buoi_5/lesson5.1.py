def mang(n):
  
    i=0
    while True:
        x=input(f"Phan tu thu {i}:")
        try:
            arr.append( int(x))
            i+=1
            if i>=n:
                break
        except:
            print("chua dung nhap lai")
    return arr
def tongmang(arr):
    s=0
    for i in arr:
        s+=i   
    return s
def tichmang(arr):
    s=1
    for i in arr:
        s*=i   
    return s
def maxmang(arr):

    max=arr[0]
    for i in arr:
        if max<i:
            max=i
    return max
def minmang(arr):
  
    min=arr[0]
    for i in arr:
        if min >i:
            min=i
    return min
def lemang(arr):

    le=[]
    for i in arr:
        if i%2!=0:
            le.append(i)
    return le
def chanmang(arr):
 
    chan=[]
    for i in arr:
        if i%2==0:
            chan.append(i)
    return chan
# def nguyento(arr):
#     x=0
#     for e in arr:
#         e
#     if x==2:
#         return True
#     return False
# def tongnguyento(arr):
#     tong=0
#     for e in arr:
#         for i in range(1,e+1):
#             if nguyento(arr[i]):
#                 tong+=i
#     return tong
    
    

   
   
    
    


arr=[]
n=int(input("Nhap so phan tu:"))

print(mang(n))
print("Tong mang",tongmang(arr))
print("Tich mang",tichmang(arr))
print("Max:",maxmang(arr))
print("min:",minmang(arr))
print("So le trong mang:",lemang(arr))
print("So chan trong mang:",chanmang(arr))

# print(tongnguyento(arr))




