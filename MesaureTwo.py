from manim import *
class IntegralScene(Scene):
    CONFIG={
        'dx':.5,
        'rango_x':[-4,4,1],
        'value':0,
        'funcion':lambda x:x*np.sin(x*2),
    }
    def construct(self):
        title=Tex('Área Bajo la Curva').to_edge(UP)
        axes=Axes(
            x_range=self.CONFIG['rango_x'],
            y_range=[-3,3,1]
        ).set_z_index(1)
        axes.set_width(7).to_edge(RIGHT)
        grafico= axes.plot(self.CONFIG['funcion'])
        def update_function(curve,dt):
            self.CONFIG['value']+=dt*.2
            curve.become(axes.plot(lambda x:x*np.sin(x*2+self.CONFIG['value'])))
        grafico.add_updater(update_function)
        rectangles=axes.get_riemann_rectangles(grafico,input_sample_type='center',dx=self.CONFIG['dx'])
        def update_rectangle(rects,dt):
            self.CONFIG['value']+=dt
            rects.become(axes.get_riemann_rectangles(axes.plot(lambda x:x*np.sin(x*2+self.CONFIG['value'])),input_sample_type='center',dx=self.CONFIG['dx']))
        for mob in rectangles.submobjects:
            mob.add_updater(lambda t:t.set_fill(BLACK).set_opacity(1).set_stroke(WHITE,width=2))
        rectangles.add_updater(update_rectangle)
        # for mob in [
        #     axes,
        #     grafico,
        #     rectangles
        # ]:
        #     pass
            # self.play(Create(mob))
        # self.play(Write(title))
        # numbers=DecimalNumber(34.676, num_decimal_places=1).to_edge(LEFT)
        # self.play(Write(numbers))
        decimales=VGroup()   
        for t in np.arange(self.CONFIG['rango_x'][0],self.CONFIG['rango_x'][1],self.CONFIG['dx']):
            decimal_on_change=DecimalNumber(self.CONFIG['funcion']((0+0+1)/2)*t)
            def update_number(num):
                num.set_value((lambda x:x*np.sin(x*2+self.CONFIG['value']))(.5)*(t+.5))   
            decimal_on_change.add_updater(update_number)
            decimal=VGroup(Tex('área:'),decimal_on_change).arrange(RIGHT)
            decimal[1].scale_to_fit_height(decimal[0].get_height()-.1)
            # decimal[1].align_to(decimal[0].get_center(),LEFT*4)
            decimales.add(decimal)
        decimales.arrange(DOWN).scale_to_fit_height(config['frame_height']-1).to_edge(LEFT)
        self.add(grafico,rectangles,decimales)
        self.wait(3)