def structure(name, surname, age, phone, email, city):
    definition = f'Имя:{name}, фамилия: {surname}, возраст:{age},телефон: {phone}, email: {email}, город проживания: ' \
                 f'{city}'
    return definition


name = input('Введите ваше имя: ')
surname = input('Введите вашу фамилию: ')
age = int(input('Введите ваш возраст: '))
phone = input('Введите ваш телефон: ')
email = input('Введите ваш mail: ')
city = input('Введите ваш город проживания: ')

print(structure(name=name, phone=phone, surname=surname, city=city, email=email, age=age))
