from manim import *
class PolarScene(Scene):
    def construct(self):
        axes=PolarPlane()
        funcion=lambda t: 4*np.cos(t*3)
        plot=axes.plot_polar_graph(funcion,[0,PI])
        self.play(Create(axes))
        self.play(Create(plot))