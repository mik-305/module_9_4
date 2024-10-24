first = 'Мама мыла раму'
second = 'Рамена мало было'

result = map(lambda x, y: x == y, first,second)
print(list(result))

def get_advanced_writer(file_name):

    def write_everything(*data_set):
        name = 'example.txt'
        file = open(name, 'a')
        file.close()
        


    return write_everything



