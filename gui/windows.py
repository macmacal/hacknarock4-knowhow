from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

from kivy.uix.boxlayout import BoxLayout


class WindowManager(ScreenManager):
    pass


class MainWindow(Screen):
    pass


class PassiveDataInspector(Screen):
    pass


kivy_builder = Builder.load_file("./gui/windows.kv")

