def celsius_to_fahrenheit(celsius):
    fahrenheit=(celsius*9/5)+32
    return fahrenheit
def fahrenheit_to_celsius(fahrenheit):
    celsius=(fahrenheit-32)*5/9
    return celsius
choice=input("Выберите вариант:\n1. Перевести из Цельсия в Фаренгейты\n2. Перевести из Фаренгейта в Цельсии\n")


if choice=='1':
    celsius=float(input("Температура в цельсиях:"))
    fahrenheit=celsius_to_fahrenheit(celsius)
    print(f"{celsius}градусов цельссия={fahrenheit}градусов френгейта")
elif choice=='2':
    fahrenheit=float(input("Температура в фаренгейтах:"))
    celsius=fahrenheit_to_celsius(fahrenheit)
    print(f"{fahrenheit}градусов фаренгейта={celsius}градусов цельсия")
else:
    print("неправильный выбор. Ведите число 1 или 2")