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
            self.CONFIG['value']+=dt
            curve.become(axes.plot(lambda x:x*np.sin(x*2+self.CONFIG['value'])))
        grafico.add_updater(update_function)
        rectangles=axes.get_riemann_rectangles(grafico,input_sample_type='center',dx=self.CONFIG['dx'])
        def update_rectangle(rects,dt):
            self.CONFIG['value']+=dt
            rects.become(axes.get_riemann_rectangles(axes.plot(lambda x:x*np.sin(x*2+self.CONFIG['value'])),input_sample_type='center',dx=self.CONFIG['dx']))
        for mob in rectangles.submobjects:
            mob.add_updater(lambda t:t.set_fill(BLACK).set_opacity(1).set_stroke(WHITE,width=2))
        rectangles.add_updater(update_rectangle)
        decimales=VGroup()   
        for i in range(len(rectangles)):
            decimal=VGroup(Tex('Area: '),DecimalNumber(i)).arrange(RIGHT)
            decimales.add(decimal)
        decimales.arrange(DOWN).scale_to_fit_height(config['frame_height']-1).to_edge(LEFT)
        decimales[0][-1].add_updater(lambda t: t.set_value((-8+0)*np.sin((-8+0)**2+self.CONFIG['value'])))
        decimales[1][-1].add_updater(lambda t: t.set_value((-8+1)*np.sin((-8+1)**2+self.CONFIG['value'])))
        decimales[2][-1].add_updater(lambda t: t.set_value((-8+2)*np.sin((-8+2)**2+self.CONFIG['value'])))
        decimales[3][-1].add_updater(lambda t: t.set_value((-8+3)*np.sin((-8+3)**2+self.CONFIG['value'])))
        decimales[4][-1].add_updater(lambda t: t.set_value((-8+4)*np.sin((-8+4)**2+self.CONFIG['value'])))
        decimales[5][-1].add_updater(lambda t: t.set_value((-8+5)*np.sin((-8+5)**2+self.CONFIG['value'])))
        decimales[6][-1].add_updater(lambda t: t.set_value((-8+6)*np.sin((-8+6)**2+self.CONFIG['value'])))
        decimales[7][-1].add_updater(lambda t: t.set_value((-8+7)*np.sin((-8+7)**2+self.CONFIG['value'])))
        decimales[8][-1].add_updater(lambda t: t.set_value((-8+8)*np.sin((-8+8)**2+self.CONFIG['value'])))
        decimales[9][-1].add_updater(lambda t: t.set_value((-8+9)*np.sin((-8+9)**2+self.CONFIG['value'])))
        decimales[10][-1].add_updater(lambda t: t.set_value((-8+10)*np.sin((-8+10)**2+self.CONFIG['value'])))
        decimales[11][-1].add_updater(lambda t: t.set_value((-8+11)*np.sin((-8+11)**2+self.CONFIG['value'])))
        decimales[12][-1].add_updater(lambda t: t.set_value((-8+12)*np.sin((-8+12)**2+self.CONFIG['value'])))
        decimales[13][-1].add_updater(lambda t: t.set_value((-8+13)*np.sin((-8+13)**2+self.CONFIG['value'])))
        decimales[14][-1].add_updater(lambda t: t.set_value((-8+14)*np.sin((-8+14)**2+self.CONFIG['value'])))
        decimales[15][-1].add_updater(lambda t: t.set_value((-8+15)*np.sin((-8+15)**2+self.CONFIG['value'])))
        self.add(grafico,rectangles,decimales)
        self.wait(20)