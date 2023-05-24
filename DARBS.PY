import random


def uzdevums_1():
    alex = []
    while True:
        n = int(input("Ievadi skaitli n - "))
        if n <= 1  or n >= 200:
            print("Nepareiza ievade. Lūdzu, ievadiet atbilstošo ciparu no 2 līdz 199.")
            continue
        else:
            break


    for i in range(n):
        n = random.randrange(-150, 150)
        alex.append(n)



    for elementi in alex:
        print(elementi, end=' : ')

    print()
    alex.sort()

    for elementi in alex:
        print(elementi, end=' ')

    print()

    for elementi in reversed(alex):
        print(elementi, end=' ')


# uzdevums_1()

def uzd_2():

    array = []
    given_file = open("dati.txt", "r")


    lines = given_file.readlines()

    for line in lines:
        for c in line:
            if c.isdigit() == True:
                array.append(c)

    print(array)

    given_file.close()



    def malas_apr():
        global mala1
        global mala2
        global mala3
        global mala4
        mala1 = int(array[0]) + int(array[2])
        mala2 = int(array[4]) + int(array[6])
        mala3 = int(array[1]) + int(array[5])
        mala4 = int(array[3]) + int(array[7])



    def perimetrs():
        malas_apr()
        global perimetrs
        perimetrs = mala1 + mala2 + mala3 + mala4
        with open("rezult.txt", "w") as f:
            f.write("Perimetrs ir - " + str(perimetrs) + "\n")
        return perimetrs


    print(perimetrs())

uzd_2()