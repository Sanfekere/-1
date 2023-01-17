#4.uzd
# n = int(input("Ievadiet sk n: "))
# i = 1
# x = 1
# s = 1
# while i <= n:
#     x *= 1/2**i
#     i += 1
#     s += x

# print("Summa ir: ", s)

#5.4

n = int(input("Ievadiet sk n: "))
i = 1
x = 1
s = 0
while i <= n:
    x *= i
    i += 1
    s += x

print("Summa ir: ", s)