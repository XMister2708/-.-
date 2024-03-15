import csv


'''
Файл для выполнение третьего задания.

ПУТЬ К ФАЙЛУ 'rocket.csv': '../rocket.csv'
'''


with open('../rocket.csv','r', encoding='utf-8') as csvfile:
    '''Открытие файла 'rocket.csv'
       Вывод кода по дате
    '''
    f = list(csv.reader(csvfile))[1:]
    a = input()
    while a != 'sleep':
        i = 0
        k = False
        lop = len(f)
        while i != lop:
            date, code, rocketparts = f[i]
            if date != a:
                i += 1
                k = True
            else:
                break
        if k:
            print(f'Шифр: {code} от: {rocketparts} был получен {date}')
        else:
            print('в этот день космос молчал')
        a = input()
        

