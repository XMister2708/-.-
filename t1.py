import csv


data = {
    '01': 0,
    '02': 0,
    '03': 0,
    '04': 0,
    '05': 0,
    '06': 0,
    '07': 0,
    '08': 0,
    '09': 0,
    '10': 0,
    '11': 0,
    '12': 0,
        }


with open('../rocket.csv','r', encoding='utf-8') as csvfile:
    f = list(csv.reader(csvfile))[1:]
    for date, code, rc in f:
        s = date.split('-')[1]
        data[s] += 1


with open('rocket_part.txt', 'w', encoding='utf-8') as file:
    for n, kol in data.items():
        file.write(f'В {n} было получено - {kol} шифров\n')


with open('rocket_part.txt', 'r', encoding='utf-8') as file:
    f = file.readlines()
    ind = int(input())
    print(f[ind - 1])
