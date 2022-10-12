# Создайте инструмент, который будет создавать новостную ленту, сгенерированную пользователем:
# 1. Пользователь выбирает, какой тип данных он хочет добавить
# 2. Предоставьте требуемые данные типа записи
# 3.Запись публикуется в текстовом файле в специальном формате

# Вам необходимо реализовать:
# 1.Новости – текст и город в качестве ввода. Дата рассчитывается во время публикации.
# 2.Приватное объявление – на входе текст и дата истечения срока действия. Оставшийся день рассчитывается во время публикации.
# 3. Ваш уникальный с уникальными правилами публикации.

# Created a constractor witch will add new publication to the txt file
class File_creator:

    def record_to_file(self, text):
        with open("OOP/result.txt", "a+") as f:
            f.write(text)

# create a class wich will be creating a news
class News(File_creator):

    def __init__(self, city, text):
        self.city = city
        self.text = text
    # created constructer wich will be creating a news and add it to the txt file

    def new_constr(self):
        import datetime
        text = f'\nNews {"-" * 25}\n{self.text}\n{self.city}, {datetime.date.today()}\n{"-" * 30}\n\n'
        gener = File_creator()
        gener.record_to_file(text)


# created constructer wich will be creating an adv and add it to the txt file
class Adv(File_creator):
    def __init__(self, text, date):
        self.text = text
        self.date = date

    def calculate_date(self):
        import datetime
        return datetime.date.today() + datetime.timedelta(self.date)

    def generator_of_adv(self):
        text = f'\nPrivate Ad{"-" * 20}\n{self.text}\n{self.calculate_date()}, {self.date} days left\n\n '
        gener = File_creator()
        gener.record_to_file(text)


class Joke(File_creator):
    def __init__(self, text, answer, rate):
        self.text = text
        self.rate = rate
        self.answer = answer

    def joke_generator(self):
        text = f'\nJoke{"-" * 26}\n{self.text}\n{self.answer}\nFunny meter  {self.rate} of 10\n\n'
        gener = File_creator()
        gener.record_to_file(text) 


# created class wich invoke a class after wheh user will be asked about a type of publication
class Generator(Adv, News):

    @classmethod
    def comunnication_with_user(cls):
        while True:
            text = input('Please, input the type of publication (News or Adv or Joke) if you do not want to add a publication enter "stop": ').lower()
            if text == 'news':
                text = input('Please, enter your text of the news: ')
                city = input('Please, enter the city where it happend: ')
                myobj = News(city, text)
                myobj.new_constr()
            elif text == 'adv':
                text = input('Please, input the text of the adv: ')
                days = int((input('Please, input period after how many days adv will be available: ')))
                myobj = Adv(text, days)
                myobj.generator_of_adv()
            elif text == 'joke':
                text = input('Please, enter the joke question: ')
                answer = input('Please, enter the answer for the joke: ')
                rate = int(input('Enter the rate of this joke: '))
                myobj = Joke(text, answer, rate)
                myobj.joke_generator()
            elif text == 'stop':
                break
            else:
                print('Incorrect enter. Please, only News,Adv or 0')


myobj = Generator.comunnication_with_user()
