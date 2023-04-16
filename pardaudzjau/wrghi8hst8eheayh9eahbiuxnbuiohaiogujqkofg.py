import random
# 1. Definēsim jaunu sarakstu un aizpildīsim to ar n nejaušiem skaitļiem no 1-20, n jāpajautā ievadīt lietotājam
sanja = []

n = int(input("Cik skaitļus ģenerēsim "))
for i in range(n):
    sanja.append(random.randrange(1, 21))
# 2. Izvadīsim iegūto sarakstu
print(sanja)
# 3. Izvadīsim 1-mo saraksta elementu
print(sanja[0])
# 4. Izvadīsim pēdējo saraksta elementu
print(sanja[n-1])
# 5. Izvadīsim iepriekšpēdējo saraksta elementu
print(sanja[n-2])
# 6. Pievienosim sarakstam lietotāja ievadītu skaitli X
sanja.append(int(input("Ievadi sk x ")))
# 7. Izvadīsim iegūto sarakstu ar jauno skaitli
print(sanja)
# 8. Izdzēsīsim no saraksta pirmo elementu
sanja.remove(sanja[0])
# 9. Izvadīsim tagad iegūto sarakstu 
print(sanja)
# 10. Izvadīsim katru trešo saraksta elementu
print(sanja[::3])
# 11. Izveidosim jaunu sarakstu, kur ir tikai pāra skaitļi no sākuma saraksta un beigās izvadīsim to summu 
s = 0
for i in sanja:
    if i % 2 == 0:
        s += i 
        print(i, end=" ")

print(s)
# 12. Izveidosim jaunu sarakstu, kur ir tikai nepāra skaitļi no sākuma saraksta un beigās izvadīsim to summu 
odd = 0
for i in sanja:
    if i % 2 == 1:
        odd += i 
        print(i, end=" ")

print(odd)
# 13. Izvadīsim tikai tos skaitļus, kas dalās ar 3 
three = 0
for i in sanja:
    if i % 3 == 0:
        print(i, end=" " + ".\n")

# 14. Visu saraksta skaitļu summu
print(sum(sanja))
# 15. Visu saraksta skaitļu vidējo aritmētisko, noapaļotu līdz 2 zīmēm aiz komata
# 16. Cik reizes sarakstā ir sastopams skaitlis `7`
# 17. Izvadīsim visus saraksta elementus sakārtotā augošā secībā 
# 18. Izvadīsim visus saraksta elementus sakārtotā dilstošā secībā

