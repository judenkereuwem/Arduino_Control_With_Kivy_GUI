from kivy.app import App
from kivy.metrics import dp
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget


import serial
import time

ser = serial.Serial('COM7', 9600, timeout=1)
time.sleep(2)



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

    slider_value_txt = StringProperty("Value")


    def on_switch_active(self, widget):
        print("Switch " + str(widget.active))
        if widget.active == True:
            ser.write([int(widget.value)])
            #print("led on")
        if widget.active == False:
            ser.write(b'L')
            #print("led off")

    def on_slider_value(self, widget):
        print("Slider: " + str(int(widget.value)))
        #self.slider_value_txt = str(int(widget.value))
        ser.write([int(widget.value)])



             


class MainWidget(Widget):
    pass

class TheLabApp(App):
    pass




TheLabApp().run()
#BoxLayoutExample()#.run()

ser.close()
