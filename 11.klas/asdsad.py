dz = {}

dz["kakis"] = {
    "V":["Masdfad", "Nigga"],
    "k":['m', "Nigga"],
    "Ve":["1g", "Nigga"],
    "Suga":["Siama", "Nigga"]
}


dz["pele"] = {
    "V":["Merere"],
    "k":['peleka'],
    "Ve":["1men"],
    "Suga":["vor"]
}


dz["zilonis"] = {
    "V":["Oleg"],
    "k":['peleka'],
    "Ve":["15 leyt"],
    "Suga":["6 kajis"],
    "Snukis":["6 metri"]
}

for dz_s, dz_d in dz.items():

    print(f"{dz_s}")
    for i in range(len(dz_d["V"])):
        print(f"{i+1}. Dziv")
        print(f"V {dz_d['V'][i]}")
        print(f"K {dz_d['k'][i]}")
        print(f"Ve {dz_d['Ve'][i]}")
        print(f"Suga {dz_d['Suga'][i]}")
        if 'Snukis' in dz_d:
            print(f"Snukis {dz_d['Snukis'][i]}")
