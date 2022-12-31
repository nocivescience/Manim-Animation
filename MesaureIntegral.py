from manim import *
class IntegralScene(Scene):
    CONFIG={
        'dx':.5,
        'rango_x':[-4,4,1],
    }
    def construct(self):
        title=Tex('Área Bajo la Curva').to_edge(UP)
        axes=Axes(
            x_range=self.CONFIG['rango_x'],
            y_range=[-3,3,1]
        ).set_z_index(1)
        axes.set_width(7).to_edge(RIGHT)
        function= axes.plot(lambda x:x*np.sin(x*2))
        rectangles=axes.get_riemann_rectangles(function,input_sample_type='center',dx=self.CONFIG['dx'])
        for mob in [
            axes,
            function,
            rectangles
        ]:
            self.play(Create(mob))
        self.play(Write(title))
        ejemplo=MathTex(r"\int_0^\infty f_1(x)dx&=\ln(x)\\ \int_0^\infty f_2(x)dx&=\cos(x)\\\int_{-\infty}^\infty f_3(x)dx&=\sin(x)\\\int_{Rec(x)} g(x)dx&=(1-x^2)").to_edge(LEFT)
        self.play(Write(ejemplo),run_time=8)
        self.wait()
        