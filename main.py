from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=900, height=800)
turtles = []
colors = ["blue", "red", "yellow", "green", "orange", "pink"]
random.shuffle(colors)
race = True


class TurtleRacer(Turtle):
    def set_att(self, color, height):
        self.team = color
        self.color(color)
        self.shape("turtle")
        self.penup()
        self.goto(-440, height)

    def run(self):
        self.forward(random.randint(30,50))
        x = self.xcor()
        if x > 400:
            return False
        else:
            return True


user_bet = screen.textinput("Place a bet", f"The contestants are {colors}. ""Which turtle is going to win?").lower()


start_height = 250
for index in colors:
    turtle = TurtleRacer()
    turtle.set_att(index, start_height)
    start_height -= 80
    turtles.append(turtle)


while race == True:
    for n in turtles:
        race = n.run()
        if race == False:
            winner = str(n.team)
            break

print(f"The winner was {winner}")
if user_bet == winner:
    print("You bet on the right turtle and won!")
else:
    print("You bet on the wrong turtle...")

screen.exitonclick()