dz = {}

dz["kakis"] = {
    "V":["Masdfad", "Nigga", "SSSSSSSSASS"],
    "k":['m', "Nigga", "SSSSSSSSASS"],
    "Ve":["1g", "Nigga", "SSSSSSSSASS"],
    "Suga":["Siama", "Nigga", "SSSSSSSSASS"],
    "Astes":[5, 12, 23],
    "KG":[4,5,7],
}


dz["pele"] = {
    "V":["Merere", "sad"],
    "k":['peleka', "asd"],
    "Ve":["1men", "asd"],
    "Suga":["vor", "asd"],
    "Astes":[123, 21, 5],
    "KG":[0.5],
}


dz["zilonis"] = {
    "V":["Oleg"],
    "k":['peleka'],
    "Ve":["15 leyt"],
    "Suga":["6 kajis"],
    "Snukis":["6 metri"],
    "KG":[15000],
}

dz["Gliemezis"] = {
    "V":["Oleg"],
    "k":['peleka'],
    "Ve":["15 leyt"],
    "Suga":["6 kajis"],
    "Snukis":["6 metri"],
    "KG":[1],
}
dz["Sams"] = {
    "V":["Oleg"],
    "k":['peleka'],
    "Ve":["15 leyt"],
    "Suga":["6 kajis"],
    "Snukis":["6 metri"],
    "KG":[50000],
}
astes_kop = 0
sk1 = 0
sk = 0 
kakis_g = 0
for dz_s, dz_d in dz.items():
    print(f"{dz_s}")
    for i in range(len(dz_d["V"])):
        print(f"{i+1}. Dziv")

        print(f"V {dz_d['V'][i]}")
        print(f"K {dz_d['k'][i]}")
        print(f"Ve {dz_d['Ve'][i]}")
        print(f"Suga {dz_d['Suga'][i]}")
        if 'Astes' in dz_d:
            print(f"Astes {dz_d['Astes'][i]}")
            if 'kakis' in dz_s:
                kakis_g += dz_d['Astes'][i]
                sk1 += 1
            if 'pele' in dz_s:
                astes_kop += dz_d['Astes'][i]
                sk += 1


        if 'Snukis' in dz_d:
            print(f"Snukis {dz_d['Snukis'][i]}")
print(f"Suņu videjais astes gr : {astes_kop/sk}")
print(f"Kaķu videjais astes gr :{kakis_g/sk}")
print(sk1)