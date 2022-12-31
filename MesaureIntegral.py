from manim import *
class IntegralScene(Scene):
    def construct(self):
        title=Tex('Área Bajo la Curva').to_edge(UP)
        axes=Axes(
            x_range=[-4,4,1],
            y_range=[-3,3,1]
        ).set_z_index(1)
        axes.set_width(7).to_edge(RIGHT)
        function= axes.plot(lambda x:x*np.sin(x*2))
        rectangles=axes.get_riemann_rectangles(function,input_sample_type='center',dx=.5)
        for mob in [
            axes,
            function,
            rectangles
        ]:
            self.play(Create(mob))
        self.play(Write(title))
        self.wait()