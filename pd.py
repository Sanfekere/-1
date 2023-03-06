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
    elif vaivods[i] >= 0:
        nepozitivi += 1
    i += 1

print(pozitivi)