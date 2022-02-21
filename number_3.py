# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

# Через список
month_number = int(input('Введите номер месяца '))
winter = [1,2,12]
spring = [3,4,5]
summer = [6,7,8]
autumn = [9,10,11]
if 1 <= month_number <= 12:
    if month_number in winter:
        print('Найдено через список: Зима')
    elif month_number in spring:
        print('Найдено через список: Весна')
    elif month_number in autumn:
        print('Найдено через список: Осень')
    elif month_number in summer:
        print('Найдено через список: Лето')
else:
    print('Давай не хулигань, номера месяца лежат в диапаоне от 1 до 12')

# Через словарь
seasons = {
    'Зима':[1,2,12],
    'Весна':[3,4,5],
    'Лето':[6,7,8],
    'Осень':[9,10,11]
}
for key in seasons.keys():
    if month_number in seasons.get(key):
        print('Найдено через словарь: ',key)