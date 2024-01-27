from manim import * 
class BlinkingCursor(VMobject):
    def __init__(self, *args, **kwargs):
        self.cursor_frame = Rectangle(width=0.1,height=0.5).scale(0.4).move_to([2,2,0])
        self.cursor_frame.set_fill(color=PURE_GREEN, opacity=1)
        self.cursor_frame.set_stroke(color=BLACK,width=0,opacity=0)
        super().__init__(*args, **kwargs)
        self.add(self.cursor_frame)
    def blinking_on(self):
        self.fade_in_anims = [FadeIn(self.cursor_frame, run_time=0.5) for _ in range(3)]
        self.fade_out_anims = [FadeOut(self.cursor_frame, run_time=0.5) for _ in range(3)]
        self.blinking_anim = [item for pair in zip(self.fade_out_anims,self.fade_in_anims) for item in pair]
        return self.blinking_anim
    def get_cursor(self):
        return self.cursor_frame
    def write_text(self,text):
        text = text.scale(0.3).next_to(self.get_cursor(),RIGHT,buff=0.05,aligned_edge=LEFT)
        anims = []
        for letter in text :
            if not letter == "*":
                anims.append((AnimationGroup(Write(letter),run_time=0.1),AnimationGroup(self.get_cursor().animate(run_time=0.1).next_to(letter, buff=0, aligned_edge=DOWN))))
            elif letter == "*":
                anims.append((AnimationGroup(Write(letter),run_time=0.1),AnimationGroup(self.get_cursor().animate(run_time=0.1).next_to(letter, buff=0, aligned_edge=UP))))
        return anims
    def get_text_object(self):
        return self.text

class Exp(Scene):
    def construct(self):
        constraints_def = Table([["NOT NULL", "Ensures that a column can't have a NULL value. Like making sure every apple has a color."],
                                   ["UNIQUE", "Ensures that all values in a column are different. Like making sure every apple has a unique ID."],
                                   ["PRIMARY KEY", "A special kind of UNIQUE constraint. Each table can have one primary key. It's like the\nmain ID for each apple."],
                                   ["FOREIGN KEY", "Allows you to link two tables together. Like if you have an apple, and you want to know\nwhich tree it came from."],
                                   ["CHECK", "Lets you add custom data validation. Like making sure no apple weighs less than 0 grams."],
                                   ],line_config={'color': ORANGE},include_outer_lines=True)
        constraints_examples = Table([["NOT NULL", "CREATE TABLE Books ( Title TEXT, Author TEXT, Year INT, Genre TEXT );"],
                                      ["UNIQUE", "CREATE TABLE Apples (ID INT UNIQUE);"],
                                      ["PRIMARY KEY", "CREATE TABLE Apples (ID INT PRIMARY KEY);"],
                                      ["FOREIGN KEY", "CREATE TABLE Apples (TreeID INT, FOREIGN KEY (TreeID) REFERENCES Trees(ID));"],
                                      ["CHECK", "CREATE TABLE Apples (Weight INT CHECK (Weight > 0));"]]
                                     ,line_config={'color': ORANGE},include_outer_lines=True)
        self.wait(5)