num = int(input('Сколько товаров вы хотите добавить?'))
goods = []
for i in range(num):
    goods.append((i, {"название": input('Введите название товара: '), 'цена': int(input('Введите цену товара: ')),
                      'количество':
                          int(input('Введите количество товара: ')),
                      'ед': input('Измерение количества товара: ')}))

analytics = {}
for i in range(num):
    for key, item in goods[i][1].items():
        analytics[key] = []
for i in range(num):
    for key, item in goods[i][1].items():
        analytics[key].append(item)
analytics['ед'] = list(set(analytics['ед']))

print(analytics)
