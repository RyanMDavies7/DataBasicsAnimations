from manim import *



def custom_create_starting_mobject(self) -> Mobject:
    start_arrow = self.mobject.copy()
    try :
        start_arrow.scale(0, scale_tips=True, about_point=self.point)
    except:
        start_arrow.scale(0, about_point=self.point)
    if self.point_color:
        start_arrow.set_color(self.point_color)
    return start_arrow
GrowArrow.create_starting_mobject = custom_create_starting_mobject



class Joins(Scene):
    def construct(self):
        font_to_use = "resources/Quicksand-VariableFont_wght.ttf"
        sql_image = ImageMobject('resources/image (1).png')
        gear_image = ImageMobject('resources/image (2).png').scale(0.7).next_to(sql_image.get_end()-[1.4,-0.72,0],buff=0)
        gear_image.set_z_index(sql_image.z_index)
        sql_logo = Group(sql_image,gear_image).move_to([-5,3,0]).scale(0.2)
        self.play(FadeIn(sql_logo))
        always_rotate(gear_image, rate=60*DEGREES)
        title = Text("Combining Datasets with JOIN & UNION", font=font_to_use).scale(0.6).next_to(sql_logo,RIGHT*3)
        self.play(DrawBorderThenFill(title))
        self.play(FadeToColor(title[21:25], YELLOW))
        self.play(FadeToColor(title[26:], YELLOW))
        self.wait(1)
        table1 = Table([["0", "0", "0"],
                        ["0", "0", "0"],
                        ["0", "0", "0"],
                        ["0", "0", "0"]], include_outer_lines=True, line_config={'color':RED}).scale(0.2).move_to([3,1.5,0])
        table1.get_rows().set_opacity(0)
        table2 = Table([["0", "0", "0"],
                        ["0", "0", "0"],
                        ["0", "0", "0"],
                        ["0", "0", "0"]], include_outer_lines=True, line_config={'color':PURE_GREEN}).scale(0.2).next_to(table1, RIGHT*4)
        table2.get_rows().set_opacity(0)
        
        join_logo = ImageMobject('resources/combine.png').scale(0.2).next_to(table1,DOWN*3+RIGHT)
        left_arrow = Arrow(table1.get_bottom(),join_logo.get_top()+[-0.5,0,0],tip_length=0.1)
        right_arrow = Arrow(table2.get_bottom(),join_logo.get_top()+[0.25,0,0],tip_length=0.1)
        table3 = Table([["0", "0", "0", "0", "0"],
                        ["0", "0", "0", "0", "0"],
                        ["0", "0", "0", "0", "0"],
                        ["0", "0", "0", "0", "0"]], include_outer_lines=True, line_config={'color':YELLOW}).scale(0.2).next_to(join_logo, DOWN*4)
        table3.get_rows().set_opacity(0)
        
        down_arrow = Arrow(join_logo.get_bottom(), table3.get_top(), tip_length=0.1)
        point1 = Text("A join works by using a key or value\nthat is related between the tables via a\ncolumn such as product_id or country", font=font_to_use, line_spacing=1).scale(0.4).move_to([-3,1,0])
        point1_pointer = Circle(radius=0.1, color=PURE_GREEN).next_to(point1,LEFT)
        self.play(Create(point1_pointer))
        self.play(Write(point1),FadeIn(table1,table2), run_time=3)
        point2 = Text("Think of it as figuring out a way of\ncombining tables horizontally by each\nrecord. Combining rows by each related\nkey or value", font=font_to_use, line_spacing=1).scale(0.4).next_to(point1, DOWN*2, aligned_edge=LEFT)
        point2_pointer = Circle(radius=0.1, color=PURE_GREEN).next_to(point2,LEFT)
        self.play(Create(point2_pointer),FadeIn(join_logo))
        self.play(Write(point2),Succession(GrowArrow(left_arrow), GrowArrow(right_arrow),GrowArrow(down_arrow),FadeIn(table3)), run_time=4)
        self.wait(20)
        self.play(FadeOut(point1_pointer,point2_pointer,point1,point2,table1,table2,table3,left_arrow,right_arrow,down_arrow, join_logo))
        self.wait(2)
        join_types = Text("Types of SQL JOIN", font=font_to_use).scale(0.6).next_to(title,DOWN)
        join_types.set_stroke(color=BLACK,opacity=1)
        highlighting_rectangle = Rectangle(width=3.5,height=0.28).move_to([0.1,2.26,0])
        highlighting_rectangle.set_fill(color=LIGHT_PINK, opacity=.5)
        highlighting_rectangle.set_stroke(color=None, opacity=0)
        join_types.set_z_index(highlighting_rectangle.z_index+1)
        self.play(Create(highlighting_rectangle))
        self.play(Write(join_types), run_time=1.5)
        self.wait(2)
        circle1 = Circle(radius=0.5, color= PURPLE_A).move_to([-4,1,0])
        circle1.set_fill(color= PURPLE_A, opacity=.5)
        circle1.set_stroke(color=None)
        circle2 = Circle(radius=0.5, color=GREEN).move_to([-3.5,1,0])
        circle2.set_fill(color=GREEN, opacity=.5)
        circle2.set_stroke(color=None)
        self.play(Create(circle1))
        self.play(Create(circle2))
        inner_join = Intersection(circle1, circle2, color="#98838F", fill_opacity=0.5)  
        inner_join_copy = inner_join.copy()
        inner_join.set_stroke(color=None)
        inner_join_text = Text("INNER JOIN", color="#98838F", font=font_to_use).scale(0.3)
        self.play(inner_join_copy.animate.next_to(VGroup(circle1,circle2), RIGHT*3))
        self.play(FadeIn(inner_join_text.next_to(inner_join_copy,DOWN) ))
        
        self.wait(2)
        
        circle3 = Circle(radius=0.5, color= BLUE).move_to([2,1,0])
        circle3.set_fill(color= BLUE, opacity=.5)
        circle3.set_stroke(color=None)
        circle4 = Circle(radius=0.5, color="#98ce00").move_to([2.5,1,0])
        circle4.set_fill(color="#98ce00", opacity=.5)
        circle4.set_stroke(color=None)
        circle3.set_z_index(circle4.z_index+1)
        section1 = Intersection(circle3,circle4,color="#98ce00",fill_opacity=0.5)
        self.play(Create(circle3))
        self.play(Create(circle4))
        left_join = circle3.copy().set_fill(color=BLUE, opacity=0.5)
        left_join_text = Text("LEFT (OUTER) JOIN", color=BLUE, font=font_to_use).scale(0.3)
        self.play(left_join.animate.next_to(VGroup(circle3,circle4), RIGHT*3))
        self.add(section1.move_to(left_join.get_center()+[0.25,0,0]))
        self.play(FadeIn(left_join_text.next_to(left_join,DOWN)))
        
        self.wait(2)
        
        circle5 = Circle(radius=0.5, color= "#61c9a8").move_to([-4,-0.5,0])
        circle5.set_fill(color= "#61c9a8", opacity=.5)
        circle5.set_stroke(color=None)
        circle6 = Circle(radius=0.5, color="#ff2e00").move_to([-3.5,-0.5,0])
        circle6.set_fill(color="#ff2e00", opacity=.5)
        circle6.set_stroke(color=None)
        section2 = Intersection(circle5,circle6,color=ORANGE,fill_opacity=0.5)
        section2.set_z_index(-10)
        self.play(Create(circle5))
        self.play(Create(circle6))
        right_join = circle6.copy().set_fill(color="#ff2e00", opacity=0.5)
        right_join_text = Text("RIGHT (OUTER) JOIN", color="#fea82f", font=font_to_use).scale(0.3)
        self.play(right_join.animate.next_to(VGroup(circle5,circle6), RIGHT*3))
        self.add(section2.move_to(right_join.get_center()+[-0.25,0,0]))
        self.play(FadeIn(right_join_text.next_to(right_join,DOWN)))
        
        self.wait(2)
        
        
        circle7 = Circle(radius=0.5, color= "#ef8354").move_to([2,-0.5,0])
        circle7.set_fill(color= "#ef8354", opacity=.5)
        circle7.set_stroke(color=None)
        circle8 = Circle(radius=0.5, color="#db222a").move_to([2.5,-0.5,0])
        circle8.set_fill(color="#db222a", opacity=.5)
        circle8.set_stroke(color=None)
        self.play(Create(circle7))
        self.play(Create(circle8))
        full_join = Union(circle7, circle8, color="#eb8258", fill_opacity=.5)
        full_join_copy = full_join.copy()  
        full_join.set_stroke(color=None, opacity=0)
        full_join_text = Text("FULL (OUTER) JOIN", color="#eb8258", font=font_to_use).scale(0.3)
        self.play(full_join_copy.animate.next_to(VGroup(circle7,circle8), RIGHT*3))
        self.play(FadeIn(full_join_text.next_to(full_join_copy,DOWN)))
        
        self.wait(2)
        
        self_circle = Circle(radius=0.5, color=GRAY_BROWN).move_to([-4,-2,0])
        self_circle.set_fill(color= GRAY_BROWN, opacity=.5)
        self_circle.set_stroke(color=None)
        self.play(Create(self_circle))
        self_arrow = CurvedArrow(self_circle.get_top(), self_circle.get_center()+[0.6,0,0],angle=180*DEGREES,tip_length=0.15, color=GRAY_BROWN).flip().rotate(88*DEGREES).shift(RIGHT*0.2+UP*0.1)
        self.play(Create(self_arrow))
        self_join = self_circle.copy()
        self_join.set_opacity(.5)
        self_join_text = Text("SELF JOIN", color=GRAY_BROWN, font=font_to_use).scale(0.3)
        self.play(self_join.animate.next_to(self_circle, RIGHT*5))
        self.play(FadeIn(self_join_text.next_to(self_join,DOWN)))
        
        self.wait(2)
        
        cross_circle1 = Circle(radius=0.5, color= YELLOW_E).move_to([2,-2,0])
        cross_circle1.set_fill(color= YELLOW_E, opacity=.5)
        cross_circle1.set_stroke(color=None)
        cross_circle2 = Circle(radius=0.5, color=GREEN).move_to([3.5,-2,0])
        cross_circle2.set_fill(color=GREEN, opacity=.5)
        cross_circle2.set_stroke(color=None)
        self.play(Create(cross_circle1))
        self.play(Create(cross_circle2))
        point1 = Dot(radius=0.05).move_to(cross_circle1.get_center()+[0,0.3,0])
        point2 = Dot(radius=0.05).move_to(cross_circle1.get_center()+[0,-0.3,0])
        point3 = Dot(radius=0.05).move_to(cross_circle2.get_center()+[0,0.3,0])
        point4 = Dot(radius=0.05).move_to(cross_circle2.get_center()+[0,-0.3,0])
        self.play(FadeIn(point1,point2,point3,point4))
        link1 = Arrow(point1,point3,tip_length=0.1,buff=0.1,stroke_width=1)
        link2 = Arrow(point1,point4,tip_length=0.1,buff=0.1,stroke_width=1)
        link3 = Arrow(point2,point3,tip_length=0.1,buff=0.1,stroke_width=1)
        link4 = Arrow(point2,point4,tip_length=0.1,buff=0.1,stroke_width=1)
        cross_join_text = Text("CROSS JOIN", color=WHITE, font=font_to_use).scale(0.3).next_to(cross_circle2,RIGHT+DOWN*0.5)
        self.play(GrowArrow(link1),GrowArrow(link2),GrowArrow(link3),GrowArrow(link4),FadeIn(cross_join_text), run_time=2)
        
        self.wait(3)
        
        
        self.play(FadeOut(circle1,circle2,circle3,circle4,circle5,circle6,circle7,circle8,
                          inner_join_copy,inner_join_text,left_join,left_join_text,
                          right_join,right_join_text,full_join_copy,full_join_text,
                          self_circle,self_arrow,self_join,self_join_text,cross_circle1,
                          cross_circle2,point1,point2,point3,point4,link1,link2,link3,link4,
                          cross_join_text,section1,section2))
        
        
        
        
        inner_join = Text("INNER JOIN", font=font_to_use).scale(0.6).next_to(title,DOWN)
        inner_join.set_stroke(color=BLACK,opacity=1)
        highlighting_rectangle1 = Rectangle(width=2.5,height=0.28).move_to([0.1,2.26,0])
        highlighting_rectangle1.set_fill(color=LIGHT_PINK, opacity=.5)
        highlighting_rectangle1.set_stroke(color=None, opacity=0)
        self.play(ReplacementTransform(highlighting_rectangle,highlighting_rectangle1))
        self.play(ReplacementTransform(join_types, inner_join))
        self.wait(2)
        circle9 = Circle(radius=2, color="#0e9594").move_to([1.8,0,0])
        circle9.set_fill(color="#0e9594", opacity=0.5)
        circle9.set_stroke(color=None)
        self.play(Create(circle9))
        table9 = Table([["ID", "Name"],
                        ["1", "Alice"],
                        ["2", "Bob"],
                        ["3", "Charlie"],
                        ["4", "Diana"]], include_outer_lines=True, line_config={'color':YELLOW}).scale(0.2).move_to(circle9.get_center()+[-0.5,0,0])
        table9.add_highlighted_cell((3,1), color=GREEN)
        table9.add_highlighted_cell((4,1), color=GREEN)
        table9.add_highlighted_cell((5,1), color=RED)
        table9.add_highlighted_cell((2,1), color=RED)
        table9.set_z_index(circle9.z_index+1)
        circle9_label = Text("Customers", font=font_to_use).scale(0.5).next_to(table9,UP)
        circle9_label.set_z_index(circle9.z_index+1)
        self.play(FadeIn(table9, circle9_label))
        circle10 = Circle(radius=2, color=PINK).move_to([4.8,0,0])
        circle10.set_fill(color=PINK, opacity=0.5)
        circle10.set_stroke(color=None)
        self.play(Create(circle10))
        table10 = Table([["OrderId", "CustomerID", "Product"],
                        ["101", "2", "Book"],
                        ["102", "3", "Pen"],
                        ["103", "5", "Notebook"]], include_outer_lines=True, line_config={'color':YELLOW}).scale(0.2).move_to(circle10.get_center()+[0.5,0,0])
        table10.add_highlighted_cell((2,2), color=GREEN)
        table10.add_highlighted_cell((3,2), color=GREEN)
        table10.add_highlighted_cell((4,2), color=RED)
        table10.set_z_index(circle10.z_index+1)
        circle10_label = Text("Orders", font=font_to_use).scale(0.5).next_to(table10,UP)
        circle10_label.set_z_index(circle10.z_index+1)
        self.play(FadeIn(table10, circle10_label))
        self.wait(3)
        prompt_image = ImageMobject("resources/image (7).png").scale(0.2).next_to([-6.5,0,0])
        self.play(FadeIn(prompt_image))
        command1 = Text("SELECT * FROM Customers\nINNER JOIN Orders\nON\nCustomers.ID = Orders.CustomerID;", font=font_to_use, line_spacing=1).scale(0.4).next_to(prompt_image)
        command1[0:6].set_color(ORANGE)
        command1[7:11].set_color(ORANGE)
        command1[20:29].set_color(ORANGE)
        command1[35:37].set_color(ORANGE)
        self.play(Write(command1))
        self.wait(2)
        inner_join_result = Intersection(circle9,circle10,fill_opacity=0.5)
        table11 = Table([["ID", "Name", "OrderID","CustomerID", "Product"],
                         ["2", "Bob", "101", "2","Book"],
                         ["3", "Charlie", "102","3", "Pen"]],include_outer_lines=True, line_config={'color':YELLOW}).scale(0.3).move_to([-2,-2.5,0])
        table11.add_highlighted_cell((2,1), color=GREEN)
        table11.add_highlighted_cell((3,1), color=GREEN)
        table11.add_highlighted_cell((2,4), color=GREEN)
        table11.add_highlighted_cell((3,4), color=GREEN)
        self.play(ReplacementTransform(inner_join_result,table11))
        self.wait(20)
        
        self.play(FadeOut(circle9, table9, circle10, table10, circle9_label, circle10_label, prompt_image, command1, table11))
        self.wait(2)
        
        
        left_join = Text("LEFT OUTER JOIN", font=font_to_use).scale(0.6).next_to(title,DOWN)
        left_join.set_stroke(color=BLACK,opacity=1)
        highlighting_rectangle2 = Rectangle(width=3.5,height=0.28).move_to([0.1,2.26,0])
        highlighting_rectangle2.set_fill(color=LIGHT_PINK, opacity=.5)
        highlighting_rectangle2.set_stroke(color=None, opacity=0)
        self.play(ReplacementTransform(highlighting_rectangle1,highlighting_rectangle2))
        self.play(ReplacementTransform(inner_join, left_join))
        self.wait(2)
        circle9 = Circle(radius=2, color="#0e9594").move_to([1.8,0,0])
        circle9.set_fill(color="#0e9594", opacity=0.5)
        circle9.set_stroke(color=None)
        self.play(Create(circle9))
        table9 = Table([["ID", "Name"],
                        ["1", "Alice"],
                        ["2", "Bob"],
                        ["3", "Charlie"],
                        ["4", "Diana"]], include_outer_lines=True, line_config={'color':YELLOW}).scale(0.2).move_to(circle9.get_center()+[-0.5,0,0])
        table9.add_highlighted_cell((3,1), color=GREEN)
        table9.add_highlighted_cell((4,1), color=GREEN)
        table9.add_highlighted_cell((5,1), color=GREEN)
        table9.add_highlighted_cell((2,1), color=GREEN)
        table9.set_z_index(circle9.z_index+1)
        circle9_label = Text("Customers", font=font_to_use).scale(0.5).next_to(table9,UP)
        circle9_label.set_z_index(circle9.z_index+1)
        self.play(FadeIn(table9, circle9_label))
        circle10 = Circle(radius=2, color=PINK).move_to([4.8,0,0])
        circle10.set_fill(color=PINK, opacity=0.5)
        circle10.set_stroke(color=None)
        circle9.set_z_index(circle10.z_index+1)
        self.play(Create(circle10))
        table10 = Table([["OrderId", "CustomerID", "Product"],
                        ["101", "2", "Book"],
                        ["102", "3", "Pen"],
                        ["103", "5", "Notebook"]], include_outer_lines=True, line_config={'color':YELLOW}).scale(0.2).move_to(circle10.get_center()+[0.5,0,0])
        table10.add_highlighted_cell((2,2), color=GREEN)
        table10.add_highlighted_cell((3,2), color=GREEN)
        table10.add_highlighted_cell((4,2), color=RED)
        table10.set_z_index(circle10.z_index+1)
        circle10_label = Text("Orders", font=font_to_use).scale(0.5).next_to(table10,UP)
        circle10_label.set_z_index(circle10.z_index+1)
        self.play(FadeIn(table10, circle10_label))
        self.wait(3)
        prompt_image = ImageMobject("resources/image (7).png").scale(0.2).next_to([-6.5,0,0])
        self.play(FadeIn(prompt_image))
        command2 = Text("SELECT * FROM Customers\nLEFT JOIN Orders\nON\nCustomers.ID = Orders.CustomerID;", font=font_to_use, line_spacing=1).scale(0.4).next_to(prompt_image)
        command2[0:6].set_color(ORANGE)
        command2[7:11].set_color(ORANGE)
        command2[20:28].set_color(ORANGE)
        command2[34:36].set_color(ORANGE)
        self.play(Write(command2))
        self.wait(2)
        left_join_result = circle9.copy()
        left_join_result.set_fill(color=YELLOW, opacity=.5)
        left_join_result.set_stroke(color=None, opacity=0)  
        table11 = Table([["ID", "Name", "OrderID", "CustomerID","Product"],
                         ["1", "Alice", "NULL","NULL", "NULL"],
                         ["2", "Bob", "101","2", "Book"],
                         ["3", "Charlie", "102","3", "Pen"],
                         ["4", "Diana", "NULL", "NULL", "NULL"]],include_outer_lines=True, line_config={'color':YELLOW}).scale(0.3).move_to([-2.4,-2.5,0])
        table11.add_highlighted_cell((2,1), color=GREEN)
        table11.add_highlighted_cell((3,1), color=GREEN)
        table11.add_highlighted_cell((4,1), color=GREEN)
        table11.add_highlighted_cell((5,1), color=GREEN)
        table11.add_highlighted_cell((3,4), color=GREEN)
        table11.add_highlighted_cell((4,4), color=GREEN)
        table11.add_highlighted_cell((2,3), color=RED)
        table11.add_highlighted_cell((2,4), color=RED)
        table11.add_highlighted_cell((2,5), color=RED)
        table11.add_highlighted_cell((5,3), color=RED)
        table11.add_highlighted_cell((5,4), color=RED)
        table11.add_highlighted_cell((5,5), color=RED)
        self.play(ReplacementTransform(left_join_result,table11))
        self.wait(20)
        self.play(FadeOut(circle9, table9, circle10, table10, circle9_label, circle10_label, prompt_image, command2, table11))
        self.wait(2)
        
        
        
        
        
        
        right_join = Text("RIGHT OUTER JOIN", font=font_to_use).scale(0.6).next_to(title,DOWN)
        right_join.set_stroke(color=BLACK,opacity=1)
        highlighting_rectangle3 = Rectangle(width=3.8,height=0.28).move_to([0.1,2.26,0])
        highlighting_rectangle3.set_fill(color=LIGHT_PINK, opacity=.5)
        highlighting_rectangle3.set_stroke(color=None, opacity=0)
        self.play(ReplacementTransform(highlighting_rectangle2,highlighting_rectangle3))
        self.play(ReplacementTransform(left_join,right_join))
        self.wait(2)
        circle9 = Circle(radius=2, color="#0e9594").move_to([1.8,0,0])
        circle9.set_fill(color="#0e9594", opacity=0.5)
        circle9.set_stroke(color=None)
        table9 = Table([["ID", "Name"],
                        ["1", "Alice"],
                        ["2", "Bob"],
                        ["3", "Charlie"],
                        ["4", "Diana"]], include_outer_lines=True, line_config={'color':YELLOW}).scale(0.2).move_to(circle9.get_center()+[-0.5,0,0])
        table9.add_highlighted_cell((3,1), color=GREEN)
        table9.add_highlighted_cell((4,1), color=GREEN)
        table9.add_highlighted_cell((5,1), color=RED)
        table9.add_highlighted_cell((2,1), color=RED)
        table9.set_z_index(circle9.z_index+1)
        circle9_label = Text("Customers", font=font_to_use).scale(0.5).next_to(table9,UP)
        circle9_label.set_z_index(circle9.z_index+1)
        
        circle10 = Circle(radius=2, color=PINK).move_to([4.8,0,0])
        circle10.set_fill(color=PINK, opacity=0.5)
        circle10.set_stroke(color=None)
        circle10.set_z_index(circle9.z_index+1)
        self.play(Create(circle10))
        table10 = Table([["OrderId", "CustomerID", "Product"],
                        ["101", "2", "Book"],
                        ["102", "3", "Pen"],
                        ["103", "5", "Notebook"]], include_outer_lines=True, line_config={'color':YELLOW}).scale(0.2).move_to(circle10.get_center()+[0.5,0,0])
        table10.add_highlighted_cell((2,2), color=GREEN)
        table10.add_highlighted_cell((3,2), color=GREEN)
        table10.add_highlighted_cell((4,2), color=GREEN)
        table10.set_z_index(circle10.z_index+1)
        circle10_label = Text("Orders", font=font_to_use).scale(0.5).next_to(table10,UP)
        circle10_label.set_z_index(circle10.z_index+1)
        self.play(FadeIn(table10, circle10_label))
        self.play(Create(circle9))
        self.play(FadeIn(table9, circle9_label))
        self.wait(3)
        prompt_image = ImageMobject("resources/image (7).png").scale(0.2).next_to([-6.5,0,0])
        self.play(FadeIn(prompt_image))
        command3 = Text("SELECT * FROM Customers\nRIGHT JOIN Orders\nON\nCustomers.ID = Orders.CustomerID;", font=font_to_use, line_spacing=1).scale(0.4).next_to(prompt_image)
        command3[0:6].set_color(ORANGE)
        command3[7:11].set_color(ORANGE)
        command3[20:29].set_color(ORANGE)
        command3[35:37].set_color(ORANGE)
        self.play(Write(command3))
        self.wait(2)
        right_join_result = circle10.copy()
        right_join_result.set_fill(color=YELLOW, opacity=.5)
        right_join_result.set_stroke(color=None, opacity=0)  
        table11 = Table([["ID", "Name", "OrderID", "CustomerID","Product"],
                         ["2", "Bob", "101","2", "Book"],
                         ["3", "Charlie", "102","3", "Pen"],
                         ["NULL", "NULL", "103", "5", "Notebook"]],include_outer_lines=True, line_config={'color':YELLOW}).scale(0.3).move_to([-2.4,-2.5,0])
        table11.add_highlighted_cell((2,1), color=GREEN)
        table11.add_highlighted_cell((3,1), color=GREEN)
        table11.add_highlighted_cell((4,1), color=RED)
        table11.add_highlighted_cell((4,2), color=RED)
        table11.add_highlighted_cell((2,4), color=GREEN)
        table11.add_highlighted_cell((3,4), color=GREEN)
        table11.add_highlighted_cell((4,4), color=GREEN)
        self.play(ReplacementTransform(right_join_result,table11))
        self.wait(20)
        self.play(FadeOut(circle9, table9, circle10, table10, circle9_label, circle10_label, prompt_image, command3, table11))
        self.wait(2)
        
        
        
        
        
        full_join = Text("FULL OUTER JOIN", font=font_to_use).scale(0.6).next_to(title,DOWN)
        full_join.set_stroke(color=BLACK,opacity=1)
        highlighting_rectangle4 = Rectangle(width=3.7,height=0.28).move_to([0.1,2.26,0])
        highlighting_rectangle4.set_fill(color=LIGHT_PINK, opacity=.5)
        highlighting_rectangle4.set_stroke(color=None, opacity=0)
        self.play(ReplacementTransform(highlighting_rectangle3,highlighting_rectangle4))
        self.play(ReplacementTransform(right_join,full_join))
        self.wait(2)
        circle9 = Circle(radius=2, color="#0e9594").move_to([1.8,0,0])
        circle9.set_fill(color="#0e9594", opacity=0.5)
        circle9.set_stroke(color=None)
        self.play(Create(circle9))
        table9 = Table([["ID", "Name"],
                        ["1", "Alice"],
                        ["2", "Bob"],
                        ["3", "Charlie"],
                        ["4", "Diana"]], include_outer_lines=True, line_config={'color':YELLOW}).scale(0.2).move_to(circle9.get_center()+[-0.5,0,0])
        table9.add_highlighted_cell((3,1), color=GREEN)
        table9.add_highlighted_cell((4,1), color=GREEN)
        table9.add_highlighted_cell((5,1), color=GREEN)
        table9.add_highlighted_cell((2,1), color=GREEN)
        table9.set_z_index(circle9.z_index+1)
        circle9_label = Text("Customers", font=font_to_use).scale(0.5).next_to(table9,UP)
        circle9_label.set_z_index(circle9.z_index+1)
        self.play(FadeIn(table9, circle9_label))
        
        circle10 = Circle(radius=2, color=PINK).move_to([4.8,0,0])
        circle10.set_fill(color=PINK, opacity=0.5)
        circle10.set_stroke(color=None)
        circle10.set_z_index(circle9.z_index+1)
        self.play(Create(circle10))
        table10 = Table([["OrderId", "CustomerID", "Product"],
                        ["101", "2", "Book"],
                        ["102", "3", "Pen"],
                        ["103", "5", "Notebook"]], include_outer_lines=True, line_config={'color':YELLOW}).scale(0.2).move_to(circle10.get_center()+[0.5,0,0])
        table10.add_highlighted_cell((2,2), color=GREEN)
        table10.add_highlighted_cell((3,2), color=GREEN)
        table10.add_highlighted_cell((4,2), color=GREEN)
        table10.set_z_index(circle10.z_index+1)
        circle10_label = Text("Orders", font=font_to_use).scale(0.5).next_to(table10,UP)
        circle10_label.set_z_index(circle10.z_index+1)
        self.play(FadeIn(table10, circle10_label))
        self.wait(3)
        prompt_image = ImageMobject("resources/image (7).png").scale(0.2).next_to([-6.5,0,0])
        self.play(FadeIn(prompt_image))
        command4 = Text("SELECT * FROM Customers\nFULL OUTER JOIN Orders\nON\nCustomers.ID = Orders.CustomerID;", font=font_to_use, line_spacing=1).scale(0.4).next_to(prompt_image)
        command4[0:6].set_color(ORANGE)
        command4[7:11].set_color(ORANGE)
        command4[20:33].set_color(ORANGE)
        command4[39:41].set_color(ORANGE)
        self.play(Write(command4))
        self.wait(2)
        full_join_result = Union(circle9,circle10, color=YELLOW, fill_opacity=.5, stroke_width=0)   
        table11 = Table([["ID", "Name", "OrderID", "CustomerID","Product"],
                        ["1", "Alice", "NULL","NULL", "NULL"],
                         ["2", "Bob", "101","2", "Book"],
                         ["3", "Charlie", "102","3", "Pen"],
                         ["4", "Diana", "NULL", "NULL", "NULL"],
                         ["NULL", "NULL", "103", "5", "Notebook"]],include_outer_lines=True, line_config={'color':YELLOW}).scale(0.3).move_to([-2.9,-2.5,0])
        table11.add_highlighted_cell((2,1), color=GREEN)
        table11.add_highlighted_cell((3,1), color=GREEN)
        table11.add_highlighted_cell((4,1), color=GREEN)
        table11.add_highlighted_cell((5,1), color=GREEN)
        table11.add_highlighted_cell((6,1), color=RED)
        table11.add_highlighted_cell((2,3), color=RED)
        table11.add_highlighted_cell((2,4), color=RED)
        table11.add_highlighted_cell((2,5), color=RED)
        table11.add_highlighted_cell((5,3), color=RED)
        table11.add_highlighted_cell((5,4), color=RED)
        table11.add_highlighted_cell((5,5), color=RED)
        table11.add_highlighted_cell((6,2), color=RED)
        table11.add_highlighted_cell((3,4), color=GREEN)
        table11.add_highlighted_cell((4,4), color=GREEN)
        table11.add_highlighted_cell((6,4), color=GREEN)
        self.play(ReplacementTransform(full_join_result,table11))
        self.wait(20)
        self.play(FadeOut(circle9, table9, circle10, table10, circle9_label, circle10_label, prompt_image, command4, table11))
        self.wait(2)
        
        
        
        self_join = Text("SELF JOIN", font=font_to_use).scale(0.6).next_to(title,DOWN)
        self_join.set_stroke(color=BLACK,opacity=1)
        highlighting_rectangle5 = Rectangle(width=2,height=0.28).move_to([0.1,2.26,0])
        highlighting_rectangle5.set_fill(color=LIGHT_PINK, opacity=.5)
        highlighting_rectangle5.set_stroke(color=None, opacity=0)
        self.play(ReplacementTransform(highlighting_rectangle4,highlighting_rectangle5))
        self.play(ReplacementTransform(full_join,self_join))
        self.wait(2)
        circle9 = Circle(radius=2, color="#0e9594").move_to([2.3,0,0])
        circle9.set_fill(color="#0e9594", opacity=0.5)
        circle9.set_stroke(color=None)
        self.play(Create(circle9))
        table9 = Table([["EmployeeID", "EmployeeName", "ManagerID"],
                        ["1", "John","3"],
                        ["2", "Emma","1"],
                        ["3", "Alice","NULL"],
                        ], include_outer_lines=True, line_config={'color':YELLOW}).scale(0.2).move_to(circle9.get_center())
        table9.set_z_index(circle9.z_index+1)
        table9.add_highlighted_cell((2,1),color=GREEN)
        table9.add_highlighted_cell((3,1),color=GREEN)
        table9.add_highlighted_cell((4,1),color=GREEN)
        table9.add_highlighted_cell((2,3),color=GREEN)
        table9.add_highlighted_cell((3,3),color=GREEN)
        table9.add_highlighted_cell((4,3),color=RED)
        circle9_label = Text("Employees", font=font_to_use).scale(0.5).next_to(table9,UP)
        circle9_label.set_z_index(circle9.z_index+1)
        self.play(FadeIn(table9, circle9_label))
        
        
        prompt_image = ImageMobject("resources/image (7).png").scale(0.2).next_to([-6.5,0,0])
        self.play(FadeIn(prompt_image))
        command5 = Text("SELECT e1.EmployeeName AS Employee,\ne2.EmployeeName AS Manager\nFROM Employees e1\nLEFT JOIN Employees e2\nON e1.ManagerID = e2.EmployeeID;", font=font_to_use, line_spacing=1).scale(0.4).next_to(prompt_image)
        command5[0:6].set_color(ORANGE)
        command5[21:23].set_color(ORANGE)
        command5[47:49].set_color(ORANGE)
        command5[56:60].set_color(ORANGE)
        command5[71:79].set_color(ORANGE)
        command5[90:92].set_color(ORANGE)
        self.play(Write(command5))
        
        self_arrow = CurvedArrow(circle9.get_top(), circle9.get_center()+[2.2,0,0], tip_length=0.2,angle=180*DEGREES, color="#0e9594").flip().rotate(88*DEGREES).shift(RIGHT*0.5+UP*0.38)
        self.play(Create(self_arrow))
        self.wait(2)
        self_join_result = circle9.copy()  
        table11 = Table([["Employee", "Manager"],
                        ["John","Alice"],
                         ["Emma", "John"],
                         ["Alice", "NULL"]
                         ],include_outer_lines=True, line_config={'color':YELLOW}).scale(0.3).move_to([-2.9,-2.5,0])
        table11.add_highlighted_cell((4,2), color=RED)
        self.play(ReplacementTransform(self_join_result,table11))
        self.wait(20)
        self.play(FadeOut(circle9, table9,  circle9_label, prompt_image, command5, table11, self_arrow))
        self.wait(2)
        
        
        
        cross_join = Text("CROSS JOIN", font=font_to_use).scale(0.6).next_to(title,DOWN)
        cross_join.set_stroke(color=BLACK,opacity=1)
        highlighting_rectangle6 = Rectangle(width=2.5,height=0.28).move_to([0.1,2.26,0])
        highlighting_rectangle6.set_fill(color=LIGHT_PINK, opacity=.5)
        highlighting_rectangle6.set_stroke(color=None, opacity=0)
        self.play(ReplacementTransform(highlighting_rectangle5,highlighting_rectangle6))
        self.play(ReplacementTransform(self_join, cross_join))
        self.wait(2)
        circle9 = Circle(radius=2, color="#0e9594").move_to([1.8,0,0])
        circle9.set_fill(color="#0e9594", opacity=0.5)
        circle9.set_stroke(color=None)
        self.play(Create(circle9))
        table9 = Table([["Size"],
                        ["Small"],
                        ["Medium"],
                        ["Large"],
                    ], include_outer_lines=True, line_config={'color':YELLOW}).scale(0.3).move_to(circle9.get_center())
       
        table9.set_z_index(circle9.z_index+1)
        circle9_label = Text("TShirt_sizes", font=font_to_use).scale(0.5).next_to(table9,UP)
        circle9_label.set_z_index(circle9.z_index+1)
        self.play(FadeIn(table9, circle9_label))
        
        circle10 = Circle(radius=2, color=PINK).move_to([4.8,0,0])
        circle10.set_fill(color=PINK, opacity=0.5)
        circle10.set_stroke(color=None)
        circle10.set_z_index(circle9.z_index+1)
        self.play(Create(circle10))
        table10 = Table([["Color"],
                        ["Red"],
                        ["Blue"],
                        ["Green"]], include_outer_lines=True, line_config={'color':YELLOW}).scale(0.3).move_to(circle10.get_center())
       
        table10.set_z_index(circle10.z_index+1)
        circle10_label = Text("TShirt_colors", font=font_to_use).scale(0.5).next_to(table10,UP)
        circle10_label.set_z_index(circle10.z_index+1)
        self.play(FadeIn(table10, circle10_label))
        self.wait(3)
        prompt_image = ImageMobject("resources/image (7).png").scale(0.2).next_to([-6.5,1.5,0])
        self.play(FadeIn(prompt_image))
        command6 = Text("SELECT S.Size,C.Color\nFROM TShirt_sizes S\nCROSS JOIN TShirt_colors C;", font=font_to_use, line_spacing=1).scale(0.4).next_to(prompt_image)
        command6[0:6].set_color(ORANGE)
        command6[20:24].set_color(ORANGE)
        command6[37:46].set_color(ORANGE)
        conn1 = Arrow(table9.get_cell((2,0)).get_center()+[0.4,0,0],table10.get_cell((2,0)).get_center()+[-0.2,0,0],tip_length=0.1,stroke_width=1.5,buff=0.1)
        conn1.set_z_index(10)
        conn2 = Arrow(table9.get_cell((2,0)).get_center()+[0.4,0,0],table10.get_cell((3,0)).get_center()+[-0.2,0,0],tip_length=0.1,stroke_width=1.5,buff=0.1)
        conn2.set_z_index(10)
        conn3 = Arrow(table9.get_cell((2,0)).get_center()+[0.4,0,0],table10.get_cell((4,0)).get_center()+[-0.2,0,0],tip_length=0.1,stroke_width=1.5,buff=0.1)
        conn3.set_z_index(10)
        conn4 = Arrow(table9.get_cell((3,0)).get_center()+[0.4,0,0],table10.get_cell((2,0)).get_center()+[-0.2,0,0],tip_length=0.1,stroke_width=1.5,buff=0.1)
        conn4.set_z_index(10)
        conn5 = Arrow(table9.get_cell((3,0)).get_center()+[0.4,0,0],table10.get_cell((3,0)).get_center()+[-0.2,0,0],tip_length=0.1,stroke_width=1.5,buff=0.1)
        conn5.set_z_index(10)
        conn6 = Arrow(table9.get_cell((3,0)).get_center()+[0.4,0,0],table10.get_cell((4,0)).get_center()+[-0.2,0,0],tip_length=0.1,stroke_width=1.5,buff=0.1)
        conn6.set_z_index(10)
        conn7 = Arrow(table9.get_cell((4,0)).get_center()+[0.4,0,0],table10.get_cell((2,0)).get_center()+[-0.2,0,0],tip_length=0.1,stroke_width=1.5,buff=0.1)
        conn7.set_z_index(10)
        conn8 = Arrow(table9.get_cell((4,0)).get_center()+[0.4,0,0],table10.get_cell((3,0)).get_center()+[-0.2,0,0],tip_length=0.1,stroke_width=1.5,buff=0.1)
        conn8.set_z_index(10)
        conn9 = Arrow(table9.get_cell((4,0)).get_center()+[0.4,0,0],table10.get_cell((4,0)).get_center()+[-0.2,0,0],tip_length=0.1,stroke_width=1.5,buff=0.1)
        conn9.set_z_index(10)
        table11 = Table([["Size", "Color"],
                         ["Small", "Red"],
                         ["Small", "Blue"], 
                         ["Small", "Green"],
                         ["Medium", "Red"],
                         ["Medium", "Blue"],
                         ["Medium", "Green"],
                         ["Large", "Red"],
                         ["Large", "Blue"],
                         ["Large", "Green"]],include_outer_lines=True, line_config={'color':YELLOW}).scale(0.3).move_to([-3,-1.3,0])
        cell1 = VGroup(table11.get_cell((1,1)),table11.get_cell((1,2)),table11.get_rows()[0])
        self.play(Write(command6), FadeIn(cell1))
        self.play(GrowArrow(conn1))
        cell2 = VGroup(table11.get_cell((2,1)),table11.get_cell((2,2)),table11.get_rows()[1])
        self.play(FadeIn(cell2), run_time=0.5)
        self.play(GrowArrow(conn2), run_time=0.5)
        cell3 = VGroup(table11.get_cell((3,1)),table11.get_cell((3,2)),table11.get_rows()[2])
        self.play(FadeIn(cell3), run_time=0.5)
        self.play(GrowArrow(conn3), run_time=0.5)
        cell4 = VGroup(table11.get_cell((4,1)),table11.get_cell((4,2)),table11.get_rows()[3])
        self.play(FadeIn(cell4), run_time=0.5)
        self.play(GrowArrow(conn4), run_time=0.5)
        cell5 = VGroup(table11.get_cell((5,1)),table11.get_cell((5,2)),table11.get_rows()[4])
        self.play(FadeIn(cell5), run_time=0.5)
        self.play(GrowArrow(conn5), run_time=0.5)
        cell6 = VGroup(table11.get_cell((6,1)),table11.get_cell((6,2)),table11.get_rows()[5])
        self.play(FadeIn(cell6), run_time=0.5)
        self.play(GrowArrow(conn6), run_time=0.5)
        cell7 = VGroup(table11.get_cell((7,1)),table11.get_cell((7,2)),table11.get_rows()[6])
        self.play(FadeIn(cell7), run_time=0.5)
        self.play(GrowArrow(conn7), run_time=0.5)
        cell8 = VGroup(table11.get_cell((8,1)),table11.get_cell((8,2)),table11.get_rows()[7])
        self.play(FadeIn(cell8), run_time=0.5)
        self.play(GrowArrow(conn8), run_time=0.5)
        cell9 = VGroup(table11.get_cell((9,1)),table11.get_cell((9,2)),table11.get_rows()[8])
        self.play(FadeIn(cell9), run_time=0.5)
        self.play(GrowArrow(conn9), run_time=0.5)
        cell10 = VGroup(table11.get_cell((10,1)),table11.get_cell((10,2)),table11.get_rows()[9])
        self.play(FadeIn(cell10), run_time=0.5)
        self.wait(20)
        self.play(FadeOut(circle9, table9, circle10, table10, circle9_label, circle10_label, prompt_image, command6,
                         cell1,cell2,cell3,cell4,cell5,cell6,cell7,cell8,cell9,cell10,
                         conn1,conn2,conn3,conn4,conn5,conn6,conn7,conn8,conn9))
        
        self.wait(2)
        
        union_all = Text("UNION ALL", font=font_to_use).scale(0.6).next_to(title,DOWN)
        union_all.set_stroke(color=BLACK,opacity=1)
        highlighting_rectangle7 = Rectangle(width=2.3,height=0.28).move_to([0.1,2.26,0])
        highlighting_rectangle7.set_fill(color=LIGHT_PINK, opacity=.5)
        highlighting_rectangle7.set_stroke(color=None, opacity=0)
        
        self.play(ReplacementTransform(highlighting_rectangle6,highlighting_rectangle7))
        self.play(ReplacementTransform(cross_join, union_all))
        self.wait(2)
        circle9 = Circle(radius=1.5, color="#0e9594").move_to([3,1,0])
        circle9.set_fill(color="#0e9594", opacity=0.5)
        circle9.set_stroke(color=None)
        self.play(Create(circle9))
        table9 = Table([["Fruit"],
                        ["Apple"],
                        ["Banana"],
                        ["Cherry"],
                        ], include_outer_lines=True, line_config={'color':YELLOW}).scale(0.3).move_to(circle9.get_center())
        
        table9.set_z_index(circle9.z_index+1)
        circle9_label = Text("Fruits_A", font=font_to_use).scale(0.5).next_to(table9,UP, buff=0.1)
        circle9_label.set_z_index(circle9.z_index+1)
        self.play(FadeIn(table9, circle9_label))
        
        circle10 = Circle(radius=1.5, color=PINK).next_to(circle9,DOWN)
        circle10.set_fill(color=PINK, opacity=0.5)
        circle10.set_stroke(color=None)
        circle10.set_z_index(circle9.z_index+1)
        self.play(Create(circle10))
        table10 = Table([["Fruit"],
                        ["Banana"],
                        ["Dragonfruit"],
                        ["Cherry"]], include_outer_lines=True, line_config={'color':YELLOW}).scale(0.3).move_to(circle10.get_center())
        table10.set_z_index(circle10.z_index+1)
        circle10_label = Text("Fruits_B", font=font_to_use).scale(0.5).next_to(table10,UP,buff=0.1)
        circle10_label.set_z_index(circle10.z_index+1)
        self.play(FadeIn(table10, circle10_label))
        self.wait(3)
        prompt_image = ImageMobject("resources/image (7).png").scale(0.2).next_to([-6.5,1,0])
        self.play(FadeIn(prompt_image))
        command6 = Text("SELECT Fruit FROM Fruits_A\nUNION ALL\nSELECT Fruit FROM Fruits_B;", font=font_to_use, line_spacing=1).scale(0.4).next_to(prompt_image)
        command6[0:6].set_color(ORANGE)
        command6[11:15].set_color(ORANGE)
        command6[23:31].set_color(ORANGE)
        command6[31:37].set_color(ORANGE)
        command6[42:46].set_color(ORANGE)
        self.play(Write(command6))
        self.wait(2) 
        table9_copy = table9.copy()
        table10_copy = Table([["Banana"],
                        ["Dragonfruit"],
                        ["Cherry"]], include_outer_lines=True, line_config={'color':YELLOW}).scale(0.3).move_to(circle10.get_center())
        self.play(table9_copy.animate.move_to([-2,-1,0]))
        self.play(table10_copy.animate.next_to(table9_copy,DOWN,buff=0))
        self.wait(2)
        table11 = Table([["Fruit"],
                         ["Apple"],
                         ["Banana"],
                         ["Cherry"],
                         ["Banana"],
                         ["Dragonfruit"],
                         ["Cherry"]],include_outer_lines=True, line_config={'color':YELLOW}).scale(0.3).move_to(VGroup(table9_copy,table10_copy).get_center())
        self.play(FadeTransform(VGroup(table9_copy,table10_copy),table11,stretch=False, dim_to_match=0), run_time=2)
        self.wait(20)
        self.play(FadeOut(table9,table10,circle9,circle10,circle9_label,circle10_label,prompt_image,command6,table11))
        
        
        
        
        
        
        union = Text("UNION ", font=font_to_use).scale(0.6).next_to(title,DOWN)
        union.set_stroke(color=BLACK,opacity=1)
        highlighting_rectangle8 = Rectangle(width=1.5,height=0.28).move_to([0.1,2.26,0])
        highlighting_rectangle8.set_fill(color=LIGHT_PINK, opacity=.5)
        highlighting_rectangle8.set_stroke(color=None, opacity=0)
        
        
        self.play(ReplacementTransform(highlighting_rectangle7,highlighting_rectangle8))
        self.play(ReplacementTransform(union_all,union))
        self.wait(2)
        circle9 = Circle(radius=1.5, color="#0e9594").move_to([3,1,0])
        circle9.set_fill(color="#0e9594", opacity=0.5)
        circle9.set_stroke(color=None)
        self.play(Create(circle9))
        table9 = Table([["Fruit"],
                        ["Apple"],
                        ["Banana"],
                        ["Cherry"],
                        ], include_outer_lines=True, line_config={'color':YELLOW}).scale(0.3).move_to(circle9.get_center())
        
        table9.set_z_index(circle9.z_index+1)
        circle9_label = Text("Fruits_A", font=font_to_use).scale(0.5).next_to(table9,UP, buff=0.1)
        circle9_label.set_z_index(circle9.z_index+1)
        self.play(FadeIn(table9, circle9_label))
        
        circle10 = Circle(radius=1.5, color=PINK).next_to(circle9,DOWN)
        circle10.set_fill(color=PINK, opacity=0.5)
        circle10.set_stroke(color=None)
        circle10.set_z_index(circle9.z_index+1)
        self.play(Create(circle10))
        table10 = Table([["Fruit"],
                        ["Banana"],
                        ["Dragonfruit"],
                        ["Cherry"]], include_outer_lines=True, line_config={'color':YELLOW}).scale(0.3).move_to(circle10.get_center())
        table10.set_z_index(circle10.z_index+1)
        circle10_label = Text("Fruits_B", font=font_to_use).scale(0.5).next_to(table10,UP,buff=0.1)
        circle10_label.set_z_index(circle10.z_index+1)
        self.play(FadeIn(table10, circle10_label))
        self.wait(3)
        prompt_image = ImageMobject("resources/image (7).png").scale(0.2).next_to([-6.5,1,0])
        self.play(FadeIn(prompt_image))
        command6 = Text("SELECT Fruit FROM Fruits_A\nUNION\nSELECT Fruit FROM Fruits_B;", font=font_to_use, line_spacing=1).scale(0.4).next_to(prompt_image)
        command6[0:6].set_color(ORANGE)
        command6[11:15].set_color(ORANGE)
        command6[23:28].set_color(ORANGE)
        command6[28:34].set_color(ORANGE)
        command6[39:43].set_color(ORANGE)
        self.play(Write(command6))
        self.wait(2) 
        table9_copy = table9.copy()
        table10_copy = Table([
                        ["Dragonfruit"],
                        ], include_outer_lines=True, line_config={'color':YELLOW}).scale(0.3).move_to(circle10.get_center())
        self.play(table9_copy.animate.move_to([-2,-1,0]))
        self.play(table10_copy.animate.next_to(table9_copy,DOWN,buff=0))
        self.wait(2)
        table11 = Table([["Fruit"],
                         ["Apple"],
                         ["Banana"],
                         ["Cherry"],
                         ["Dragonfruit"],
                         ],include_outer_lines=True, line_config={'color':YELLOW}).scale(0.3).move_to(VGroup(table9_copy,table10_copy).get_center())
        self.play(FadeTransform(VGroup(table9_copy,table10_copy),table11,stretch=False, dim_to_match=0), run_time=2)
        self.wait(20)
        self.play(FadeOut(table9,table10,circle9,circle10,circle9_label,circle10_label,prompt_image,command6,table11))
        
        
        
        
        
        
        
        join_vs_union = Text("JOIN vs UNION", font=font_to_use).scale(0.6).next_to(title,DOWN)
        join_vs_union.set_stroke(color=BLACK,opacity=1)
        highlighting_rectangle9 = Rectangle(width=3,height=0.28).move_to([0.1,2.26,0])
        highlighting_rectangle9.set_fill(color=LIGHT_PINK, opacity=.5)
        highlighting_rectangle9.set_stroke(color=None, opacity=0)
        self.play(ReplacementTransform(highlighting_rectangle8,highlighting_rectangle9))
        self.play(ReplacementTransform(union,join_vs_union))
        join_heading = Text("JOIN", font=font_to_use, color=YELLOW).scale(0.5).move_to([-3,1.5,0])
        union_heading = Text("UNION", font=font_to_use, color=YELLOW).scale(0.5).move_to([3,1.5,0])
        sep_line = Line([0,1,0], [0,-3.5,0], color=YELLOW)
        self.add(join_heading)
        self.add(union_heading)
        self.play(Create(sep_line))
        
        table1 = Table([['0','0'],
                        ['0','0']], include_outer_lines=True, line_config={'color':BLUE}).scale(0.2).move_to([-4,0.5,0])
        table1.get_rows().set_opacity(0)
        table2 = Table([["0", "0"],
                        ["0", "0"],], include_outer_lines=True, line_config={'color':GREEN}).scale(0.2).next_to(table1, RIGHT*4)
        table2.get_rows().set_opacity(0)
        table3 = Table([['0','0'],
                        ['0','0']], include_outer_lines=True, line_config={'color':BLUE}).scale(0.2).move_to([3,0.5,0])
        table3.get_rows().set_opacity(0)
        table4 = Table([["0", "0"],
                        ["0", "0"],], include_outer_lines=True, line_config={'color':GREEN}).scale(0.2).next_to(table3, RIGHT*4)
        table4.get_rows().set_opacity(0)
        self.play(FadeIn(table1,table2,table3,table4))
        self.wait(1)
        join_point1 = Text("Think of a JOIN as horizontally combining tables together", font=font_to_use).scale(0.3).move_to([-3.8,-0.8,0])
        join_point1_marker = Dot(radius=0.05,color=YELLOW).next_to(join_point1,LEFT,buff=0.1)
        join_point2 = Text("A JOIN uses a key or value to help organise what's records\nto join together via related columns", font=font_to_use, line_spacing=1).scale(0.3).next_to([-6.85,-1.4,0], aligned_edge=LEFT)
        join_point2_marker = Dot(radius=0.05,color=YELLOW).next_to(join_point2,LEFT,buff=0.1)
        join_point3 = Text("Tables can be joined together in many different ways", font=font_to_use).scale(0.3).move_to([-4,-2,0])
        join_point3_marker = Dot(radius=0.05,color=YELLOW).next_to(join_point3,LEFT,buff=0.1)
        join_point4 = Text("The most common types of join are INNER, LEFT, RIGHT & FULL",font=font_to_use).scale(0.3).move_to([-3.45,-2.5,0])
        join_point4_marker = Dot(radius=0.05,color=YELLOW).next_to(join_point4,LEFT,buff=0.1)
        union_point1 = Text("Think of a UNION as vertically combining tables together", font=font_to_use).scale(0.3).move_to([3.4,-0.8,0])
        union_point1_marker = Dot(radius=0.05,color=YELLOW).next_to(union_point1,LEFT,buff=0.1)
        union_point2 = Text("A UNION uses an equal number of columns to combine tables\ntogether via a SELECT statement", font=font_to_use, line_spacing=1).scale(0.3).next_to([0.37,-1.4,0], aligned_edge=LEFT)
        union_point2_marker = Dot(radius=0.05,color=YELLOW).next_to(union_point2,LEFT,buff=0.1)
        union_point3 = Text("You can use a UNION ALL to combine tables and records\nwhilst keeping duplicate records", font=font_to_use, line_spacing=1).scale(0.3).next_to([0.37,-2.2,0], aligned_edge=LEFT)
        union_point3_marker = Dot(radius=0.05,color=YELLOW).next_to(union_point3,LEFT,buff=0.1)
        union_point4 = Text("You can use UNION to combine tables and records but \nremove duplicate records", font=font_to_use, line_spacing=1).scale(0.3).next_to([0.37,-3,0], aligned_edge=LEFT)
        union_point4_marker = Dot(radius=0.05,color=YELLOW).next_to(union_point4,LEFT,buff=0.1)
        self.play(Create(join_point1_marker),Write(join_point1),Create(union_point1_marker),Write(union_point1),table2.animate.next_to(table1,buff=0),table4.animate.next_to(table3,DOWN,buff=0))
        self.wait(3)
        self.play(Create(join_point2_marker),Write(join_point2),Create(union_point2_marker),Write(union_point2))
        self.wait(3)
        self.play(Create(join_point3_marker),Write(join_point3),Create(union_point3_marker),Write(union_point3))
        self.wait(3)
        self.play(Create(join_point4_marker),Write(join_point4),Create(union_point4_marker),Write(union_point4))
        self.wait(15)