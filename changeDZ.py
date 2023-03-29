def change(text):
    found = False
    data = open('data.txt', 'r', encoding='utf-8')
    lines = data.readlines()
    data.close()
    for line in lines:
        if line.split(' ')[1] == text or line.split(' ')[0] == text:
            newline = changeMenu(line)
            index = lines.index(line)
            lines[index] = newline
            found = True 
    if found == True:
        data = open('data.txt', 'w+', encoding='utf-8')
        data.writelines(lines)
        print("Изменено")
    else:
        print("Не найдено")
    data.close()

def changeMenu(line):
    print("1.Изменить имя")
    print("2.Изменить фамилию")
    print("3.Изменить отчество")
    print("4.Изменить телефон")
    
    userInput = int(input())
    
    if userInput == 1:
        temp = input("Введите новое имя: ") + " " + line.split(' ')[1] + " " + line.split(' ')[2] + " " + line.split(' ')[3]
        return temp
    if userInput == 2:
        temp = line.split(' ')[0] + " " +  input("Введите новую фамилию: ") + " " + line.split(' ')[2] + " " + line.split(' ')[3]
        return temp
    if userInput == 3:
        temp = line.split(' ')[0] + " " + line.split(' ')[1] + " " + input("Введите новое отчество: ") + " " + line.split(' ')[3]
        return temp
    if userInput == 4:
        temp = line.split(' ')[0] + " " + line.split(' ')[1] + " " + line.split(' ')[2] + " " + input("Введите новый номер телефона: ") + "\n"
        return temp

