from kivy.uix.screenmanager import Screen

from database.EntityDAO import DataDAO
from gui.popup import information_poup
from data.PassiveData import PassiveData
from PIL import Image
from pyzbar.pyzbar import decode
from VideoCapture import Device

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.label import Label
from kivy.properties import BooleanProperty, ListProperty, StringProperty, ObjectProperty
from kivy.uix.recyclegridlayout import RecycleGridLayout
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.popup import Popup


class TextInputPopup(Popup):
    obj = ObjectProperty(None)
    obj_text = StringProperty("")

    def __init__(self, obj, **kwargs):
        super(TextInputPopup, self).__init__(**kwargs)
        self.obj = obj
        self.obj_text = obj.text


class SelectableRecycleGridLayout(FocusBehavior, LayoutSelectionBehavior,
                                  RecycleGridLayout):
    """ Adds selection and focus behaviour to the view. """
    pass


class TableCell(RecycleDataViewBehavior, Label):
    """ Add selection support to the Button """
    index = None
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)

    def refresh_view_attrs(self, rv, index, data):
        """ Catch and handle the view changes """
        self.index = index
        return super(TableCell, self).refresh_view_attrs(rv, index, data)

    def update_changes(self, txt):
        self.text = txt


class DatabaseList(Screen):
    loaded_db = ListProperty([])

    db_preview = ObjectProperty(None)
    id_input = ObjectProperty(None)
    name_input = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.get_data()

    def get_data(self):
        self.loaded_db[:] = []
        for it in DataDAO.get_all_data():
            self.loaded_db.append('[b]{}[/b]'.format(str(it.id)))
            self.loaded_db.append('[i]{}[/i]'.format(str(it.name)))

    def parse_passive_data_to_list(self):
        data_list = []
        for it in DataDAO.get_all_data():
            data_list.append('{}  -  {}'.format(str(it.id), str(it.name)))
        return "\n".join(data_list)

    def btn_read_barcode(self):
        try:
            cam = Device()
            cam.saveSnapshot('codebars/photo.png')
        except:
            information_poup(msg='Failed to take a photo!')
            return
        try:
            data_decoded = decode(Image.open('codebars/photo.png'))
            self.id_input.text = data_decoded[0][0]
        except:
            information_poup(msg='Failed to read barcode!')

    def btn_inspect(self):
        if self.id_input.text == '' and self.name_input.text == '':
            information_poup(msg='Wrong parameters')
            return
        if self.id_input.text != '' or (self.id_input.text != '' and self.name_input.text != ''):
            if DataDAO.id_exists(int(self.id_input.text)):
                self.manager.get_screen('passive_data_inspector').item_id.text = self.id_input.text
                self.manager.current = 'passive_data_inspector'
            else:
                information_poup(msg='There is no item with ID {} !'.format(self.id_input.text))
                return
        if self.name_input.text != '':
            if DataDAO.name_exists(self.name_input.text):
                id = DataDAO.get_data_by_name(self.name_input.text).id
                self.manager.get_screen('passive_data_inspector').item_id.text = str(id)
                self.manager.current = 'passive_data_inspector'
            else:
                information_poup(msg='There is no item with name {} !'.format(self.id_input.text))
                return

    def btn_create_new(self):
        if self.id_input.text == '':
            information_poup(msg='Wrong ID')
            return
        if DataDAO.id_exists(int(self.id_input.text)):
            information_poup(msg='Item with ID {} already exists !'.format(self.id_input.text))
            return
        else:
            DataDAO.save_or_update_data(PassiveData(id=int(self.id_input.text), name='New item'))
            self.manager.get_screen('passive_data_inspector').item_id.text = self.id_input.text
            self.manager.current = 'passive_data_inspector'

    def on_enter(self, *args):
        # self.db_preview.text = self.parse_passive_data_to_list()
        self.get_data()
