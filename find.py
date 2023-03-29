def find(text):
    print('\n'*10)
    data = open('data.txt', 'r', encoding='utf-8')
    for line in data:
        if line.split(' ')[1] == text:
            print(line)
            data.close()
            return
    print("Не найден!")
    data.close()
    print('\n')