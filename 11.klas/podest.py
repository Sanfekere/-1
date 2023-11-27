def materialuAprekins(garums, platums, augstums, skaits):
    vajadzibasVars = (garums * platums * augstums)/ 1000
    return vajadzibasVars * skaits, vajadzibasVars


def materialaUzskaite(tips, izmers1, izmers2, skaits):

    if tips == "FINIERIS":
        podestaSkaits, iegādesVērtība = materialuAprekins(izmers1, izmers2, 1, skaits)

    elif tips == "LISTE":
        podestaSkaits, iegādesVērtība = materialuAprekins(izmers1, 1, 1, skaits)

    elif tips == "STURIS":
        podestaSkaits, iegādesVērtība = materialuAprekins(1, 1, 1, skaits)

    return podestaSkaits, iegādesVērtība

print(materialaUzskaite("FINIERIS", 8, 12, 5))
print(materialaUzskaite("LISTE", 15, 0, 7))
print(materialaUzskaite("STURIS", 0, 0, 100))
