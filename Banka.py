import tkinter as tk
import json

uznemuma_nosaukums = "ManA Banka"

class Banka:
    def __init__(self, nosaukums):
        self.nosaukums = nosaukums
        self.klienti = {}
        self.klienta_id_skaitītājs = 0


    def pievienot_klientu(self, klienta_vards, klienta_uzvards, konta_bilance=0):
        self.klienta_id_skaitītājs += 1
        klienta_id = self.klienta_id_skaitītājs
        jauns_klients = Klients(klienta_id, klienta_vards, klienta_uzvards, konta_bilance)
        self.klienti[klienta_id] = jauns_klients

    def dzest_klientu(self, klienta_id):
        if klienta_id in self.klienti:
            dzestais_klients = self.klienti.pop(klienta_id)
            print(f"Klients dzests: {dzestais_klients}")
            self.atjaunot_klienta_id_skaitītāju()
            tukso_id = self.atrast_tukso_id()
            if tukso_id is not None and tukso_id > klienta_id:
                self.klienti[tukso_id] = dzestais_klients
        else:
            print("Klients ar šādu ID nav atrasts.")

    def aktualizet_klienta_id_skaits(self):
        if self.klienti:
            self.klienta_id_skaitītājs = max(self.klienti.keys())
        else:
            self.klienta_id_skaitītājs = 0

    def paradiet_klientus(self):
        klientu_saraksts = []
        for klienta_id, klients in self.klienti.items():
            klientu_saraksts.append({
                'ID': klienta_id,
                'Vārds': klients.vards,
                'Uzvārds': klients.uzvards,
                'Bilance': klients.bilance
            })
        return klientu_saraksts

    def paradiet_konta_bilanci(self, klienta_id):
        if klienta_id in self.klienti:
            klients = self.klienti[klienta_id]
            return klients.bilance
        else:
            return "Klients ar šādu ID nav atrasts."

    def pievienot_naudu(self, klienta_id, summa):
        if klienta_id in self.klienti:
            klients = self.klienti[klienta_id]
            klients.bilance += summa
        else:
            print("Klients ar šādu ID nav atrasts.")

    def saglabat_datus(self, fails):
        dati = {
            'nosaukums': self.nosaukums,
            'klienti': []
        }
        for klienta_id, klients in self.klienti.items():
            dati['klienti'].append({
                'klienta_id': klienta_id,
                'vards': klients.vards,
                'uzvards': klients.uzvards,
                'bilance': klients.bilance
            })

        with open(fails, 'w') as f:
            json.dump(dati, f, indent=4)

        print("Dati ir saglabāti!")

    def nodzest_datus(self):
        self.klienti = {}
        self.atjaunot_klienta_id_skaitītāju()
        print("Dati ir nodzēsti!")

    def atjaunot_klienta_id_skaitītāju(self):
        self.klienta_id_skaitītājs = max(self.klienti.keys(), default=0)

    def atrast_tukso_id(self):
        pieejamie_id = set(range(1, self.klienta_id_skaitītājs + 2))
        izmantotie_id = set(self.klienti.keys())
        tukso_id = next(iter(pieejamie_id - izmantotie_id), None)
        return tukso_id

class Klients:
    def __init__(self, klienta_id, vards, uzvards, bilance=0):
        self.klienta_id = klienta_id
        self.vards = vards
        self.uzvards = uzvards
        self.bilance = bilance

    def __str__(self):
        return f"ID: {self.klienta_id}, Vārds: {self.vards}, Uzvārds: {self.uzvards}, Bilance: {self.bilance}"

