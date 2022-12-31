from manim import *
class AreaCurveScene(Scene):
    CONFIG={
        'function':lambda x: np.cos(x)*x
    }
    def construct(self):
        axes=Axes(          
            x_range=[-5,5,1],
            y_range=[-3,3,1]
        )
        grafico=axes.plot(self.CONFIG['function'])
        Rectangulos=VGroup()
        self.play(Create(axes))
        for t in reversed(np.linspace(.05,2,18)):
            rectangulos=axes.get_riemann_rectangles(grafico,input_sample_type='center',dx=t)
            Rectangulos.add(rectangulos)
        for mob in Rectangulos:
            self.play(Transform(Rectangulos[0],mob))
        self.wait()
        