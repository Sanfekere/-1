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

def simulator():
    global nauda_uzraksts

    root = tk.Tk()
    root.title("Biznesa simulatora palīdzība")
    root.geometry("400x300")

    nauda_uzraksts = tk.Label(root, text="Jūsu nauda: " + str(nauda) + " dolāri")
    nauda_uzraksts.pack()

    darba_poga = tk.Button(root, text="Darbs", command=darbs)
    darba_poga.pack()

    def aizvert_programmu():
        root.destroy()

    aizvert_poga = tk.Button(root, text="Iziet no simulators", command=aizvert_programmu)
    aizvert_poga.pack()

    root.mainloop()

simulator()
