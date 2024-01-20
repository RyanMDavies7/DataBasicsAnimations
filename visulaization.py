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
class VISUALIZATION(Scene):
    def construct(self):
        font_to_use = "resources/Quicksand-VariableFont_wght.ttf"
        sql_image = ImageMobject('resources/image (1).png')
        gear_image = ImageMobject('resources/image (2).png').scale(0.7).next_to(sql_image.get_end()-[1.4,-0.72,0],buff=0)
        gear_image.set_z_index(sql_image.z_index)
        sql_logo = Group(sql_image,gear_image).move_to([-4,3,0]).scale(0.2)
        self.play(FadeIn(sql_logo))
        always_rotate(gear_image, rate=60*DEGREES)
        title = Text("Introduction to Calculations in SQL", font=font_to_use).scale(0.6).next_to(sql_logo,RIGHT*3)
        self.play(DrawBorderThenFill(title))
        self.wait(2)
        calculations_text = Text("Calculations in SQL let you do\nmath operations on your data",font=font_to_use,line_spacing=1).scale(0.4).next_to(sql_logo,DOWN*3,aligned_edge=LEFT)
        self.play(Write(calculations_text))
        plus = ImageMobject('resources/plus.png').scale(0.2).next_to(calculations_text,DOWN*8+LEFT)
        plus_arrow = Arrow(calculations_text.get_center()+[-1,-0.5,0],plus,tip_length=0.2,color=PURE_GREEN)
        self.play(GrowArrow(plus_arrow))
        self.play(FadeIn(plus))
        minus = ImageMobject('resources/minus.png').scale(0.2).next_to(plus,DOWN*3+RIGHT)
        minus_arrow = Arrow(calculations_text.get_center()+[-0.5,-0.5,0],minus.get_top(),tip_length=0.2,color=PURE_RED)
        self.play(GrowArrow(minus_arrow))
        self.play(FadeIn(minus))
        multiply = ImageMobject('resources/cancel.png').scale(0.2).next_to(minus,UP+RIGHT*4)
        multiply_arrow = Arrow(calculations_text.get_center()+[0,-0.5,0],multiply.get_top(),tip_length=0.2,color=YELLOW)
        self.play(GrowArrow(multiply_arrow))
        self.play(FadeIn(multiply))
        divide = ImageMobject('resources/divide.png').scale(0.2).next_to(multiply,UP+RIGHT*3)
        divide_arrow = Arrow(calculations_text.get_center()+[0.5,-0.5,0],divide.get_top(),tip_length=0.2,color=PURE_BLUE)
        self.play(GrowArrow(divide_arrow))
        self.play(FadeIn(divide))
        self.wait(1)
        visualization_text = Text("Calculations can help you look at,\nunderstand, and present your data",font=font_to_use,line_spacing=1).scale(0.4).next_to(calculations_text,RIGHT*6,aligned_edge=LEFT)
        self.play(Write(visualization_text))
        ax = Axes().add_coordinates()
        curve = ax.plot(lambda x: 2 * np.sin(x), color=DARK_BLUE)
        area = ax.get_area(
            curve,
            x_range=(PI / 2, 3 * PI / 2),
            color=(GREEN_B, GREEN_D),
            opacity=1,
        )
        graph = VGroup(ax,curve,area)
        graph.scale(0.4).next_to(visualization_text,DOWN)
        self.play(Create(ax))
        self.play(Create(curve))
        self.play(Create(area))
        self.wait(3)
        
        self.play(FadeOut(visualization_text,calculations_text,graph,plus_arrow,minus_arrow,multiply_arrow,divide_arrow))
        self.play(plus.animate.scale(1.1).move_to([-5,1,0]),minus.animate.scale(1.1).move_to([-2,1,0]),
                  multiply.animate.scale(1.1).move_to([1,1,0]),divide.animate.scale(1.1).move_to([4,1,0]))
        plus_symbol = Text("+", color=YELLOW).next_to(plus,DOWN*2)
        plus_text = Text("Is the addition\noperator, used to\nadd two numbers \ntogether",font=font_to_use,line_spacing=1).scale(0.3).next_to(plus,DOWN*4)
        self.play(FadeIn(plus_symbol))
        self.play(Write(plus_text))
        minus_symbol = Text("-", color=YELLOW).scale(1.5).next_to(minus,DOWN*2)
        minus_text = Text("Is the subtraction\noperator, used to\nsubtract one \nnumber from \nanother",font=font_to_use,line_spacing=1).scale(0.3).next_to(minus,DOWN*4)
        self.play(FadeIn(minus_symbol))
        self.play(Write(minus_text))
        multiplication_symbol = Text("*", color=YELLOW).next_to(multiply,DOWN*2)
        multiplication_text = Text("Is the multiplication\noperator, used to\nmultiply two numbers \ntogether",font=font_to_use,line_spacing=1).scale(0.3).next_to(multiply,DOWN*4)
        self.play(FadeIn(multiplication_symbol))
        self.play(Write(multiplication_text))
        divide_symbol = Text("/",color=YELLOW).scale(0.8).next_to(divide,DOWN*2)
        divide_text = Text("Is the division\noperator, used to\ndivide one number \nby another",font=font_to_use,line_spacing=1).scale(0.3).next_to(divide,DOWN*4)
        self.play(FadeIn(divide_symbol))
        self.play(Write(divide_text))
        self.wait(3)
        self.play(FadeOut(plus,plus_symbol,plus_text,minus,minus_symbol,minus_text,
                          multiply,multiplication_symbol,multiplication_text,
                          divide,divide_symbol,divide_text))
        self.wait(1)
        addition_examples_heading = Text("Addition Examples",color= '#03fc88',font=font_to_use).scale(0.4).next_to(sql_logo,DOWN*2)
        dot1 = Dot(radius=0.04).next_to(addition_examples_heading,aligned_edge=DOWN)
        dot1.set_color('#03fc88')
        dot2 = Dot(radius=0.04).next_to(dot1, buff=0.2)
        dot2.set_color('#03fc88')
        dot3 = Dot(radius=0.04).next_to(dot2, buff=0.2)
        dot3.set_color('#03fc88')
        dot4 = Dot(radius=0.04).next_to(dot3, buff=0.2)
        dot4.set_color('#03fc88')
        dot5 = Dot(radius=0.04).next_to(dot4, buff=0.2)
        dot5.set_color('#03fc88')
        self.play(FadeIn(addition_examples_heading))
        fadein_anims = [FadeIn(dot1, run_time=0.5),FadeIn(dot2, run_time=0.5),FadeIn(dot3, run_time=0.5),FadeIn(dot4, run_time=0.5),FadeIn(dot5, run_time=0.5)]
        fadeout_anims = [FadeOut(dot1),FadeOut(dot2),FadeOut(dot3),FadeOut(dot4),FadeOut(dot5)]
        example_table = Table([["Number_A","Number_B"],
                               ["1","6"],
                               ["2", "7"],
                               ["3", "8"],
                               ["4", "9"],
                               ["5", "10"]],
                              include_outer_lines=True,line_config={'color':YELLOW}).scale(0.3).move_to([-3,0,0])
        self.play(Succession(*fadein_anims),Create(example_table))
        terminal = Terminal().move_to([3.3,-0.5,0])
        prompt1 = TerminalPrompt("~").move_to([0.5,1.6,0])
        cursor1 = BlinkingCursor().next_to(prompt1)
        self.play(*fadeout_anims,FadeIn(terminal), FadeIn(prompt1), FadeIn(cursor1), example_table.animate.shift(UP*0.5))
        output_console = Rectangle(height=3,width=5).next_to(example_table,DOWN)
        ouput_console_text = Text("Output :").scale(0.3).next_to(output_console,LEFT)
        self.play(Create(output_console), FadeIn(ouput_console_text))
        for anim in cursor1.blinking_on():
            self.play(anim)
        for anim in cursor1.write_text('SELECT 2+2;',"#f3b700"):
            self.play(*anim)
        for anim in cursor1.blinking_on():
            self.play(anim)
        output1 = Text("4", color="#f3b700").scale(0.5).move_to(output_console.get_center())
        prompt2 = TerminalPrompt("~").next_to(prompt1,DOWN,buff=0.1)
        cursor2 = BlinkingCursor().next_to(prompt2)
        self.play(FadeOut(cursor1),FadeIn(prompt2), FadeIn(cursor2), run_time=0.5)
        self.play(FadeIn(output1))
        self.play(ShowPassingFlash(output_console.copy().set_color('#f3b700'), time_width=100, run_time=2))
        for anim in cursor2.blinking_on():
            self.play(anim)
        self.play(FadeOut(output1))
        for anim in cursor2.write_text('SELECT Number_A + Number_B FROM Numbers;',"#b7eb34"):
            self.play(*anim)
        for anim in cursor2.blinking_on():
            self.play(anim)
        output2 = Table([["Number_A + Number_B"],
                         ["7"],
                         ["9"],
                         ["11"],
                         ["13"],
                         ["15"]],include_outer_lines=True,line_config={'color':"#b7eb34"}).scale(0.3).move_to(output_console.get_center())
        prompt3 = TerminalPrompt("~").next_to(prompt2,DOWN,buff=0.1)
        cursor3 = BlinkingCursor().next_to(prompt3)
        self.play(FadeOut(cursor2),FadeIn(prompt3), FadeIn(cursor3), run_time=0.5)
        self.play(FadeIn(output2))
        self.play(ShowPassingFlash(output_console.copy().set_color('#b7eb34'), time_width=100, run_time=2))
        for anim in cursor3.blinking_on():
            self.play(anim)
        self.play(FadeOut(output2), FadeOut(addition_examples_heading))
        subtraction_examples_heading = Text("Subtraction Examples",color= '#03fc88',font=font_to_use).scale(0.4).next_to(sql_logo,DOWN*2)
        dot1 = Dot(radius=0.04).next_to(subtraction_examples_heading,aligned_edge=DOWN)
        dot1.set_color('#03fc88')
        dot2 = Dot(radius=0.04).next_to(dot1, buff=0.2)
        dot2.set_color('#03fc88')
        dot3 = Dot(radius=0.04).next_to(dot2, buff=0.2)
        dot3.set_color('#03fc88')
        dot4 = Dot(radius=0.04).next_to(dot3, buff=0.2)
        dot4.set_color('#03fc88')
        dot5 = Dot(radius=0.04).next_to(dot4, buff=0.2)
        dot5.set_color('#03fc88')
        self.play(FadeIn(subtraction_examples_heading))
        fadein_anims = [FadeIn(dot1, run_time=0.5),FadeIn(dot2, run_time=0.5),FadeIn(dot3, run_time=0.5),FadeIn(dot4, run_time=0.5),FadeIn(dot5, run_time=0.5)]
        fadeout_anims = [FadeOut(dot1),FadeOut(dot2),FadeOut(dot3),FadeOut(dot4),FadeOut(dot5)]
        self.play(Succession(*fadein_anims))
        self.play(*fadeout_anims)
        for anim in cursor3.write_text('SELECT 2-2;',"#34eb99"):
            self.play(*anim)
        for anim in cursor3.blinking_on():
            self.play(anim)
        output3 = Text("0", color="#34eb99").scale(0.5).move_to(output_console.get_center())
        prompt4 = TerminalPrompt("~").next_to(prompt3,DOWN,buff=0.1)
        cursor4 = BlinkingCursor().next_to(prompt4)
        self.play(FadeOut(cursor3),FadeIn(prompt4), FadeIn(cursor4), run_time=0.5)
        self.play(FadeIn(output3))
        self.play(ShowPassingFlash(output_console.copy().set_color('#34eb99'), time_width=100, run_time=2))
        for anim in cursor4.blinking_on():
            self.play(anim)
        self.play(FadeOut(output3))
        for anim in cursor4.write_text('SELECT Number_B - Number_A FROM Numbers;',"#f2e86d"):
            self.play(*anim)
        for anim in cursor4.blinking_on():
            self.play(anim)
        output4 = Table([["Number_B - Number_A"],
                         ["5"],
                         ["5"],
                         ["5"],
                         ["5"],
                         ["5"]],include_outer_lines=True,line_config={'color':"#f2e86d"}).scale(0.3).move_to(output_console.get_center())
        prompt5 = TerminalPrompt("~").next_to(prompt4,DOWN,buff=0.1)
        cursor5 = BlinkingCursor().next_to(prompt5)
        self.play(FadeOut(cursor4),FadeIn(prompt5), FadeIn(cursor5), run_time=0.5)
        self.play(FadeIn(output4))
        self.play(ShowPassingFlash(output_console.copy().set_color('#f2e86d'), time_width=100, run_time=2))
        for anim in cursor5.blinking_on():
            self.play(anim)
        self.play(FadeOut(output4), FadeOut(subtraction_examples_heading))
        multiplication_examples_heading = Text("Multiplication Examples",color= '#03fc88',font=font_to_use).scale(0.4).next_to(sql_logo,DOWN*2)
        dot1 = Dot(radius=0.04).next_to(multiplication_examples_heading,aligned_edge=DOWN)
        dot1.set_color('#03fc88')
        dot2 = Dot(radius=0.04).next_to(dot1, buff=0.2)
        dot2.set_color('#03fc88')
        dot3 = Dot(radius=0.04).next_to(dot2, buff=0.2)
        dot3.set_color('#03fc88')
        dot4 = Dot(radius=0.04).next_to(dot3, buff=0.2)
        dot4.set_color('#03fc88')
        dot5 = Dot(radius=0.04).next_to(dot4, buff=0.2)
        dot5.set_color('#03fc88')
        self.play(FadeIn(multiplication_examples_heading))
        fadein_anims = [FadeIn(dot1, run_time=0.5),FadeIn(dot2, run_time=0.5),FadeIn(dot3, run_time=0.5),FadeIn(dot4, run_time=0.5),FadeIn(dot5, run_time=0.5)]
        fadeout_anims = [FadeOut(dot1),FadeOut(dot2),FadeOut(dot3),FadeOut(dot4),FadeOut(dot5)]
        self.play(Succession(*fadein_anims))
        self.play(*fadeout_anims)
        for anim in cursor5.write_text('SELECT 2*2;',"#34eb99"):
            self.play(*anim)
        for anim in cursor5.blinking_on():
            self.play(anim)
        output5 = Text("4", color="#34eb99").scale(0.5).move_to(output_console.get_center())
        prompt6 = TerminalPrompt("~").next_to(prompt5,DOWN,buff=0.1)
        cursor6 = BlinkingCursor().next_to(prompt6)
        self.play(FadeOut(cursor5),FadeIn(prompt6), FadeIn(cursor6), run_time=0.5)
        self.play(FadeIn(output5))
        self.play(ShowPassingFlash(output_console.copy().set_color('#34eb99'), time_width=100, run_time=2))
        for anim in cursor6.blinking_on():
            self.play(anim)
        self.play(FadeOut(output5))
        for anim in cursor6.write_text('SELECT Number_A * Number_B FROM Numbers;',"#f2e86d"):
            self.play(*anim)
        for anim in cursor6.blinking_on():
            self.play(anim)
        output6 = Table([["Number_A * Number_B"],
                         ["6"],
                         ["14"],
                         ["24"],
                         ["36"],
                         ["50"]],include_outer_lines=True,line_config={'color':"#f2e86d"}).scale(0.3).move_to(output_console.get_center())
        prompt7 = TerminalPrompt("~").next_to(prompt6,DOWN,buff=0.1)
        cursor7 = BlinkingCursor().next_to(prompt7)
        self.play(FadeOut(cursor6),FadeIn(prompt7), FadeIn(cursor7), run_time=0.5)
        self.play(FadeIn(output6))
        self.play(ShowPassingFlash(output_console.copy().set_color('#f2e86d'), time_width=100, run_time=2))
        for anim in cursor7.blinking_on():
            self.play(anim)
        self.play(FadeOut(output6), FadeOut(multiplication_examples_heading))
        division_examples_heading = Text("division Examples",color= '#03fc88',font=font_to_use).scale(0.4).next_to(sql_logo,DOWN*2)
        dot1 = Dot(radius=0.04).next_to(division_examples_heading,aligned_edge=DOWN)
        dot1.set_color('#03fc88')
        dot2 = Dot(radius=0.04).next_to(dot1, buff=0.2)
        dot2.set_color('#03fc88')
        dot3 = Dot(radius=0.04).next_to(dot2, buff=0.2)
        dot3.set_color('#03fc88')
        dot4 = Dot(radius=0.04).next_to(dot3, buff=0.2)
        dot4.set_color('#03fc88')
        dot5 = Dot(radius=0.04).next_to(dot4, buff=0.2)
        dot5.set_color('#03fc88')
        self.play(FadeIn(division_examples_heading))
        fadein_anims = [FadeIn(dot1, run_time=0.5),FadeIn(dot2, run_time=0.5),FadeIn(dot3, run_time=0.5),FadeIn(dot4, run_time=0.5),FadeIn(dot5, run_time=0.5)]
        fadeout_anims = [FadeOut(dot1),FadeOut(dot2),FadeOut(dot3),FadeOut(dot4),FadeOut(dot5)]
        self.play(Succession(*fadein_anims))
        self.play(*fadeout_anims)
        for anim in cursor7.write_text('SELECT 2/2;',"#34eb99"):
            self.play(*anim)
        for anim in cursor7.blinking_on():
            self.play(anim)
        output7 = Text("1", color="#34eb99").scale(0.5).move_to(output_console.get_center())
        prompt8 = TerminalPrompt("~").next_to(prompt7,DOWN,buff=0.1)
        cursor8 = BlinkingCursor().next_to(prompt8)
        self.play(FadeOut(cursor7),FadeIn(prompt8), FadeIn(cursor8), run_time=0.5)
        self.play(FadeIn(output7))
        self.play(ShowPassingFlash(output_console.copy().set_color('#34eb99'), time_width=100, run_time=2))
        for anim in cursor8.blinking_on():
            self.play(anim)
        self.play(FadeOut(output7))
        for anim in cursor8.write_text('SELECT Number_B / Number_A FROM Numbers;',"#f2e86d"):
            self.play(*anim)
        for anim in cursor8.blinking_on():
            self.play(anim)
        output8 = Table([["Number_B / Number_A"],
                         ["6"],
                         ["3.5"],
                         ["2.6"],
                         ["2.2"],
                         ["2"]],include_outer_lines=True,line_config={'color':"#f2e86d"}).scale(0.3).move_to(output_console.get_center())
        prompt9 = TerminalPrompt("~").next_to(prompt8,DOWN,buff=0.1)
        cursor9 = BlinkingCursor().next_to(prompt9)
        self.play(FadeOut(cursor8),FadeIn(prompt9), FadeIn(cursor9), run_time=0.5)
        self.play(FadeIn(output8))
        self.play(ShowPassingFlash(output_console.copy().set_color('#f2e86d'), time_width=100, run_time=2))
        for anim in cursor9.blinking_on():
            self.play(anim)
        self.play(FadeOut(output8), FadeOut(division_examples_heading))
        aggregate_fun_examples_heading = Text("Using Aggregate Functions",color= '#03fc88',font=font_to_use).scale(0.4).next_to(sql_logo,DOWN*2)
        dot1 = Dot(radius=0.04).next_to(aggregate_fun_examples_heading,aligned_edge=DOWN)
        dot1.set_color('#03fc88')
        dot2 = Dot(radius=0.04).next_to(dot1, buff=0.2)
        dot2.set_color('#03fc88')
        dot3 = Dot(radius=0.04).next_to(dot2, buff=0.2)
        dot3.set_color('#03fc88')
        dot4 = Dot(radius=0.04).next_to(dot3, buff=0.2)
        dot4.set_color('#03fc88')
        dot5 = Dot(radius=0.04).next_to(dot4, buff=0.2)
        dot5.set_color('#03fc88')
        self.play(FadeIn(aggregate_fun_examples_heading))
        fadein_anims = [FadeIn(dot1, run_time=0.5),FadeIn(dot2, run_time=0.5),FadeIn(dot3, run_time=0.5),FadeIn(dot4, run_time=0.5),FadeIn(dot5, run_time=0.5)]
        fadeout_anims = [FadeOut(dot1),FadeOut(dot2),FadeOut(dot3),FadeOut(dot4),FadeOut(dot5)]
        self.play(Succession(*fadein_anims))
        self.play(FadeOut(example_table))
        self.play(*fadeout_anims)
        introductory_text = Text("SQL has many built-in function \nthat can calculate for you", font=font_to_use).scale(0.4).next_to(aggregate_fun_examples_heading,DOWN, aligned_edge=LEFT)
        self.play(Write(introductory_text))
        self.wait(2)
        self.play(FadeOut(introductory_text))
        count_func = Text("COUNT() Counts the number of rows").scale(0.3).next_to(aggregate_fun_examples_heading,DOWN)
        count_func[:7].set_color(YELLOW)
        sum_func = Text("SUM() Adds up all the values").scale(0.3).next_to(count_func,DOWN,aligned_edge=LEFT)
        sum_func[:5].set_color(YELLOW)
        avg_func = Text("AVG() Calculates the average value").scale(0.3).next_to(sum_func,DOWN,aligned_edge=LEFT)
        avg_func[:5].set_color(YELLOW)
        min_func = Text("MIN() Finds the smallest value").scale(0.3).next_to(avg_func,DOWN,aligned_edge=LEFT)
        min_func[:5].set_color(YELLOW)
        max_func = Text("MAX() Finds the largest value").scale(0.3).next_to(min_func,DOWN,aligned_edge=LEFT)
        max_func[:5].set_color(YELLOW)
        self.play(Write(count_func))
        self.play(Write(sum_func))
        self.play(Write(avg_func))
        self.play(Write(min_func))
        self.play(Write(max_func))
        self.wait(3)
        self.play(FadeOut(count_func),FadeOut(sum_func),FadeOut(avg_func),FadeOut(min_func),FadeOut(max_func),FadeIn(example_table))
        for anim in cursor9.write_text('SELECT AVG(Number_A) FROM Numbers;',"#34eb99"):
            self.play(*anim)
        for anim in cursor9.blinking_on():
            self.play(anim)
        output9 = Text("3", color="#34eb99").scale(0.5).move_to(output_console.get_center())
        prompt10 = TerminalPrompt("~").next_to(prompt9,DOWN,buff=0.1)
        cursor10 = BlinkingCursor().next_to(prompt10)
        self.play(FadeOut(cursor9),FadeIn(prompt10), FadeIn(cursor10), run_time=0.5)
        self.play(FadeIn(output9))
        self.play(ShowPassingFlash(output_console.copy().set_color('#34eb99'), time_width=100, run_time=2))
        for anim in cursor10.blinking_on():
            self.play(anim)
        self.play(FadeOut(output9))
        for anim in cursor10.write_text('SELECT COUNT(Number_B) FROM Numbers;',"#f2e86d"):
            self.play(*anim)
        for anim in cursor10.blinking_on():
            self.play(anim)
        output10 = Text("5", color="#34eb99").scale(0.5).move_to(output_console.get_center())
        prompt11 = TerminalPrompt("~").next_to(prompt10,DOWN,buff=0.1)
        cursor11 = BlinkingCursor().next_to(prompt11)
        self.play(FadeOut(cursor10),FadeIn(prompt11), FadeIn(cursor11), run_time=0.5)
        self.play(FadeIn(output10))
        self.play(ShowPassingFlash(output_console.copy().set_color("#34eb99"), time_width=100, run_time=2))
        for anim in cursor11.blinking_on():
            self.play(anim)
        
        self.wait()