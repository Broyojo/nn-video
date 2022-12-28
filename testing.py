from math import exp

import numpy as np
from manim import *


class Test(Scene):
    def construct(self):
        equation = MathTex(
            r"e^x = x^0 + x^1 + \frac{1}{2} x^2 + \frac{1}{6} x^3 + \cdots + \frac{1}{n!} x^n + \cdots"
        )
        equation.set_color_by_tex("x", YELLOW)
        self.play(Write(equation))


class ArgMinExample(Scene):
    def construct(self):
        ax = Axes(
            x_range=[0, 10], y_range=[0, 100, 10], axis_config={"include_tip": False}
        )
        labels = ax.get_axis_labels(x_label="x", y_label="f(x^2)")

        t = ValueTracker(0)

        def func(x):
            return 2 * (x - 5) ** 2

        graph = ax.plot(func, color=MAROON)

        initial_point = [ax.coords_to_point(t.get_value(), func(t.get_value()))]
        dot = Dot(point=initial_point)

        dot.add_updater(lambda x: x.move_to(ax.c2p(t.get_value(), func(t.get_value()))))
        x_space = np.linspace(*ax.x_range[:2], 200)
        minimum_index = func(x_space).argmin()

        self.add(ax, labels, graph, dot)
        self.play(t.animate.set_value(x_space[minimum_index]))
        self.wait()


class Calculus(Scene):
    def construct(self):
        eq1 = MathTex(r"\frac{dy}{dx} = \frac{x}{y}")
        eq2 = MathTex(r"\frac{dy}{y} = x \, dx")
        eq3 = MathTex(r"\int \frac{dy}{y} = \int x \, dx")
        eq4 = MathTex(r"\ln |y| = \frac{1}{2}x^2 + C")
        eq5 = MathTex(r"y=e^{\frac{1}{2}x^2+C}")
        eq6 = MathTex(r"y=e^{\frac{1}{2}x^2}e^C")
        eq7 = MathTex(r"y=Ce^{\frac{1}{2}x^2}")
        self.play(Write(eq1))
        self.wait()
        self.play(MoveToTarget(eq2))
        self.wait()
        self.play(Transform(eq1, eq3))
        self.wait()
        self.play(Transform(eq1, eq4))
        self.wait()
        self.play(Transform(eq1, eq5))
        self.wait()
        self.play(Transform(eq1, eq6))
        self.wait()
        self.play(Transform(eq1, eq7))
        self.wait()

        self.play(eq1.animate.shift(LEFT * 5))

        init = MathTex("(2, 3)")
        self.play(Write(init))

        self.play(init.animate.shift(UP * 3 + LEFT * 5))

        eq8 = MathTex(r"3=Ce^{1/2*2^2}")
        eq9 = MathTex(r"3=Ce^{1/2*4}")
        eq10 = MathTex(r"3=Ce^2")
        eq11 = MathTex(r"C=\frac{3}{e^2}")
        self.play(Write(eq8))
        self.wait()
        self.play(Transform(eq8, eq9))
        self.wait()
        self.play(Transform(eq8, eq10))
        self.wait()
        self.play(Transform(eq8, eq11))
        self.wait()

        self.play(eq8.animate.shift(DOWN * 3 + LEFT * 5))

        eq12 = MathTex(r"y=\frac{3}{e^2}e^{\frac{1}{2}x^2}")

        eq13 = MathTex(r"y=3e^{\frac{1}{2}x^2-2}")

        self.play(eq1.animate.shift(RIGHT * 5))
        self.wait()
        self.play(Transform(eq1, eq12))
        self.wait()
        self.play(Transform(eq1, eq13))
        self.wait()
        self.play(FadeOut(init), FadeOut(eq1), FadeOut(eq8))
        self.wait()

        ax = Axes(
            x_range=[0, 10], y_range=[0, 100, 10], axis_config={"include_tip": False}
        )
        labels = ax.get_axis_labels(x_label="x", y_label=eq13)

        graph = ax.plot(lambda x: 3 * exp(0.5 * x * x - 2))

        self.play(DrawBorderThenFill(ax), Write(labels))

        self.play(Create(graph))

        self.wait()


class BetterCalculus(Scene):
    def construct(self):
        lines = VGroup(
            MathTex("x", "=", "\\frac{dy}{dx}"),
            MathTex("\\int", "x", "dx", "=", "y"),
        )

        self.play(Write(lines[0]))
        self.wait()
        for i, step in enumerate(lines[1:]):
            self.play(
                TransformMatchingTex(lines[i - 1].copy(), step, path_arc=90 * DEGREES)
            )
            self.wait()
        self.wait()


class Neuron(Scene):
    def construct(self):
        neuron = SVGMobject("neuron.svg", stroke_width=0).scale(2.5)

        self.play(Write(neuron))
        self.play(ScaleInPlace(neuron, 0.7))
        self.play(neuron.animate.shift(LEFT * 2 + DOWN * 2))

        neuron_2 = SVGMobject("neuron.svg", stroke_width=0).scale(1.75).next_to(neuron)

        self.play(Write(neuron_2))


class LinearGradientDescent(Scene):
    def construct(self):
        axes = Axes(
            x_range=[0, 10],
            y_range=[0, 10],
        )

        labels = axes.get_axis_labels(x_label="x", y_label="y")

        self.play(DrawBorderThenFill(axes), Write(labels))
        dots = [
            axes.coords_to_point(2, 3),
            axes.coords_to_point(4, 5),
            axes.coords_to_point(5, 7),
        ]
        self.play(*[Write(Dot(dot, color=GREEN)) for dot in dots])
        self.play(Create(axes.plot(lambda x: 1.4 * x + 0.2)))

        line_eq = MathTex("{{f(x)}}={{m}}{{x}}+{{b}}").move_to(LEFT * 4)

        self.play(Write(line_eq))

        self.play(Indicate(line_eq[2]))
        self.play(Indicate(line_eq[5]))

        self.play(ReplacementTransform(line_eq[2], MathTex("1.4")))

        self.play(Create(axes.plot(lambda x: 2 * x + 0.1, color=RED)))
        self.play(Create(axes.plot(lambda x: 1.3 * x - 1.5, color=RED)))
