import json


def gsu():
    fn = 'C:/Users/Юрий 2/Desktop/Задачки/cats.txt'
    try:
        with open(fn) as r:
            f = json.load(r)
            print("ваше имя тут есть")
    except TypeError:
        if True:
            return None
        else:
            return f


def gu():
    f = gsu()
    if f:
        print("Добро пожаловать" + f)
    else:
        f = gnu()
        print("нужна новая регистрация" + f)
    fn = 'C:/Users/Юрий 2/Desktop/Задачки/cats.txt'
    with open(fn, 'w') as r:
        json.dump(f, r)
        print("добро пожаловать - " + f)


def gnu():
    f = input("как вас зовут?")
    fn = 'C:/Users/Юрий 2/Desktop/Задачки/cats.txt'
    with open(fn, 'w') as r:
        json.dump(f, r)
        return f


def ggg():
    fn = 'C:/Users/Юрий 2/Desktop/Задачки/cats.txt'

    with open(fn) as r:
        f = json.load(r)
        s = int(input("Ваше имя " + f + '. если да нажмите 1, если нет 2 "'))

        if s == 1:
            gu()
            print("вы ответили - да")
        else:
            gnu()
            print("вы ответили - нет")

ggg ()