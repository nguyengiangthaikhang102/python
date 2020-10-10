n = int(input("nhập n là số nguyên dương [1->1000]: "))
while(n>999 or n < 0):
    n = int(input("nhập lại n là số nguyên dương [1->1000]: "))
sum=0
while (n > 0):
        sum = sum + n % 10
        n = int(n / 10)
print(sum)