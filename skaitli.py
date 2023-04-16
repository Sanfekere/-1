with open('skaitli.txt', 'r') as f:
    skaitli = list(map(int, f.read().split()))

summa = sum(skaitli)
print("Summa:", summa)
with open('atbilde.txt', 'w') as f:
    f.write(str(summa))
print()

skaitli_augosa = sorted(skaitli)
skaitli_augosa_rinda = ""
for i, skaitlis in enumerate(skaitli_augosa):
    skaitli_augosa_rinda += str(skaitlis) + ", "
    if (i + 1) % 30 == 0:
        print(skaitli_augosa_rinda)
        with open('atbilde.txt', 'a') as f:
            f.write(skaitli_augosa_rinda + "\n")
        skaitli_augosa_rinda = ""
if skaitli_augosa_rinda:
    print(skaitli_augosa_rinda)
    with open('atbilde.txt', 'a') as f:
        f.write(skaitli_augosa_rinda + "\n")
print()

skaitli_dilstosa = sorted(skaitli, reverse=True)
skaitli_dilstosa_rinda = ""
for i, skaitlis in enumerate(skaitli_dilstosa):
    skaitli_dilstosa_rinda += str(skaitlis) + ", "
    if (i + 1) % 30 == 0:
        print(skaitli_dilstosa_rinda)
        with open('atbilde.txt', 'a') as f:
            f.write(skaitli_dilstosa_rinda + "\n")
        skaitli_dilstosa_rinda = ""
if skaitli_dilstosa_rinda:
    print(skaitli_dilstosa_rinda)
    with open('atbilde.txt', 'a') as f:
        f.write(skaitli_dilstosa_rinda + "\n")
print()