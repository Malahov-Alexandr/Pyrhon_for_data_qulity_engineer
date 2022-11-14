import os.path
import datetime


# create a new txt file with the publication and then delete it
def record_to_file(text, path='C:\\Users\\'):
    with open(os.path.join(path + 'result.txt'), 'a+') as f:
        f.write(text)
    os.remove(path + 'result.txt')


# create a class that will be creating a news
class News:

    def __init__(self, city, text):
        # the name of the city where it happened -str
        self.city = city
        # the text of a news-str
        self.text = text

    # create a constructor which will be creating news and add it to the txt file

    def text_generator(self):
        text = f'\nNews \n{self.text}\n{self.city}, {datetime.date.today()}\n\n'
        record_to_file(text, path())


# created constructor which will be creating an adv and add it to the txt file
class Adv:
    def __init__(self, text, date):
        # the text of the adv - str
        self.text = text
        # date after how many days adv will be expired- int
        self.date = date

    def calculate_date(self):
        import datetime
        return datetime.date.today() + datetime.timedelta(self.date)

    def text_generator(self, ):
        text = f'\nPrivate Ad\n{self.text}\n{self.calculate_date()}, {self.date} days left\n\n '
        record_to_file(text, path())


# created constructor which will be creating a joke like the Armenian radio and add it to the txt file
class Joke:
    def __init__(self, question, answer, rate):
        # user needs to enter a question -str
        self.text = question
        # user adds answer for the question - str
        self.answer = answer
        # user adds the int number of rate for this joke - int
        self.rate = rate

    def text_generator(self):
        text = f'\nJoke\n{self.text}\n{self.answer}\nFunny meter  {self.rate} of 10\n\n'
        record_to_file(text, path())


# define a path for the file or leave the default
def path():
    path_for_file = input(
        'If you want to save the adv by default path enter "0", if you want to enter your own path, enter "1": ')
    if path_for_file == '0':
        return 'C:\\Users\\'

    else:
        return input('Please enter a new path to save the adv ( example C:\\Users\\): ')


# define how many adv a user will create
def counter_of_adv():
    try:
        return int(input('Enter how many adv need to create: '))
    except ValueError:
        return counter_of_adv()


# created class which invokes a class after when a user is asked about a type of publication
class GeneratorOfAdv:
    for adv in range(counter_of_adv()):
        text = input('Please, input the type of publication (News or Adv or Joke): ').lower()
        if text == 'news':
            text = input('Please, enter your text of the news: ')
            city = input('Please, enter the city where it happend: ')
            news = News(city, text)
            news.text_generator()
        elif text == 'adv':
            text = input('Please, input the text of the adv: ')
            days = int((input('Please, input period after how many days adv will be available: ')))
            adv = Adv(text, days)
            adv.text_generator()
        elif text == 'joke':
            text = input('Please, enter the joke question: ')
            answer = input('Please, enter the answer for the joke: ')
            rate = int(input('Enter the rate of this joke: '))
            joke = Joke(text, answer, rate)
            joke.text_generator()

        else:
            print('Incorrect enter. Please, only News, Adv or Joke')


GeneratorOfAdv

