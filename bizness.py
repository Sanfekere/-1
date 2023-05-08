import random
import time
import tkinter as tk

nauda = 1000
uznemuma_nosaukums = "Mans uzņēmums"
nauda_uzraksts = None

def atjaunot_naudu():
    global nauda_uzraksts
    nauda_uzraksts.config(text="Jūsu nauda: " + str(nauda) + " dolāri")

def darbs():
    global nauda
    peles_klikskenis = random.randint(1, 100)
    nauda += peles_klikskenis
    atjaunot_naudu()
    print("Jūs nopelnījāt " + str(peles_klikskenis) + " dolārus.")
    # time.sleep(1)

def reklamas_skatisana():
    global nauda
    reklamas_klikskenis = random.randint(10, 100)
    nauda += reklamas_klikskenis
    atjaunot_naudu()
    print("Jūs nopelnījāt " + str(reklamas_klikskenis) + " dolārus, skatoties reklāmas.")
    # time.sleep(1)

def produkta_pardeve():
    global nauda
    produkta_cena = random.randint(50, 200)
    nauda += produkta_cena
    atjaunot_naudu()
    print("Jūs nopelnījāt " + str(produkta_cena) + " dolārus, pārdodot produktu.")
    # time.sleep(1)

def simulator():
    global nauda_uzraksts

    root = tk.Tk()
    root.title("Biznesa simulatora palīdzība")
    root.geometry("400x300")

    nauda_uzraksts = tk.Label(root, text="Jūsu nauda: " + str(nauda) + " dolāri")
    nauda_uzraksts.pack()

    darba_poga = tk.Button(root, text="Darbs", command=darbs)
    darba_poga.pack()

    reklamas_poga = tk.Button(root, text="Skatīties reklāmas", command=reklamas_skatisana)
    reklamas_poga.pack()

    produkta_pard_poga = tk.Button(root, text="Pārdot produktu", command=produkta_pardeve)
    produkta_pard_poga.pack()

    def aizvert_programmu():
        root.destroy()

    aizvert_poga = tk.Button(root, text="Iziet no simulators", command=aizvert_programmu)
    aizvert_poga.pack()

    root.mainloop()


if __name__ == "__start_game__":
    simulator()
