from tornado import template
import tornado.web
import random

loader = template.Loader("./templates")


def rolldice(sides):
    return random.randrange(1, sides+1)


class HomePage(tornado.web.RequestHandler):
    template = loader.load("homepage.html")

    def get(self):
        self.write(self.template.generate(result=''))

    def post(self):
        roll = self.get_argument('roll', '')
        roll_template = 'You rolled a {dice1} and a {dice2}, with {roll} that is a {result}'
        dice1 = rolldice(20)

        if roll == 'advantage' or roll == 'disadvantage':
            dice2 = rolldice(20)
            decisionmaker = max if roll == 'advantage' else min
            result = decisionmaker(dice1, dice2)
            roll_output = roll_template.format(dice1=dice1, dice2=dice2, roll=roll, result=result)

        else:
            roll_output = 'You rolled a {result}'.format(result=dice1)
        self.write(self.template.generate(result=roll_output))
