# Примерный словарь
cook_book_example = {
  'яйчница': [
    {'ingridient_name': 'яйца', 'quantity': 2, 'measure': 'шт.'},
    {'ingridient_name': 'помидоры', 'quantity': 100, 'measure': 'гр.'}
    ],
  'стейк': [
    {'ingridient_name': 'говядина', 'quantity': 300, 'measure': 'гр.'},
    {'ingridient_name': 'специи', 'quantity': 5, 'measure': 'гр.'},
    {'ingridient_name': 'масло', 'quantity': 10, 'measure': 'мл.'}
    ],
  'салат': [
    {'ingridient_name': 'помидоры', 'quantity': 100, 'measure': 'гр.'},
    {'ingridient_name': 'огурцы', 'quantity': 100, 'measure': 'гр.'},
    {'ingridient_name': 'масло', 'quantity': 100, 'measure': 'мл.'},
    {'ingridient_name': 'лук', 'quantity': 1, 'measure': 'шт.'}
    ]
}
# Вывод словаря сформированного из фаила
def print_dish(dictionary):
  for key, value in dictionary.items():
    print(key, end = ':\n')
    for dic in value:
      print(dic)

# Конвертируем элемент списка в integer
def integer_quantity(list):
  for value in range(len(list)):
    if list[value].isdigit() == True:
      list.insert(value, int(list.pop(value)))
  return list

# Заполняем словарь блюд по данным из фаила data_file.txt
def cook_book_complite():
  with open('data_file.txt', encoding = 'utf-8') as file:
    cook_book = dict() # Словарь блюд

    for data in file:
      # Считываем кол-во ингридиентов в блюде
      ingridient_quantity = file.readline().strip()
      ingridient_quantity = int(ingridient_quantity)

      list_key_ingridient = ['ingridient_name', 'quantity', 'measure'] # Список ключей для продукитов в блюде
      list_dictionary_ingridient = [] # Список словарей ингридиентов
      # Считываем ингридиенты
      for ingridient in range(ingridient_quantity):
        dictionary_ingridient = {} # Словарь ингридиентов

        ingridient_str = file.readline().strip()
        ingridient_str = ingridient_str.lower()
        ingridient_str = ingridient_str.split(' | ')
        ingridient_str = integer_quantity(ingridient_str)

        #print(ingridient_str) # Отладочный принт

        # Словарь ингридиента
        for products in range(len(ingridient_str)):
          dictionary_ingridient[list_key_ingridient[products]] = ingridient_str[products]

        #print(dictionary_ingridient)# Отладочный принт

        list_dictionary_ingridient.append(dictionary_ingridient)

        #print(list_dictionary_ingridient)# Отладочный принт

      file.readline() # Считываем пустую строку
      cook_book[data.strip().lower()] = list_dictionary_ingridient
  return cook_book

def get_shop_list_by_dishes(dishes, person_count):
      cook_book = cook_book_complite()
      # Проверочные принты
      print_dish(cook_book_example)
      print('\n')
      print_dish(cook_book)

      shop_list = {}
      for dish in dishes:
        for ingridient in cook_book[dish]:
          new_shop_list_item = dict(ingridient)

          new_shop_list_item['quantity'] *= person_count
          if new_shop_list_item['ingridient_name'] not in shop_list:
            shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
          else:
            shop_list[new_shop_list_item['ingridient_name']]['quantity'] += new_shop_list_item['quantity']
      return shop_list

def print_shop_list(shop_list):
      for shop_list_item in shop_list.values():
        print('{} {} {}'.format(shop_list_item['ingridient_name'], shop_list_item['quantity'], 
                                shop_list_item['measure']))

def create_shop_list():
      person_count = int(input('Введите количество человек: '))
      dishes = input('Введите блюда в расчете на одного человека (через запятую): ') \
        .lower().split(', ')
      shop_list = get_shop_list_by_dishes(dishes, person_count)
      print_shop_list(shop_list)

create_shop_list()