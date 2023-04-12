import random

num_count = random.randint(0, 999)

with open("rezult.txt", "w") as f:
    for i in range(num_count):
        num = random.randint(1, 500)
        f.write(str(num) + "\n")

with open("rezult.txt", "r") as f:
    skaits = f.readlines()
    summa = [int(num.strip()) for num in skaits]

print("Skaits:", len(skaits))
print("Summa:", sum(summa))

with open("rezult.txt", "r") as f:
    numbers = f.readlines()
    numbers = [int(num.strip()) for num in numbers]

average = sum(numbers) / len(numbers)
print("Vidējais aritmētiskais: {:.2f}".format(average))

min_num = min(numbers)
max_num = max(numbers)
print("Mazākais skaitlis: ", min_num)
print("Lielākais skaitlis: ", max_num)

print("Skaitļi, kas dalās ar 5:")
divisible_by_5 = [str(num) for num in numbers if num % 5 == 0]
print(" ".join(divisible_by_5))

