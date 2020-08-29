from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


def information_poup(title='Information', msg='Generic msg'):
    box_popup = BoxLayout(orientation='vertical')

    pop = Popup(title=title,
                content=box_popup,
                size_hint=(None, None), size=(400, 400))

    box_popup.add_widget(Label(text=msg))

    box_popup.add_widget(Button(
        text="OK",
        on_press=pop.dismiss,
        size_hint=(1.0, 1.0)))

    pop.open()
