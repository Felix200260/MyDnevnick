



human = {
    "name": "John",
    "age": "18",
    "id": "188989",
    "team": ["John", "john2", "john3"]
}
keys = human.keys()  # получаем ключи словаря

while True:
    input_key = input("Введите ключ (для выхода введите 'exit'): ")
    if input_key == "exit":
        break

    found_key = False  # флаг, указывающий, был ли найден ключ "data"

    for key in keys:
        if key == input_key:
            print("данный ключ имеется")
            found_key = True  # устанавливаем флаг в True, если ключ найден
            break  # выходим из цикла, если ключ найден

    if not found_key:
        print("Данного ключа не существует")  # выводим сообщение, если ключ не найден

#КОММЕНТАРИЙ
#проверка на длинну комментария commitaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa