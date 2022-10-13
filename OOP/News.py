# Create a tool, which will do user generated news feed:
# 1.User select what data type he wants to add
# 2.Provide record type required data
# 3.Record is published on text file in special format
# You need to implement:
# 1.News – text and city as input. Date is calculated during publishing.
# 2.Private ad – text and expiration date as input. Day left is calculated during publishing.
# 3.Your unique one with unique publish rules.

# Created a constractor which will add new publication to the txt file

import datetime


def record_to_file(text):
    with open("result.txt", "a+") as f:
        f.write(text)


# create a class which will be creating a news
class News:

    def __init__(self, city, text):
        # the name of the city where it happend -str
        self.city = city
        # the text of a news - str
        self.text = text

    # create constructor which will be creating a news and add it to the txt file

    def text_generator(self):
        text = f'\nNews \n{self.text}\n{self.city}, {datetime.date.today()}\n\n'
        record_to_file(text)


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

    def text_generator(self):
        text = f'\nPrivate Ad\n{self.text}\n{self.calculate_date()}, {self.date} days left\n\n '
        record_to_file(text)


# created constuctor which will be creating a joke like the Armenian radio and add it to the txt file
class Joke:
    def __init__(self, question, answer, rate):
        # user need to enter a question -str
        self.text = question
        # user add an aswer for the question - str
        self.answer = answer
        # user add the int number of rate for this joke - int
        self.rate = rate

    def text_generator(self):
        text = f'\nJoke\n{self.text}\n{self.answer}\nFunny meter  {self.rate} of 10\n\n'
        record_to_file(text)


# created class which invoke a class after when user will be asked about a type of publication
def communication_with_user():
    while True:
        text = input('Please, input the type of publication (News or Adv or Joke) if you do not want to add a '
                     'publication enter "stop": ').lower()
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
        elif text == 'stop':
            break
        else:
            print('Incorrect enter. Please, only News,Adv or stop')

communication_with_user()
