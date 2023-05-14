
import bizness


print("==== Spēļu simulatora galvenais izvēlnis ====")
print("Izvēlieties spēli:")
print("1. Banka")
print("2. Clicker Simulator(Bizzness) - kurā jums jāspiež uz pogām, lai nopelnītu punktus")


while True:
    user_choice = input("Lai izvēlētos, ievadiet atbilstošo ciparu: ")
    if user_choice not in ["1", "2"]:
        print("Nepareiza ievade. Lūdzu, ievadiet atbilstošo ciparu no 1 līdz 4.")
        continue
    else:
        break

if user_choice == "1":
    print("Jūs izvēlējāties spēli Banka.")
    import Banka
elif user_choice == "2":
    print("Jūs izvēlējāties spēli Clicker Simulator(Bizzness).")
    bizness.simulator()