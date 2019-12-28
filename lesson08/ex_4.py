class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


class Storage:
    def __init__(self):
        self.store = {'model': [], 'type of equip': [], 'count': [], 'price': [], 'weight': []}

    def get_equip(self, *equips):
        try:
            for equip in equips:
                if not equip.price.isdigit():
                    raise OwnError(f'Цена {equip.__class__.__name__} должна быть числом')
                elif not equip.weight.isdigit():
                    raise OwnError(f'Вес {equip.__class__.__name__} должен быть числом')
                elif not equip.count.isdigit():
                    raise OwnError(f'Количество {equip.__class__.__name__} должно быть числом')
                self.store['price'].append(equip.price)
                self.store['weight'].append(equip.weight)
                self.store['model'].append(equip.model)
                self.store['count'].append(equip.count)
                self.store['type of equip'].append(equip.__class__.__name__)
            print(self.store)
        except OwnError as err:
            print(err)


class OfficeEquip():
    def __init__(self, model=None, count=0, price=0, weight=0):
        self.price = price
        self.weight = weight
        self.model = model
        self.count = count


class Printer(OfficeEquip):
    def __init__(self, model, count, price, weight):
        super().__init__(model, count, price, weight)


class Scanner(OfficeEquip):
    def __init__(self, model, count, price, weight):
        super().__init__(model, count, price, weight)


class Xerox(OfficeEquip):
    def __init__(self, model, count, price, weight):
        super().__init__(model, count, price, weight)


storage_1 = Storage()
officeEquip = OfficeEquip()
count = int(input('Сколько видов оборудования вы хотите добавить? '))
equipment = []
for i in range(count):
    try:
        what = input('Что вы хотите добавить? P - принтер, X - ксерокс, S - сканнер ')
        if what == "P":
            equipment.append(Printer(input('Название? '), input('Количество '), input('Цена '), input('Масса ')))
        elif what == 'X':
            equipment.append(Xerox(input('Название? '), input('Количество '), input('Цена '), input('Масса ')))
        elif what == 'S':
            equipment.append(Scanner(input('Название? '), input('Количество '), input('Цена '), input('Масса ')))
        else:
            raise OwnError('Вы не выбрали оборудование')
        storage_1.get_equip(equipment[i])
    except OwnError as err:
        print(err)
