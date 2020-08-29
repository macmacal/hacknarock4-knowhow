from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.modalview import ModalView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty, StringProperty


class ActiveDataInspector(Screen):
    text_input = ObjectProperty()
    text_preview = ObjectProperty()

    def showedit(self):
     #TODO: add parsing for [ref] markup formatting
        pass

    def btn_preview(self):
        self.text_preview.text = self.text_input.text
