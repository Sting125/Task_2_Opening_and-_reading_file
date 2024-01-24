import os  # Импорт модуля os для операций с путями файлов
from pprint import pprint

def cook_book_read(): #Задание 1. Получения словаря cook_book
    cook_book = {}  # Инициализация пустого словаря для хранения данных кулинарной книги
    file_path = os.path.join(os.getcwd(), 'recipes.txt')  # Создание пути к файлу recipes.txt в текущем рабочем каталоге

    with open(file_path, 'r', encoding='utf-8') as f:  # Открытие файла в режиме чтения с кодировкой UTF-8
        data = f.read().split('\n\n')  # Чтение файла и разделение его на части, разделенные двумя последовательными символами новой строки

        for dish in data:  # Итерация по каждой части, представляющей блюдо
            dish = dish.split('\n')  # Разделение части на строки

            ingrdns_all = []  # Инициализация списка для хранения ингредиентов текущего блюда

            # Итерация по каждой строке, начиная с третьей строки (индекс 2), для извлечения информации об ингредиентах
            for ingr in dish[2:]:
                ingrdns = {}  # Инициализация словаря для хранения информации о каждом ингредиенте
                ingrdns['ingredient_name'], ingrdns['quantity'], ingrdns['measure'] = ingr.split('|')  # Разделение строки на имя ингредиента, количество и ед. изм, используя разделитель '|'
                ingrdns['quantity'] = int(ingrdns['quantity'])  # Преобразование количества в целое число
                ingrdns_all.append(ingrdns)  # Добавление информации об ингредиенте в список для текущего блюда

            cook_book[dish[0]] = ingrdns_all  # Добавление блюда и соответствующего списка ингредиентов в словарь cook_book

    return cook_book  # Возврат окончательного словаря кулинарной книги
cook_book = cook_book_read()
pprint(cook_book)


def get_shop_list_by_dishes(dishes, person_count): #Задание 2.Получения словаря исходя из количества персон
    ingrs_list = {}  # Инициализация пустого словаря для хранения списка покупок
    for dish_name in dishes:  # Итерация по каждому блюду из списка
        for ingr in cook_book[dish_name]:  # Итерация по каждому ингредиенту в текущем блюде
            dict_ingrs = {}  # Инициализация словаря для хранения информации об ингредиенте
            if ingr['ingredient_name'] not in ingrs_list:  # Проверка, есть ли ингредиент уже в списке покупок
                dict_ingrs['measure'] = ingr['measure']  # Добавление единицы измерения в словарь
                dict_ingrs['quantity'] = ingr['quantity'] * person_count  # Рассчет общего количества ингредиента для указанного количества персон
                ingrs_list[ingr['ingredient_name']] = dict_ingrs  # Добавление ингредиента в список покупок
            else:
                # Если ингредиент уже есть в списке покупок, увеличиваем количество на необходимую величину
                ingrs_list[ingr['ingredient_name']]['quantity'] += ingr['quantity'] * person_count

    return ingrs_list  # Возврат окончательного списка покупок
pprint(get_shop_list_by_dishes(['Омлет', 'Запеченный картофель', 'Омлет'], 2))



    #Задание3

# Функция для создания словаря с данными о файлах в указанной директории
def list_file_create(txt):
    dict_file = {}  # Инициализация пустого словаря для хранения данных о файлах (имя файла: количество строк)
    list_file = os.listdir(txt)  # Получение списка имен файлов в указанной директории


    # Итерация по каждому файлу в списке
    for i in list_file:
        # Открытие файла для чтения
        with open(os.path.join(txt, i), 'r', encoding='utf-8') as f:
            file_1 = f.readlines()  # Чтение всех строк файла в список
            dict_file[i] = len(file_1)  # Запись в словарь: имя файла -> количество строк в файле

    return dict_file  # Возврат словаря с данными о файлах


# Функция для записи данных о файлах в отсортированном порядке в новый файл
def file_res(txt):
    # Получение списка кортежей (имя файла, количество строк)
    list_tuple = list(list_file_create(txt).items())


    list_sorted = [i[0] for i in sorted(list_tuple, key=lambda items: items[1])]  # Сортировка по количеству строк

    # Проверка наличия файла 'write_file.txt' перед его удалением
    if os.path.exists('write_file.txt'):
        os.remove('write_file.txt')  # Удаление файла 'write_file.txt', если он существует

    # Итерация по отсортированным именам файлов. Для каждого файла:
    for name_file in list_sorted:
        # Открытие файла 'write_file.txt' в режиме добавления (если файла нет, он будет создан)
        with open('write_file.txt', 'a', encoding='utf-8') as f_1:
            # Открытие исходного файла для чтения
            with open(os.path.join(txt, name_file), 'r', encoding='utf-8') as f:
                text_file = f.readlines()  # Чтение всех строк файла в список
            f_1.write(name_file + '\n')  # Запись имени файла в 'write_file.txt'
            f_1.write(str(len(text_file)) + '\n')  # Запись количества строк в 'write_file.txt'
            f_1.writelines(text_file)  # Запись всех строк файла в 'write_file.txt'
            f_1.write('\n')  # Добавление пустой строки после каждого файла в 'write_file.txt'

    return
def read_and_print_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            print(content)
    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
    except Exception as e:
        print(f"Произошла ошибка при чтении файла: {e}")

# Вызов функции для чтения и вывода содержимого файла 'write_file.txt'
read_and_print_file('write_file.txt')

# Вызов функции file_res для директории 'txt'
file_res('txt')