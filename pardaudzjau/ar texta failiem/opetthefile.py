MAPE = "faili/"

sanja = open("jalina.txt", "r",encoding="utf-8")

# print(sanja.read(5))
# print(sanja.readline())

# def f(t):
#     burtuSk = 0 
#     burtuSk = burtuSk + t.count("a") + t.count("A")
#     print(burtuSk)

t = sanja.read()

# f(t)

# with open('jalina.txt', 'r', encoding="utf-8") as fails:
#     rindas = fails.readlines()
#     vardi_ar_a = []
#     for rinda in rindas:
#         vardi = rinda.split()
#         for vards in vardi:
#             if 'a' in vards or 'A' in vards:
#                 vardi_ar_a.append(vards)
#     print("Vārdi, kas satur burtu 'a' un 'A':")
#     print(vardi_ar_a)

def f(t):
    burtuSk = 0 
    burtuSk = burtuSk + t.count(",")
    print(burtuSk)

f(t)

with open('jalina.txt', 'r', encoding="utf-8") as fails:
    rindas = fails.readlines()
    skaits = len(rindas)
    print("Failā ir", skaits, "rindas.")

with open('jalina.txt', 'r', encoding="utf-8") as fails:
    teksts = fails.read()
    jaunais_teksts = teksts.replace(".", "!")
    print(jaunais_teksts)


with open('jalina.txt', 'r', encoding="utf-8") as fails:
    teksts = fails.read()
    simbolu_skaiti = {}
    for simbols in teksts:
        if simbols in simbolu_skaiti:
            simbolu_skaiti[simbols] += 1
        else:
            simbolu_skaiti[simbols] = 1
    for simbols, skaitlis in simbolu_skaiti.items():
        print(simbols, "-", skaitlis)
