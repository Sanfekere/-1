import random
linards = 14+10+2006
vaivods = []

for i in range(linards):
    vaivods.append(random.randrange(-150, 150))

# print(vaivods)

# pozitivi = 0
# nepozitivi = 0

# for i in range(linards):
#     if vaivods[i] >= 0:
#         pozitivi += 1
#     elif vaivods[i] < 0:
#         nepozitivi += 1
#     i += 1

# print("Pozitīvo sk skaits =", pozitivi, "Negatīvo sk skaits =",nepozitivi)

# para = 0
# nepara = 0

# for i in range(linards):
#     if vaivods[i]%2 == 0:
#         para += 1
#     else:
#         nepara += 1
#     i +=1

# print("Para sk skaits =", para, "Nepara sk skaits =",nepara)

# vdar = 0

# for i in range(linards):
#     vdar += vaivods[i]
#     i += 1

# print("Vidējais aritmētiskais =",vdar/linards)

nepara2 = []
for i in range(linards):
    if vaivods[i]%2 == 0:
        None
    else:
        nepara2.append(vaivods[i])
    i +=1

print(nepara2)

# sk = 0
# for i in range(linards):
#     if vaivods[i] == 14:
#         sk += 1
#     i +=1

# if sk == 0:
#     print("Skaitļu kas sakrīt ar manu dzimšanas dienu nav.")
# else:
#     print("Skaitļu kas sakrīt ar manu dzimšanas dienu ", sk)

# mzvar = 0
# for i in range(linards):
#     if vaivods[i] < vdar/linards:
#         mzvar += 1
#     i +=1

# print("Skaitļu kas ir mazāki par vidējo aritmētisko ", mzvar)
# divciparsk = 0
# for i in range(linards):
#     if vaivods[i] >= -99 and vaivods[i] < -9:
#         divciparsk += 1
#     elif vaivods[i] >= 10 and vaivods[i] < 100:
#         divciparsk += 1
#     i +=1

# print(divciparsk)
# pirmsk = []
# for i in range(linards):
#     prime = True
#     for i in range(2,vaivods[i]):
#         if (vaivods[i]%i==0):
#             prime = False
#     if prime:
#        pirmsk.append(vaivods[i])
#     i += 1
# print(pirmsk)
# vaivods.sort()
# print(vaivods)

# vaivods2 = []
# for i in range(linards):
#     if vaivods[i]%5 == 0 and vaivods[i]%3 == 0:
#         vaivods2.append(vaivods[i])
#     i +=1
# print(vaivods2)  


# rows, cols = (8, 16)
# vaivods3 = [[random.randrange(0, 1) for i in range(cols)] for j in range(rows)]
# print(vaivods3)