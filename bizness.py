import random
import time
import tkinter as tk
import pickle

nauda = 1000
pārdoti_produkti = 0
noskatītas_reklāmas = 0
kliki = []
uznemuma_nosaukums = "Mans uzņēmums"
nauda_uzraksts = None
produkta_uzraksts = None
reklamas_uzraksts = None
kliki_uzraksts = None

def atjaunot_naudu():
    global nauda_uzraksts
    nauda_uzraksts.config(text="Jūsu nauda: " + str(nauda) + " dolāri")

def atjaunot_produktus():
    global produkta_uzraksts
    produkta_uzraksts.config(text="Pārdoti produkti: " + str(pārdoti_produkti))

def atjaunot_reklamas():
    global reklamas_uzraksts
    reklamas_uzraksts.config(text="Noskatītas reklāmas: " + str(noskatītas_reklāmas))

def atjaunot_kliki():
    global kliki_uzraksts
    kliki_uzraksts.config(text="Klikšķi: " + str(len(kliki)))

def darbs():
    global nauda
    global kliki
    peles_klikskenis = random.randint(1, 100)
    nauda += peles_klikskenis
    kliki.append(peles_klikskenis)
    atjaunot_naudu()
    atjaunot_kliki()
    print("Jūs nopelnījāt " + str(peles_klikskenis) + " dolārus.")
    with open('uznemuma_stavoklis.pickle', 'wb') as f:
        pickle.dump((nauda, pārdoti_produkti, noskatītas_reklāmas, kliki), f)

def reklamas_skatisana():
    global nauda
    global noskatītas_reklāmas
    reklamas_klikskenis = random.randint(10, 100)
    nauda += reklamas_klikskenis
    noskatītas_reklāmas += 1
    atjaunot_naudu()
    atjaunot_reklamas()
    print("Jūs nopelnījāt " + str(reklamas_klikskenis) + " dolārus, skatoties reklāmas.")
    with open('uznemuma_stavoklis.pickle', 'wb') as f:
        pickle.dump((nauda, pārdoti_produkti, noskatītas_reklāmas, kliki), f)

def produkta_pardeve():
    global nauda
    global pārdoti_produkti
    produkta_cena = random.randint(50, 200)
    nauda += produkta_cena
    pārdoti_produkti += 1
    atjaunot_naudu()
    atjaunot_produktus()
    print("Jūs nopelnījāt " + str(produkta_cena) + " dolārus, pārdodot produktu.")
    with open('uznemuma_stavoklis.pickle', 'wb') as f:
        pickle.dump((nauda, pārdoti_produkti, noskatītas_reklāmas, kliki), f)

def saglabat_stavokli():
    with open('uznemuma_stavoklis.pickle', 'wb') as f:
        pickle.dump((nauda, pārdoti_produkti, noskatītas_reklāmas, kliki), f)

def ielasit_stavokli():
    global nauda
    global pārdoti_produkti
    global noskatītas_reklāmas
    global kliki
    try:
        with open('uznemuma_stavoklis.pickle', 'rb') as f: # nolasīt failu "rb" režīmā
            nauda, pārdoti_produkti, noskatītas_reklāmas, kliki = pickle.load(f)
    except FileNotFoundError:
        pass

def simulator():
    global nauda_uzraksts
    global produkta_uzraksts
    global reklamas_uzraksts
    global kliki_uzraksts
    ielasit_stavokli()
    root = tk.Tk()
    root.title("Biznesa simulatora palīdzība")
    root.geometry("400x300")
    def aizvert_programmu():
        root.destroy()

    nauda_uzraksts = tk.Label(root, text="Jūsu nauda: " + str(nauda) + " dolāri")
    nauda_uzraksts.pack()

    produkta_uzraksts = tk.Label(root, text="Pārdoti produkti: " + str(pārdoti_produkti))
    produkta_uzraksts.pack()

    reklamas_uzraksts = tk.Label(root, text="Noskatītas reklāmas: " + str(noskatītas_reklāmas))
    reklamas_uzraksts.pack()

    kliki_uzraksts = tk.Label(root, text="Klikšķi: " + str(len(kliki)))
    kliki_uzraksts.pack()

    darba_poga = tk.Button(root, text="Darbs", command=darbs)
    darba_poga.pack()

    reklamas_poga = tk.Button(root, text="Skatīties reklāmas", command=reklamas_skatisana)
    reklamas_poga.pack()

    produkta_pard_poga = tk.Button(root, text="Pārdot produktu", command=produkta_pardeve)
    produkta_pard_poga.pack()

    aizvert_poga = tk.Button(root, text="Iziet no simulators", command=aizvert_programmu)
    aizvert_poga.pack()

    root.protocol("WM_DELETE_WINDOW", saglabat_stavokli)
    root.mainloop()




    root.mainloop()

if __name__ == "__start_game__":
    simulator()