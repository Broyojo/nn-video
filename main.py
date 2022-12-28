import math
import random

from manim import *

config["max_files_cached"] = 500


class LinearScene(Scene):
    def construct(self):
        axes = Axes(x_range=[0, 5], y_range=[0, 25, 5])

        labels = axes.get_axis_labels(x_label="x", y_label="y")

        dot_coords = [
            axes.coords_to_point(2.2, 14.3),
            axes.coords_to_point(3.5, 20.1),
            axes.coords_to_point(4.1, 23.5),
        ]

        dots = [Dot(dot, color=GREEN) for dot in dot_coords]

        def guess_fn(x):
            return -3 * x + 24

        guess_line = axes.plot(guess_fn, color=BLUE)

        self.play(
            DrawBorderThenFill(axes), Write(labels), *[Write(dot) for dot in dots]
        )

        self.wait()

        self.play(Create(guess_line))

        self.wait()

        error_braces = [
            BraceBetweenPoints(axes.coords_to_point(2.2, guess_fn(2.2)), dot_coords[0]),
            BraceBetweenPoints(axes.coords_to_point(3.5, guess_fn(3.5)), dot_coords[1]),
            BraceBetweenPoints(axes.coords_to_point(4.1, guess_fn(4.1)), dot_coords[2]),
        ]

        error_brace_labels = [
            MathTex(r"e_1").next_to(error_braces[0], RIGHT),
            MathTex(r"e_2").next_to(error_braces[1], RIGHT),
            MathTex(r"e_3").next_to(error_braces[2], RIGHT),
        ]

        self.play(*[Create(brace) for brace in error_braces])

        self.wait()

        self.play(*[Write(label) for label in error_brace_labels])

        self.wait()

        graph_scene = VGroup(
            axes, labels, guess_line, *error_braces, *error_brace_labels, *dots
        )

        graph_scene.generate_target()

        graph_scene.target.shift(3 * LEFT + 2 * UP).scale(0.5)

        self.play(MoveToTarget(graph_scene))

        self.wait()

        eqs = [
            MathTex(r"\text{error}=e_1^2 + e_2^2 + e_3^2"),
            MathTex(r"=\sum_{i=1}^{n} e_i^2"),
            MathTex(r"=\sum_{i=1}^{3} (y_i-f(x_i))^2"),
            MathTex(r"=\sum_{i=1}^{3} (y_i-(mx_i + b))^2"),
            MathTex(r"E(m,b)=(y_1-(mx_1+b))^2+(y_2-(mx_2+b))^2+(y_3-(mx_3+b))^2"),
            MathTex(r"\frac{\mathrm{d} }{\mathrm{d} ?}E(m,b)=?"),
            MathTex(r"\frac{\partial }{\partial m}E(m,b)"),
            MathTex(r"\frac{\partial }{\partial b}E(m,b)"),
            MathTex(
                r"\frac{\partial }{\partial m}[(y_1-(mx_1+b))^2+(y_2-(mx_2+b))^2+(y_3-(mx_3+b))^2]"
            ),
            MathTex(r"2(y_1-(mx_1+b))+2(y_2-(mx_2+b))+2(y_3-(mx_3+b))"),
            MathTex(r"-2x_1(y_1-(mx_1+b))-2x_2(y_2-(mx_2+b))-2x_3(y_3-(mx_3+b))"),
            MathTex(
                r"\frac{\partial }{\partial b}[(y_1-(mx_1+b))^2+(y_2-(mx_2+b))^2+(y_3-(mx_3+b))^2]"
            ),
            MathTex(r"2(y_1-(mx_1+b))+2(y_2-(mx_2+b))+2(y_3-(mx_3+b))"),
            MathTex(r"-2(y_1-(mx_1+b))-2(y_2-(mx_2+b))-2(y_3-(mx_3+b))"),
            MathTex(r"-2x_1(y_1-(mx_1+b))-2x_2(y_2-(mx_2+b))-2x_3(y_3-(mx_3+b))=0"),
            MathTex(r"-2(y_1-(mx_1+b))-2(y_2-(mx_2+b))-2(y_3-(mx_3+b))=0"),
        ]

        for i, eq in enumerate(eqs[:4]):
            self.play(Write(eq.move_to(RIGHT * 3 + UP * 3 + 1.5 * DOWN * i)))
            self.wait()

        self.play(Write(eqs[4].move_to(DOWN * 3).scale(0.9)))

        self.wait()

        self.play(eqs[4].animate.shift(UP * 6), FadeOut(graph_scene), FadeOut(*eqs[:4]))

        self.wait()

        self.play(Write(eqs[5]))

        self.wait()

        partial_eqs = VGroup(eqs[6].move_to(LEFT * 2), eqs[7].move_to(RIGHT * 2))

        self.play(Transform(eqs[5], partial_eqs))

        self.wait()

        self.play(Flash(eqs[6], flash_radius=1.4))

        self.wait()

        self.play(Flash(eqs[7], flash_radius=1.4))

        self.wait()

        self.play(FadeOut(eqs[5], eqs[6], eqs[7], eqs[4]))

        self.wait()

        self.play(Write(eqs[8].move_to(UP * 2.5)))
        self.wait()
        self.play(FadeIn(eqs[9].move_to(UP * 1.5), shift=DOWN))
        self.wait()
        self.play(ReplacementTransform(eqs[9], eqs[10].scale(0.9).move_to(UP * 1.5)))
        self.wait()

        self.play(Write(eqs[11].move_to(DOWN)))
        self.wait()
        self.play(FadeIn(eqs[12].move_to(DOWN * 2), shift=DOWN))
        self.wait()
        self.play(ReplacementTransform(eqs[12], eqs[13].move_to(DOWN * 2)))
        self.wait()

        self.play(
            FadeOut(eqs[8], eqs[9], eqs[11], eqs[12]),
            eqs[10].animate.shift(UP * 2).scale(0.9),
            eqs[13].animate.shift(UP * 4.5).scale(0.8),
        )
        self.wait()

        self.play(ReplacementTransform(eqs[10], eqs[14].move_to(eqs[10]).scale(0.83)))
        self.wait()
        self.play(ReplacementTransform(eqs[13], eqs[15].move_to(eqs[13]).scale(0.9)))
        self.wait()

        system_of_eqs = VGroup(eqs[14], eqs[15])

        system_of_eqs_brace = Brace(system_of_eqs, direction=LEFT)

        self.play(Create(system_of_eqs_brace))
        self.wait()

        point_table = DecimalTable(
            [[2.2, 3.5, 4.1], [14.3, 20.1, 23.5]],
            row_labels=[MathTex(r"x"), MathTex(r"y")],
            h_buff=1,
        )

        self.play(Create(point_table.move_to(LEFT * 3)))
        self.wait()

        eq_arrow = Arrow(start=UP, end=DOWN).move_to(RIGHT * 2 + UP * 1.3)

        self.play(Create(eq_arrow))
        self.wait()

        m_approx = MathTex(r"m\approx 4.781")
        b_approx = MathTex(r"b\approx 3.68")

        self.play(Write(m_approx.move_to(RIGHT * 2 + UP * 0.2)))
        self.wait()
        self.play(Write(b_approx.move_to(RIGHT * 2 + DOWN * 0.3)))
        self.wait()

        solving_scene = VGroup(
            point_table, system_of_eqs_brace, system_of_eqs, eqs[14], eqs[15], eq_arrow
        )

        axes = Axes(x_range=[0, 5], y_range=[0, 25, 5])

        labels = axes.get_axis_labels(x_label="x", y_label="y")

        dot_coords = [
            axes.coords_to_point(2.2, 14.3),
            axes.coords_to_point(3.5, 20.1),
            axes.coords_to_point(4.1, 23.5),
        ]

        dots = [Dot(dot, color=GREEN) for dot in dot_coords]

        def good_fn(x):
            return 4.781 * x + 3.68

        good_line = axes.plot(good_fn, color=BLUE)

        self.play(
            FadeOut(solving_scene),
            m_approx.animate.shift(LEFT * 6 + UP * 3),
            b_approx.animate.shift(LEFT * 6 + UP * 3),
            DrawBorderThenFill(axes),
            Write(labels),
            *[Write(dot) for dot in dots],
        )
        self.wait()

        self.play(Create(good_line))

        self.wait()


