# n = int(input("Ievadiet sk n: "))
# i = 1
# x = 3
# s = 0
# while i <= n :
#     s += x
#     x += 3
#     i += 1

# print("Summa ir: ", s)

n = int(input("Ievadiet sk n: "))
i = 1
x = 1
s = 0
while i <= n:
    s += x
    x = 1 + 1*i
    i += 1

print("Summa ir: ", s)
