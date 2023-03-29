def delete(text):
    fileData = open('data.txt', 'r',encoding='utf-8')
    data = fileData.readlines()
    fileData.close()
    
    fileData = open('data.txt', 'w',encoding='utf-8')
    found = False
    for line in data:
        if line.split(' ')[1] != text and line.split(' ')[0] != text:
            fileData.write(line)
        else:
            found = True
    if found == False:
        print("Не найден")
    else:
        print("Удалено")
    print('\n')
    return