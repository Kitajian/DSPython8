"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1, number_range: int = 101) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.
        number_range (int, optional): Максимальное значение загаданного числа. Defaults to 101

    Returns:
        int: Число попыток
    """
    count = 0

    predict_number = number_range // 2
    min_number = 1 #минимальное значение при поиске числа
    max_number = number_range #максимальное значение при поиске числа
    while True:
        count += 1
        if number == predict_number:
            break  # выход из цикла если угадали
        if number < predict_number: #если загадываемое число меньше предполагаемого, то максимум равен предполагаемому числу
            max_number = predict_number
            predict_number = predict_number // 2  # а предполагаемое число делим пополам
        else:
            min_number = predict_number #если загадываемое число больше предполагаемого, то миниумм равен предполагаемому числу
            predict_number = min_number + (max_number-min_number) // 2 #предполагаемое число равно среднему между мин и макс
    return count


def score_game(random_predict, number_range: int = 101) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания
        number_range (int, optional): Максимальное значение загаданного числа. Defaults to 101

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, number_range, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number, number_range))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
