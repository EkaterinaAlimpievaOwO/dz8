from show import *
from find import *
from deleteDZ import *
from changeDZ import *

def menuHello():
    print("1.Добавить")
    print("2.Вывести всех")
    print("3.Поиск по фамилии")
    print("4.Изменить данные")
    print("5.Удалить по фамилии")
    print("6.Выход")
    userInput = int(input())
    if userInput == 1:
        addData()
        return True
    if userInput == 2:
        printAll()
        return True
    if userInput == 3:
        find(input("Введите фамилию: "))
        return True
    if userInput == 4:
        change(input("Введите имя или фамилию: "))
        return True
    if userInput == 5:
        delete(input("Введите имя или фамилию: "))
        return True    
    if userInput == 6:
        return False

def addData():
    data = open('data.txt', 'a', encoding='utf-8')
    print('\n'*10) 
    first_name = input("Введите имя: ")
    second_name = input("Введите фамилию: ")
    mid_name = input("Введите отчество: ")
    number = input("Введите номер телефона: ")
    item = [first_name, second_name, mid_name, number]
    s = ' '
    data.writelines(s.join(item) + '\n')
    data.close()
    print('\n'*10)