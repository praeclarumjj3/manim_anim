#!/usr/bin/env python

from big_ol_pile_of_manim_imports import *

# To watch one of these scenes, run the following:
# python -m manim example_scenes.py Training_set_1 -pl
#
# Use the flat -l for a faster rendering at a lower
# quality.
# Use -s to skip to the end and just save the final frame
# Use the -p to have the animation (or image, if -s was
# used) pop up once done.
# Use -i to save the animation as a gif
# Use -n <number> to skip ahead to the n'th animation of a scene.

class Lost_coins_1D(Scene):
    def construct(self):
        intro = TextMobject("1 Dimension")
        line=Line(np.array([-8,-2,0]),np.array([8,-2,0]))
        line.set_color(YELLOW)
        text = TextMobject("10m")
        text.next_to(line,DOWN)
        coin1 = Dot(radius = 0.10, color = DARK_RED)
        coin1.next_to(line,UP)
        coin1.shift(6*LEFT)
        coin2 = Dot(radius = 0.10, color = DARK_RED)
        coin2.next_to(line,UP)
        coin2.shift(4*LEFT)
        coin3 = Dot(radius = 0.10, color = DARK_RED)
        coin3.next_to(line,UP)
        coin4 = Dot(radius = 0.10, color = DARK_RED)
        coin4.next_to(line,UP)
        coin4.shift(2*RIGHT)
        coin5 = Dot(radius = 0.10, color = DARK_RED)
        coin5.next_to(line,UP)
        coin5.shift(4*RIGHT)
        success = TextMobject("Easy to win!")

        self.add(intro)
        self.wait(1)
        self.play(ApplyMethod(intro.shift,3.5*UP))
        self.play(ApplyMethod(intro.scale,0.75))
        self.wait(0.5)
        self.play(GrowFromCenter(line))
        self.wait(0.5)
        self.add(text)
        self.wait(0.5)
        self.play(ApplyMethod(text.scale,0.75))
        self.play(FadeIn(coin1))
        self.play(FadeIn(coin2))
        self.play(FadeIn(coin3))
        self.play(FadeIn(coin4))
        self.play(FadeIn(coin5))
        self.wait(0.5)
        self.add(success)
        self.wait(0.5)
        self.play(ApplyMethod(success.scale,0.75))

class Lost_coins_2D(Scene):
    def construct(self):
        intro = TextMobject("2 Dimensions: Sparsity increases :(")
        square = Square(side_length = 6)
        square.set_color(YELLOW)
        circle = Circle(radius = 3)
        circle.set_color(DARK_BLUE)
        text = TextMobject("10m")
        text.next_to(square,DOWN)
        coin1 = Dot(radius = 0.10, color = DARK_RED)
        coin1.move_to(2.5*UP+2*LEFT)
        coin2 = Dot(radius = 0.10, color = DARK_RED)
        coin2.move_to(1*UP+0.2345*LEFT)
        coin3 = Dot(radius = 0.10, color = DARK_RED)
        coin3.move_to(0.5*DOWN+1*RIGHT)
        coin4 = Dot(radius = 0.10, color = DARK_RED)
        coin4.move_to(2*DOWN+1.75*RIGHT)
        coin5 = Dot(radius = 0.10, color = DARK_RED)
        coin5.move_to(1*DOWN)
        success1 = TextMobject("Difficult to win!")
        success1.move_to(5*RIGHT)

        self.add(intro)
        self.wait(1)
        self.play(ApplyMethod(intro.shift,3.5*UP))
        self.play(ApplyMethod(intro.scale,0.75))
        self.wait(0.5)
        self.play(GrowFromCenter(square))
        self.wait(0.5)
        self.add(text)
        self.wait(0.5)
        self.play(ApplyMethod(text.scale,0.75))
        self.play(FadeIn(coin1))
        self.play(FadeIn(coin2))
        self.play(FadeIn(coin3))
        self.play(FadeIn(coin4))
        self.play(FadeIn(coin5))
        self.wait(0.5)
        self.play(GrowFromCenter(circle))
        self.add(success1)
        self.wait(0.5)
        self.play(ApplyMethod(success1.scale,0.75))