class BankaSimulators:
    def __init__(self, logs):
        self.logs = logs
        self.banka = Banka("Mana Banka")

        self.logs.insert(tk.END, "Sveiki! Laipni lūdzam bankas simulatorā.\n")

        self.izveidot_interfeisu()
    def saglabat_datus_katra_klikski(self):
        fails = "bankas_dati.json"
        self.banka.saglabat_datus(fails)
        self.logs.config(state=tk.NORMAL)
        self.logs.config(state=tk.DISABLED)

    def izveidot_interfeisu(self):
        self.logs.config(state=tk.DISABLED)

        self.logs.pack()

        self.klienta_vards_entry = tk.Entry(root)
        self.klienta_vards_entry.insert(0, "Vārds")
        self.klienta_vards_entry.pack()

        self.klienta_uzvards_entry = tk.Entry(root)
        self.klienta_uzvards_entry.insert(0, "Uzvārds")
        self.klienta_uzvards_entry.pack()

        pievienot_klientu_btn = tk.Button(root, text="Pievienot klientu", command=self.pievienot_klientu)
        pievienot_klientu_btn.pack()

        self.klienta_id_dzest_entry = tk.Entry(root)
        self.klienta_id_dzest_entry.insert(0, "Id")
        self.klienta_id_dzest_entry.pack()

        dzest_klientu_btn = tk.Button(root, text="Dzēst klientu", command=self.dzest_klientu)
        dzest_klientu_btn.pack()

        paradiet_klientus_btn = tk.Button(root, text="Parādīt klientus", command=self.paradiet_klientus)
        paradiet_klientus_btn.pack()

        self.klienta_id_bilance_entry = tk.Entry(root)
        self.klienta_id_bilance_entry.insert(0, "Id")
        self.klienta_id_bilance_entry.pack()

        paradiet_konta_bilanci_btn = tk.Button(root, text="Parādīt konta bilanci", command=self.paradiet_konta_bilanci)
        paradiet_konta_bilanci_btn.pack()

        self.klienta_id_pievienot_entry = tk.Entry(root)
        self.klienta_id_pievienot_entry.insert(0, "Id")
        self.klienta_id_pievienot_entry.pack()

        self.naudas_summa_entry = tk.Entry(root)
        self.naudas_summa_entry.insert(0, "Summa")
        self.naudas_summa_entry.pack()

        pievienot_naudu_btn = tk.Button(root, text="Pievienot naudu", command=self.pievienot_naudu)
        pievienot_naudu_btn.pack()

        saglabat_datus_btn = tk.Button(root, text="Saglabāt datus", command=self.saglabat_datus)
        saglabat_datus_btn.pack()

        nodzest_datus_btn = tk.Button(root, text="Nodzēst datus", command=self.nodzest_datus)
        nodzest_datus_btn.pack()

        self.klientu_saraksta_logs = tk.Text(root, width=70, height=15)
        self.klientu_saraksta_logs.pack()

        self.konta_bilances_logs = tk.Text(root, width=70, height=10)
        self.konta_bilances_logs.pack()

        bankas_uzraksts_label = tk.Label(root, text="Bankas nosaukums:")
        bankas_uzraksts_label.pack()

        self.bankas_uzraksts_entry = tk.Entry(root)
        self.bankas_uzraksts_entry.pack()

        bankas_uzraksts_btn = tk.Button(root, text="Mainīt uzrakstu", command=self.mainit_bankas_uzrakstu)
        bankas_uzraksts_btn.pack()
        self.paradiet_klientus()


    def mainit_bankas_uzrakstu(self):
        jauns_uzraksts = self.bankas_uzraksts_entry.get()
        if jauns_uzraksts:
            self.banka.nosaukums = jauns_uzraksts
            self.logs.config(state=tk.NORMAL)
            self.logs.insert(tk.END, f"Bankas uzraksts ir mainīts uz: {jauns_uzraksts}\n")
            self.logs.config(state=tk.DISABLED)

            self.bankas_uzraksts_entry.delete(0, tk.END)
        else:
            self.logs.config(state=tk.NORMAL)
            self.logs.insert(tk.END, "Lūdzu, ievadiet jauno bankas uzrakstu.\n")
            self.logs.config(state=tk.DISABLED)
            self.bankas_uzraksts_entry.insert(0, "Bankas Nosaukums")
            self.bankas_uzraksts_entry.config(fg="gray")




    def pievienot_klientu(self):
        klienta_vards = self.klienta_vards_entry.get()
        klienta_uzvards = self.klienta_uzvards_entry.get()

        if klienta_vards and klienta_uzvards:
            self.banka.pievienot_klientu(klienta_vards, klienta_uzvards)
            self.logs.config(state=tk.NORMAL)
            self.logs.insert(tk.END, f"Jauns klients pievienots: Vārds: {klienta_vards}, Uzvārds: {klienta_uzvards}\n")
            self.logs.config(state=tk.DISABLED)

            self.klienta_vards_entry.delete(0, tk.END)
            self.klienta_uzvards_entry.delete(0, tk.END)
        else:
            self.logs.config(state=tk.NORMAL)
            self.logs.insert(tk.END, "Lūdzu, ievadiet gan klienta vārdu, gan uzvārdu.\n")
            self.logs.config(state=tk.DISABLED)

        self.saglabat_datus_katra_klikski()
        self.paradiet_klientus()


    def dzest_klientu(self):
        klienta_id = self.klienta_id_dzest_entry.get()

        try:
            klienta_id = int(klienta_id)
        except ValueError:
            self.logs.config(state=tk.NORMAL)
            self.logs.insert(tk.END, "Klienta ID jābūt skaitlim.\n")
            self.logs.config(state=tk.DISABLED)
            return

        self.banka.dzest_klientu(klienta_id)
        self.logs.config(state=tk.NORMAL)
        self.logs.insert(tk.END, f"Klients dzests: ID: {klienta_id}\n")
        self.logs.config(state=tk.DISABLED)

        self.klienta_id_dzest_entry.delete(0, tk.END)

        self.saglabat_datus_katra_klikski()
        self.paradiet_klientus()

    def paradiet_klientus(self):
            with open('bankas_dati.json', 'r') as file:
                dati = json.load(file)

            klientu_saraksts = dati['klienti']

            self.klientu_saraksta_logs.config(state=tk.NORMAL)
            self.klientu_saraksta_logs.delete('1.0', tk.END)

            for klienta_dati in klientu_saraksts:
                self.klientu_saraksta_logs.insert(tk.END, f"Klients ID: {klienta_dati['klienta_id']}, Vārds: {klienta_dati['vards']}, Uzvārds: {klienta_dati['uzvards']}, Bilance: {klienta_dati['bilance']}\n")

            self.klientu_saraksta_logs.config(state=tk.DISABLED)


    def paradiet_konta_bilanci(self):
        klienta_id = self.klienta_id_bilance_entry.get()

        try:
            klienta_id = int(klienta_id)
        except ValueError:
            self.logs.config(state=tk.NORMAL)
            self.logs.insert(tk.END, "Klienta ID jābūt skaitlim.\n")
            self.logs.config(state=tk.DISABLED)
            return

        bilance = self.banka.paradiet_konta_bilanci(klienta_id)
        self.konta_bilances_logs.config(state=tk.NORMAL)
        self.konta_bilances_logs.delete('1.0', tk.END)
        self.konta_bilances_logs.insert(tk.END, f"Konta bilance klientam ar ID: {klienta_id}: {bilance}\n")
        self.konta_bilances_logs.config(state=tk.DISABLED)

        self.klienta_id_bilance_entry.delete(0, tk.END)

    def pievienot_naudu(self):
        klienta_id = self.klienta_id_pievienot_entry.get()
        naudas_summa = self.naudas_summa_entry.get()

        try:
            klienta_id = int(klienta_id)
            naudas_summa = float(naudas_summa)
        except ValueError:
            self.logs.config(state=tk.NORMAL)
            self.logs.insert(tk.END, "Klienta ID jābūt skaitlim, naudas summai jābūt skaitliskai vērtībai.\n")
            self.logs.config(state=tk.DISABLED)
            return

        self.banka.pievienot_naudu(klienta_id, naudas_summa)

        self.logs.config(state=tk.NORMAL)
        self.logs.insert(tk.END, f"Pievienota nauda klientam ar ID: {klienta_id}, summa: {naudas_summa}\n")
        self.logs.config(state=tk.DISABLED)

        self.klienta_id_pievienot_entry.delete(0, tk.END)
        self.naudas_summa_entry.delete(0, tk.END)
        self.saglabat_datus_katra_klikski()
        self.paradiet_klientus()

    def saglabat_datus(self):
        fails = "bankas_dati.json"
        self.banka.saglabat_datus(fails)
        self.logs.config(state=tk.NORMAL)
        self.logs.insert(tk.END, "Dati ir saglabāti!\n")
        self.logs.config(state=tk.DISABLED)

    def nodzest_datus(self):
        self.banka.nodzest_datus()
        self.logs.config(state=tk.NORMAL)
        self.logs.insert(tk.END, "Dati ir nodzēsti!\n")
        self.logs.config(state=tk.DISABLED)
        self.saglabat_datus_katra_klikski()
        self.paradiet_klientus()



root = tk.Tk()
root.title("Bankas Simulators")

logs = tk.Text(root, width=70, height=10)
banka_simulators = BankaSimulators(logs)

root.mainloop()
