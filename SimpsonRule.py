from manim import *
class SimpsonRulesScene(Scene):
    CONFIG={
        'function': lambda t: t*np.sin(5*t),
        'subdivision':np.arange(5,120,5),
    }
    def construct(self):
        self.play(Write(Tex('La Regla del Trapecio').to_edge(UP)))
        axes=Axes(
            x_range=[-4,4,1],
            y_range=[-3,3,1]
        )
        self.play(Create(axes))
        grafico=axes.plot(self.CONFIG['function'])
        self.play(Create(grafico))
        PATHS=VGroup()
        for i in self.CONFIG['subdivision']:
            paths=VGroup().set_z_index(-1)
            dots_x=VGroup(*[
            Dot().move_to(axes.c2p(point,0)) for point in np.linspace(axes.x_range[0],axes.x_range[1],i)
            ])
            dots_f=VGroup(*[
                Dot().move_to(axes.c2p(point,self.CONFIG['function'](point))) for point in np.linspace(axes.x_range[0],axes.x_range[1],i)
            ])
            for i in range(len(dots_f)-1):
                path=VMobject(stroke_width=.5,color=BLACK,fill_color=ORANGE,fill_opacity=1).set_points_as_corners([
                    dots_x[i].get_center(),
                    dots_x[i+1].get_center(),
                    dots_f[i+1].get_center(),
                    dots_f[i].get_center(),
                    dots_x[i].get_center()
                ])
                paths.add(path)
            PATHS.add(paths)
        path_copy=PATHS[0].copy()
        self.play(Create(path_copy))
        for i in range(len(PATHS)):
            self.play(Transform(PATHS[0],PATHS[i]))
            self.remove(path_copy)
        self.wait()