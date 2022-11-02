import requests
from datetime import date
import os

base_url = 'http://localhost:8000/'


def all_sensors():
    add_url = 'all/'
    url = base_url + add_url

    res = requests.get(url=url)

    if res.status_code == 200:
        count = 1
        for i in res.json():
            desc = f'{count}. id: {i["id"]}, Датчик: {i["title"]}, местоположение: {i["description"]}'
            print(desc)
            if len(i['monitoring']) > 0:
                for k in i['monitoring']:
                    desc_ = f"\t Дата: {k['date']}, Температура: {k['temperature']}"
                    print(desc_)
            else:
                print('\t Измерений по данному датчику нет')
            count = count + 1
        print('_______________________')
        main()
    else:
        print('Что-то пошло не так')


def add_sensor():
    add_url = 'add/'
    title = input("Введите название датчика: ")
    description = input("Введите местоположение датчика: ")
    url = base_url + add_url
    requests.post(url, data={"title": title, "description": description})
    print(f'Датчик {title} с местонахождением {description} добавлен в базу данных')
    print('_______________________')
    main()


def sensor_edit(id_sensor):
    add_url = f'edit/{id_sensor}/'
    url = base_url + add_url
    description = input("Введите новое местоположение датчика: ")
    requests.patch(url=url, data={"title": 'None', "description": description}, )
    print(f'Местоположение датчика изменено')
    print('________________')
    main()


def add_temps(id_sensor):
    temperature = input('Введите температуру: ')
    add_url = 'add_temp/'
    url = base_url + add_url
    requests.post(url=url, data={"id_sensor": id_sensor, "temperature": temperature, "date": date.today()})
    print(f'Температура датчика с id {id_sensor} добавлена')
    print('_____________')
    main()


def sensor_get_id():
    id_ = input('Введите id датчика: ')

    add_url = f'{id_}'

    url = base_url + add_url

    res = requests.get(url=url)

    if res.status_code == 200:

        desc = f'id: {res.json()["id"]}, Датчик: {res.json()["title"]}, местоположение: {res.json()["description"]}'
        print(desc)
        if len(res.json()['monitoring']) > 0:
            for i in res.json()['monitoring']:
                desc_ = f"\t Дата: {i['date']}, Температура: {i['temperature']}"
                print(desc_)
            command_dict = {
                'temp': 'Добавление температуры',
                'move': 'Перенести датчик',
                'skip': 'Ничего не делать',
            }
            for k, v in command_dict.items():
                print(f'Команда: {k} - операция: {v}')
            command = input('Введите команду: ')
            if command in command_dict.keys():
                if command == 'temp':
                    add_temps(id_)
                elif command == 'move':
                    sensor_edit(id_)
                else:
                    main()
            else:
                print('Команда не правильная')
                sensor_get_id()
        else:
            print('\t Измерений по данному датчику нет')
            command_dict = {
                'temp': 'Добавление температуры',
                'move': 'Перенести датчик',
                'skip': 'Ничего не делать',
            }
            for k, v in command_dict.items():
                print(f'Команда: {k} - операция: {v}')
            command = input('Введите команду: ')
            if command in command_dict.keys():
                if command == 'temp':
                    add_temps(id_)
                elif command == 'move':
                    sensor_edit(id_)
                else:
                    main()
            else:
                print('Команда не правильная')
                sensor_get_id()


    else:
        print('Датчика с таким id нет. Посмотрите список датчиков:')
        all_sensors()


def main():
    file = os.path.join(os.getcwd(), 'Readme.txt')
    with open(file, mode='r', encoding='utf-8') as f:
        data = f.readlines()
        for i in data:
            print('\t\t', i.strip())

    count = False
    while not count:
        command = input('Введите команду: ')
        if command == 'List':
            count = True
            all_sensors()
        elif command == 'Add':
            count = True
            add_sensor()
        elif command == 'Id':
            count = True
            sensor_get_id()
        else:
            print('Введена не корректная комманда')


main()
