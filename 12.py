stop_char = input("Ievadiet simbolu, pie kura vēlaties pārtraukt ievadi: ")

with open("sanja.txt", 'w',encoding="utf-8") as file:
    while True:
        text = input("Ievadiet tekstu: ")
        if stop_char in text:
            file.write(text[:text.index(stop_char)])
            break
        else:
            file.write(text)

with open("sanja.txt", 'r',encoding="utf-8") as file:
    print(file.read())
