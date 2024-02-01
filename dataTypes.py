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
        self.wait(2)
        data_types_text = Text("Data types are like labels that tell a computer what kind of data it's dealing with such\nas numbers, text, or dates so it knows how to store, process, and use it correctly, ensuring \nthat numbers don't get mixed up with words and dates are handled appropriately.", font=font_to_use,line_spacing=1).scale(0.4).next_to([-6,1,0],aligned_edge=LEFT)
        self.play(Write(data_types_text))
        self.wait(2)
        abacus = ImageMobject('resources/abacus (2).png').scale(0.4).move_to([-4.9,-0.8,0])
        numeric_type = Text("Numeric", font=font_to_use,color=BLUE).scale(0.4).rotate(90*DEGREES).next_to(abacus,LEFT)
        self.play(FadeIn(abacus,numeric_type))
        dot1 = Dot(radius=0.05, color=YELLOW).next_to(abacus,DOWN,aligned_edge=LEFT)
        self.play(FadeIn(dot1))
        example1 = Text("integer",font=font_to_use).scale(0.4).next_to(dot1)
        self.play(FadeIn(example1))
        dot2 = Dot(radius=0.05, color=YELLOW).next_to(dot1,DOWN)
        self.play(FadeIn(dot2))
        example2 = Text("float",font=font_to_use).scale(0.4).next_to(dot2)
        self.play(FadeIn(example2))
        textual = ImageMobject('resources/keyboard.png').scale(0.45).next_to(abacus,RIGHT*4)
        textual_type = Text("Textual", font=font_to_use,color=BLUE).scale(0.4).rotate(90*DEGREES).next_to(textual,LEFT)
        self.play(FadeIn(textual_type,textual))
        dot3 = Dot(radius=0.05, color=YELLOW).next_to(dot1,RIGHT*10)
        self.play(FadeIn(dot3))
        example3 = Text("char",font=font_to_use).scale(0.4).next_to(dot3)
        self.play(FadeIn(example3))
        dot4 = Dot(radius=0.05, color=YELLOW).next_to(dot3,DOWN)
        self.play(FadeIn(dot4))
        example4 = Text("varchar",font=font_to_use).scale(0.4).next_to(dot4)
        self.play(FadeIn(example4))
        dot5 = Dot(radius=0.05, color=YELLOW).next_to(dot4,DOWN)
        self.play(FadeIn(dot5))
        example5 = Text("text",font=font_to_use).scale(0.4).next_to(dot5)
        self.play(FadeIn(example5))
        boolean = ImageMobject('resources/boolean.png').scale(0.3).next_to(textual,RIGHT*5)
        boolean_type = Text("Boolean", font=font_to_use,color=BLUE).scale(0.4).rotate(90*DEGREES).next_to(boolean,LEFT)
        self.play(FadeIn(boolean_type,boolean))
        dot6 = Dot(radius=0.05, color=YELLOW).next_to(dot3,RIGHT*10)
        self.play(FadeIn(dot6))
        example6 = Text("true",font=font_to_use).scale(0.4).next_to(dot6)
        self.play(FadeIn(example6))
        dot7 = Dot(radius=0.05, color=YELLOW).next_to(dot6,DOWN)
        self.play(FadeIn(dot7))
        example7 = Text("false",font=font_to_use).scale(0.4).next_to(dot7)
        self.play(FadeIn(example7))
        date_time = ImageMobject('resources/calendar.png').scale(0.35).next_to(boolean,RIGHT*5)
        date_time_type = Text("Date and Time", font=font_to_use,color=BLUE).scale(0.4).rotate(90*DEGREES).next_to(date_time,LEFT)
        self.play(FadeIn(date_time_type,date_time))
        dot8 = Dot(radius=0.05, color=YELLOW).next_to(dot6,RIGHT*10)
        self.play(FadeIn(dot8))
        example8 = Text("date",font=font_to_use).scale(0.4).next_to(dot8)
        self.play(FadeIn(example8))
        dot9 = Dot(radius=0.05, color=YELLOW).next_to(dot8,DOWN)
        self.play(FadeIn(dot9))
        example9 = Text("time",font=font_to_use).scale(0.4).next_to(dot9)
        self.play(FadeIn(example9))
        dot10 = Dot(radius=0.05, color=YELLOW).next_to(dot9,DOWN)
        self.play(FadeIn(dot10))
        example10 = Text("timestamp",font=font_to_use).scale(0.4).next_to(dot10)
        self.play(FadeIn(example10))
        dot11 = Dot(radius=0.05, color=YELLOW).next_to(dot10,DOWN)
        self.play(FadeIn(dot11))
        example11 = Text("interval",font=font_to_use).scale(0.4).next_to(dot11)
        self.play(FadeIn(example11))
        other_types = ImageMobject('resources/postgresql.png').scale(0.35).next_to(date_time,RIGHT*5)
        other_types_type = Text("Other Types", font=font_to_use,color=BLUE).scale(0.4).rotate(90*DEGREES).next_to(other_types,LEFT)
        self.play(FadeIn(other_types_type,other_types))
        dot12 = Dot(radius=0.05, color=YELLOW).next_to(dot8,RIGHT*7)
        self.play(FadeIn(dot12))
        example12 = Text("For everything else,\nPostgreSQL has a \nrange of specific \ntypes for handling \nvaried data",line_spacing=1,font=font_to_use).scale(0.4).next_to([4,-2.7,0],aligned_edge=LEFT)
        self.play(FadeIn(example12))
        self.wait(5)
        self.play(FadeOut(data_types_text,abacus,numeric_type,dot1,example1,dot2,example2,textual,textual_type,dot3,example3,dot4,example4,dot5,example5,
                          boolean,boolean_type,dot6,example6,dot7,example7,date_time,date_time_type,dot8,example8,dot9,example9,
                          dot10,example10,dot11,example11,other_types,other_types_type,dot12,example12))
        
        
        
        
        
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
        text1 = Text("CREATE TABLE Books ( Title TEXT,",t2c={'CREATE':YELLOW,'TABLE':YELLOW, 'TEXT':YELLOW},font=font_to_use)
        for anim in cursor1.write_text(text1):
            self.play(*anim)
        cursor1.next_to(old_position1,DOWN,buff=0.15)
        text2 = Text("Author TEXT, PYear INT, Genre TEXT );",t2c={'TEXT':YELLOW,'INT':YELLOW},font=font_to_use)
        for anim in cursor1.write_text(text2):
            self.play(*anim)
        table1 = Table([["Title", "Author", "PYear", "Genre", "DateAdded"],
                        ['The Great Gatsby', 'F. Scott Fitzgerald', '1926', 'Fiction','2023-11-06']],line_config={'color': WHITE},include_outer_lines=True).scale(0.25).move_to([-3.5,0,0])
        cell5 = VGroup(table1.get_cell((1,5),color=WHITE),table1.get_entries((1,5)))
        cell6 = VGroup(table1.get_cell((2,5),color=WHITE),table1.get_entries((2,5)))
        row2 = VGroup(table1.get_cell((2,1),color=WHITE),table1.get_entries((2,1)),
                      table1.get_cell((2,2),color=WHITE),table1.get_entries((2,2)),
                      table1.get_cell((2,3),color=WHITE),table1.get_entries((2,3)),
                      table1.get_cell((2,4),color=WHITE),table1.get_entries((2,4))
                      )
        
        table1 = VGroup(table1.get_cell((1,1),color=WHITE),table1.get_entries((1,1)),
                        table1.get_cell((1,2),color=WHITE),table1.get_entries((1,2)),
                        table1.get_cell((1,3),color=WHITE),table1.get_entries((1,3)),
                        table1.get_cell((1,4),color=WHITE),table1.get_entries((1,4)))
        
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
        text3 = Text("INSERT INTO Books (Title, Author, PYear,",t2c={'INSERT':YELLOW,'INTO':YELLOW},font=font_to_use)
        for anim in cursor2.write_text(text3):
            self.play(*anim)
        cursor2.next_to(old_position2,DOWN,buff=0.15)
        text4 = Text("Genre) VALUES ('The Great Gatsby',",t2c={'VALUES':YELLOW},font=font_to_use)
        old_position3 = cursor2.get_center()
        for anim in cursor2.write_text(text4):
            self.play(*anim)
        cursor2.next_to(old_position3,DOWN,buff=0.15)
        text5 = Text("'F. Scott Fitzgerald', 1926, 'Fiction');",font=font_to_use)
        for anim in cursor2.write_text(text5):
            self.play(*anim)
       
        prompt3 = TerminalPrompt("postgres>",color=PINK).next_to(prompt2,DOWN*3,buff=0.2)
        cursor3 = BlinkingCursor().next_to(prompt3)
        self.play(FadeOut(cursor2),FadeIn(prompt3), FadeIn(cursor3), run_time=0.5)
        self.play(FadeIn(row2))
        
        
        
        
        
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
        text6 = Text("UPDATE Books SET PYear = 1925",t2c={'UPDATE':YELLOW,'SET':YELLOW}, font=font_to_use)
        for anim in cursor3.write_text(text6):
            self.play(*anim)
        cursor3.next_to(old_position4,DOWN,buff=0.15)
        text7 = Text("WHERE Title = 'The Great Gatsby';",t2c={'WHERE':YELLOW}, font=font_to_use)
        for anim in cursor3.write_text(text7):
            self.play(*anim)
            
       
        
        prompt4 = TerminalPrompt("postgres>",color=PINK).next_to(prompt3,DOWN*2,buff=0.2)
        cursor4 = BlinkingCursor().next_to(prompt4)
        self.play(FadeOut(cursor3),FadeIn(prompt4), FadeIn(cursor4), run_time=0.5)
        replacement_text = Text("1925",color=YELLOW)
        self.play(Transform(row2[5], replacement_text.scale(0.28).move_to(row2[5])))
        
        
        
        
        
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
        text8 = Text("DELETE FROM Books",t2c={'DELETE':YELLOW,'FROM':YELLOW},font=font_to_use)
        for anim in cursor4.write_text(text8):
            self.play(*anim)
        cursor4.next_to(old_position5,DOWN,buff=0.15)
        text9 = Text("WHERE Title = 'The Great Gatsby';",t2c={'WHERE':YELLOW}, font=font_to_use)
        for anim in cursor4.write_text(text9):
            self.play(*anim)
        prompt5 = TerminalPrompt("postgres>",color=PINK).next_to(prompt4,DOWN*2,buff=0.2)
        cursor5 = BlinkingCursor().next_to(prompt5)
        self.play(FadeOut(cursor4),FadeIn(prompt5), FadeIn(cursor5), run_time=0.5)
        self.play(FadeOut(row2))
        
        
        
        
        
        
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
        text10 = Text("ALTER TABLE Books",t2c={'ALTER':YELLOW,'TABLE':YELLOW}, font=font_to_use)
        for anim in cursor5.write_text(text10):
            self.play(*anim)
        cursor5.next_to(old_position6,DOWN,buff=0.15)
        text11 = Text("ADD COLUMN DateAdded DATE;",t2c={'ADD':YELLOW,'COLUMN':YELLOW,'DATE':YELLOW},font=font_to_use)
        for anim in cursor5.write_text(text11):
            self.play(*anim)
        prompt6 = TerminalPrompt("postgres>",color=PINK).next_to(prompt5,DOWN*2,buff=0.2)
        cursor6 = BlinkingCursor().next_to(prompt6)
        self.play(FadeOut(cursor5),FadeIn(prompt6), FadeIn(cursor6), run_time=0.5)
        self.wait(1)
        self.play(FadeIn(cell5))
        self.play(FadeToColor(cell5,YELLOW))
        
        
        
        
        
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
        text12 = Text("INSERT INTO Books (Title, Author, PYear,",t2c={'INSERT':YELLOW,'INTO':YELLOW}, font=font_to_use)
        for anim in cursor6.write_text(text12):
            self.play(*anim)
        cursor6.next_to(old_position7,DOWN,buff=0.15)
        old_position8 = cursor6.get_center()
        text13 = Text("Genre, DateAdded) VALUES ('The Great ",t2c={'VALUES':YELLOW}, font=font_to_use)
        for anim in cursor6.write_text(text13):
            self.play(*anim)
        cursor6.next_to(old_position8,DOWN,buff=0.15)
        old_position9 = cursor6.get_center()
        text14 = Text("Gatsby','F. Scott Fitzgerald', 1925, 'Fiction'", font=font_to_use)
        for anim in cursor6.write_text(text14):
            self.play(*anim)
        cursor6.next_to(old_position9,DOWN,buff=0.15)
        text15 = Text("2023-11-06');", font=font_to_use)
        for anim in cursor6.write_text(text15):
            self.play(*anim)
        
        prompt7 = TerminalPrompt("postgres>",color=PINK).next_to(prompt6,DOWN*4,buff=0.2)
        cursor7 = BlinkingCursor().next_to(prompt7)
        self.play(FadeOut(cursor6),FadeIn(prompt7), FadeIn(cursor7), run_time=0.5)
        cell6.set_z_index(10)
        row2[5].set_color(WHITE)
        self.play(FadeIn(cell6.set_color(YELLOW), row2))
        
        
        
        
        
        indexing = Text("Creating an Index", font=font_to_use).scale(0.6).next_to(title,DOWN).shift(LEFT*2.1)
        indexing.set_stroke(color=BLACK,opacity=1)
        highlighting_rectangle7 = Rectangle(width=3.5,height=0.28).move_to(indexing.get_center()+[0,-0.15,0])
        highlighting_rectangle7.set_fill(color="#1be7ff", opacity=.5)
        highlighting_rectangle7.set_stroke(color=None, opacity=0)
        indexing.set_z_index(highlighting_rectangle7.z_index+1)
        self.play(ReplacementTransform(highlighting_rectangle6,highlighting_rectangle7))
        self.play(ReplacementTransform(insert2,indexing))
        old_position10 = cursor7.get_center()
        for anim in cursor7.blinking_on():
            self.play(anim)
        text16 = Text("CREATE INDEX author_index",t2c={'CREATE':YELLOW,'INDEX':YELLOW}, font=font_to_use)
        for anim in cursor7.write_text(text16):
            self.play(*anim)
        cursor7.next_to(old_position10,DOWN,buff=0.15)
        text17 = Text("ON Books(Author);",t2c={'ON':YELLOW},font=font_to_use)
        for anim in cursor7.write_text(text17):
            self.play(*anim)
        prompt8 = TerminalPrompt("postgres>",color=PINK).next_to(prompt7,DOWN*2,buff=0.2)
        cursor8 = BlinkingCursor().next_to(prompt8)
        self.play(FadeOut(cursor7),FadeIn(prompt8), FadeIn(cursor8), run_time=0.5)
        self.wait(1)
        # check_index = Text("SELECT indexname,indexdef\nFROM\npg_indexes\nWHERE\ntablename='Books';", font=font_to_use,line_spacing=1,t2c={'SELECT':YELLOW, 'FROM':YELLOW, 'WHERE':YELLOW, 'Books':PURE_GREEN}).scale(0.4).next_to(table1,DOWN*2,aligned_edge=LEFT).shift(RIGHT*2)
        # self.play(FadeIn(check_index))
        # self.wait(4)
        table5 = Table([['indexname', 'indexdef'],
                        ['author_index', 'Create UNIQUE INDEX author_index ON\nLibrary.Books USING btree (book_id)']],line_config={'color': WHITE},include_outer_lines=True).scale(0.25).next_to(table1,DOWN*5, aligned_edge=LEFT)
        self.play(FadeIn(table5))
        self.wait(5)
        self.play(FadeOut(table5))
        
        
        drop = Text("DROP a Table", font=font_to_use).scale(0.6).next_to(title,DOWN).shift(LEFT*2.1)
        drop.set_stroke(color=BLACK,opacity=1)
        highlighting_rectangle8 = Rectangle(width=3.2,height=0.28).move_to(drop.get_center()+[0,-0.15,0])
        highlighting_rectangle8.set_fill(color="#1be7ff", opacity=.5)
        highlighting_rectangle8.set_stroke(color=None, opacity=0)
        drop.set_z_index(highlighting_rectangle8.z_index+1)
        self.play(ReplacementTransform(highlighting_rectangle7,highlighting_rectangle8))
        self.play(ReplacementTransform(indexing, drop))
        for anim in cursor8.blinking_on():
            self.play(anim)
        text18 = Text("DROP TABLE Books;",t2c={'DROP':YELLOW,'TABLE':YELLOW}, font=font_to_use)
        for anim in cursor8.write_text(text18):
            self.play(*anim)
        self.play(FadeOut(table1,cell5,cell6,row2))
        self.wait(2)
        self.play(FadeOut(terminal,prompt1,prompt2,prompt3,prompt4,prompt5,prompt6,prompt7,prompt8,
                          cursor8,
                          text1,text2,text3,text4,text5,text6,text7,text8,text9,text10,text11,
                          text12,text13,text14,text15,text16,text17,text18))
        self.wait(1)
        
        
        constraints = Text("Constraints", font=font_to_use).scale(0.6).next_to(title,DOWN)
        constraints.set_stroke(color=BLACK,opacity=1)
        highlighting_rectangle9 = Rectangle(width=2.5,height=0.28).move_to(constraints.get_center()+[0,-0.15,0])
        highlighting_rectangle9.set_fill(color="#1be7ff", opacity=.5)
        highlighting_rectangle9.set_stroke(color=None, opacity=0)
        constraints.set_z_index(highlighting_rectangle9.z_index+1)
        self.play(ReplacementTransform(highlighting_rectangle8,highlighting_rectangle9))
        self.play(ReplacementTransform(drop,constraints))
        
        constraints_def = Table([["NOT NULL", "Ensures that a column can't have a NULL value. Like making sure every apple has a \ncolor."],
                                   ["UNIQUE", "Ensures that all values in a column are different. Like making sure every apple has a \nunique ID."],
                                   ["PRIMARY KEY", "A special kind of UNIQUE constraint. Each table can have one primary key. It's like the\nmain ID for each apple."],
                                   ["FOREIGN KEY", "Allows you to link two tables together. Like if you have an apple, and you want to know\nwhich tree it came from."],
                                   ["CHECK", "Lets you add custom data validation. Like making sure no apple weighs less than zero \ngrams."],
                                   ],line_config={'color': ORANGE},include_outer_lines=True,arrange_in_grid_config={"cell_alignment": LEFT}).scale(0.3).next_to(title,DOWN*3.5)
        # constraints_def.get_vertical_lines()[1].set_opacity(0)
        constraints_def.get_entries((1,1)).set_color(YELLOW)
        constraints_def.get_entries((2,1)).set_color(YELLOW)
        constraints_def.get_entries((3,1)).set_color(YELLOW)
        constraints_def.get_entries((4,1)).set_color(YELLOW)
        constraints_def.get_entries((5,1)).set_color(YELLOW)
        constraints_examples = Table([["NOT NULL", "CREATE TABLE Books ( Title TEXT, Author TEXT, Year INT, Genre TEXT );"],
                                      ["UNIQUE", "CREATE TABLE Apples (ID INT UNIQUE);"],
                                      ["PRIMARY KEY", "CREATE TABLE Apples (ID INT PRIMARY KEY);"],
                                      ["FOREIGN KEY", "CREATE TABLE Apples (TreeID INT, FOREIGN KEY (TreeID) REFERENCES Trees(ID));"],
                                      ["CHECK", "CREATE TABLE Apples (Weight INT CHECK (Weight > 0));"]]
                                     ,line_config={'color': ORANGE},include_outer_lines=True,arrange_in_grid_config={"cell_alignment": LEFT}).scale(0.3).next_to(constraints_def,DOWN)
        # constraints_examples.get_vertical_lines()[1].set_opacity(0)
        # constraints_examples.get_vertical_lines()[1].set_opacity(0)
        constraints_examples.get_entries((1,1)).set_color(YELLOW)
        constraints_examples.get_entries((2,1)).set_color(YELLOW)
        constraints_examples.get_entries((3,1)).set_color(YELLOW)
        constraints_examples.get_entries((4,1)).set_color(YELLOW)
        constraints_examples.get_entries((5,1)).set_color(YELLOW)
        constraints_examples.get_entries((1,2))[0][:11].set_color(PURE_GREEN)
        constraints_examples.get_entries((1,2))[0][22:26].set_color(PURE_GREEN)
        constraints_examples.get_entries((1,2))[0][33:37].set_color(PURE_GREEN)
        constraints_examples.get_entries((1,2))[0][42:45].set_color(PURE_GREEN)
        constraints_examples.get_entries((1,2))[0][51:55].set_color(PURE_GREEN)
        constraints_examples.get_entries((2,2))[0][:11].set_color(PURE_GREEN)
        constraints_examples.get_entries((2,2))[0][20:29].set_color(PURE_GREEN)
        constraints_examples.get_entries((3,2))[0][:11].set_color(PURE_GREEN)
        constraints_examples.get_entries((3,2))[0][20:33].set_color(PURE_GREEN)
        constraints_examples.get_entries((4,2))[0][:11].set_color(PURE_GREEN)
        constraints_examples.get_entries((4,2))[0][24:27].set_color(PURE_GREEN)
        constraints_examples.get_entries((4,2))[0][28:38].set_color(PURE_GREEN)
        constraints_examples.get_entries((4,2))[0][46:56].set_color(PURE_GREEN)
        constraints_examples.get_entries((5,2))[0][:11].set_color(PURE_GREEN)
        constraints_examples.get_entries((5,2))[0][24:32].set_color(PURE_GREEN) 
        self.wait(1)
        self.play(FadeIn(constraints_def))
        self.wait(5)
        self.play(FadeIn(constraints_examples))
        self.wait(30)