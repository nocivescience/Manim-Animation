from manim import *
class Example(Scene):
    def construct(self):
        objectos=VGroup(
            Circle(),
            Square(),
            Triangle(),
            Rectangle()
        ).arrange(DOWN)
        self.play(Create(objectos[0].copy()))
        for t in objectos:
            self.play(TransformFromCopy(objectos[0],t))
            self.add(objectos[0])
        self.wait()