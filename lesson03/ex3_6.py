def int_func(string):
    if len(string.split()) <= 1:
        if string.istitle():
            print(string)
            return 'Ваше слово итак начинается с прописных букв'
        else:
            return string.title()
    elif len(string.split()) >=1:
        if string.istitle():
            print(string)
            return 'Ваша строка итак начинается с прописных букв'
        else:
            return string.title()

word = input('Введите слово из маленьких латинских букв: ')
if word.isdigit():
    print('Вы ввели число')
else:
    print(int_func(word))
string = input('Введите предложение из слов из латинских букв, разделенных пробелами: ')
if string.isdigit():
    print('Вы ввели число')
else :
    print(int_func(string))