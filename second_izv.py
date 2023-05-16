import tkinter as tk
import bizness
import random

def atvert_bankas_simulatoru():
    import Banka



def atvert_clicker_simulatoru():
    bizness.simulator()

def izveleties_speli():
    user_choice = choice_var.get()
    if user_choice == "1":
        print("Jūs izvēlējāties spēli Banka.")
        rows, cols = (8, 16)
        vv = [[random.randrange(0, 1)]*cols]*rows
        print(vv)
        atvert_bankas_simulatoru()
    elif user_choice == "2":
        print("Jūs izvēlējāties spēli Clicker Simulator(Bizzness).")
        rows, cols = (8, 16)
        vv = [[random.randrange(0, 1)]*cols]*rows
        print(vv)
        atvert_clicker_simulatoru()

root = tk.Tk()
root.title("Spēļu simulatora galvenais izvēlnis")

label = tk.Label(root, text="==== Spēļu simulatora galvenais izvēlnis ====")
label.pack()

choice_var = tk.StringVar()

banka_btn = tk.Radiobutton(root, text="Banka", variable=choice_var, value="1")
banka_btn.pack()


clicker_btn = tk.Radiobutton(root, text="Clicker Simulator(Bizzness)", variable=choice_var, value="2")
clicker_btn.pack()

select_btn = tk.Button(root, text="Izvēlēties", command=izveleties_speli)
select_btn.pack()

root.mainloop()
