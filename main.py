from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.vector import Vector

class PongGame(Widget):
    pass

class PongBall(Widget):

    # velocity of the ball on x and y axis
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)

    # referencelist property so I can use ball.velocity as
    # a shorthand, just like e.g. w.pos for w.x and w.y
    velocity =  ReferenceListProperty(velocity_x, velocity_y)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos


class PongApp(App):

    def build(self):
        return PongGame()

if __name__ == '__main__':
    PongApp().run()