class QuinticScene(Scene):
    def construct(self):
        random.seed = 69420
        randomness = 0.3
        axes = Axes(x_range=[-4, 10], y_range=[-1500, 2000, 1000])
        labels = axes.get_axis_labels(x_label="x", y_label="y")

        def fn_6(x):
            return (x + 2) * (x + 1) * (x - 3) * (x - 4) * (x - 6) * (x - 8)

        dot_coords = [
            axes.coords_to_point(
                x + random.random() * randomness, fn_6(x) + random.random() * randomness
            )
            for x in range(-4, 9)
        ]

        dots = [Dot(dot, color=GREEN) for dot in dot_coords]

        # good_line = axes.plot(fn_6, color=BLUE)

        self.play(
            DrawBorderThenFill(axes), Write(labels), *[Write(dot) for dot in dots]
        )
        self.wait()

        eqs = [
            MathTex(r"ax^6+bx^5+cx^4+dx^3+ex^2+fx+g"),
            MathTex(f"E(a,b,c,d,e,f,g)="),
            *[
                MathTex(
                    f"(y_{i}-(ax_{i}^6+bx_{i}^5+cx_{i}^4+dx_{i}^3+ex_{i}^2+fx_{i}+g))^2+"
                )
                if i != 10
                else MathTex(
                    f"(y_{{{i}}} -(ax_{{{i}}}^6+bx_{{{i}}}^5+cx_{{{i}}}^4+dx_{{{i}}}^3+ex_{{{i}}}^2+fx_{{{i}}}+g))^2"
                )
                for i in range(1, 11)
            ],  # eqs[0] - eqs[11]1
            *[
                MathTex(rf"\frac{{\partial }}{{\partial {i}}}E(a,b,c,d,e,f,g)=\cdots ")
                for i in "abcdefg"
            ],
        ]

        self.play(Write(eqs[0].move_to(UP * 3 + RIGHT * 2.5)))
        self.wait()

        graph_scene = VGroup(axes, labels, *dots, eqs[0])

        self.play(FadeOut(graph_scene))
        self.wait()

        for i, eq in enumerate(eqs[1:12]):
            eq.move_to(UP * 3.5 + DOWN * i * 0.7).scale(0.7)

        self.play(*[Write(eq) for eq in eqs[1:12]])
        self.wait()

        self.play(*[FadeOut(eq) for eq in eqs[1:12]])
        self.wait()

        for i, eq in enumerate(eqs[12:22]):
            eq.move_to(UP * 3 + DOWN * i).scale(0.8)

        self.play(*[Write(eq) for eq in eqs[12:22]])
        self.wait()

        self.play(*[FadeOut(eq) for eq in eqs[12:22]])
        self.wait()

        self.play(Write(Text("?", font_size=400)))
        self.wait()


