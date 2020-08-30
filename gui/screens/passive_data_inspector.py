from kivy.uix.screenmanager import Screen
from data.PassiveData import PassiveData
from data.ActiveData import ActiveData
from data.PDFData import PDFData
from database.DocumentDAO import DocumentDAO
from database.EntityDAO import DataDAO
from gui.popup import information_poup
from gui.popup import confirmation_poup
from datetime import datetime
from ast import literal_eval

from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.properties import BooleanProperty, ListProperty, StringProperty, ObjectProperty
from kivy.uix.recyclegridlayout import RecycleGridLayout
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.popup import Popup

from gui.screens.database_list import TableCell, SelectableRecycleGridLayout


class TextInputPopup(Popup):
    obj = ObjectProperty(None)
    obj_text = StringProperty("")

    def __init__(self, obj, **kwargs):
        super(TextInputPopup, self).__init__(**kwargs)
        self.obj = obj
        self.obj_text = obj.text


class EditableTableCell(RecycleDataViewBehavior, TextInput):
    """ Add selection support to the Button """
    index = None
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)

    def refresh_view_attrs(self, rv, index, data):
        """ Catch and handle the view changes """
        self.index = index
        return super(EditableTableCell, self).refresh_view_attrs(rv, index, data)

    def update_changes(self, txt):
        self.text = txt


class PassiveDataInspector(Screen):
    passive_data = PassiveData(id=1, name='generic')
    item_id = ObjectProperty(None)
    namee = ObjectProperty(None)
    producer = ObjectProperty(None)
    model = ObjectProperty(None)
    serial_number = ObjectProperty(None)
    activation_date = ObjectProperty(None)
    acquire_date = ObjectProperty(None)
    # ports = ObjectProperty(None)
    # other = ObjectProperty(None)
    tutorials = ObjectProperty(None)
    documents = ObjectProperty(None)

    loaded_ports = ListProperty([])
    loaded_other = ListProperty([])

    def on_enter(self, *args):
        self.passive_data = DataDAO.get_data_by_id(int(self.item_id.text))
        self.refresh()

    def refresh(self):
        self.show_passive_data()
        self.show_active_data()
        self.show_related_documents()

    def enter_tutorial(self, tutorial=''):
        self.manager.get_screen('active_data_inspector').text_title.text = tutorial
        self.manager.current = 'active_data_inspector'
        pass

    def btn_new_tutorial(self):
        for i in self.passive_data.tutorials:
            if i.name == "New tutorial":
                information_poup(msg='Can not create a new tutorial:\n A new tutorial already exists!')
                return
        self.passive_data.tutorials.append(ActiveData(name='New tutorial', tutorial='Step by step.'))
        self.parse_to_passive_data()
        DataDAO.save_or_update_data(data=self.passive_data)
        self.manager.get_screen('active_data_inspector').text_title.text = 'New tutorial'
        self.manager.current = 'active_data_inspector'

    def enter_document(self, doc_name=''):
        self.manager.get_screen('related_document_inspector').doc_name.text = doc_name
        self.manager.current = 'related_document_inspector'
        pass

    def btn_new_document(self):
        for i in self.passive_data.documents:
            if i.name == "New document":
                information_poup(msg='Can not create a new document link:\n A new document link already exists!')
                return
        self.passive_data.documents.append(PDFData(name='New document', link='GenericPath'))
        self.parse_to_passive_data()
        DataDAO.save_or_update_data(data=self.passive_data)
        self.manager.get_screen('related_document_inspector').doc_name.text = 'New document'
        self.manager.current = 'related_document_inspector'
        pass

    def btn_save(self):
        self.parse_to_passive_data()
        DataDAO.save_or_update_data(data=self.passive_data)
        information_poup(msg='The item has been saved!')
        self.refresh()

    def btn_delete(self):
        confirmation_poup(msg="Are you sure?", yes_action=self.delete_passive_data)

    def delete_passive_data(self, instance):
        DataDAO.remove_data_by_id(self.passive_data.id)
        DocumentDAO.remove_all_documents_from_id(self.passive_data.id)
        self.manager.current = 'database_list'

    def parse_to_passive_data(self):
        self.passive_data.id = int(self.item_id.text)
        self.passive_data.name = self.namee.text
        self.passive_data.producer = self.producer.text
        self.passive_data.model = self.model.text
        self.passive_data.serial_number = self.serial_number.text
        self.passive_data.activation_date = datetime.strptime(self.activation_date.text, '%d/%m/%y %H:%M:%S')
        self.passive_data.acquire_date = datetime.strptime(self.acquire_date.text, '%d/%m/%y %H:%M:%S')
        self.parse_ports()
        self.parse_other()
        # TODO: Edit und save
        # self.passive_data.ports = literal_eval(self.ports.text)
        # self.passive_data.other = literal_eval(self.other.text)

    def parse_ports(self):
        # TODO: there is no bind with UI !
        ports_dict = {}
        # print(self.loaded_ports)
        for _ in range(1, int(len(self.loaded_ports) / 2 + 1)):
            x = self.loaded_ports.pop()
            y = self.loaded_ports.pop()
            print({str(y): str(x)})
            ports_dict.update({str(y): str(x)})
        self.passive_data.ports.update(ports_dict)
        pass

    def parse_other(self):
        # self.self.passive_data.other =
        pass

    def show_passive_data(self):
        self.item_id.text = str(self.passive_data.id)
        self.namee.text = str(self.passive_data.name)
        self.producer.text = str(self.passive_data.producer)
        self.model.text = str(self.passive_data.model)
        self.serial_number.text = str(self.passive_data.serial_number)
        self.activation_date.text = self.passive_data.activation_date.strftime('%d/%m/%y %H:%M:%S')
        self.acquire_date.text = self.passive_data.acquire_date.strftime('%d/%m/%y %H:%M:%S')
        self.show_ports()
        self.show_other()

    def show_ports(self):
        self.loaded_ports[:] = []
        for (x, y) in self.passive_data.ports.items():
            self.loaded_ports.append(str(x))
            self.loaded_ports.append(str(y))

    def show_other(self):
        self.loaded_other[:] = []
        for (x, y) in self.passive_data.other.items():
            self.loaded_other.append(str(x))
            self.loaded_other.append(str(y))

    def show_active_data(self):
        tuts_list = []
        for i in self.passive_data.tutorials:
            tuts_list.append(' > [ref={}][b][u]{}[/u][/b][/ref]'.format(i.name, i.name))

        if len(tuts_list) == 0:
            self.tutorials.text = '[b]There are no tutorials for this item.[/b]'
        else:
            self.tutorials.text = '\n'.join(tuts_list)

    def show_related_documents(self):
        docs_list = []
        for i in self.passive_data.documents:
            docs_list.append(' > [ref={}][b][u]{}[/u][/b][/ref]'.format(i.name, i.name))

        if len(docs_list) == 0:
            self.documents.text = '[b]There are no related documents for this item.[/b]'
        else:
            self.documents.text = '\n'.join(docs_list)
