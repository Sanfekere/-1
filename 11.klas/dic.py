muzika = {
    "Autors" : "Sanfekere",
    "MontL" : "2485",
    "Sekotāju" : "165",
    "TotalStreams" : "166K",
    "Dziesma0" : "Latgale Trip",
    "Dziesma1" : "Latgale Trip Vol 2",
    "Dziesma2" : "Latgale Trip V3",
    "Dziesma3" : "Latgale Trip V4",
    "Dziesma4" : "Latgale Trip V",
    "Dziesma5" : "Latgale Trip VI",
    "Dziesma6" : "NEW TALE",
    "Dziesma7" : "CAPÍTULO ATO",
    "Dziesma8" : "Brazil Rua",
    "Albums" : "LATGALE TRIP END",
}
print(muzika)
print(muzika["MontL"])

y = input("Ievadiet tēmu ")
x = input("Ievadiet aprakstu ")


muzika.update({y: x})

print(muzika)

o = input("Ievadiet jaunu autoru ")

muzika["Autors"] = o

print(muzika)

muzika.pop("Autors")

print(muzika)


muzika.clear()

print(muzika)


