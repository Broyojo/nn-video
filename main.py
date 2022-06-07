import random
from manim import *


class LinearScene(Scene):
    def construct(self):
        axes = Axes(x_range=[0, 5], y_range=[0, 25, 5])

        labels = axes.get_axis_labels(x_label="x", y_label="y")

        dot_coords = [
            axes.coords_to_point(2.2, 14.3),
            axes.coords_to_point(3.5, 20.1),
            axes.coords_to_point(4.1, 23.5),
        ]

        dots = [
            Dot(dot, color=GREEN) for dot in dot_coords
        ]

        def guess_fn(x): return -3*x+24

        guess_line = axes.plot(guess_fn, color=BLUE)

        self.play(DrawBorderThenFill(axes), Write(labels), *
                  [Write(dot) for dot in dots])

        self.play(Create(guess_line))

        error_braces = [
            BraceBetweenPoints(
                axes.coords_to_point(2.2, guess_fn(2.2)), dot_coords[0]),
            BraceBetweenPoints(
                axes.coords_to_point(3.5, guess_fn(3.5)), dot_coords[1]),
            BraceBetweenPoints(
                axes.coords_to_point(4.1, guess_fn(4.1)), dot_coords[2]),
        ]

        error_brace_labels = [
            MathTex(r"e_1").next_to(error_braces[0], RIGHT),
            MathTex(r"e_2").next_to(error_braces[1], RIGHT),
            MathTex(r"e_3").next_to(error_braces[2], RIGHT),
        ]

        self.play(*[Create(brace) for brace in error_braces])

        self.play(*[Write(label) for label in error_brace_labels])

        graph_scene = VGroup(axes, labels, guess_line, *error_braces,
                             *error_brace_labels, *dots)

        graph_scene.generate_target()

        graph_scene.target.shift(3*LEFT + 2*UP).scale(0.5)

        self.play(MoveToTarget(graph_scene))

        eqs = [
            MathTex(r"\text{error}=e_1^2 + e_2^2 + e_3^2"),
            MathTex(r"=\sum_{i=1}^{n} e_i^2"),
            MathTex(r"=\sum_{i=1}^{3} (y_i-f(x_i))^2"),
            MathTex(r"=\sum_{i=1}^{3} (y_i-(mx_i + b))^2"),
            MathTex(
                r"E(m,b)=(y_1-(mx_1+b))^2+(y_2-(mx_2+b))^2+(y_3-(mx_3+b))^2"),
            MathTex(r"\frac{\mathrm{d} }{\mathrm{d} ?}E(m,b)=?"),
            MathTex(r"\frac{\partial }{\partial m}E(m,b)"),
            MathTex(r"\frac{\partial }{\partial b}E(m,b)"),
            MathTex(
                r"\frac{\partial }{\partial m}[(y_1-(mx_1+b))^2+(y_2-(mx_2+b))^2+(y_3-(mx_3+b))^2]"),
            MathTex(r"2(y_1-(mx_1+b))+2(y_2-(mx_2+b))+2(y_3-(mx_3+b))"),
            MathTex(r"-2x_1(y_1-(mx_1+b))-2x_2(y_2-(mx_2+b))-2x_3(y_3-(mx_3+b))"),
            MathTex(
                r"\frac{\partial }{\partial b}[(y_1-(mx_1+b))^2+(y_2-(mx_2+b))^2+(y_3-(mx_3+b))^2]"),
            MathTex(r"2(y_1-(mx_1+b))+2(y_2-(mx_2+b))+2(y_3-(mx_3+b))"),
            MathTex(r"-2(y_1-(mx_1+b))-2(y_2-(mx_2+b))-2(y_3-(mx_3+b))"),
            MathTex(r"-2x_1(y_1-(mx_1+b))-2x_2(y_2-(mx_2+b))-2x_3(y_3-(mx_3+b))=0"),
            MathTex(r"-2(y_1-(mx_1+b))-2(y_2-(mx_2+b))-2(y_3-(mx_3+b))=0"),
        ]

        for i, eq in enumerate(eqs[: 4]):
            self.play(Write(eq.move_to(RIGHT*3 + UP*3 + 1.5*DOWN*i)))

        self.play(Write(eqs[4].move_to(DOWN*3).scale(0.9)))

        self.play(eqs[4].animate.shift(UP*6),
                  FadeOut(graph_scene), FadeOut(*eqs[:4]))

        self.play(Write(eqs[5]))

        partial_eqs = VGroup(eqs[6].move_to(LEFT*2), eqs[7].move_to(RIGHT*2))

        self.play(Transform(eqs[5], partial_eqs))

        self.play(Flash(eqs[6], flash_radius=1.4))
        self.play(Flash(eqs[7], flash_radius=1.4))

        self.play(FadeOut(eqs[5], eqs[6], eqs[7], eqs[4]))

        self.play(Write(eqs[8].move_to(UP*2.5)))
        self.play(FadeIn(eqs[9].move_to(UP*1.5), shift=DOWN))
        self.play(ReplacementTransform(
            eqs[9], eqs[10].scale(0.9).move_to(UP*1.5)))

        self.play(Write(eqs[11].move_to(DOWN)))
        self.play(FadeIn(eqs[12].move_to(DOWN*2), shift=DOWN))
        self.play(ReplacementTransform(eqs[12], eqs[13].move_to(DOWN*2)))

        self.play(FadeOut(eqs[8], eqs[9], eqs[11], eqs[12]), eqs[10].animate.shift(
            UP*2).scale(0.9), eqs[13].animate.shift(UP*4.5).scale(0.8))

        self.play(ReplacementTransform(
            eqs[10], eqs[14].move_to(eqs[10]).scale(0.83)))
        self.play(ReplacementTransform(
            eqs[13], eqs[15].move_to(eqs[13]).scale(0.9)))

        system_of_eqs = VGroup(eqs[14], eqs[15])

        system_of_eqs_brace = Brace(system_of_eqs, direction=LEFT)

        self.play(Create(system_of_eqs_brace))

        point_table = DecimalTable(
            [[2.2, 3.5, 4.1], [14.3, 20.1, 23.5]],
            row_labels=[MathTex(r"x"), MathTex(r"y")],
            h_buff=1,
        )

        self.play(Create(point_table.move_to(LEFT*3)))

        eq_arrow = Arrow(start=UP, end=DOWN).move_to(RIGHT*2+UP*1.3)

        self.play(Create(eq_arrow))

        m_approx = MathTex(r"m\approx 4.781")
        b_approx = MathTex(r"b\approx 3.68")

        self.play(Write(m_approx.move_to(RIGHT*2+UP*0.2)))
        self.play(Write(b_approx.move_to(RIGHT*2+DOWN*0.3)))

        solving_scene = VGroup(
            point_table, system_of_eqs_brace, system_of_eqs, eqs[14], eqs[15], eq_arrow)

        axes = Axes(x_range=[0, 5], y_range=[0, 25, 5])

        labels = axes.get_axis_labels(x_label="x", y_label="y")

        dot_coords = [
            axes.coords_to_point(2.2, 14.3),
            axes.coords_to_point(3.5, 20.1),
            axes.coords_to_point(4.1, 23.5),
        ]

        dots = [
            Dot(dot, color=GREEN) for dot in dot_coords
        ]

        def good_fn(x): return 4.781*x+3.68

        good_line = axes.plot(good_fn, color=BLUE)

        self.play(FadeOut(solving_scene), m_approx.animate.shift(
            LEFT*6+UP*3), b_approx.animate.shift(LEFT*6+UP*3),
            DrawBorderThenFill(axes), Write(labels), *
            [Write(dot) for dot in dots])

        self.play(Create(good_line))

        self.wait()


