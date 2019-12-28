import datetime

class Data:
    def __init__(self,date):
        self.date = date

    @classmethod
    def get_int(cls,date):
        print([int(i) for i in date.split('-')])

    @staticmethod
    def get_valid(date):
        date = date.split('-')
        try:
            right_date = datetime.date(int(date[2]),int(date[1]),int(date[0]))
            return f'Всё введено верно {right_date}'
        except ValueError:
            return f'Дата введена неверно {date}'


date_1 = Data('31-08-1999')
date_1.get_int('31-08-1999')
print(Data.get_valid('31-08-1999'))
print(Data.get_valid('30-02-2015'))

