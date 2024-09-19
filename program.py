import math
import csv
X = []
Y = X.copy()

def f(x):
    """
    користувацька функція
    :param x: double
    :return: double
    """
    return math.sin(x)
def parsefunctionjson(location):
    """
    Даємо функції розміщення json-файлу зі списком словників, де кожен
    має ключі "key" та "value", вона нам повертає це у вигляді двох
    списків - x та y
    """
    import json
    x = []
    y = x.copy()
    with open(location, "r") as file:
        jsonische = json.loads(file.read())
    for i in jsonische:
        x.append(i["key"])
        y.append(i["value"])
    return x, y


def wkx(k, x):
    """

    """
    global X
    global Y

    p = 1
    for i in range(k+1):
        p = p * (x - X[i])
    return p

def rr(k):
    """

    """
    global X
    global Y

    S = 0
    for i in range(k + 1):
        p = 1
        for j in range(k + 1):
            if j != i:
                p *= X[i]-X[j]

        S += Y[i] / p
    return S

def Nn(x, N):
    """

    """
    global X
    global Y

    S = Y[0]
    for k in range(N + 1):
        S += wkx(k-1, x) * rr(k)

    return S


def main():
    """


    """
    global X
    global Y

    X, Y = parsefunctionjson("tabulation.json")
    #X = [0.0] + X
    #Y = [0.0] + Y

    x = X[0]
    N = len(X) - 1
    h = (X[N] - X[0]) / (20 * N)

    toWrite1 = ""
    toWrite2 = ""
    toWrite3 = ""

    result = []

    to_convert_list = []
    for j in range((20 * N) + 1):
        R = abs(f(x) - Nn(x, N))
        to_convert_list.append({"key": x, "value": Nn(x, N)})
        toWrite1 += f"{x}    {Nn(x, N)}\n"
        toWrite2 += f"{x}    {wkx(N, x)}\n"
        toWrite2 += f"{x}    {R}\n"
        x += h

    with open("file1.txt", "wt") as file:
        file.write(toWrite1)
    with open("file2.txt", "wt") as file:
        file.write(toWrite2)
    with open("file3.txt", "wt") as file:
        file.write(toWrite3)

    # in the end
    with open('data_result.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=to_convert_list[0].keys())
        writer.writeheader()
        for row in to_convert_list:
            writer.writerow(row)

if __name__ == '__main__':
    main()
