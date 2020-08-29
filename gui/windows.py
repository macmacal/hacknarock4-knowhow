from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from data.PassiveData import PassiveData
from database.PassiveDataFactory import get_passive_data

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
    data = get_passive_data()[0]

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
        self.item_id.text = str(self.data.id)
        self.namee.text = str(self.data.name)
        self.producer.text = str(self.data.producer)
        self.model.text = str(self.data.model)
        self.serial_number.text = str(self.data.serial_number)
        self.activation_date.text = str(self.data.activation_date)
        self.purchase_date.text = str(self.data.acquire_date)
        self.ports.text = str(self.data.ports)
        self.other.text = str(self.data.other)

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
