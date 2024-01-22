from manim import *


class Editor(VMobject):
    def __init__(self, *args, **kwargs):
        self.font_to_use = "resources/resources/Quicksand-VariableFont_wght.ttf"
        self.main_frame = Rectangle(width=9,height=5).set_stroke(color=None,opacity=0).set_fill(color=GREY_E,opacity=1)#.set_stroke(WHITE,opacity=.5)
        self.header_rectangle = Rectangle(width=9,height=0.5).set_stroke(color=None,opacity=0).set_fill(color=BLACK,opacity=.5).next_to(self.main_frame.get_left()+self.main_frame.get_top(),buff=0,aligned_edge=self.main_frame.get_top())
        self.logo = ImageMobject('resources/postgresql1.png').next_to(self.header_rectangle.get_left())
        self.pgadmin_text = Text("pgAdmin 4",font=self.font_to_use,color=BLUE_C).scale(0.4).next_to(self.logo)
        self.file_text = Text("File",font=self.font_to_use).scale(0.35).next_to(self.pgadmin_text)
        self.drop_down_arrow1 = ImageMobject('resources/drop_down_Arrow.png').scale(0.04).next_to(self.file_text,buff=0.1,aligned_edge=DOWN)
        self.object_text = Text("Object",font=self.font_to_use).scale(0.35).next_to(self.file_text,RIGHT*2)
        self.drop_down_arrow2 = ImageMobject('resources/drop_down_Arrow.png').scale(0.04).next_to(self.object_text,buff=0.1,aligned_edge=DOWN)
        self.tools_text = Text("Tools",font=self.font_to_use).scale(0.35).next_to(self.object_text,RIGHT*2)
        self.drop_down_arrow3 = ImageMobject('resources/drop_down_Arrow.png').scale(0.04).next_to(self.tools_text,buff=0.1,aligned_edge=DOWN)
        self.help_text = Text("Help",font=self.font_to_use).scale(0.35).next_to(self.tools_text,RIGHT*2)
        self.drop_down_arrow4 = ImageMobject('resources/drop_down_Arrow.png').scale(0.04).next_to(self.help_text,buff=0.1,aligned_edge=DOWN)
        self.dashboard_box = Rectangle(width=1.8,height=0.4).set_fill(color=GREY_D,opacity=1).set_stroke(color=None,opacity=0).next_to(self.header_rectangle,DOWN,buff=0,aligned_edge=self.main_frame.get_left())
        self.dashboard_logo = ImageMobject('resources/speedometer1.png').scale(0.08).next_to(self.dashboard_box.get_left()+[0.1,0,0],buff=0)
        self.dashboard_text = Text("Dashboard", font=self.font_to_use).scale(0.35).next_to(self.dashboard_logo,buff=0.1)
        self.properties_box = Rectangle(width=1.7,height=0.4).set_fill(color=GREY_D,opacity=1).set_stroke(color=None,opacity=0).next_to(self.dashboard_box,buff=0.02)
        self.properties_logo = ImageMobject('resources/settings_gear1.png').scale(0.08).next_to(self.properties_box.get_left()+[0.1,0,0],buff=0)
        self.properties_text = Text("Properties", font=self.font_to_use).scale(0.35).next_to(self.properties_logo,buff=0.1)
        self.query_box = Rectangle(width=4.8,height=0.4).set_fill(color=BLACK,opacity=0.5).set_stroke(color=None,opacity=0).next_to(self.properties_box,buff=0.03,aligned_edge=DOWN)
        self.query_box_line = Rectangle(width=4.8,height=0.01).set_fill(color=PURE_GREEN,opacity=1).set_stroke(color=None,opacity=0).next_to(self.query_box,UP,buff=0,aligned_edge=UP)
        self.query_logo = ImageMobject('resources/flash1.png').scale(0.06).next_to(self.query_box.get_left()+[0.1,0,0],buff=0)
        self.query_text = Text("Query-postgres on postgres@Postgres", font=self.font_to_use).scale(0.35).next_to(self.query_logo,buff=0.1)
        self.editor = Group(self.main_frame,self.header_rectangle,self.logo,self.pgadmin_text,
                            self.file_text,self.drop_down_arrow1, self.object_text,self.drop_down_arrow2,
                            self.tools_text,self.drop_down_arrow3,self.help_text,self.drop_down_arrow4,
                            self.dashboard_box,self.dashboard_logo,self.dashboard_text,self.properties_box,
                            self.properties_logo,self.properties_text,self.query_box,self.query_box_line,
                            self.query_logo,self.query_text)
        
        super().__init__(*args, **kwargs)
        self.add(self.editor)


class EditorCreation(Scene):
    def construct(self):
        self.add(Editor())
        self.wait(5)