class GradientScene(Scene):
    def construct(self):
        eqs = [
            MathTex(
                r"\frac{\partial }{\partial m}=-2x_1(y_1-(mx_1+b))-2x_2(y_2-(mx_2+b))-2x_3(y_3-(mx_3+b))"
            ),
            MathTex(
                r"\frac{\partial }{\partial b}=-2(y_1-(mx_1+b))-2(y_2-(mx_2+b))-2(y_3-(mx_3+b))"
            ),
            MathTex(
                r"\nabla E(m,b)=\left \langle \frac{\partial }{\partial m},\ \frac{\partial }{\partial b} \right \rangle",
            ),
            MathTex(r"f(x)=x^2"),
            MathTex(r"f'(x)=2x"),
        ]

        self.play(
            Write(eqs[0].move_to(UP / 2).scale(0.8)),
            Write(eqs[1].move_to(DOWN / 2).scale(0.8)),
        )
        self.wait()

        partials = VGroup(eqs[0], eqs[1])

        self.play(ReplacementTransform(partials, eqs[2]))
        self.wait()

        self.wait()

        self.play(FadeOut(partials, eqs[2]))
        self.wait()

        axes = Axes(
            x_range=[-8, 8, 2],
            y_range=[0, 9, 2],
            axis_config={"include_numbers": True},
        )

        labels = axes.get_axis_labels(x_label="x", y_label="y")

        def x2_fn(x):
            return x**2

        def x2_prime(x):
            return 2 * x

        x2_line = axes.plot(x2_fn, color=BLUE)

        self.play(
            DrawBorderThenFill(axes),
            Write(labels),
            Write(eqs[3].move_to(UP * 3 + LEFT * 4)),
            Write(eqs[4].move_to(UP * 2.3 + LEFT * 4)),
        )
        self.wait()

        self.play(Create(x2_line))
        self.wait()

        t = ValueTracker(2)

        vec_orig = Dot(
            axes.coords_to_point(t.get_value(), x2_fn(t.get_value())), color=YELLOW
        )

        vec_orig.add_updater(
            lambda x: x.move_to(
                axes.coords_to_point(t.get_value(), x2_fn(t.get_value()))
            )
        )

        vec_1d = Vector(
            [x2_prime(t.get_value()), 0], color=YELLOW
        ).put_start_and_end_on(
            axes.coords_to_point(t.get_value(), x2_fn(t.get_value())),
            axes.coords_to_point(
                t.get_value() + x2_prime(t.get_value()), x2_fn(t.get_value())
            ),
        )

        vec_1d.add_updater(
            lambda x: x.put_start_and_end_on(
                axes.coords_to_point(t.get_value(), x2_fn(t.get_value())),
                axes.coords_to_point(
                    t.get_value() + x2_prime(t.get_value()), x2_fn(t.get_value())
                ),
            )
        )

        vec_1d_mag = DecimalNumber(x2_prime(t.get_value())).move_to(
            axes.coords_to_point(
                t.get_value() + x2_prime(t.get_value()),
                x2_fn(t.get_value()),
            )
            + DOWN * 0.5
        )

        vec_1d_mag.add_updater(lambda x: x.set_value(abs(x2_prime(t.get_value()))))
        vec_1d_mag.add_updater(
            lambda x: x.move_to(
                axes.coords_to_point(
                    t.get_value() + x2_prime(t.get_value()),
                    x2_fn(t.get_value()),
                )
                + DOWN * 0.5
            )
        )

        self.play(Create(vec_1d), Create(vec_orig), Write(vec_1d_mag))
        self.wait()

        self.play(t.animate.set_value(0))
        self.wait()

        t.set_value(-0.0001)

        self.play(t.animate.set_value(-2))
        self.wait()


