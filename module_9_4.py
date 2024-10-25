from random import choice
import random

first = 'Мама мыла раму'
second = 'Рамена мало было'

result = map(lambda x, y: x == y, first,second)
print(list(result))


def get_advanced_writer(file_name):

    def write_everything(*data_set):
        file = open(file_name, 'a', encoding='utf8')
        for i in range(len(data_set)):
            file.write(str(data_set[i])+'\n')
        file.close()
    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])
write('Бирио барады', [777, 9999, 'A', 0], '3,14')


class MysticBall:
    def __init__(self, *words):
        self.words = words
    def __call__(self):
        return choice(self.words)
first_ball = MysticBall('Да', 'Нет', 'Наверное','Может быть')
print(first_ball())
print(first_ball())
print(first_ball())
print(first_ball())




