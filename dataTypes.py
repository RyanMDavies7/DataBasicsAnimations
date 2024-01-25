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
    def write_text(self,text,*args,**kwargs):
        font_to_use = "resources/Quicksand-VariableFont_wght.ttf"
        text = Text(text,*args,**kwargs, font=font_to_use).scale(0.3).next_to(self.get_cursor(),RIGHT,buff=0.05,aligned_edge=LEFT)
        anims = []
        for letter in text :
            if not letter == "*":
                anims.append((AnimationGroup(Write(letter),run_time=0.1),AnimationGroup(self.get_cursor().animate(run_time=0.1).next_to(letter, buff=0, aligned_edge=DOWN))))
            elif letter == "*":
                anims.append((AnimationGroup(Write(letter),run_time=0.1),AnimationGroup(self.get_cursor().animate(run_time=0.1).next_to(letter, buff=0, aligned_edge=UP))))
        return anims
class TerminalPrompt(VMobject):
    def __init__(self,directory="~", *args, **kwargs):
        font_to_use = "resources/Quicksand-VariableFont_wght.ttf"
        self.directory = directory
        self.terminal_prompt_text =  Text(self.directory,*args,**kwargs, font=font_to_use).scale(0.35)
        self.terminal_prompt_frame = SurroundingRectangle(self.terminal_prompt_text, buff=0.05)
        self.terminal_prompt_frame.set_stroke(width=2,opacity=1)
        self.terminal_prompt_frame.set_fill("#32a871",opacity=1)
        self.terminal_prompt_text.move_to(self.terminal_prompt_frame.get_center())
        self.terminal_prompt = VGroup(
                               self.terminal_prompt_text)
        super().__init__(*args, **kwargs)
        self.add(self.terminal_prompt)
class Terminal(VMobject):
    def __init__(self, *args, **kwargs):
        self.terminal_frame = Rectangle(width=6,height=6).round_corners(radius=0.2)
        self.terminal_frame.set_fill(color="#002B36", opacity=.50)
        self.terminal_frame.set_stroke(color=ORANGE, opacity=1)
        self.terminal_upper_portion_line = Line(LEFT*3,RIGHT*3).next_to(self.terminal_frame.get_center(),UP*9.8)
        self.terminal_upper_portion_line.set_stroke(color=ORANGE, opacity=1)
        self.text1 = Text("⌄", color=YELLOW).scale(0.5).next_to(self.terminal_frame.get_center(),UP*10.5+RIGHT*8)
        self.text2 = Text("^", color=BLUE).scale(0.4).next_to(self.text1,buff=0.1)
        self.text3 = Text("✖",color=PURE_RED).scale(0.3).next_to(self.text2,buff=0.1)
        self.terminal_dots = VGroup( self.text1, self.text2,self.text3)
        self.terminal_user_name = Text("user@user-Laptop",color="#bafc03").scale(0.3).next_to(self.terminal_frame.get_center(),UP*10.5)
        self.terminal = VGroup(self.terminal_frame,self.terminal_upper_portion_line,
                               self.terminal_dots,self.terminal_user_name)
        
        super().__init__(*args, **kwargs)
        self.add(self.terminal)


