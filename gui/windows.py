from datetime import datetime
from ast import literal_eval
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from database.PassiveDataDAO import PassiveDataDAO
from data.PassiveData import PassiveData
from gui.popup import information_poup
import constants

DataDAO = PassiveDataDAO(constants.DATABASE_PATH)


def parse_passive_data_to_list(db=()):
    data_list = ["ID  -  NAME"]
    for it in db:
        data_list.append("{}  -  {}".format(str(it.id), str(it.name)))
    return "\n".join(data_list)


class MainWindow(Screen):
    pass


class DatabaseList(Screen):
    db_preview = ObjectProperty(None)
    id_input = ObjectProperty(None)

    def on_enter(self, *args):
        database = DataDAO.get_passive_data()
        self.db_preview.text = parse_passive_data_to_list(database)


class PassiveDataInspector(Screen):
    passive_data = PassiveData(id=1, name='generic')
    item_id = ObjectProperty(None)
    namee = ObjectProperty(None)
    producer = ObjectProperty(None)
    model = ObjectProperty(None)
    serial_number = ObjectProperty(None)
    activation_date = ObjectProperty(None)
    acquire_date = ObjectProperty(None)
    ports = ObjectProperty(None)
    other = ObjectProperty(None)

    def on_enter(self, *args):
        self.passive_data = DataDAO.get_passive_data_by_id(int(self.item_id.text))
        self.show_passive_data()

    def update_passive_data(self):
        self.parse_to_passive_data()
        DataDAO.save_or_update_passive_data(passive_data=self.passive_data)

    def parse_to_passive_data(self):
        self.passive_data.id = int(self.item_id.text)
        self.passive_data.name = self.namee.text
        self.passive_data.producer = self.producer.text
        self.passive_data.model = self.model.text
        self.passive_data.serial_number = self.serial_number.text
        self.passive_data.activation_date = datetime.strptime(self.activation_date.text, '%d/%m/%y %H:%M:%S')
        self.passive_data.acquire_date = datetime.strptime(self.acquire_date.text, '%d/%m/%y %H:%M:%S')
        self.passive_data.ports = literal_eval(self.ports.text)
        self.passive_data.other = literal_eval(self.other.text)

    def show_passive_data(self):
        self.namee.text = str(self.passive_data.name)
        self.producer.text = str(self.passive_data.producer)
        self.model.text = str(self.passive_data.model)
        self.serial_number.text = str(self.passive_data.serial_number)
        self.activation_date.text = self.passive_data.activation_date.strftime('%d/%m/%y %H:%M:%S')
        self.acquire_date.text = self.passive_data.acquire_date.strftime('%d/%m/%y %H:%M:%S')
        self.ports.text = str(self.passive_data.ports)
        self.other.text = str(self.passive_data.other)

    def popup_saved(self):
        information_poup(msg='The item has been saved!')


class WindowManager(ScreenManager):
    pass


kivy_builder = Builder.load_file("./gui/windows.kv")
sm = WindowManager()

screens = [DatabaseList(name="database_list"),
           PassiveDataInspector(name="passive_data_inspector"),
           MainWindow(name="main")]
for screen in screens:
    sm.add_widget(screen)


class AppMain(App):
    def build(self):
        return kivy_builder
