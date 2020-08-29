from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from data.PassiveData import PassiveData
from data.ActiveData import ActiveData
from database.EntityDAO import DataDAO
from gui.popup import information_poup
from gui.popup import confirmation_poup
from datetime import datetime
from ast import literal_eval


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
    tutorials = ObjectProperty(None)

    def on_enter(self, *args):
        if self.item_id.text != '':
            self.passive_data = DataDAO.get_data_by_id(int(self.item_id.text))
        else:
            self.passive_data = DataDAO.get_data_by_name(self.namee.text)

        self.show_passive_data()
        self.show_active_data()

    def btn_new_tutorial(self):
        pass

    def enter_tutorial(self, tutorial=''):
        self.manager.get_screen('active_data_inspector').text_title.text = tutorial
        self.manager.current = 'active_data_inspector'
        pass

    def btn_save(self):
        self.parse_to_passive_data()
        DataDAO.save_or_update_data(data=self.passive_data)
        information_poup(msg='The item has been saved!')

    def btn_delete(self):
        confirmation_poup(msg="Are you sure?", yes_action=self.delete_passive_data)

    def delete_passive_data(self, instance):
        DataDAO.remove_data_by_id(self.passive_data.id)
        self.manager.current = 'database_list'

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
        self.item_id.text = str(self.passive_data.id)
        self.namee.text = str(self.passive_data.name)
        self.producer.text = str(self.passive_data.producer)
        self.model.text = str(self.passive_data.model)
        self.serial_number.text = str(self.passive_data.serial_number)
        self.activation_date.text = self.passive_data.activation_date.strftime('%d/%m/%y %H:%M:%S')
        self.acquire_date.text = self.passive_data.acquire_date.strftime('%d/%m/%y %H:%M:%S')
        self.ports.text = str(self.passive_data.ports)
        self.other.text = str(self.passive_data.other)

    def show_active_data(self):
        tuts_list = []
        for i in self.passive_data.tutorials:
            tuts_list.append(' > [ref={}][b][u]{}[/u][/b][/ref]'.format(i.name, i.name))

        if len(tuts_list) == 0:
            self.tutorials.text = '[b]There are no tutorials for this item.[/b]'
        else:
            self.tutorials.text = '\n'.join(tuts_list)
