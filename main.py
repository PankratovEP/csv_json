import csv
# Вам дана частичная выборка из датасета зафиксированных преступлений, совершенных в городе Чикаго с
# 2001 года по настоящее время.
# Одним из атрибутов преступления является его тип – Primary Type.
# Вам необходимо узнать тип преступления, которое было зафиксировано максимальное число раз в 2015 году.

def search_for_crimes():
    with open('Crimes.csv') as f:
        spisok = csv.reader(f)
        di = {}
        for row in spisok:
            di[row[5]] = di.setdefault(row[5], 0) + 1
        print(max(di, key=lambda x: di[x]))
