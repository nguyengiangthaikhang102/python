N = int(input("Nhap N:"))
tongle = 0
for i in range(1, N + 1):
    if i % 2 != 0:
        tongle += i
print(tongle)