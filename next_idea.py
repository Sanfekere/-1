import tetris
import wordlies
import shooter
import jumper
import snake

# izveido funkciju, lai izvēlētos spēli
def choose_game():
    print("Lūdzu, izvēlieties spēli:")
    print("1. Tetris")
    print("2. Wordlies")
    print("3. Shooter")
    print("4. Jumper")
    print("5. Snake")

    choice = input("Jūsu izvēle: ")

    if choice == "1":
        tetris.play_game()
    elif choice == "2":
        wordlies.play_game()
    elif choice == "3":
        shooter.play_game()
    elif choice == "4":
        jumper.play_game()
    elif choice == "5":
        snake.play_game()
    else:
        print("Nepareiza ievade. Lūdzu, izvēlieties spēli no 1 līdz 5.")
        choose_game()

# galvenais kods
print("Sveiki! Laipni lūgti spēļu simulatorā.")
choose_game()
