from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty

ID = "123456789"
NAME = "Drukarka"
PRODUCER = "BIGBRO"
MODEL = "DCP-J315"
SERIAL_NUMBER = "123456"
ACTIVATION_DATE = "DEJT 1"
PURCHASE_DATE = "DEJT 2"
PORTS = "PORTS 1, PORTS 2"
OTHER = "AHJOs"


class MainWindow(Screen):
    pass


class PassiveDataInspector(Screen):
    item_id = ObjectProperty(None)
    namee = ObjectProperty(None)
    producer = ObjectProperty(None)
    model = ObjectProperty(None)
    serial_number = ObjectProperty(None)
    activation_date = ObjectProperty(None)
    purchase_date = ObjectProperty(None)
    ports = ObjectProperty(None)
    other = ObjectProperty(None)

    def on_enter(self, *args):
        self.item_id.text = ID
        self.namee.text = NAME
        self.producer.text = PRODUCER
        self.model.text = MODEL
        self.serial_number.text = SERIAL_NUMBER
        self.activation_date.text = ACTIVATION_DATE
        self.purchase_date.text = PURCHASE_DATE
        self.ports.text = PORTS
        self.other.text = OTHER

class WindowManager(ScreenManager):
    pass


kivy_builder = Builder.load_file("./gui/windows.kv")
sm = WindowManager()

screens = [PassiveDataInspector(name="passive_data_inspector"), MainWindow(name="main")]
for screen in screens:
    sm.add_widget(screen)


class AppMain(App):
    def build(self):
        return kivy_builder
