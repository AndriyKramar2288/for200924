# -*- coding: utf-8 -*-
import json
import csv
import math


def f(x):
    """
    Користувацька функція
    """
    return math.sin(x)


def main():
    """
    Головна функція, що генерує табуляцію прописаної в цьому файлі функції.
    """
    start = float(input("Введіть нижню межу\n>>"))
    stop = float(input("Введіть верхню межу\n>>"))
    n = int(input("Введіть к-ть вузлів\n>>"))
    hh = ((stop - start) / n)

    current = start
    x = []
    y = []
    h = []
    for i in range(n+1):
        x.append(current)
        y.append(f(current))
        h.append(hh)
        current += hh

    to_convert_list = [{"key": x[i], "value": y[i]} for i in range(n+1)]

    with open("tabulation.json", "wt") as file:
        file.write(json.dumps(to_convert_list))

    with open('data.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=to_convert_list[0].keys())
        writer.writeheader()
        for row in to_convert_list:
            writer.writerow(row)


if __name__ == '__main__':
    main()
