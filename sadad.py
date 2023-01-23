# n = int(input("Ievadiet sk n: "))
# i = 1
# x = 3
# s = 0
# while i <= n :
#     s += x
#     x += 3
#     i += 1

# print("Summa ir: ", s)

# n = int(input("Ievadiet sk n: "))
# i = 1
# x = 1
# s = 0
# while i <= n:
#     x *= i
#     i += 1
#     s += x

# print("Summa ir: ", s)


# n = int(input("Ievadiet sk n: "))
# s = 1
# while n >= 1:
#     s *= n
#     n -= 1

# print("Summa ir: ", s)

# n = int(input("Ievadiet sk n: "))
# s = 1
# for i in range(1, n + 1):
#     s *= i

# print(s)

# x = int(input("Ievadiet sk x: "))
# y = int(input("Ievadiet sk y: "))
# s = 1

# for i in int(y):
#     s = x^y

# print(s)


# n = int(input("Ievadiet sk n: "))
# for i in range(1, n, 6):
#     print(i)

# i = 1
# while i < n:
#   print(i)
#   if i == n:
#     break
#   i += 6

# x = int(input("Ievadi sk x "))
# y = int(input("Ievadi sk Y "))

# rez = x
# for i in range(1, y):
#     rez = rez * x
# print(rez)

# n = int(input("Ievadi sk n "))
# sum = 0

# for i in range(1, n + 1):
#     sum = sum + 1/(i * 2 + 1)**2

# print(sum)

# n = int(input("Ievadi sk n "))
# sum = 0

# for i in range(1, n + 1):
#     sum = sum + 1/i**2

# print(sum)

# n = int(input("Ievadi sk n "))
# sum = 0

# for i in range(1, n + 1):
#     sum = 2 ** i/(i**2*(i  + 1))

# print(sum)

# n = int(input("Ievadi sk n "))
# sum = 1

# for i in range(1, n + 1):
#     sum *= i
#     i += 1
#     sum += n

# print(sum)

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

# n = int(input("Ievadiet sk n: "))
# i = 1
# x = 1
# s = 0
# while i <= n:
#     x *= i
#     i += 1
#     s += x

# print("Summa ir: ", s)

# n = int(input("Ievadiet sk n: "))
# a = 0
# b = 1
# for i in range(2,n):
#             c = a + b
#             a = b
#             b = c
#             print(c)
# print(c)

# def fib(n):
#     a = 0
#     b = 1
#     g = 0
#     if n == 1:
#         print(a)
#     else:
#         print(a)
#         print(b)
#         for i in range(2,n):
#             c = a + b
#             # g += c
#             a = b
#             b = c
#             print(c)
# fib(n)


i = -5
x1 = -5
x2 = 5
y = 0.5
while i <= x2:
    print(i, "|", 2 * i ** 2)
    i += y 
