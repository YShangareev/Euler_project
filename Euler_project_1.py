# Проект Эйлера
# Задача 1

def search_and_sum(a):
    # Создаем новый список для хранения чисел кратных 3 и 5
    newList = []
    # Присваиваем переменной i длину списка а
    for i in range(len(a)):
        # Проверяем условия кратности 3 или 5
        if i % 3 == 0 or i % 5 == 0:
            # Добавляем в новый список
            newList.append(i)
    # Суммируем все элементы нового списка
    sum_search = sum(newList)
    # Выводим сумму итоговую
    print(sum_search)

my_list = [i for i in range(1, 1000)]
search_and_sum(my_list)