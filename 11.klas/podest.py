# def materialuAprekins(garums, platums, augstums, skaits):

#     total_volume = garums * platums * augstums
#     total_material = total_volume * skaits
#     return total_material

# def materialaUzskaite(tips, izmers1, izmers2, skaits):
#     if tips == "FINIERIS":
#         # Aprēķini, kas attiecas uz FINIERIS tipu
#         # Izmantojot izmers1 un izmers2
#         print(f"FINIERIS: izmers1={izmers1}, izmers2={izmers2}, skaits={skaits}")
#     elif tips == "LISTE":
#         # Aprēķini, kas attiecas uz LISTE tipu
#         # Izmantojot tikai izmers1
#         print(f"LISTE: izmers1={izmers1}, skaits={skaits}")
#     elif tips == "STURIS":
#         # Aprēķini, kas attiecas uz STURIS tipu
#         # Šeit izmers1 un izmers2 nav svarīgi
#         print("STURIS: parametri nav svarīgi")
#     else:
#         print("Nepareiza tips")


# materialuAprekins_result = materialuAprekins(10, 5, 3, 2)
# print("Materialu aprekins rezultāts:", materialuAprekins_result)

# materialaUzskaite("FINIERIS", 8, 12, 5)
# materialaUzskaite("LISTE", 15, None, 7)
# materialaUzskaite("STURIS", None, None, 10)


def materialuAprekins(garums, platums, augstums, skaits):
    vajadzibasVars = (garums * platums * augstums) / 1000
    return vajadzibasVars * skaits, vajadzibasVars


def materialaUzskaite(tips, izmers1, izmers2, skaits):

    if tips == "FINIERIS":
        podestaSkaits, iegādesVērtība = materialuAprekins(izmers1, izmers2, 0.1, skaits)

    elif tips == "LISTE":
        podestaSkaits, iegādesVērtība = materialuAprekins(izmers1, 0.1, 0.1, skaits)

    elif tips == "STURIS":
        podestaSkaits, iegādesVērtība = materialuAprekins(1, 1, 0.1, skaits)

    return podestaSkaits, iegādesVērtība

print(materialaUzskaite("FINIERIS", 8, 12, 5))
print(materialaUzskaite("LISTE", 15, 0, 7))
print(materialaUzskaite("STURIS", 0, 0, 100))