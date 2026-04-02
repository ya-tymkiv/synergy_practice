import random
import json
import os
import time

FILE_NAME = "results.json"

# Уровни сложности
LEVELS = {
    "1": {"name": "Лёгкий", "range": 50, "attempts": 10},
    "2": {"name": "Средний", "range": 100, "attempts": 7},
    "3": {"name": "Сложный", "range": 200, "attempts": 5},
}

def load_results():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_results(results):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=4)

def show_rating(results):
    if not results:
        print("Рейтинг пока пуст.\n")
        return

    print("\n=== Рейтинг игроков ===")
    sorted_results = sorted(results, key=lambda x: (x["attempts"], x["time"]))
    
    for i, r in enumerate(sorted_results[:10], 1):
        print(f"{i}. {r['name']} — попытки: {r['attempts']}, время: {r['time']:.2f} сек, уровень: {r['level']}")
    print()

def choose_level():
    print("Выберите уровень сложности:")
    for key, value in LEVELS.items():
        print(f"{key} — {value['name']} (1–{value['range']}, попыток: {value['attempts']})")

    while True:
        choice = input("Ваш выбор: ")
        if choice in LEVELS:
            return LEVELS[choice]
        print("Некорректный выбор.")

def get_number(max_range):
    while True:
        try:
            num = int(input(f"Введите число от 1 до {max_range}: "))
            if 1 <= num <= max_range:
                return num
            else:
                print("Число вне диапазона.")
        except ValueError:
            print("Введите целое число.")

def play_game():
    level = choose_level()
    secret = random.randint(1, level["range"])
    attempts = 0

    print(f"\nЯ загадал число от 1 до {level['range']}")

    start_time = time.time()

    while attempts < level["attempts"]:
        guess = get_number(level["range"])
        attempts += 1

        if guess < secret:
            print("Слишком маленькое.")
        elif guess > secret:
            print("Слишком большое.")
        else:
            end_time = time.time()
            duration = end_time - start_time

            print(f"🎉 Вы угадали за {attempts} попыток!")

            name = input("Введите ваше имя: ")

            return {
                "name": name,
                "attempts": attempts,
                "time": duration,
                "level": level["name"]
            }

        print(f"Осталось попыток: {level['attempts'] - attempts}")

    print(f"Вы проиграли. Число было: {secret}")
    return None

def main():
    results = load_results()

    while True:
        print("\n=== МЕНЮ ===")
        print("1 — Играть")
        print("2 — Рейтинг")
        print("3 — Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            result = play_game()
            if result:
                results.append(result)
                save_results(results)
        elif choice == "2":
            show_rating(results)
        elif choice == "3":
            print("Выход из игры.")
            break
        else:
            print("Неверный выбор.")

if __name__ == "__main__":
    main()
