import random

options = ["камень", "ножницы", "бумага"]
player_score = 0
computer_score = 0
winning_score = 3

print("Игра Камень, Ножницы, Бумага. Играем до 3 побед!")

while player_score < winning_score and computer_score < winning_score:
    player_choice = input("Выберите камень, ножницы или бумагу: ").lower()
    if player_choice not in options:
        print("Неверный ввод, попробуйте снова.")
        continue

    computer_choice = random.choice(options)
    print(f"Компьютер выбрал: {computer_choice}")

    if player_choice == computer_choice:
        print("Ничья!")
    elif (player_choice == "камень" and computer_choice == "ножницы") or \
         (player_choice == "ножницы" and computer_choice == "бумага") or \
         (player_choice == "бумага" and computer_choice == "камень"):
        player_score += 1
        print("Вы выиграли этот раунд!")
    else:
        computer_score += 1
        print("Компьютер выиграл этот раунд!")

    print(f"Счёт: Вы {player_score} : Компьютер {computer_score}\n")

if player_score == winning_score:
    print("Поздравляю! Вы победили в игре!")
else:
    print("Компьютер победил. Попробуйте ещё раз!")
