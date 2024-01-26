from manim import * 


class Exp(Scene):
    def construct(self):
        table1 = Table([["Title", "Create UNIQUE INDEX author_index ON\nLibrary.Books USING btree (book_id)"],
                        ],line_config={'color': WHITE},include_outer_lines=True).scale(0.3).move_to([-3,1,0])
        self.play(FadeIn(table1))
        self.wait(5)