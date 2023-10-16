vard = {
    'Latvija' : '1884000', 
    'Igaunija' : '1331000', 
    'Lietuva' : '2801000', 
    'Polija' : '37750000', 
    'Vācija' : '83200000', 
    'Francija' : '67750000', 
    'Spānija' : '47420000', 
    'Portugāle' : '10330000', 
    'Itālija' : '59110000', 
    'Maroka' : '31000000', 
}

def func0():
    for x in vard:
        print(f"Valsts: {x}", end=', '+ ".")

def func1():
    for x in vard:
        print(f"Valsts: {x}, Iedzīvotāju skaits {vard[x]}, ")

def func2():
    vards = input("Ievadiet kādu valsti vēlaties ievietot: ")
    iedz = input("Ievadiet iedzīvotāju sk: ")
    vard[vards] = iedz


def func3():
    valsts = input("Ievadiet kādu valsti vēlaties izņemt: ").strip()
    vard.pop(valsts)

def func4():
    valsts = input("Ievadiet kādu valstij vēlaties izmainīt iedz sk: ").strip()
    iedzsk = input("Ievadiet iedz sk: ").strip()
    vard[valsts] = iedzsk

def func5():
    iedzsk = 100000000000000000000

    for x in vard:
        if iedzsk >= int(vard[x]):
            iedzsk = int(vard[x])
            g = x
    print(g)

def func6():
    iedzsk = 1

    for x in vard:
        if iedzsk < int(vard[x]):
            iedzsk = int(vard[x])
            g = x
    print(g)



def main():
    while True:
        print("")

        izv = input("""Ievadiet izvēli: 
                    1 - Izvadīt valstis
                    2 - Izvadīt valstis un iedz
                    3 -  Pievienot valsti
                    4 - Dzēst kādu valsti
                    5 -    Izmainīt iedz
                    6 - Vizmazāk iedz
                    7 - Visvairāk iedz
                    8 - BEIGAS""")
        if izv == "1":
            func0()
        elif izv == "2":
            func1()
        elif izv == "3":
            func2()
        elif izv == "4":
            func3()
        elif izv == "5":
            func4()
        elif izv == "6":
            func5()
        elif izv == "7":
            func6()
        elif izv == "8":
            print("Paldies par programmas izmantošanu!")
            break

main()
