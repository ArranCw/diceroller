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
        sides = int(self.get_argument('sides', 20))
        roll = self.get_argument('roll', None)
        if roll is None:
            dice1 = rolldice(sides)
            roll_output = 'You rolled a d{sides} and got a {result}'.format(sides=sides, result=dice1)

        else:
            dice1 = rolldice(sides)
            dice2 = rolldice(sides)
            decisionmaker = max if roll == 'advantage' else min
            result = decisionmaker(dice1, dice2)
            roll_template = 'You rolled a {dice1} and a {dice2}, with {roll} that is a {result}'
            roll_output = roll_template.format(dice1=dice1, dice2=dice2, roll=roll, result=result)
        self.write(self.template.generate(result=roll_output))
