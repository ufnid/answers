import csv

def check(file_name):
    """
    :param file_name: название файла, в котором ищем все ошибки, где содержится 55
    :return: список, где такие ошибки заменены на Done, а дата это нули
    """
    itog = []

    with open(file_name, encoding='utf-8') as file:
        file = file.read().split('\n')
        for i in file:
            spis = i.split('$')
            if "55" in spis[-2]:
                print(f"У персонажа\t{spis[1]}\tв игре\t{spis[0]}\tнашлась ошибка с кодом:\t{spis[-2]}\tДата фиксации:\t{spis[-1]}")
                spis[-2] = 'Done'
                spis[-1] = '0000-00-00'
            itog.append(spis)

    return itog


def write(file_name, spis):
    """
    :param file_name: название файла (если его нет, то он создастся), куда запишутся полученные измененные данные
    :param spis: список с этими данными
    """
    with open(file_name, 'w', newline='') as output:
        writer = csv.writer(output, delimiter=";", quotechar='"')
        for i in spis:
            writer.writerow(i)


spis_data = check("game.txt")
write("game_new.csv", spis_data)