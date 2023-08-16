# # 1. Дано предложение. Удалить все повторяющиеся слова.
# someText = input('input some text: ')
# someTextSplit = someText.split(' ')
# for i in someTextSplit:
#     if someTextSplit.count(i) > 1:
#         someTextSplit.remove(i)
# for i in someTextSplit:
#     print(i)

# Домашнее задание:
# Список людей на проекте (похожее на то что делали на занятии)
# Действия: Запись в файл(при выходе), чтение из файла(при запуске программы),
# Добавление человека на проект, удаление человека с проекта,
# получение списка людей на проекте, есть ли человек на проекте
# В список людей должен храниться в алфавитном порядке
# 2. Пишем программу с двумя действиями : запись в файл, чтение из файла, - и меню.
# while True ... , затем по пунктам меню - выполнение вышеуказанных операций.
import os

with open('programm of coun peapl on projekt.txt', 'r') as fille:
    someProgramers = fille.readlines()
    Programers = [i.rstrip('\n') for i in someProgramers]

while True:
    print('1.Добавление человека на проект: ')
    print('2.удаление человека с проекта: ')
    print('3.получение списка людей на проекте: ')
    print('4.есть ли человек на проекте: ')
    print('5. выход: ')
    try:
        choise = int(input('выберите действие: '))
    except Exception as e:
        print(e)
        print('Введено не число!')
        continue
    if choise == 1:
        programmerAdd = input('введите имя чедовека: ')
        Programers.append(programmerAdd)
    elif choise == 2:
        programmerDel = input('введите имя чедовека: ')
        if programmerDel in Programers:
            Programers.remove(programmerDel)
        else:
            print('Человека нет на проекте!')
    elif choise == 3:
        print(Programers)
    elif choise == 4:
        choisenName = input('введите имя чедовека: ')
        if choisenName in Programers:
            print('Этот человек есть на проекте!')
        else:
            print('этого человека на проекте нет!')
    elif choise == 5:
        with open('programm of coun peapl on projekt.txt', 'w') as fille:
            for i in Programers:
                fille.write(i+'\n')
        break
    else:
        print('выберите пункт из меню!')
    os.system("pause")
    os.system("cls")


