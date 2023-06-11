



human = {
    "name": "John",
    "age": "18",
    "id": "188989",
    "team": ["John", "john2", "john3"],
    1: ["John", "john2", "john3"],
}
keys = human.keys()  # получаем ключи словаря

def check_key_existence(input_key):
    found_key = False  # флаг, указывающий, был ли найден ключ "data"

# !разобраться что делает данный код
    for key in keys:
        if key == input_key or (isinstance(key, int) and str(key) == input_key):
            print("данный ключ имеется")
            found_key = True  # устанавливаем флаг в True, если ключ найден
            break  # выходим из цикла, если ключ найден

    if not found_key:
        print("Данного ключа не существует")  # выводим сообщение, если ключ не найден

def input_data():
    while True:
            input_key = input("Введите ключ (для выхода введите 'exit'): ")
            check_key_existence(input_key)
            if input_key == "exit":
                break

print("1 - поиск ключа в словаре")
print("2 - удаление ключа с данными")
print("3 - удаление данных (через ключ)")

while True:
    get_number = input("\n" + "Введите номер: ")
    if get_number == "1":
        input_data()
    elif get_number == "2":
        break  # прекращаем работу программы, если введено число "2"
    elif get_number == "3":
        break  # прекращаем работу программы, если введено число "3"
    else:
        print("Данного номера не существует")







