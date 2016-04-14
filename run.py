#!/usr/bin/env python3
import tornado.ioloop
import tornado.web
import random

page = '''
<!doctype html>
<html>
    <head>
    </head>
    <body>
        <h1>Diceroller!</h1>
        <form method="post">
            <input type="radio" name="roll" value="disadvantage"> Disadvantage
            <br>
            <input type="radio" name="roll" value="normal"> Normal
            <br>
            <input type="radio" name="roll" value="advantage"> Advantage
            <br><br>
            <input type="submit" value="Roll">
        </form>
        {result}
    </body>
</html>
'''


class HomePage(tornado.web.RequestHandler):
    def get(self):
        self.write(page.format(result=''))
    def post(self):
        roll = self.get_argument('roll', '')
        if roll == 'advantage':
            dice1 = random.randrange(1,21)
            dice2 = random.randrange(1,21)
            result = max(dice1,dice2)
            roll_output = 'You rolled a {dice1} and a {dice2}, with {roll} that is a {result}'.format(dice1=dice1, dice2=dice2, roll=roll, result=result)
        elif roll == 'disadvantage':
            dice1 = random.randrange(1,21)
            dice2 = random.randrange(1,21)
            result = min(dice1,dice2)
            roll_output = 'You rolled a {dice1} and a {dice2}, with {roll} that is a {result}'.format(dice1=dice1, dice2=dice2, roll=roll, result=result)
        else:
            result = random.randrange(1,21)
            roll_output = 'You rolled a {result}'.format(result=result)
        self.write(page.format(result=roll_output))


def make_app():
    routes = [
        (r"/", HomePage),
    ]
    return tornado.web.Application(routes, autoreload=True, debug=True)


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    print("The server is running on http://localhost:8888")
    tornado.ioloop.IOLoop.current().start()
