# 1. Напишите функцию, которая будет принимать номер кредитной карты и показывать только последние 4 цифры.
# Остальные цифры должны заменяться звездочками


def number_card():

    card = print(input("Введите номер карты:"))
    return '*' * len(card[:-4]) + card[-4:]



