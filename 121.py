# judz = 1.609
# i = 5
# x2 = 7.5
# y = float(input("Ievadiet SOLI "))
# while i <= x2:
#     print(i, "jūdzes", "|", i * judz, "km")
#     i += y 

y1 = float(input("Ievadiet % cik skriesi nākam dien"))
x1 = float(input("Noskrieto km 1 diena "))
x2 = float(input("Noskrieto km vēlēsana "))
i = x1
y = y1/100
diena = 0

while i <= x2:
    i += x1*y 
    print(i)
    diena += 1
    if i == x2:
        break

print(diena,"dienā" + " tiks noskrieti", x2, "km")
print(diena,"dienās" + " tiks noskrieti", x2, "km")