class QuinticScene(Scene):
    def construct(self):
        random.seed = 69420
        randomness = 0.3
        axes = Axes(x_range=[-4, 10], y_range=[-1500, 2000, 1000])
        labels = axes.get_axis_labels(x_label="x", y_label="y")
        def fn_6(x): return (x+2)*(x+1)*(x-3)*(x-4)*(x-6)*(x-8)
        dot_coords = [
            axes.coords_to_point(x + random.random() * randomness,
                                 fn_6(x) + random.random() * randomness)
            for x in range(-4, 9)
        ]

        dots = [
            Dot(dot, color=GREEN) for dot in dot_coords
        ]

        good_line = axes.plot(fn_6, color=BLUE)

        self.play(DrawBorderThenFill(axes), Write(labels), *
                  [Write(dot) for dot in dots])

        self.play(Create(good_line))

        eqs = [
            MathTex(r"ax^6+bx^5+cx^4+dx^3+ex^2+fx+g"),

            MathTex(f"E(a,b,c,d,e,f,g)="),
            *[MathTex(f"(y_{i}-(ax_{i}^6+bx_{i}^5+cx_{i}^4+dx_{i}^3+ex_{i}^2+fx_{i}+g))^2+") if i != 10 else MathTex(
                f"(y_{{{i}}} -(ax_{{{i}}}^6+bx_{{{i}}}^5+cx_{{{i}}}^4+dx_{{{i}}}^3+ex_{{{i}}}^2+fx_{{{i}}}+g))^2") for i in range(1, 11)],  # eqs[0] - eqs[11]1

            *[MathTex(rf"\frac{{\partial }}{{\partial {i}}}E(a,b,c,d,e,f,g)=\cdots ")
              for i in "abcdefg"],
        ]

        self.play(Write(eqs[0].move_to(UP*3+RIGHT*2.5)))

        graph_scene = VGroup(axes, labels, *dots, good_line, eqs[0])

        self.play(FadeOut(graph_scene))

        for i, eq in enumerate(eqs[1:12]):
            eq.move_to(UP*3.5+DOWN*i*0.7).scale(0.7)

        self.play(*[Write(eq) for eq in eqs[1:12]])

        self.play(*[FadeOut(eq) for eq in eqs[1:12]])

        for i, eq in enumerate(eqs[12:22]):
            eq.move_to(UP*3+DOWN*i).scale(0.8)

        self.play(*[Write(eq) for eq in eqs[12:22]])

        self.play(*[FadeOut(eq) for eq in eqs[12:22]])

        self.play(Write(Text("?", font_size=400)))


