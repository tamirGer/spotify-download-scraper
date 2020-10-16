from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label

class WindowManager(ScreenManager):
    pass

class MainWindow(Screen):
    n = ObjectProperty(None)
    created = ObjectProperty(None)
    current = ""

kv = Builder.load_file("my.kv")
sm = WindowManager()
sm.add_widget(MainWindow(name="main"))

sm.current = "main"


class MyMainApp(App):
    def build(self):
        return sm


if __name__ == "__main__":
    MyMainApp().run()
