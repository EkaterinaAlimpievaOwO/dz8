def printAll():
    print('\n'*10)
    data = open('data.txt', 'r', encoding='utf-8')
    for line in data:
        print(line)
    data.close()
    print('\n')