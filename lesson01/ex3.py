num = input('Введите ваше число n: ')

sum = int(num) + int(str(num)+str(num)) + int(int(str(num)+str(num)+str(num)))

print(f'Ваша сумма в формате n+nn+nnn: {sum}')