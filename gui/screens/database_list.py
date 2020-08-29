from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from database.PassiveDataDAO import DataDAO
from gui.popup import information_poup
from data.PassiveData import PassiveData


class DatabaseList(Screen):
    db_preview = ObjectProperty(None)
    id_input = ObjectProperty(None)

    def parse_passive_data_to_list(self):
        data_list = ['ID  -  NAME']
        for it in DataDAO.get_passive_data():
            data_list.append('{}  -  {}'.format(str(it.id), str(it.name)))
        return "\n".join(data_list)

    def btn_inspect(self):
        if DataDAO.id_exists(int(self.id_input.text)):
            self.manager.get_screen('passive_data_inspector').item_id.text = self.id_input.text
            self.manager.current = 'passive_data_inspector'
        else:
            information_poup(msg='There is no item with ID {} !'.format(self.id_input.text))

    def btn_create_new(self):
        if DataDAO.id_exists(int(self.id_input.text)):
            information_poup(msg='Item with ID {} already exists !'.format(self.id_input.text))
        else:
            DataDAO.save_or_update_passive_data(PassiveData(id=int(self.id_input.text), name='New item'))
            self.manager.get_screen('passive_data_inspector').item_id.text = self.id_input.text
            self.manager.current = 'passive_data_inspector'

    def on_enter(self, *args):
        self.db_preview.text = self.parse_passive_data_to_list()
