from manim import * 


class Exp(Scene):
    def construct(self):
        table1 = Table([["Title", "Author", "PYear", "Genre", "DateAdded"],
                        ],line_config={'color': WHITE},include_outer_lines=True).scale(0.3).move_to([-3,1,0])
        cell5 = VGroup(table1.get_cell((1,5),color=WHITE),table1.get_entries((1,5)))
        table1 = VGroup(table1.get_cell((1,1),color=WHITE),table1.get_cell((1,2),color=WHITE),
                        table1.get_cell((1,3),color=WHITE),table1.get_cell((1,4),color=WHITE),
                        table1.get_entries((1,1)),table1.get_entries((1,2)),
                        table1.get_entries((1,3)),table1.get_entries((1,4)))
        self.play(FadeIn(table1))
        self.play(FadeIn(cell5))
        self.wait(5)