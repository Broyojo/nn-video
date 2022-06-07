from manim import *


class LinearScene(Scene):
    def construct(self):
        axes = Axes(x_range=[0, 5], y_range=[0, 25, 5])

        labels = axes.get_axis_labels(x_label="x", y_label="y")

        dots = [
            axes.coords_to_point(2.2, 14.3),
            axes.coords_to_point(3.5, 20.1),
            axes.coords_to_point(4.1, 23.5),
        ]

        def guess_fn(x): return 4*x+6

        guess_line = axes.plot(guess_fn, color=BLUE)

        self.play(DrawBorderThenFill(axes), Write(labels), *
                  [Write(Dot(dot, color=GREEN)) for dot in dots])

        self.play(Create(guess_line))

        self.play(Create(BraceBetweenPoints(
            axes.coords_to_point(4.1, guess_fn(4.1)), dots[2])))

        self.wait(5)
