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
    def write_text(self,text,color):
        text = Text(text,color=color).scale(0.3).next_to(self.get_cursor(),RIGHT,buff=0.05,aligned_edge=LEFT)
        anims = []
        for letter in text :
            if not letter == "*":
                anims.append((AnimationGroup(Write(letter),run_time=0.1),AnimationGroup(self.get_cursor().animate(run_time=0.1).next_to(letter, buff=0, aligned_edge=DOWN))))
            elif letter == "*":
                anims.append((AnimationGroup(Write(letter),run_time=0.1),AnimationGroup(self.get_cursor().animate(run_time=0.1).next_to(letter, buff=0, aligned_edge=UP))))
        return anims
class TerminalPrompt(VMobject):
    def __init__(self,directory="~", *args, **kwargs):
        self.directory = directory
        self.terminal_prompt_text =  Text(self.directory).scale(0.4)
        self.terminal_prompt_frame = SurroundingRectangle(self.terminal_prompt_text, buff=0.05)
        self.terminal_prompt_frame.set_stroke(width=2,opacity=1)
        self.terminal_prompt_frame.set_fill("#32a871",opacity=1)
        self.terminal_prompt_text.move_to(self.terminal_prompt_frame.get_center())
        self.terminal_prompt = VGroup(self.terminal_prompt_frame,
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
class SqlTutorial(Scene):
    def construct(self):
        font_to_use = "resources/Quicksand-VariableFont_wght.ttf"
        sql_image = ImageMobject('resources/image (1).png')
        gear_image = ImageMobject('resources/image (2).png').scale(0.7).next_to(sql_image.get_end()-[1.4,-0.72,0],buff=0)
        gear_image.set_z_index(sql_image.z_index)
        sql_logo = Group(sql_image,gear_image).move_to([-4,3,0]).scale(0.2)
        self.play(FadeIn(sql_logo))
        always_rotate(gear_image, rate=60*DEGREES)
        title = Text("Understanding SELECT Queries in SQL", font=font_to_use).scale(0.6).next_to(sql_logo,RIGHT*3)
        self.play(DrawBorderThenFill(title))
        self.wait(1)
        self.play(FadeToColor(title[13:19],YELLOW))
        self.wait(1)
        table1 = Table(
        [["Employee ID", "Name", "Department", "Salary"],
        ["1001", "John Smith", "Marketing", "€40,000"],
        ["1002", "Emily Johnson", "Sales", "€42,000"],
        ["1003", "Micheal Patel", "IT", "€45,000"],
        ["1004", "Sarah Davies", "Human Resources", "€40,500"],
        ["1005", "Christopher", "Operations", "€41,000"],
        ["1006", "Ben Stepson", "IT", "€39,000"]
        ],include_outer_lines=True,line_config={"color": YELLOW}).move_to([-3.4,0,0]).scale(0.3)
        terminal = Terminal().move_to([3.3,-0.5,0])
        prompt1 = TerminalPrompt("~").move_to([0.5,1.6,0])
        cursor1 = BlinkingCursor().next_to(prompt1)
        self.play(FadeIn(terminal), FadeIn(prompt1), FadeIn(cursor1), run_time=0.5)
        for anim in cursor1.blinking_on():
            self.play(anim)
        for anim in cursor1.write_text('SELECT * FROM Employees;',YELLOW):
            self.play(*anim)
        for anim in cursor1.blinking_on():
            self.play(anim)
        prompt2 = TerminalPrompt("~").next_to(prompt1,DOWN,buff=0.1)
        cursor2 = BlinkingCursor().next_to(prompt2)
        self.play(FadeOut(cursor1),FadeIn(prompt2), FadeIn(cursor2), run_time=0.5)
        self.play(GrowFromPoint(table1,prompt1.get_center()+RIGHT*2), run_time=2)
        for anim in cursor2.blinking_on():
            self.play(anim)
        self.play(table1.animate.scale(0.7).shift(UP))
        for anim in cursor2.write_text('SELECT Name,Department FROM Employees;',"#b7eb34"):
            self.play(*anim)
        for anim in cursor2.blinking_on():
            self.play(anim)
        table2 = Table([["Name", "Department"],
                        ["John Smith","Marketing"],
                        ["Emily Johnson","Sales"],
                        ["Micheal Patel","IT"],
                        ["Sarah Davies","Human Resources"],
                        ["Christopher","Operations"],
                        ["Ben Stepson", "IT"]],line_config={"color": "#b7eb34"},include_outer_lines=True).scale(0.2).next_to(table1, DOWN//2)
        prompt3 = TerminalPrompt("~").next_to(prompt2,DOWN,buff=0.1)
        cursor3 = BlinkingCursor().next_to(prompt3)
        self.play(FadeOut(cursor2),FadeIn(prompt3), FadeIn(cursor3), run_time=0.5)
        self.play(GrowFromPoint(table2,table1.get_columns()[1:2]))
        for anim in cursor3.blinking_on():
            self.play(anim)
        self.play(FadeOut(table2))
        for anim in cursor3.write_text('SELECT Department FROM Employees;',"#34eb99"):
            self.play(*anim)
        for anim in cursor3.blinking_on():
            self.play(anim)
        table3 = Table([["Department"],
        ["Marketing"],
        ["Sales"],
        ["IT"],
        ["Human Resources"],
        ["Operations"],
        ["IT"]
        ],line_config={'color': '#34eb99'},include_outer_lines=True).scale(0.2).next_to(table1,DOWN)
        prompt4 = TerminalPrompt("~").next_to(prompt3,DOWN,buff=0.1)
        cursor4 = BlinkingCursor().next_to(prompt4)
        self.play(FadeOut(cursor3),FadeIn(prompt4), FadeIn(cursor4), run_time=0.5)
        self.play(GrowFromPoint(table3,table1.get_columns()[2]))
        for anim in cursor4.blinking_on():
            self.play(anim)
        for anim in cursor4.write_text('SELECT DISTINCT Department FROM Employees;',"#fc4903"):
            self.play(*anim)
        for anim in cursor4.blinking_on():
            self.play(anim)
        table4 = Table([["Department"],
        ["Marketing"],
        ["Sales"],
        ["IT"],
        ["Human Resources"],
        ["Operations"],
       ],line_config={'color':"#fc4903"},include_outer_lines=True).scale(0.2).next_to(table3)
        prompt5 = TerminalPrompt("~").next_to(prompt4,DOWN,buff=0.1)
        cursor5 = BlinkingCursor().next_to(prompt5)
        old_position1 = cursor5.get_center()
        self.play(FadeOut(cursor4),FadeIn(prompt5), FadeIn(cursor5), run_time=0.5)
        self.play(Transform(table3,table4))
        for anim in cursor5.blinking_on():
            self.play(anim)
        for anim in cursor5.write_text('SELECT Name,Salary FROM Employees ORDER BY',"#eb34c3"):
            self.play(*anim)
        cursor5.next_to(old_position1,DOWN, buff=0.1)
        for anim in cursor5.write_text("Salary DESC;","#eb34c3"):
            self.play(*anim)
        self.play(FadeOut(table3), FadeOut(table4))
        for anim in cursor5.blinking_on():
            self.play(anim)
        table5 = Table([["Name", "Salary"],
                        ["Micheal Patel", "€45,000"],
                        ["Emily Johnson", "€42,000"],
                        ["Christopher", "€41,000"],
                       ["Sarah Davies","€40,500"],
                       ["John Smith", "€40,000"],
                       ["Ben Stepson", "€39,000"]],line_config={'color': "#eb34c3"},include_outer_lines=True).scale(0.2).next_to(table1,DOWN)
        prompt6 = TerminalPrompt("~").next_to(prompt5,DOWN*2,buff=0.2)
        cursor6 = BlinkingCursor().next_to(prompt6)
        self.play(FadeOut(cursor5),FadeIn(prompt6), FadeIn(cursor6), run_time=0.5)
        self.play(GrowFromPoint(table5,table1.get_columns()[1:]))
        for anim in cursor6.blinking_on():
            self.play(anim)
        for anim in cursor6.write_text('SELECT * FROM Employees LIMIT 2;',"#a3f7c3"):
            self.play(*anim)
        self.play(FadeOut(table5))
        for anim in cursor6.blinking_on():
            self.play(anim)
        table6 = Table([["Employee ID", "Name", "Department", "Salary"],
        ["1001", "John Smith", "Marketing", "€40,000"],
        ["1002", "Emily Johnson", "Sales", "€42,000"]],line_config={"color": "#a3f7c3"},include_outer_lines=True).scale(0.2).next_to(table1,DOWN)
        prompt7 = TerminalPrompt("~").next_to(prompt6,DOWN,buff=0.1)
        cursor7 = BlinkingCursor().next_to(prompt7)
        old_position2 = cursor7.get_center()
        self.play(FadeOut(cursor6),FadeIn(prompt7), FadeIn(cursor7), run_time=0.5)
        self.play(GrowFromPoint(table6,table1.get_rows()[:2]))
        for anim in cursor7.blinking_on():
            self.play(anim)
        for anim in cursor7.write_text('SELECT Name FROM Employees WHERE ',"#f21137"):
            self.play(*anim)
        cursor7.next_to(old_position2,DOWN,buff=0.1)
        for anim in cursor7.write_text("Department = 'IT';","#f21137"):
            self.play(*anim)
        self.play(FadeOut(table6))
        for anim in cursor7.blinking_on():
            self.play(anim)
        table7 = Table([["Name"],
                        ["Micheal Patel"],
                        ["Ben Stepson"]],line_config={'color': "#f21137"},include_outer_lines=True).scale(0.2).next_to(table1,DOWN)
        prompt8 = TerminalPrompt("~").next_to(prompt7,DOWN*2,buff=0.2)
        cursor8 = BlinkingCursor().next_to(prompt8)
        self.play(FadeOut(cursor7),FadeIn(prompt8), FadeIn(cursor8), run_time=0.5)
        self.play(GrowFromPoint(table7,table1.get_columns()[:]))
        for anim in cursor8.blinking_on():
            self.play(anim)
        self.wait(2)