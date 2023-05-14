# import snake
# import shooter
# import jumper
import bizness

print("==== Spēļu simulatora galvenais izvēlnis ====")
print("Izvēlieties spēli:")
print("1. Snake")
print("2. Shooter")
print("3. Jumper")
print("4. Clicker Simulator(Bizzness) - kurā jums jāspiež uz pogām, lai nopelnītu punktus")


while True:
    user_choice = input("Lai izvēlētos, ievadiet atbilstošo ciparu: ")
    if user_choice not in ["1", "2", "3", "4"]:
        print("Nepareiza ievade. Lūdzu, ievadiet atbilstošo ciparu no 1 līdz 4.")
        continue
    else:
        break


if user_choice == "1":
    print("Jūs izvēlējāties spēli Snake.")
elif user_choice == "2":
    print("Jūs izvēlējāties spēli Shooter.")
elif user_choice == "3":
    print("Jūs izvēlējāties spēli Jumper.")
elif user_choice == "4":
    print("Jūs izvēlējāties spēli Clicker Simulator(Bizzness).")
    bizness.simulator()