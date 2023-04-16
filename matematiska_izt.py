import random

def generate_numbers(max_num):
    num1 = random.randint(0, max_num)
    num2 = random.randint(0, max_num)
    return num1, num2

def generate_operator():
    operators = ["+", "-", "*", "/", "**"]
    return random.choice(operators)

def calculate_answer(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1 / num2
    elif operator == "**":
        return num1 ** num2

def main():
    max_num = int(input("Ievadiet maksimālo skaitli: "))
    correct_answers = 0
    incorrect_answers = 0

    while True:
        num1, num2 = generate_numbers(max_num)
        operator = generate_operator()
        answer = calculate_answer(num1, num2, operator)

        user_answer = input(f"{num1} {operator} {num2} = ")

        if user_answer == str(answer):
            print("PAREIZI")
            correct_answers += 1
        else:
            print("NEPAREIZI")
            incorrect_answers += 1

        continue_answer = input("Vai turpināt? (jā/nē) ")
        if continue_answer.lower() == "nē":
            break

    total_answers = correct_answers + incorrect_answers
    percentage = (correct_answers / total_answers) * 100

    print(f"Pareizo atbilžu skaits: {correct_answers}")
    print(f"Nepareizo atbilžu skaits: {incorrect_answers}")
    print(f"Jūsu vērtējums: {percentage}%")

    with open("rezultati.txt", mode="a", encoding="utf-8") as f:
        f.write(f"Pareizo atbilžu skaits: {correct_answers}\n")
        f.write(f"Nepareizo atbilžu skaits: {incorrect_answers}\n")
        f.write(f"Jūsu vērtējums: {percentage}%\n")

if __name__ == "__main__":
    main()