class GradientScene(Scene):
    def construct(self):
        eqs = [
            MathTex(
                r"\frac{\partial }{\partial m}=-2x_1(y_1-(mx_1+b))-2x_2(y_2-(mx_2+b))-2x_3(y_3-(mx_3+b))"),
            MathTex(
                r"\frac{\partial }{\partial b}=-2(y_1-(mx_1+b))-2(y_2-(mx_2+b))-2(y_3-(mx_3+b))"),
            MathTex(
                r"\nabla E(m,b)=\left \langle \frac{\partial }{\partial m},\ \frac{\partial }{\partial b} \right \rangle",
            )
        ]

        # self.play(Write(eqs[0].move_to(UP/2).scale(0.8)),
        #           Write(eqs[1].move_to(DOWN/2).scale(0.8)))

        # partials = VGroup(eqs[0], eqs[1])

        # self.play(ReplacementTransform(partials, eqs[2]))

        # self.play(FadeOut(partials, eqs[2]))

        axes = Axes(x_range=[-4, 4], y_range=[0, 6],
                    axis_config={"include_numbers": True},)

        labels = axes.get_axis_labels(x_label="x", y_label="f(x)=x^2")

        def x2_fn(x): return x**2

        x2_line = axes.plot(x2_fn, color=BLUE)

        self.play(DrawBorderThenFill(axes), Write(labels))

        self.play(Create(x2_line))

        vec_1d = 0
