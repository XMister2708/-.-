import csv


'''
Файл для выполнение второго задания.

ПУТЬ К ФАЙЛУ 'rocket.csv': '../rocket.csv'
'''


with open('../rocket.csv','r', encoding='utf-8') as csvfile:
    '''Открытие файла 'rocket.csv'
    '''
    f = list(csv.reader(csvfile))[1:]
    for i in range(1, len(f)):
        date, code, rocketparts = f[i]
        date1, code1, rocketparts1 = f[i]
        years, mouth, day = list(map(int, date.split('-')))
        years1, mouth1, day1 = list(map(int, date.split('-')))
        if 
        
    
