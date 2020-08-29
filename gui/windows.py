from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from data.PassiveData import PassiveData
from database.PassiveDataFactory import get_passive_data


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
        database = get_passive_data()
        self.db_preview.text = parse_passive_data_to_list(database)

    def btn_inspection(self):
        screen2 = self.manager.get_screen('passive_data_inspector')
        screen2.ids.item_id.text = self.id_input.text


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

    db = get_passive_data()

    def on_enter(self, *args):
        data = self.db[int(self.item_id.text) - 1]
        self.namee.text = str(data.name)
        self.producer.text = str(data.producer)
        self.model.text = str(data.model)
        self.serial_number.text = str(data.serial_number)
        self.activation_date.text = str(data.activation_date)
        self.purchase_date.text = str(data.acquire_date)
        self.ports.text = str(data.ports)
        self.other.text = str(data.other)


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