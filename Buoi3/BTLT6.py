
def pangram(str, alphabet):
    for char in alphabet:
        if char not in str.lower():
            return False
    return True
n=input("Nhap chuoi: ")
alphabet="abcdefghijklmnopqrstuvwxyz"
if pangram(n,alphabet):
    print("la chuoi pangram")
else:
    print("khong la chuoi pangram")