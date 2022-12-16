txt_book = r'C:\Users\79274\Desktop\Python_homework\Homework_7\dataBase.txt'


def write_contact():
    with open(txt_book, 'r+') as data:
        if data.read() == '':
            data.write(input('Fill a name: ') + '\n')
            data.write(input('Fill a surname: ') + '\n')
            data.write(input('Fill a telephone number: '))
        else:
            data.write('\n\n' + input('Fill a name: ') + '\n')
            data.write(input('Fill a surname: ') + '\n')
            data.write(input('Fill a telephone number: '))

def read_contact():
    with open(txt_book, 'r') as data:
        return data.read()

def rewrite(data_list: list):
    temp_list =[]
    for i in range(len(data_list)):
            temp_list.append('\n'.join(data_list[i]))
    temp_str = '\n\n'.join(temp_list)
    with open(txt_book, 'w') as data:
        data.write(temp_str)

def conclusion_contact():
    with open(txt_book, 'r') as data:
        print('=====================')
        return print(data.read())
