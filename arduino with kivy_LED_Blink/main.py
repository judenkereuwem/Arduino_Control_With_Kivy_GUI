from kivy.app import App
from kivy.metrics import dp
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget
from kivy.graphics.vertex_instructions import Line, Rectangle, Ellipse
from kivy.graphics.context_instructions import Color
from kivy.properties import Clock

import serial
import time

ser = serial.Serial('COM7', 9600, timeout=1)
time.sleep(2)

class CanvasExample1(Widget):
    pass

class CanvasExample2(Widget):
    pass

class CanvasExample3(Widget):
    pass

class CanvasExample4(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Line(points=(100, 100, 400, 500), width=2)
            Color(0, 1, 0)
            Line(circle=(400, 200, 80), width=2)
            Line(rectangle=(700, 500, 150, 100), width=3)
            self.rect = Rectangle(pos=(700, 200), size=(150, 100))

    def on_button_a_click(self):
        #print("foo")
        x, y = self.rect.pos
        w, h = self.rect.size
        inc = dp(10)

        diff = self.width - (x+w)
        if diff < inc:
            inc = diff
            
        x += inc
        self.rect.pos = (x, y)




        

#increment number with button click
class WidgetsExample(GridLayout):
    count = 1
    #count_enabled = False
    count_enabled = BooleanProperty(False)
    my_text = StringProperty("1")
    text_input_str = StringProperty("boom")
    # slider_value_txt = StringProperty("Value")
    
    def on_button_click(self):
        print("Button clicked")
        if self.count_enabled:
            self.count += 1
            self.my_text = str(self.count)

    def on_toggle_button_state(self, widget):
        print("Toggle state: " + widget.state)
        if widget.state == "normal":
            widget.text = "OFF"
            self.count_enabled = False
        else:
            widget.state == "down"
            widget.text = "ON"
            self.count_enabled = True

    def on_switch_active(self, widget):
        print("Switch " + str(widget.active))
        if widget.active == True:
            ser.write(b'H')
            print("led on")
        elif widget.active == False:
            ser.write(b'L')
            print("led off")






    
        
###increment number with button click
##class WidgetsExample(GridLayout):
##    count = 1
##    my_text = StringProperty("1")
##    
##    def on_button_click(self):
##        print("Button clicked")
##        self.count += 1
##        self.my_text = str(self.count)
##
##    def on_toggle_button_state(self, widget):
##        print("Toggle state: " + widget.state)
##        if widget.state == "normal":
##            widget.text = "OFF"
##        else:
##            widget.state == "down"
##            widget.text = "ON"

             







class StackLayoutExample(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #self.orientation = "lr-tb"
        for i in range(0, 100):
            size = dp(100)
            b = Button(text=str(i+1), size_hint=(None, None), size=(size, size))
            self.add_widget(b)

#class GridLayoutExample(GridLayout):
    #pass

class AnchorLayoutExample(AnchorLayout):
    pass

class BoxLayoutExample(BoxLayout):
    pass
"""   def __init__(self, **kwargs):
        super().__init__(**kwargs)
        b1 = Button(text="A")
        b2 = Button(text="B")
        self.add_widget(b1)
        self.add_widget(b2)
"""

class MainWidget(Widget):
    pass

class TheLabApp(App):
    pass




TheLabApp().run()
#BoxLayoutExample()#.run()

ser.close()
