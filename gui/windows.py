from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from gui.screens.main_window import MainWindow
from gui.screens.database_list import DatabaseList
from gui.screens.active_data_inspector import ActiveDataInspector
from gui.screens.passive_data_inspector import PassiveDataInspector
from gui.screens.related_document_inspector import RelatedDocumentInspector


class WindowManager(ScreenManager):
    pass


kivy_builder = Builder.load_file('./gui/layout.kv')
sm = WindowManager()

screens = [MainWindow(name='main_window'),
           DatabaseList(name='database_list'),
           PassiveDataInspector(name='passive_data_inspector'),
           ActiveDataInspector(name='active_data_inspector'),
           RelatedDocumentInspector(name='related_document_inspector')]
for screen in screens:
    sm.add_widget(screen)


class AppMain(App):
    def build(self):
        return kivy_builder
