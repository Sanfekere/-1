import random
linards = 14+10+2006
vaivods = []

for i in range(linards):
    vaivods.append(random.randrange(-150, 150))

print(vaivods)

pozitivi = 0
nepozitivi = 0

for i in range(linards):
    if vaivods[i] >= 0:
        pozitivi += 1
    elif vaivods[i] < 0:
        nepozitivi += 1
    i += 1

print("Pozitīvo sk skaits =", pozitivi, "Negatīvo sk skaits =",nepozitivi)

para = 0
nepara = 0

for i in range(linards):
    if vaivods[i]%2 == 0:
        para += 1
    else:
        nepara += 1
    i +=1

print("Para sk skaits =", para, "Nepara sk skaits =",nepara)

vdar = 0

for i in range(linards):
    vdar += vaivods[i]
    i += 1

print("Vidējais aritmētiskais =",vdar/linards)

nepara2 = []
for i in range(linards):
    if vaivods[i]%2 == 0:
        None
    else:
        nepara2.append(vaivods[i])
    i +=1

print(nepara2, maxlen=20)

sk = 0
for i in range(linards):
    if vaivods[i] == 14:
        sk += 1
    i +=1
if i == 0:
    