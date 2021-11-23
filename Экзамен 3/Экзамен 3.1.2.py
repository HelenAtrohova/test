# 2. Напишите функцию, которая проверяет: является ли слово палиндромом


def palindrome(data):
    data = data.replace(' ','').lower()
    return 'Палиндром' if data == data[::-1] else 'Не является палиандром'