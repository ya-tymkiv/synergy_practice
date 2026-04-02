import math
import time

MAX_NUMBER = 100000  # ограничение для защиты от слишком больших значений

def factorial_manual(n):
    """Вычисление факториала вручную (итеративно)"""
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def factorial_math(n):
    """Вычисление факториала через библиотеку math"""
    return math.factorial(n)

def get_valid_number():
    """Запрашивает корректное число у пользователя"""
    while True:
        user_input = input("Введите положительное целое число (или 'q' для выхода): ")
        
        if user_input.lower() == 'q':
            return None

        try:
            number = int(user_input)

            if number < 0:
                print("Ошибка: число должно быть неотрицательным.")
            elif number > MAX_NUMBER:
                print(f"Слишком большое число! Максимум: {MAX_NUMBER}")
            else:
                return number

        except ValueError:
            print("Ошибка: введите целое число.")

def choose_method():
    """Выбор метода вычисления"""
    while True:
        print("\nВыберите способ вычисления:")
        print("1 — Быстрый (math.factorial)")
        print("2 — Ручной (цикл)")

        choice = input("Ваш выбор: ")

        if choice == '1':
            return factorial_math
        elif choice == '2':
            return factorial_manual
        else:
            print("Некорректный выбор. Попробуйте снова.")

def main():
    print("=== Калькулятор факториала ===")

    while True:
        number = get_valid_number()

        if number is None:
            print("Выход из программы.")
            break

        method = choose_method()

        start_time = time.time()
        result = method(number)
        end_time = time.time()

        print(f"\nФакториал числа {number}:")
        
        # Ограничим вывод очень длинных чисел
        result_str = str(result)
        if len(result_str) > 100:
            print(result_str[:100] + "... [обрезано]")
            print(f"(всего цифр: {len(result_str)})")
        else:
            print(result)

        print(f"Время выполнения: {end_time - start_time:.6f} сек\n")

if __name__ == "__main__":
    main()
