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


def confirmation_poup(title='Confirmation', msg='Generic msg', yes_action=information_poup):
    box_popup = BoxLayout(orientation='vertical')

    pop = Popup(title=title,
                content=box_popup,
                size_hint=(None, None), size=(400, 400))

    box_popup.add_widget(Label(text=msg))

    def callback(instance):
        yes_action(instance)
        pop.dismiss()

    box_popup.add_widget(Button(
        text="Yes",
        on_press=callback,
        size_hint=(1.0, 0.5)))

    box_popup.add_widget(Button(
        text="No",
        on_press=pop.dismiss,
        size_hint=(1.0, 0.5)))

    pop.open()


