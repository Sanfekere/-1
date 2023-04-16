import random
#Patstāvīgā darba uzdevumi programmēšanā stundai:

# 1) pildam Snakify uzdevumus par tēmām, kuras ir stundās risinātas: https://snakify.org,
# 2) studējam W3schools materiālus par List: https://www.w3schools.com/python/python_lists.asp

# 4) klases un mājas uzdevums līdz nākamai stundai:
# a) sastādīt programmu, kas ģenerē sarakstu, kas satur n nejaušus skaitļus (skaitļu diapazons no -50 līdz +50, n ievada lietotājs 0<n<100),
# b) iegūto sarakstu izvadīt,
# c) lietotājam tiek pajautāts ievadīt skaitli x un programmai jāatrod pirmo saraksta elementu, kas ir mazāks par x un jāizvada to, kā arī jāizvada šī elementa kārtas numurs sarakstā,
# d) izmest no saraksta visas nulles, ja tādas ir, un iegūto sarakstu izvadīt,
# e) izmest no saraksta visus skaitļus, kas atkārtojas un iegūto sarakstu izvadīt.
# f) papildināt sarakstu ar tādu skaitli no intervāla -50 līdz +50, kurš nav atrodams esošajā sarakstā un izvadīt šo pievienojamo skaitli un iegūto sarakstu.
sanja = []
n = int(input("Ievadiet sk līdz 100: "))

for i in range(n):
    sanja.append(random.randrange(-50, 51))

print(sanja)

x = int(input("Ievadiet sk x: "))

for i in range(len(sanja)):
    if x > sanja[i]:
        print("Skaitlis NR", i+1, sanja[i], "ir mazāks par skaitli", x)
        break

sanja_bez_null = list(filter(lambda x: x != 0, sanja))

print(sanja_bez_null)

sanja_unikals = list(set(sanja_bez_null))

print(sanja_unikals)

sanja_jauns = None

for i in range(-50, 51):
    if i not in sanja_unikals:
        sanja_jauns = i
        sanja_unikals.append(sanja_jauns)
        break

print("Pievienotais skaitlis:", sanja_jauns)
print("Saraksts ar jauno skaitli:", sanja_unikals)
