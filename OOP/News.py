# Создайте инструмент, который будет создавать новостную ленту, сгенерированную пользователем:
# 1. Пользователь выбирает, какой тип данных он хочет добавить
# 2. Предоставьте требуемые данные типа записи
# 3.Запись публикуется в текстовом файле в специальном формате

# Вам необходимо реализовать:
# 1.Новости – текст и город в качестве ввода. Дата рассчитывается во время публикации.
# 2.Приватное объявление – на входе текст и дата истечения срока действия. Оставшийся день рассчитывается во время публикации.
# 3. Ваш уникальный с уникальными правилами публикации.


class File_creator:

    def record_to_file(self, text):
        with open("result.txt", "a+") as f:
            f.write(text)



class News(File_creator):
    import datetime

    def __init__(self, city, text):
        self.city = city
        self.text = text

    def new_constr(self):
        import datetime
        text = f'\nNews {"-"*25}\n{self.text}\n{self.city}, {datetime.date.today()}\n{"-" * 30}\n\n'
        gener = File_creator()
        gener.record_to_file(text)


class Adv(File_creator):
    def __init__(self, text, date):
        self.text = text
        self.date = date

    def calculate_date(self):
        import datetime
        return datetime.date.today() + datetime.timedelta(self.date)

    def generator_of_adv(self):
        text = f'\nPrivate Ad{"-"*20}\n{self.text}\n{self.calculate_date()}, {self.date} days left\n\n '
        gener = File_creator()
        gener.record_to_file(text)


t = News('Bar', 'greatesh event has comming')
t.new_constr()

# a = Adv('I will sell', 30)
# a.generator_of_adv()
print(len('------------------------------------------------------'))