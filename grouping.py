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
class GROUPING(Scene):
    def construct(self):
        font_to_use = "resources/Quicksand-VariableFont_wght.ttf"
        sql_image = ImageMobject('resources/image (1).png')
        gear_image = ImageMobject('/resources/image (2).png').scale(0.7).next_to(sql_image.get_end()-[1.4,-0.72,0],buff=0)
        gear_image.set_z_index(sql_image.z_index)
        sql_logo = Group(sql_image,gear_image).move_to([-4,3,0]).scale(0.2)
        self.play(FadeIn(sql_logo))
        always_rotate(gear_image, rate=60*DEGREES)
        title = Text("Grouping in SQL", font=font_to_use).scale(0.6).next_to(sql_logo,RIGHT*3)
        self.play(DrawBorderThenFill(title))
        self.wait(2)
        group_by_question = Text("What is GROUP BY ?", font=font_to_use).scale(0.6).next_to(title, DOWN*3)
        self.play(Write(group_by_question))
        self.wait(2)
        ball1 = Dot(radius=0.09, color=PURE_GREEN).next_to(group_by_question, DOWN*2+LEFT)
        ball2 = Dot(radius=0.09, color=PURE_RED).next_to(ball1)
        ball3 = Dot(radius=0.09, color=PURE_GREEN).next_to(ball2)
        ball4 = Dot(radius=0.09, color=YELLOW).next_to(ball1, DOWN)
        ball5 = Dot(radius=0.09, color=YELLOW).next_to(ball4)
        ball6 = Dot(radius=0.09, color=PURE_GREEN).next_to(ball5)
        ball7 = Dot(radius=0.09, color=PURE_RED).next_to(ball4,DOWN)
        ball8 = Dot(radius=0.09, color=YELLOW).next_to(ball7)
        ball9 = Dot(radius=0.09, color=PURE_RED).next_to(ball8)
        random_group = VGroup(ball1,ball2, ball3, ball4, ball5, ball6, ball7, ball8, ball9)
        balla = Dot(radius=0.09, color=PURE_GREEN).next_to(ball7, DOWN)
        ballb = Dot(radius=0.09, color=PURE_RED).next_to(balla)
        ballc = Dot(radius=0.09, color=YELLOW).next_to(ballb)
        balld = Dot(radius=0.09, color=PURE_GREEN).next_to(balla, DOWN)
        balle = Dot(radius=0.09, color=PURE_RED).next_to(balld)
        ballf = Dot(radius=0.09, color=YELLOW).next_to(balle)
        ballg = Dot(radius=0.09, color=PURE_GREEN).next_to(balld,DOWN)
        ballh = Dot(radius=0.09, color=PURE_RED).next_to(ballg)
        balli = Dot(radius=0.09, color=YELLOW).next_to(ballh)
        grouped_group = VGroup(balla, ballb, ballc,balld,balle,ballf,ballg,ballh,balli)
        grouping_text = Text("Use GROUP BY to organize your data\ninto categories,making it easier \nto see patterns and trends",font=font_to_use, line_spacing=1).scale(0.4).next_to(grouped_group, DOWN+LEFT, aligned_edge=LEFT)
        example_table = Table([["product_id", "category", "revenue"],
                               ["1", "A", "100"], 
                               ["2", "B", "150"], 
                               ["3", "A", "120"], 
                               ["1", "B", "200"],
                               ["2", "A", "180"]], include_outer_lines=True,line_config={"color":YELLOW}).scale(0.3).next_to(group_by_question, DOWN+RIGHT)
        example_table.add_highlighted_cell((2,2),color=LIGHT_PINK)
        example_table.add_highlighted_cell((3,2),color=PURE_GREEN)
        example_table.add_highlighted_cell((4,2),color=LIGHT_PINK)
        example_table.add_highlighted_cell((5,2),color=PURE_GREEN)
        example_table.add_highlighted_cell((2,2),color=LIGHT_PINK)
        example_table.add_highlighted_cell((6,2),color=LIGHT_PINK)
        transformed_table = Table([["category", "total_revenue"],
                                   ["A", "400"],
                                   ["B", "350"]],include_outer_lines=True,line_config={"color":YELLOW}).scale(0.3).next_to(group_by_question, DOWN*2+RIGHT)
        transformed_table.add_highlighted_cell((2,1),color=LIGHT_PINK)
        transformed_table.add_highlighted_cell((3,1),color=PURE_GREEN)
        grouping_text2 =  Text("The GROUP BY statement groups rows\nthat have the same value in\nspecified columns into summary rows",font=font_to_use, line_spacing=1).scale(0.4).next_to(example_table, DOWN)
        self.play(FadeIn(random_group, example_table))
        self.wait(3)
        self.play(Write(grouping_text), Write(grouping_text2),ReplacementTransform(random_group,grouped_group), FadeTransform(example_table, transformed_table),run_time=2.5)
        self.wait(7)
        self.play(FadeOut(grouping_text,grouping_text2,grouped_group,transformed_table))
        groupby_functions_text = Text("GROUP BY Functions & Syntax", font=font_to_use).scale(0.6).next_to(title, DOWN*3)
        self.play(ReplacementTransform(group_by_question, groupby_functions_text))
        counting_logo = ImageMobject("resources/image (3).png").scale(0.2).next_to(groupby_functions_text, LEFT*0.5+DOWN*2)
        counting_text = Text("COUNT(): Counts the number of rows", font=font_to_use).scale(0.3).next_to(counting_logo,DOWN)
        counting_text[:7].set_color(YELLOW)
        sum_logo = ImageMobject("resources/image (4).png").scale(0.3).next_to(counting_logo, RIGHT*11)
        sum_text = Text("SUM(): ADDS up all the values", font=font_to_use).scale(0.3).next_to(sum_logo,DOWN*0.3)
        sum_text[:5].set_color(YELLOW)
        avg_logo = ImageMobject("resources/financial.png").scale(0.3).next_to(sum_logo, RIGHT*11)
        avg_text = Text("AVG(): Calculates the Average value", font=font_to_use).scale(0.3).next_to(avg_logo,DOWN*0.3)
        avg_text[:5].set_color(YELLOW)
        min_logo = ImageMobject("resources/ant.png").scale(0.23).next_to(counting_logo, DOWN*3+RIGHT*5 )
        min_text = Text("MIN(): FINDS the smallest value", font=font_to_use).scale(0.3).next_to(min_logo,DOWN*0.4)
        min_text[:5].set_color(YELLOW)
        max_logo = ImageMobject("resources/tyrannosaurus.png").scale(0.23).next_to(min_logo, RIGHT*11)
        max_text = Text("MAX(): FINDS the largest value", font=font_to_use).scale(0.3).next_to(max_logo,DOWN*0.4)
        max_text[:5].set_color(YELLOW)
        
        self.play(FadeIn(counting_logo,counting_text,sum_logo,sum_text,avg_logo,avg_text,min_logo,min_text,max_logo,max_text))
        self.wait(2)
        syntax_image = ImageMobject("resources/image (6).png").scale(0.23).next_to(min_logo, DOWN*3+LEFT*7)
        self.play(FadeIn(syntax_image))
        bottom_line = VGroup().set_points_as_corners([syntax_image.get_bottom(),syntax_image.get_bottom()+DOWN, syntax_image.get_bottom()+DOWN+RIGHT*10, syntax_image.get_bottom()+DOWN+RIGHT*10+UP*2, syntax_image.get_bottom()+DOWN+RIGHT*10+UP*2+LEFT*10, syntax_image.get_bottom()+DOWN+RIGHT*10+UP*2+LEFT*10+DOWN*0.2])
        syntax = Text("SELECT column1, column2, ... aggregate_function(column3)\nFROM table_name\nGROUP BY column1, column2, ...;", font=font_to_use, line_spacing=1).scale(0.4).next_to(DOWN*3+LEFT*4, aligned_edge=LEFT)
        syntax[:6].set_color(ORANGE)
        syntax[25:44].set_color(PURPLE)
        syntax[52:56].set_color(ORANGE)
        syntax[66:73].set_color(ORANGE)
        self.play(Write(syntax),ShowPassingFlash(bottom_line.copy().set_color(YELLOW), time_width=100, run_time=10))
        self.play(FadeOut(counting_logo,counting_text,sum_logo,sum_text,avg_logo,avg_text,min_logo,min_text,max_logo,max_text,syntax_image,syntax))
        groupby_working = Text("How GROUP BY works ?", font=font_to_use).scale(0.6).next_to(title, DOWN*2)
        self.play(ReplacementTransform(groupby_functions_text, groupby_working))
        groupby_working_text = Text("A GROUP BY uses something called aggregation,which is like grouping \nsimilar items together and calculating something about each group.\nIt's akin to sorting various coloured marbles into piles,then counting each pile. \nThis makes complex data simpler and more digestible.", font=font_to_use, line_spacing=1).scale(0.4).next_to([-5,1,0], aligned_edge=LEFT)
        self.play(Write(groupby_working_text))
        table1 = Table([["category", "value"],
                        ["A", "1"],
                        ["A", "4"], 
                        ["B", "3"], 
                        ["B", "1"]], include_outer_lines=True, line_config={'color':ORANGE}).scale(0.3).move_to([-3,-1,0])
        table1_enteries = table1.get_entries()
        table1_enteries[2].set_color(YELLOW)
        table1_enteries[3].set_color(YELLOW)
        table1_enteries[4].set_color(YELLOW)
        table1_enteries[5].set_color(YELLOW)
        table1_enteries[6].set_color(PURE_GREEN)
        table1_enteries[7].set_color(PURE_GREEN)
        table1_enteries[8].set_color(PURE_GREEN)
        table1_enteries[9].set_color(PURE_GREEN)
        table1_enteries[2].set_color(YELLOW)
        table1.add_highlighted_cell((2,1),color=LIGHT_PINK)
        table1.add_highlighted_cell((2,2),color=LIGHT_PINK)
        table1.add_highlighted_cell((4,1),color=LIGHT_PINK)
        table1.add_highlighted_cell((4,2),color=LIGHT_PINK)
        table2 = Table([["category", "SUM(value)"],
                        ["A", "5"], 
                        ["B", "4"]], include_outer_lines=True, line_config={'color':ORANGE}).scale(0.3).next_to(table1, RIGHT*9)
        table2_enteries = table2.get_entries()
        table2_enteries[2].set_color(YELLOW)
        table2_enteries[3].set_color(YELLOW)
        table2_enteries[4].set_color(PURE_GREEN)
        table2_enteries[5].set_color(PURE_GREEN)
        table2.add_highlighted_cell((2,1),color=LIGHT_PINK)
        table2.add_highlighted_cell((2,2),color=LIGHT_PINK)
        self.play(FadeIn(table1, table2))
        arrow1 = Arrow(table1_enteries[3], table2_enteries[3], color=ORANGE, tip_length=0.1,stroke_width=3)
        arrow2 = Arrow(table1_enteries[5], table2_enteries[3], color=ORANGE, tip_length=0.1,stroke_width=3)
        arrow3 = Arrow(table1_enteries[7], table2_enteries[5], color=ORANGE, tip_length=0.1,stroke_width=3)
        arrow4 = Arrow(table1_enteries[9], table2_enteries[5], color=ORANGE, tip_length=0.1,stroke_width=3)
        self.play(GrowArrow(arrow1), GrowArrow(arrow2), GrowArrow(arrow3), GrowArrow(arrow4))
        syntax_image = ImageMobject("resources/image (6).png").scale(0.23).next_to(table1, DOWN+LEFT)
        self.play(FadeIn(syntax_image))
        bottom_line = VGroup().set_points_as_corners([syntax_image.get_bottom(),syntax_image.get_bottom()+DOWN*0.5, syntax_image.get_bottom()+DOWN*0.5+RIGHT*10, syntax_image.get_bottom()+DOWN*0.5+RIGHT*10+UP*1.5, syntax_image.get_bottom()+DOWN*0.5+RIGHT*10+UP*1.5+LEFT*10, syntax_image.get_bottom()+DOWN*0.5+RIGHT*10+UP*1.5+LEFT*10+DOWN*0.2])
        syntax = Text("SELECT category , SUM(value) FROM table GROUP BY category;", font=font_to_use, line_spacing=1).scale(0.4).next_to(DOWN*3+LEFT*4, aligned_edge=LEFT)
        syntax[0:6].set_color(ORANGE)
        syntax[15:18].set_color(ORANGE)
        syntax[25:29].set_color(ORANGE)
        syntax[34:41].set_color(ORANGE)
        self.play(Write(syntax),ShowPassingFlash(bottom_line.copy().set_color(YELLOW), time_width=100, run_time=10))
        self.play(FadeOut(groupby_working_text, table1, table2, arrow1, arrow2, arrow3, arrow4, syntax_image, syntax))
        examples_text = Text("Some Real Examples ", font=font_to_use).scale(0.6).next_to(title, DOWN*2)
        self.play(ReplacementTransform(groupby_working, examples_text))
        dot1 = Dot(radius=0.04).next_to(examples_text,aligned_edge=DOWN)
        dot1.set_color('#03fc88')
        dot2 = Dot(radius=0.04).next_to(dot1, buff=0.2)
        dot2.set_color('#03fc88')
        dot3 = Dot(radius=0.04).next_to(dot2, buff=0.2)
        dot3.set_color('#03fc88')
        dot4 = Dot(radius=0.04).next_to(dot3, buff=0.2)
        dot4.set_color('#03fc88')
        dot5 = Dot(radius=0.04).next_to(dot4, buff=0.2)
        dot5.set_color('#03fc88')
        fadein_anims = [FadeIn(dot1, run_time=0.5),FadeIn(dot2, run_time=0.5),FadeIn(dot3, run_time=0.5),FadeIn(dot4, run_time=0.5),FadeIn(dot5, run_time=0.5)]
        fadeout_anims = [FadeOut(dot1),FadeOut(dot2),FadeOut(dot3),FadeOut(dot4),FadeOut(dot5)]
        self.play(Succession(*fadein_anims))
        self.play(*fadeout_anims)
        self.play(Succession(*fadein_anims))
        table3 = Table([["order_id", "fruit"],
                        ["1", "Apple"],
                        ["2", "Banana"], 
                        ["3", "Apple"], 
                        ["4", "Cherry"],
                        ["5", "Banana"]], include_outer_lines=True, line_config={'color':ORANGE}).scale(0.3).move_to([-3,0,0])
        table4 = Table([["fruit", "COUNT(order_id)"],
                        ["Apple", "2"], 
                        ["Banana", "2"],
                        ["Cherry", "1"]], include_outer_lines=True, line_config={'color':ORANGE}).scale(0.3).next_to(table3, RIGHT*9)
        self.play(Create(table3))
        prompt_image = ImageMobject("resources/image (7).png").scale(0.2).next_to([-4,-2,0])
        self.play(FadeIn(prompt_image))
        command1 = Text("SELECT fruit, COUNT(order_id) FROM orders GROUP BY fruit;", font=font_to_use).scale(0.4).next_to(prompt_image)
        command1[:6].set_color(ORANGE)
        command1[12:17].set_color(ORANGE)
        command1[27:31].set_color(ORANGE)
        command1[37:44].set_color(ORANGE)
        self.play(Write(command1))
        self.wait(1)
        self.play(ReplacementTransform(table3.copy(), table4))
        table3_elements = table3.get_entries()
        table4_elements = table4.get_entries()
        arrow5 = Arrow(table3_elements[3], table4_elements[3], color=PURE_RED,tip_length=0.1, stroke_width=3)
        arrow6 = Arrow(table3_elements[7], table4_elements[3], color=PURE_RED,tip_length=0.1, stroke_width=3)
        arrow7 = Arrow(table3_elements[5], table4_elements[5], color=BLUE_A,tip_length=0.1, stroke_width=3)
        arrow8 = Arrow(table3_elements[11], table4_elements[5], color=BLUE_A,tip_length=0.1, stroke_width=3)
        arrow9 = Arrow(table3_elements[9], table4_elements[7], color=PURE_GREEN,tip_length=0.1, stroke_width=3)
        self.play(GrowArrow(arrow5),GrowArrow(arrow6),GrowArrow(arrow7),GrowArrow(arrow8),GrowArrow(arrow9))
        self.wait(7)
        self.play(FadeOut(table3,table4,arrow5,arrow6,arrow7,arrow8,arrow9),Unwrite(command1) )
        self.wait(1)
        table5 = Table([["sale_id", "product", "sale_amount"],
                        ["1", "X","10"],
                        ["2", "Y", "15"], 
                        ["3", "X", "20"], 
                        ["4", "Z", "25"],
                        ], include_outer_lines=True, line_config={'color':ORANGE}).scale(0.3).move_to([-3,0,0])
        table6 = Table([["product", "MAX(sale_amount)"],
                        ["X", "20"], 
                        ["Y", "15"],
                        ["Z", "25"]], include_outer_lines=True, line_config={'color':ORANGE}).scale(0.3).next_to(table3, RIGHT*9)
        self.play(Create(table5))
        command2 = Text("SELECT product, MAX(sale_amount) FROM sales GROUP BY product;", font=font_to_use).scale(0.4).next_to(prompt_image)
        command2[:6].set_color(ORANGE)
        command2[14:17].set_color(ORANGE)
        command2[30:34].set_color(ORANGE)
        command2[39:46].set_color(ORANGE)
        self.play(Write(command2))
        self.wait(1)
        self.play(ReplacementTransform(table5.copy(), table6))
        table5_elements = table5.get_entries()
        table6_elements = table6.get_entries()
        arrow10 = Arrow(table5_elements[4], table6_elements[3], color=PURE_GREEN,tip_length=0.1, stroke_width=3)
        arrow11 = Arrow(table5_elements[7], table6_elements[5], color=PURE_RED,tip_length=0.1, stroke_width=3)
        arrow12 = Arrow(table5_elements[10], table6_elements[3], color=PURE_GREEN,tip_length=0.1, stroke_width=3)
        arrow13 = Arrow(table5_elements[13], table6_elements[7], color=ORANGE,tip_length=0.1, stroke_width=3)
       
        self.play(GrowArrow(arrow10),GrowArrow(arrow11),GrowArrow(arrow12),GrowArrow(arrow13))
        self.wait(7)
        self.play(FadeOut(table5,table6,arrow10,arrow11,arrow12,arrow13, prompt_image),Unwrite(command2),*fadeout_anims)
        having_statement = Text("HAVING statement", font=font_to_use).scale(0.6).next_to(title, DOWN*2)
        self.play(ReplacementTransform(examples_text, having_statement))
        
        having_statement_working = Text("In SQL, the HAVING clause filters aggregated query results, acting similarly to \nthe WHERE clause but specifically for data grouped by the GROUP BY statement.", font=font_to_use, line_spacing=1).scale(0.4).next_to([-6,1,0], aligned_edge=LEFT)
        self.play(Write(having_statement_working))
        self.wait(2)
        syntax_image = ImageMobject("resources/image (6).png").scale(0.23).next_to([-6,-1,0])
        self.play(FadeIn(syntax_image))
        bottom_line = VGroup().set_points_as_corners([syntax_image.get_bottom(),syntax_image.get_bottom()+DOWN, syntax_image.get_bottom()+DOWN+RIGHT*10, syntax_image.get_bottom()+DOWN+RIGHT*10+UP*2, syntax_image.get_bottom()+DOWN+RIGHT*10+UP*2+LEFT*10, syntax_image.get_bottom()+DOWN+RIGHT*10+UP*2+LEFT*10+DOWN*0.2])
        syntax = Text("SELECT column1, column2, ... aggregate_function(column3)\nFROM table_name\nGROUP BY column1, column2, ... HAVING condition;", font=font_to_use, line_spacing=1).scale(0.4).next_to(DOWN*1.3+LEFT*5, aligned_edge=LEFT)
        syntax[:6].set_color(ORANGE)
        syntax[25:44].set_color(PURPLE)
        syntax[52:56].set_color(ORANGE)
        syntax[66:73].set_color(ORANGE)
        syntax[92:98].set_color(ORANGE)
        self.play(Write(syntax),ShowPassingFlash(bottom_line.copy().set_color(YELLOW), time_width=100, run_time=10))
        self.play(Unwrite(syntax), FadeOut(syntax_image))
        self.wait(2)
        self.play(having_statement_working.animate.shift(UP*0.5))
        table_to_use = Table([["employee_id", "department"],
                              ["1", "Sales"],
                             ["2", "Sales"],
                             ["3" ,"HR"],
                             ["4","HR"],
                             ["5", "Marketing"]],
                             include_outer_lines=True, line_config={'color':YELLOW}).scale(0.3).move_to([-2,-0.3,0])
        self.play(FadeIn(table_to_use))
        self.wait(1)
        prompt_image = ImageMobject("resources/image (7).png").scale(0.2).next_to([-5,-2.5,0])
        self.wait(2)
        self.play(FadeIn(prompt_image))
        syntax = Text("SELECT department, COUNT(employee_id) AS employee_count\nFROM employees\nGROUP BY department;", font=font_to_use, line_spacing=1).scale(0.4).next_to([-4,-2.5,0], aligned_edge=LEFT)
        self.play(Write(syntax))
        syntax[:6].set_color(ORANGE)
        syntax[17:22].set_color(ORANGE)
        syntax[35:37].set_color(ORANGE)
        syntax[51:55].set_color(ORANGE)
        syntax[64:71].set_color(ORANGE)
        replacement_table = Table([["department", "employee_count"], 
                                   ["Sales", "2"],
                                   ["HR","2"], 
                                   ["Marketing", "1"]],
                                 include_outer_lines=True, line_config={'color':GREEN} ).scale(0.3).next_to(table_to_use, RIGHT*3)
        self.wait(5)
        self.play(ReplacementTransform(table_to_use.copy(), replacement_table))
        self.wait(3)
        self.play(FadeOut(replacement_table), Unwrite(syntax))
        syntax = Text("SELECT department, COUNT(employee_id) AS employee_count\nFROM employees\nGROUP BY department\nHAVING COUNT(employee_id) > 1;", font=font_to_use, line_spacing=1).scale(0.4).next_to([-4,-2.5,0], aligned_edge=LEFT)
        syntax[:6].set_color(ORANGE)
        syntax[17:22].set_color(ORANGE)
        syntax[35:37].set_color(ORANGE)
        syntax[51:55].set_color(ORANGE)
        syntax[64:71].set_color(ORANGE)
        syntax[81:92].set_color(ORANGE)
        self.play(Write(syntax))
        replacement_table2 = replacement_table = Table([["department", "employee_count"], 
                                   ["Sales", "2"],
                                   ["HR","2"], 
                                   ],
                                 include_outer_lines=True, line_config={'color':PURE_GREEN} ).scale(0.3).next_to(table_to_use, RIGHT*3)
        self.wait(7)
        self.play(ReplacementTransform(table_to_use.copy(), replacement_table2))
        self.wait(3)
        self.play(FadeOut(having_statement_working, table_to_use, replacement_table2, syntax, prompt_image))
        where_vs_having_text = Text("WHERE Vs HAVING", font=font_to_use).scale(0.6).next_to(title, DOWN*2)
        self.play(ReplacementTransform(having_statement,where_vs_having_text))
        comparison_table = Table([["WHERE", "HAVING"],
                                  ["WHERE is used to filter records\nbefore any grouping occurs.","HAVING is used after grouping\nto filter the groups or aggregates."],
                                  ["WHERE introduces a condition\non individual rows.", "HAVING introduces a condition\non aggregations."],
                                  ['WHERE could be used to only\ninclude "Orders" from "2023".','HAVING could then be used to\nonly find categories "having"\nmore than 10 orders.']],
                                 include_outer_lines=True, line_config={'color':YELLOW}).scale(0.4).move_to([0,-1,0])
        self.play(FadeIn(comparison_table))
        self.wait(2)
        