class DataTypes(Scene):
    def construct(self):
        font_to_use = "resources/Quicksand-VariableFont_wght.ttf"
        sql_image = ImageMobject('resources/image (1).png')
        gear_image = ImageMobject('resources/image (2).png').scale(0.7).next_to(sql_image.get_end()-[1.4,-0.72,0],buff=0)
        gear_image.set_z_index(sql_image.z_index)
        sql_logo = Group(sql_image,gear_image).move_to([-4,3,0]).scale(0.2)
        self.play(FadeIn(sql_logo))
        always_rotate(gear_image, rate=60*DEGREES)
        title = Text("Data Types and Managing Data", font=font_to_use,color=BLACK).set_stroke(width=1,color="#FFFFFF",opacity=1).scale(0.6).next_to(sql_logo,RIGHT*3)
        title.save_state()
        self.wait(2)
        self.play(DrawBorderThenFill(title))
        self.wait(1)
        self.play(FadeToColor(title[:9], YELLOW))
        data_types = Text("Data Types", font=font_to_use).scale(0.6).next_to(title,DOWN).shift(LEFT*1.5)
        data_types.set_stroke(color=BLACK,opacity=1)
        highlighting_rectangle = Rectangle(width=2.3,height=0.28).move_to(data_types.get_center()+[0,-0.1,0])
        highlighting_rectangle.set_fill(color="#1be7ff", opacity=.5)
        highlighting_rectangle.set_stroke(color=None, opacity=0)
        data_types.set_z_index(highlighting_rectangle.z_index+1)
        self.play(Create(highlighting_rectangle))
        self.play(Write(data_types), run_time=1.5)
        # self.wait(2)
        # data_types_text = Text("Data types are like labels that tell a computer what kind of data it's dealing with such\nas numbers, text, or dates so it knows how to store, process, and use it correctly, ensuring \nthat numbers don't get mixed up with words and dates are handled appropriately.", font=font_to_use,line_spacing=1).scale(0.4).next_to([-6,1,0],aligned_edge=LEFT)
        # self.play(Write(data_types_text))
        # self.wait(2)
        # abacus = ImageMobject('resources/abacus (2).png').scale(0.4).move_to([-4.9,-0.8,0])
        # numeric_type = Text("Numeric", font=font_to_use,color=BLUE).scale(0.4).rotate(90*DEGREES).next_to(abacus,LEFT)
        # self.play(FadeIn(abacus,numeric_type))
        # dot1 = Dot(radius=0.05, color=YELLOW).next_to(abacus,DOWN,aligned_edge=LEFT)
        # self.play(FadeIn(dot1))
        # example1 = Text("integer",font=font_to_use).scale(0.4).next_to(dot1)
        # self.play(FadeIn(example1))
        # dot2 = Dot(radius=0.05, color=YELLOW).next_to(dot1,DOWN)
        # self.play(FadeIn(dot2))
        # example2 = Text("float",font=font_to_use).scale(0.4).next_to(dot2)
        # self.play(FadeIn(example2))
        # textual = ImageMobject('resources/keyboard.png').scale(0.45).next_to(abacus,RIGHT*4)
        # textual_type = Text("Textual", font=font_to_use,color=BLUE).scale(0.4).rotate(90*DEGREES).next_to(textual,LEFT)
        # self.play(FadeIn(textual_type,textual))
        # dot3 = Dot(radius=0.05, color=YELLOW).next_to(dot1,RIGHT*10)
        # self.play(FadeIn(dot3))
        # example3 = Text("char",font=font_to_use).scale(0.4).next_to(dot3)
        # self.play(FadeIn(example3))
        # dot4 = Dot(radius=0.05, color=YELLOW).next_to(dot3,DOWN)
        # self.play(FadeIn(dot4))
        # example4 = Text("varchar",font=font_to_use).scale(0.4).next_to(dot4)
        # self.play(FadeIn(example4))
        # dot5 = Dot(radius=0.05, color=YELLOW).next_to(dot4,DOWN)
        # self.play(FadeIn(dot5))
        # example5 = Text("text",font=font_to_use).scale(0.4).next_to(dot5)
        # self.play(FadeIn(example5))
        # boolean = ImageMobject('resources/boolean.png').scale(0.3).next_to(textual,RIGHT*5)
        # boolean_type = Text("Boolean", font=font_to_use,color=BLUE).scale(0.4).rotate(90*DEGREES).next_to(boolean,LEFT)
        # self.play(FadeIn(boolean_type,boolean))
        # dot6 = Dot(radius=0.05, color=YELLOW).next_to(dot3,RIGHT*10)
        # self.play(FadeIn(dot6))
        # example6 = Text("true",font=font_to_use).scale(0.4).next_to(dot6)
        # self.play(FadeIn(example6))
        # dot7 = Dot(radius=0.05, color=YELLOW).next_to(dot6,DOWN)
        # self.play(FadeIn(dot7))
        # example7 = Text("false",font=font_to_use).scale(0.4).next_to(dot7)
        # self.play(FadeIn(example7))
        # date_time = ImageMobject('resources/calendar.png').scale(0.35).next_to(boolean,RIGHT*5)
        # date_time_type = Text("Date and Time", font=font_to_use,color=BLUE).scale(0.4).rotate(90*DEGREES).next_to(date_time,LEFT)
        # self.play(FadeIn(date_time_type,date_time))
        # dot8 = Dot(radius=0.05, color=YELLOW).next_to(dot6,RIGHT*10)
        # self.play(FadeIn(dot8))
        # example8 = Text("date",font=font_to_use).scale(0.4).next_to(dot8)
        # self.play(FadeIn(example8))
        # dot9 = Dot(radius=0.05, color=YELLOW).next_to(dot8,DOWN)
        # self.play(FadeIn(dot9))
        # example9 = Text("time",font=font_to_use).scale(0.4).next_to(dot9)
        # self.play(FadeIn(example9))
        # dot10 = Dot(radius=0.05, color=YELLOW).next_to(dot9,DOWN)
        # self.play(FadeIn(dot10))
        # example10 = Text("timestamp",font=font_to_use).scale(0.4).next_to(dot10)
        # self.play(FadeIn(example10))
        # dot11 = Dot(radius=0.05, color=YELLOW).next_to(dot10,DOWN)
        # self.play(FadeIn(dot11))
        # example11 = Text("interval",font=font_to_use).scale(0.4).next_to(dot11)
        # self.play(FadeIn(example11))
        # other_types = ImageMobject('resources/postgresql.png').scale(0.35).next_to(date_time,RIGHT*5)
        # other_types_type = Text("Other Types", font=font_to_use,color=BLUE).scale(0.4).rotate(90*DEGREES).next_to(other_types,LEFT)
        # self.play(FadeIn(other_types_type,other_types))
        # dot12 = Dot(radius=0.05, color=YELLOW).next_to(dot8,RIGHT*7)
        # self.play(FadeIn(dot12))
        # example12 = Text("For everything else,\nPostgreSQL has a \nrange of specific \ntypes for handling \nvaried data",line_spacing=1,font=font_to_use).scale(0.4).next_to([4,-2.7,0],aligned_edge=LEFT)
        # self.play(FadeIn(example12))
        # self.wait(5)
        # self.play(FadeOut(data_types_text,abacus,numeric_type,dot1,example1,dot2,example2,textual,textual_type,dot3,example3,dot4,example4,dot5,example5,
        #                   boolean,boolean_type,dot6,example6,dot7,example7,date_time,date_time_type,dot8,example8,dot9,example9,
        #                   dot10,example10,dot11,example11,other_types,other_types_type,dot12,example12))
        
        
        
        
        
        self.play(Restore(title), FadeToColor(title[12:], YELLOW), run_time=1.5)
        create = Text("CREATE a Table", font=font_to_use).scale(0.6).next_to(title,DOWN).shift(LEFT*1.5)
        create.set_stroke(color=BLACK,opacity=1)
        highlighting_rectangle1 = Rectangle(width=3.1,height=0.28).move_to(create.get_center()+[0,-0.15,0])
        highlighting_rectangle1.set_fill(color="#1be7ff", opacity=.5)
        highlighting_rectangle1.set_stroke(color=None, opacity=0)
        create.set_z_index(highlighting_rectangle1.z_index+1)
        self.play(ReplacementTransform(highlighting_rectangle,highlighting_rectangle1))
        self.play(ReplacementTransform(data_types,create))
        terminal = Terminal().move_to([3.4,-0.5,0])
        prompt1 = TerminalPrompt("postgres>",color=PINK).move_to([1.2,1.6,0])
        cursor1 = BlinkingCursor().next_to(prompt1,buff=0.2)
        old_position1 = cursor1.get_center()
        self.play(FadeIn(terminal), FadeIn(prompt1), FadeIn(cursor1), run_time=0.5)
        for anim in cursor1.blinking_on():
            self.play(anim)
        for anim in cursor1.write_text("CREATE TABLE Books ( Title TEXT,",t2c={'CREATE':YELLOW,'TABLE':YELLOW, 'TEXT':YELLOW}):
            self.play(*anim)
        cursor1.next_to(old_position1,DOWN,buff=0.15)
        for anim in cursor1.write_text("Author TEXT, PYear INT, Genre TEXT );",t2c={'TEXT':YELLOW,'INT':YELLOW}):
            self.play(*anim)
        table1 = Table([["Title", "Author", "PYear", "Genre", "DateAdded"],
                        ],line_config={'color': WHITE},include_outer_lines=True).scale(0.3).move_to([-3,1,0])
        cell5 = VGroup(table1.get_cell((1,5),color=WHITE),table1.get_entries((1,5)))
        table1 = VGroup(table1.get_cell((1,1),color=WHITE),table1.get_cell((1,2),color=WHITE),
                        table1.get_cell((1,3),color=WHITE),table1.get_cell((1,4),color=WHITE),
                        table1.get_entries((1,1)),table1.get_entries((1,2)),
                        table1.get_entries((1,3)),table1.get_entries((1,4)))
        
        prompt2 = TerminalPrompt("postgres>",color=PINK).next_to(prompt1,DOWN*2,buff=0.2)
        cursor2 = BlinkingCursor().next_to(prompt2)
        self.play(FadeOut(cursor1),FadeIn(prompt2), FadeIn(cursor2), run_time=0.5)
        self.play(GrowFromPoint(table1,prompt1))
        
        
        
        
        
        insert = Text("INSERT into a Table", font=font_to_use).scale(0.6).next_to(title,DOWN).shift(LEFT*1.9)
        insert.set_stroke(color=BLACK,opacity=1)
        highlighting_rectangle2 = Rectangle(width=3.8,height=0.28).move_to(insert.get_center()+[0,-0.15,0])
        highlighting_rectangle2.set_fill(color="#1be7ff", opacity=.5)
        highlighting_rectangle2.set_stroke(color=None, opacity=0)
        insert.set_z_index(highlighting_rectangle2.z_index+1)
        self.play(ReplacementTransform(highlighting_rectangle1,highlighting_rectangle2))
        self.play(ReplacementTransform(create,insert))
        old_position2 = cursor2.get_center()
        for anim in cursor2.blinking_on():
            self.play(anim)
        for anim in cursor2.write_text("INSERT INTO Books (Title, Author, PYear,",t2c={'INSERT':YELLOW,'INTO':YELLOW}):
            self.play(*anim)
        cursor2.next_to(old_position2,DOWN,buff=0.15)
        old_position3 = cursor2.get_center()
        for anim in cursor2.write_text("Genre) VALUES ('The Great Gatsby',",t2c={'VALUES':YELLOW}):
            self.play(*anim)
        cursor2.next_to(old_position3,DOWN,buff=0.15)
        for anim in cursor2.write_text("'F. Scott Fitzgerald', 1926, 'Fiction');"):
            self.play(*anim)
        table2 = Table([["Title", "Author", "PYear", "Genre"],
                        ["The Great Gatsby", "F. Scott Fitzgerald", "1926", "Fiction"]],line_config={'color': WHITE},include_outer_lines=True).scale(0.3).next_to(table1,DOWN*2)
        prompt3 = TerminalPrompt("postgres>",color=PINK).next_to(prompt2,DOWN*3,buff=0.2)
        cursor3 = BlinkingCursor().next_to(prompt3)
        self.play(FadeOut(cursor2),FadeIn(prompt3), FadeIn(cursor3), run_time=0.5)
        self.play(GrowFromPoint(table2,prompt2))
        
        
        
        
        
        update = Text("UPDATE values in a Table", font=font_to_use).scale(0.6).next_to(title,DOWN).shift(LEFT*2.5)
        update.set_stroke(color=BLACK,opacity=1)
        highlighting_rectangle3 = Rectangle(width=5,height=0.28).move_to(update.get_center()+[0,-0.15,0])
        highlighting_rectangle3.set_fill(color="#1be7ff", opacity=.5)
        highlighting_rectangle3.set_stroke(color=None, opacity=0)
        update.set_z_index(highlighting_rectangle3.z_index+1)
        self.play(ReplacementTransform(highlighting_rectangle2,highlighting_rectangle3))
        self.play(ReplacementTransform(insert,update))
        old_position4 = cursor3.get_center()
        for anim in cursor3.blinking_on():
            self.play(anim)
        for anim in cursor3.write_text("UPDATE Books SET PYear = 1925",t2c={'UPDATE':YELLOW,'SET':YELLOW}):
            self.play(*anim)
        cursor3.next_to(old_position4,DOWN,buff=0.15)
        for anim in cursor3.write_text("WHERE Title = 'The Great Gatsby';",t2c={'WHERE':YELLOW}):
            self.play(*anim)
            
        table3 = Table([["Title", "Author", "PYear", "Genre"],
                        ["The Great Gatsby", "F. Scott Fitzgerald", "1926", "Fiction"]],line_config={'color': WHITE},include_outer_lines=True).scale(0.3).next_to(table2,DOWN*2)
        
        prompt4 = TerminalPrompt("postgres>",color=PINK).next_to(prompt3,DOWN*2,buff=0.2)
        cursor4 = BlinkingCursor().next_to(prompt4)
        self.play(FadeOut(cursor3),FadeIn(prompt4), FadeIn(cursor4), run_time=0.5)
        self.play(ReplacementTransform(table2.copy(),table3))
        self.play(Transform(table3.get_entries((2, 3)), Text("1925").scale(0.3).move_to(table3.get_entries((2, 3)))))
        
        
        
        
        delete = Text("DELETE values from a Table", font=font_to_use).scale(0.6).next_to(title,DOWN).shift(LEFT*2.9)
        delete.set_stroke(color=BLACK,opacity=1)
        highlighting_rectangle4 = Rectangle(width=5.5,height=0.28).move_to(delete.get_center()+[0,-0.15,0])
        highlighting_rectangle4.set_fill(color="#1be7ff", opacity=.5)
        highlighting_rectangle4.set_stroke(color=None, opacity=0)
        delete.set_z_index(highlighting_rectangle4.z_index+1)
        self.play(ReplacementTransform(highlighting_rectangle3,highlighting_rectangle4))
        self.play(ReplacementTransform(update,delete))
        old_position5 = cursor4.get_center()
        for anim in cursor4.blinking_on():
            self.play(anim)
        for anim in cursor4.write_text("DELETE FROM Books",t2c={'DELETE':YELLOW,'FROM':YELLOW}):
            self.play(*anim)
        cursor4.next_to(old_position5,DOWN,buff=0.15)
        for anim in cursor4.write_text("WHERE Title = 'The Great Gatsby';",t2c={'WHERE':YELLOW}):
            self.play(*anim)
        prompt5 = TerminalPrompt("postgres>",color=PINK).next_to(prompt4,DOWN*2,buff=0.2)
        cursor5 = BlinkingCursor().next_to(prompt5)
        self.play(FadeOut(cursor4),FadeIn(prompt5), FadeIn(cursor5), run_time=0.5)
        self.play(FadeOut(table3,table2))
        
        
        
        
        
        
        alter = Text("ALTER values in a Table", font=font_to_use).scale(0.6).next_to(title,DOWN).shift(LEFT*2.9)
        alter.set_stroke(color=BLACK,opacity=1)
        highlighting_rectangle5 = Rectangle(width=5,height=0.28).move_to(alter.get_center()+[0,-0.15,0])
        highlighting_rectangle5.set_fill(color="#1be7ff", opacity=.5)
        highlighting_rectangle5.set_stroke(color=None, opacity=0)
        alter.set_z_index(highlighting_rectangle5.z_index+1)
        self.play(ReplacementTransform(highlighting_rectangle4,highlighting_rectangle5))
        self.play(ReplacementTransform(delete,alter))
        old_position6 = cursor5.get_center()
        for anim in cursor5.blinking_on():
            self.play(anim)
        for anim in cursor5.write_text("ALTER TABLE Books",t2c={'ALTER':YELLOW,'TABLE':YELLOW}):
            self.play(*anim)
        cursor5.next_to(old_position6,DOWN,buff=0.15)
        for anim in cursor5.write_text("ADD COLUMN DateAdded DATE;",t2c={'ADD':YELLOW,'COLUMN':YELLOW,'DATE':YELLOW}):
            self.play(*anim)
        prompt6 = TerminalPrompt("postgres>",color=PINK).next_to(prompt5,DOWN*2,buff=0.2)
        cursor6 = BlinkingCursor().next_to(prompt6)
        self.play(FadeOut(cursor5),FadeIn(prompt6), FadeIn(cursor6), run_time=0.5)
        self.wait(1)
        self.play(FadeIn(cell5))
        
        
        
        
        
        
        insert2 = Text("ALTER values with a Date", font=font_to_use).scale(0.6).next_to(title,DOWN).shift(LEFT*2.9)
        insert2.set_stroke(color=BLACK,opacity=1)
        highlighting_rectangle6 = Rectangle(width=5,height=0.28).move_to(insert2.get_center()+[0,-0.15,0])
        highlighting_rectangle6.set_fill(color="#1be7ff", opacity=.5)
        highlighting_rectangle6.set_stroke(color=None, opacity=0)
        insert2.set_z_index(highlighting_rectangle6.z_index+1)
        self.play(ReplacementTransform(highlighting_rectangle5,highlighting_rectangle6))
        self.play(ReplacementTransform(alter,insert2))
        old_position7 = cursor6.get_center()
        for anim in cursor6.blinking_on():
            self.play(anim)
        for anim in cursor6.write_text("INSERT INTO Books (Title, Author, PYear,",t2c={'INSERT':YELLOW,'INTO':YELLOW}):
            self.play(*anim)
        cursor6.next_to(old_position7,DOWN,buff=0.15)
        old_position8 = cursor6.get_center()
        for anim in cursor6.write_text("Genre, DateAdded) VALUES ('The Great ",t2c={'VALUES':YELLOW}):
            self.play(*anim)
        cursor6.next_to(old_position8,DOWN,buff=0.15)
        old_position9 = cursor6.get_center()
        for anim in cursor6.write_text("Gatsby','F. Scott Fitzgerald', 1926, 'Fiction'"):
            self.play(*anim)
        cursor6.next_to(old_position9,DOWN,buff=0.15)
        for anim in cursor6.write_text("2023-11-06');"):
            self.play(*anim)
        table4 = Table([["Title", "Author", "PYear", "Genre", "DateAdded"],
                        ["The Great Gatsby", "F. Scott Fitzgerald", "1926", "Fiction","2023-11-06"]],line_config={'color': WHITE},include_outer_lines=True).scale(0.25).next_to(table1,DOWN*2)
        
        prompt7 = TerminalPrompt("postgres>",color=PINK).next_to(prompt6,DOWN*4,buff=0.2)
        cursor7 = BlinkingCursor().next_to(prompt7)
        self.play(FadeOut(cursor6),FadeIn(prompt7), FadeIn(cursor7), run_time=0.5)
        self.play(ReplacementTransform(table1.copy(),table4))
        self.wait(5)