class Gradient3DScene(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes(x_range=[-5, 5], y_range=[-5, 5], z_range=[-5, 5])

        labels = VGroup(
            axes.get_x_axis_label("m"),
            axes.get_y_axis_label("b"),
            axes.get_z_axis_label("E(m,b)"),
        )

        def err_fn(m, b):
            xyz = axes.coords_to_point(m, b, 7 * m * b / math.exp(m**2 + b**2))
            return xyz

        surface = Surface(
            err_fn,
            v_range=[-2, +2],
            u_range=[-2, +2],
            resolution=(42, 42),
            stroke_color=BLACK,
        )

        surface.set_shade_in_3d(True)

        self.set_camera_orientation(phi=60 * DEGREES, theta=-45 * DEGREES)

        eqs = [
            MathTex(
                r"\nabla E(m,b)=\left \langle \frac{\partial }{\partial m},\ \frac{\partial }{\partial b} \right \rangle"
            ),
            MathTex(
                r"-\nabla E(m,b)=\left \langle -\frac{\partial }{\partial m},\ -\frac{\partial }{\partial b} \right \rangle"
            ),
        ]

        self.add_fixed_in_frame_mobjects(eqs[0])

        self.play(DrawBorderThenFill(axes), Write(eqs[0].to_corner(UL)))
        self.wait()
        self.play(Write(labels[0]))
        self.wait()
        self.play(Write(labels[1]))
        self.wait()
        self.play(Write(labels[2]))
        self.wait()
        self.play(Create(surface))
        self.wait()

        grad_vec = Arrow3D(
            start=err_fn(1, -0.5), end=err_fn(1, 0.5), color=YELLOW
        ).move_to(err_fn(1, 0.1))

        self.play(Create(grad_vec))
        self.wait()
        q_mark = Text("?", font_size=200).move_to(LEFT * 5)

        self.add_fixed_in_frame_mobjects(q_mark)

        self.play(Write(q_mark))
        self.wait()

        self.play(FadeOut(q_mark))
        self.wait()

        self.play(FadeOut(eqs[0], run_time=0.5))
        self.wait()

        self.add_fixed_in_frame_mobjects(eqs[1])

        self.play(
            Write(eqs[1].to_corner(UL)),
            ReplacementTransform(
                grad_vec,
                Arrow3D(
                    start=err_fn(1, 0.5), end=err_fn(1, -0.5), color=YELLOW
                ).move_to(err_fn(1, 0.1)),
            ),
        )
        self.wait()


class GradientDescentScene(Scene):
    def construct(self):
        eqs = [
            MathTex(r"m=m_i"),
            MathTex(r"b=b_i"),
            MathTex(
                r"\nabla E(m,b)=\left \langle \frac{\partial }{\partial m},\ \frac{\partial }{\partial b} \right \rangle"
            ),
            MathTex(
                r"\Rightarrow \nabla E(m_i,b_i)=\left \langle \left.\frac{\partial }{\partial m}\right|_{m_i,b_i},\ \left.\frac{\partial }{\partial b}\right|_{m_i,b_i} \right \rangle"
            ),
            MathTex(
                r"=\left \langle \left.\frac{\partial }{\partial m}\right|_{m_i,b_i},\ \left.\frac{\partial }{\partial b}\right|_{m_i,b_i} \right \rangle"
            ),
            MathTex(
                r"\Rightarrow \left \langle -\left.\frac{\partial }{\partial m}\right|_{m_i,b_i},\ -\left.\frac{\partial }{\partial b}\right|_{m_i,b_i} \right \rangle"
            ),
            MathTex(
                r"\left \langle m_i, \, b_i \right \rangle + \left \langle -\left.\frac{\partial }{\partial m}\right|_{m_i,b_i},-\left.\frac{\partial }{\partial b}\right|_{m_i,b_i} \right \rangle"
            ),
            MathTex(
                r"\left \langle m_i-\left.\frac{\partial }{\partial m}\right|_{m_i,b_i}, \, b_i-\left.\frac{\partial }{\partial b}\right|_{m_i,b_i} \right \rangle"
            ),
            MathTex(r"m=m_i-\left.\frac{\partial }{\partial m}\right|_{m_i,b_i}"),
            MathTex(r"b=b_i-\left.\frac{\partial }{\partial b}\right|_{m_i,b_i}"),
            MathTex(
                r"\left |\left \langle -\left.\frac{\partial }{\partial m}\right|_{m_i,b_i},-\left.\frac{\partial }{\partial b}\right|_{m_i,b_i} \right \rangle \right | \ll 1"
            ),
            MathTex(r"m_{i+1}=m_i-\left.\frac{\partial }{\partial m}\right|_{m_i,b_i}"),
            MathTex(r"b_{i+1}=b_i-\left.\frac{\partial }{\partial b}\right|_{m_i,b_i}"),
        ]

        self.play(
            Write(eqs[0].move_to(UP * 3.5 + LEFT * 5.5)),
            Write(eqs[1].move_to(UP * 2.8 + LEFT * 5.5)),
            Write(eqs[2].move_to(UP * 3.2 + RIGHT)),
        )
        self.wait()
        self.play(TransformFromCopy(eqs[2], eqs[3].move_to(UP * 1.8 + RIGHT)))
        self.wait()

        self.play(TransformFromCopy(eqs[3], eqs[4].move_to(UP * 0.3 + RIGHT)))
        self.wait()

        self.play(ReplacementTransform(eqs[4], eqs[5].move_to(UP * 0.2 + RIGHT)))

        self.wait()

        self.play(
            TransformFromCopy(
                VGroup(eqs[0], eqs[1], eqs[5]), eqs[6].move_to(UP * -1.5 + RIGHT)
            )
        )

        self.wait()

        self.play(TransformFromCopy(eqs[6], eqs[7].move_to(UP * -3.1 + RIGHT)))

        self.wait()

        self.play(ReplacementTransform(eqs[0], eqs[8].move_to(eqs[0]).scale(0.7)))

        self.wait()
        self.play(
            ReplacementTransform(
                eqs[1], eqs[9].move_to(eqs[1]).scale(0.8).shift(DOWN * 0.5)
            )
        )

        self.wait()

        right_eqs = VGroup(*eqs[2:8])

        self.play(right_eqs.animate.shift(RIGHT))

        self.wait()

        self.play(Write(eqs[10].move_to(LEFT * 4).scale(0.6)))

        self.wait()


class RollingBallScene(Scene):
    def construct(self):
        axes = Axes(x_range=[-4, 10], y_range=[-1500, 2000, 1000])

        def fn_6(x):
            return (x + 2) * (x + 1) * (x - 3) * (x - 4) * (x - 6) * (x - 8)

        line = axes.plot(fn_6, color=BLUE)

        t = ValueTracker(1)

        ball = Dot(
            axes.coords_to_point(1, fn_6(1)) + UP * 0.15, radius=0.15, color=GREEN
        )

        ball.add_updater(
            lambda x: x.move_to(
                axes.coords_to_point(t.get_value(), fn_6(t.get_value())) + UP * 0.15
            )
        )

        self.play(DrawBorderThenFill(axes), Create(line), Write(ball))

        self.wait()

        self.play(t.animate.set_value(2))

        self.wait()

        self.play(t.animate.set_value(2.7))

        self.wait()

        self.play(t.animate.set_value(3.3))

        self.wait()

        self.play(t.animate.set_value(3.474))

        self.wait()

        lowest = Point(axes.coords_to_point(7.336, -998.639))

        self.play(Create(SurroundingRectangle(lowest, buff=0.5)))

        self.wait()

        top_text = Text("Gradient Descent")

        self.play(Write(top_text.to_edge(UP)))

        self.wait()


class LearningRateScene(Scene):
    def construct(self):
        eqs = [
            MathTex(r"f(x)=x^2"),
            MathTex(r"-f'(x)=-2x"),
            MathTex(r"0.01 \cdot -2x"),
        ]

        axes = Axes(
            x_range=[-8, 8, 2],
            y_range=[0, 9, 2],
            axis_config={"include_numbers": True},
        )

        labels = axes.get_axis_labels(x_label="x", y_label="y")

        def x2_fn(x):
            return x**2

        def x2_prime(x):
            return -2 * x

        x2_line = axes.plot(x2_fn, color=BLUE)

        self.play(
            DrawBorderThenFill(axes),
            Write(labels),
            Write(eqs[0].move_to(UP * 3 + LEFT * 4)),
            Write(eqs[1].move_to(UP * 2.3 + LEFT * 4)),
            Create(x2_line),
        )

        self.wait()

        t = ValueTracker(2)

        vec_orig = Dot(
            axes.coords_to_point(t.get_value(), x2_fn(t.get_value())), color=YELLOW
        )

        vec_orig.add_updater(
            lambda x: x.move_to(
                axes.coords_to_point(t.get_value(), x2_fn(t.get_value()))
            )
        )

        vec_1d = Vector(
            [x2_prime(t.get_value()), 0], color=YELLOW
        ).put_start_and_end_on(
            axes.coords_to_point(t.get_value(), x2_fn(t.get_value())),
            axes.coords_to_point(
                t.get_value() + x2_prime(t.get_value()), x2_fn(t.get_value())
            ),
        )

        vec_1d.add_updater(
            lambda x: x.put_start_and_end_on(
                axes.coords_to_point(t.get_value(), x2_fn(t.get_value())),
                axes.coords_to_point(
                    t.get_value() + x2_prime(t.get_value()), x2_fn(t.get_value())
                ),
            )
        )

        vec_1d_mag = DecimalNumber(x2_prime(t.get_value())).move_to(
            axes.coords_to_point(
                t.get_value() + x2_prime(t.get_value()),
                x2_fn(t.get_value()),
            )
            + DOWN * 0.5
        )

        vec_1d_mag.add_updater(lambda x: x.set_value(abs(x2_prime(t.get_value()))))
        vec_1d_mag.add_updater(
            lambda x: x.move_to(
                axes.coords_to_point(
                    t.get_value() + x2_prime(t.get_value()),
                    x2_fn(t.get_value()),
                )
                + DOWN * 0.5
            )
        )

        self.play(Create(vec_1d), Create(vec_orig), Write(vec_1d_mag))

        self.wait()

        self.play(t.animate.set_value(-2))

        self.wait()

        self.play(t.animate.set_value(2))

        self.wait()

        self.play(t.animate.set_value(-2))

        self.wait()

        self.play(t.animate.set_value(2))

        self.wait()

        arrow = Arrow(start=UP, end=DOWN).next_to(eqs[1], DOWN)

        self.play(
            Create(arrow), FadeIn(eqs[2].move_to(eqs[1]).shift(DOWN * 2.5), shift=DOWN)
        )

        self.wait()

        value = 2

        while value > 0.01:
            value = value + 0.3 * x2_prime(value)
            self.play(t.animate.set_value(value))
            self.wait(0.5)
        else:
            self.play(t.animate.set_value(value))
            self.wait()


class LearningRate3DScene(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes(x_range=[-5, 5], y_range=[-5, 5], z_range=[-5, 5])

        labels = VGroup(
            axes.get_x_axis_label("m"),
            axes.get_y_axis_label("b"),
            axes.get_z_axis_label("E(m,b)"),
        )

        def err_fn(m, b):
            xyz = axes.coords_to_point(m, b, 7 * m * b / math.exp(m**2 + b**2))
            return xyz

        surface = Surface(
            err_fn,
            v_range=[-2, +2],
            u_range=[-2, +2],
            resolution=(42, 42),
            stroke_color=BLACK,
        )

        surface.set_shade_in_3d(True)

        self.set_camera_orientation(phi=60 * DEGREES, theta=-45 * DEGREES)

        eqs = [
            MathTex(
                r"-\nabla E(m,b)=\left \langle -\frac{\partial }{\partial m},\ -\frac{\partial }{\partial b} \right \rangle"
            ),
            MathTex(
                r"0.001 \cdot \left \langle -\frac{\partial }{\partial m},\ -\frac{\partial }{\partial b} \right \rangle"
            ),
        ]

        grad_vec = Arrow3D(
            start=err_fn(1, 0.5), end=err_fn(1, -0.5), color=YELLOW
        ).move_to(err_fn(1, 0.1))

        self.add_fixed_in_frame_mobjects(eqs[0])

        self.play(
            DrawBorderThenFill(axes.shift(RIGHT)),
            Write(eqs[0].to_corner(UL)),
            Write(labels[0].shift(RIGHT)),
            Write(labels[1].shift(RIGHT)),
            Write(labels[2].shift(RIGHT)),
            Create(surface.shift(RIGHT)),
            Create(grad_vec.shift(RIGHT)),
        )

        self.wait()

        self.add_fixed_in_frame_mobjects(eqs[1])

        self.play(Write(eqs[1].next_to(eqs[0], DOWN)))

        self.wait()


class NeuralNetworkScene(Scene):
    def construct(self):
        xs = DecimalTable(
            [[-2, -1, 0, 1, 2]],
            h_buff=1,
            row_labels=[MathTex("x")],
            element_to_mobject_config={"num_decimal_places": 2},
            include_outer_lines=True,
        )

        ys = DecimalTable(
            [[0.14, 0.35, 1, 2.72, 7.39]],
            h_buff=1,
            row_labels=[MathTex("y")],
            element_to_mobject_config={"num_decimal_places": 2},
            include_outer_lines=True,
        )

        arrow = Arrow(start=UP * 2.5, end=DOWN * 2.5).move_to(xs)

        self.play(DrawBorderThenFill(xs.move_to(UP * 3), run_time=0.5))

        self.wait()

        f = MathTex("f(x)").scale(2).next_to(arrow, RIGHT)

        self.play(Create(arrow), Write(f))

        self.wait()

        self.play(DrawBorderThenFill(ys.move_to(DOWN * 3), run_time=0.5))

        self.wait()

        self.play(VGroup(arrow, f).animate.shift(RIGHT * 3))

        self.wait()

        msg = Text("Universal Function Approximator")

        self.play(Write(msg.shift(UP * 1.5 + LEFT * 2)))

        self.wait()

        eq = MathTex("min(E(p_i, p_{i+1},\cdots, p_n))")

        self.play(Write(eq.next_to(msg, DOWN * 2)))

        self.wait()

        self.play(FadeOut(xs, ys, arrow, f, msg, eq))

        self.wait()

        from neural_network import NeuralNetworkMobject

        network = NeuralNetworkMobject([3, 4, 1])

        self.play(Write(network.scale(2)))

        self.wait()

        network.label_inputs("x")
        network.label_outputs("y")

        eq1 = MathTex("f(x)=mx+b")

        rect = SurroundingRectangle(network.layers[1].neurons[3], buff=0.3)

        self.play(Write(eq1.next_to(network, DOWN * 1.5)), Create(rect))

        self.wait()

        self.play(
            FadeOut(eq1),
            FadeOut(rect),
            ReplacementTransform(
                network,
                NeuralNetworkMobject([16, 8, 8, 4, 2])
                .move_to(network)
                .scale(0.9)
                .label_inputs("x")
                .label_outputs("y"),
            ),
        )

        self.wait()


class DalleScene(Scene):
    def construct(self):
        nebula_img = ImageMobject("images/nebula.png").shift(UP / 2)
        nebula_cap = Text("A nebula shaped as a seahorse").next_to(nebula_img, DOWN)
        nebula_img.generate_target()
        nebula_cap.generate_target()

        homer_img = ImageMobject("images/homer.jpg").shift(UP / 2)
        homer_cap = Text("A topiary hedge cut in the shape of Homer Simpson").next_to(
            homer_img, DOWN
        )
        homer_img.generate_target()
        homer_cap.generate_target()

        panda_img = ImageMobject("images/panda.png").shift(UP / 2)
        panda_cap = Text("A cybertronic panda").next_to(panda_img[0], DOWN)
        panda_img.generate_target()
        panda_cap.generate_target()

        forest_img = ImageMobject("images/forest.png").shift(UP / 2)
        forest_cap = Text("A forest made of candy canes").next_to(forest_img[0], DOWN)
        forest_img.generate_target()
        forest_cap.generate_target()

        self.play(FadeIn(nebula_img), FadeIn(nebula_cap))
        self.wait()
        nebula_img.target.shift(LEFT * 5 + UP * 2).scale(0.5)
        nebula_cap.target.shift(LEFT * 5 + UP * 4).scale(0.5)
        self.play(MoveToTarget(nebula_img), MoveToTarget(nebula_cap))
        self.wait()

        self.play(FadeIn(homer_img), FadeIn(homer_cap))
        self.wait()
        homer_img.target.shift(UP * 1.8).scale(0.65)
        homer_cap.target.shift(UP * 3).scale(0.4)
        self.play(MoveToTarget(homer_img), MoveToTarget(homer_cap))
        self.wait()

        self.play(FadeIn(panda_img), FadeIn(panda_cap))
        self.wait()
        panda_img.target.shift(LEFT * 5 + UP * -2.2).scale(0.5)
        panda_cap.target.shift(LEFT * 5 + UP * -0.1).scale(0.7)
        self.play(MoveToTarget(panda_img), MoveToTarget(panda_cap))
        self.wait()

        self.play(FadeIn(forest_img), FadeIn(forest_cap))
        self.wait()
        forest_img.target.shift(UP * -2.3).scale(0.5)
        forest_cap.target.shift(UP * -0.005).scale(0.5)
        self.play(MoveToTarget(forest_img), MoveToTarget(forest_cap))
        self.wait()

        brace = Brace(
            mobject=Group(panda_img, nebula_img, homer_img, forest_img), direction=RIGHT
        )

        brace_txt = Text("AI Generated").scale(0.8)

        self.play(
            Create(brace.shift(RIGHT + DOWN * 0.2).scale(0.95)),
            Write(brace_txt.next_to(brace, RIGHT), run_time=0.5),
        )
        self.wait()

        self.play(
            FadeOut(
                nebula_img,
                nebula_cap,
                homer_img,
                homer_cap,
                panda_img,
                panda_cap,
                forest_img,
                forest_cap,
                brace,
                brace_txt,
            )
        )
        self.wait()

        english = Text("English Language").shift(LEFT * 4)

        arrow = Arrow(LEFT, RIGHT).scale(2).next_to(english, RIGHT)

        f = MathTex(r"f").scale(2).next_to(arrow, UP)

        images = Text("Images").next_to(arrow, RIGHT)

        self.play(Write(english))
        self.wait()
        self.play(Create(arrow), Write(f))
        self.wait()
        self.play(Write(images))
        self.wait()

        self.play(FadeOut(english, arrow, f, images))
        self.wait()

        axes = Axes(x_range=[0, 5], y_range=[0, 25, 5])

        labels = axes.get_axis_labels(x_label="x", y_label="y")

        dot_coords = [
            axes.coords_to_point(2.2, 14.3),
            axes.coords_to_point(3.5, 20.1),
            axes.coords_to_point(4.1, 23.5),
        ]

        dots = [Dot(dot, color=GREEN) for dot in dot_coords]

        def guess_fn(x):
            return 4.781 * x + 3.68

        guess_line = axes.plot(guess_fn, color=BLUE)

        self.play(
            DrawBorderThenFill(axes),
            Write(labels),
            *[Write(dot) for dot in dots],
            Create(guess_line),
        )
        self.wait()

        dot = Dot(axes.coords_to_point(3, guess_fn(3)), color=PURPLE)

        self.play(Write(Arrow(UP, DOWN).next_to(dot, UP)), Write(dot))
        self.wait()


class EndScene(Scene):
    def construct(self):
        t1 = Text("Thanks for watching! :D").shift(UP * 2)
        t2 = Text("Links to the code for this video in the description").next_to(
            t1, DOWN
        )
        t3 = Text("See you in the next video, more are to come...").next_to(t2, DOWN)

        self.play(Write(t1))
        self.wait()
        self.play(Write(t2))
        self.wait()
        self.play(Write(t3))
        self.wait()
