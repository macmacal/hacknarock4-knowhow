from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from data.ActiveData import ActiveData
from database.EntityDAO import DataDAO
from gui.popup import information_poup
from gui.popup import confirmation_poup
from utils.regex_utils import format_link, format_youtube_link


class ActiveDataInspector(Screen):
    selected_item = 1
    active_data = ActiveData(name='GenericName', tutorial='Generic tutorial text.')
    text_title = ObjectProperty(None)
    text_input = ObjectProperty(None)
    text_preview = ObjectProperty(None)

    def on_enter(self, *args):
        self.active_data.name = self.text_title.text
        self.selected_item = int(self.manager.get_screen('passive_data_inspector').item_id.text)
        self.get_tutorial_text()

    def get_tutorial_text(self):
        for i in DataDAO.get_data_by_id(self.selected_item).tutorials:
            if i.name == self.active_data.name:
                self.active_data = i
        self.text_input.text = self.active_data.tutorial
        self.text_title.text = self.active_data.name
        self.btn_preview()

    def btn_preview(self):
        self.text_preview.text = format_youtube_link(format_link(self.text_input.text))

    def btn_save(self):
        self.btn_preview()
        passive_data = DataDAO.get_data_by_id(self.selected_item)
        index = 0

        for i in passive_data.tutorials:
            if i.name == self.active_data.name:
                index = passive_data.tutorials.index(i)
        passive_data.tutorials.pop(index)
        self.active_data.name = self.text_title.text
        self.active_data.tutorial = self.text_input.text
        passive_data.tutorials.insert(index, self.active_data)
        DataDAO.save_or_update_data(passive_data)

        information_poup(msg='The item has been saved!')

    def btn_delete(self):
        confirmation_poup(msg="Are you sure?", yes_action=self.delete_active_data)

    def delete_active_data(self, instance):
        passive_data = DataDAO.get_data_by_id(self.selected_item)
        index = 0
        for i in passive_data.tutorials:
            if i.name == self.active_data.name:
                index = passive_data.tutorials.index(i)
        passive_data.tutorials.pop(index)
        DataDAO.save_or_update_data(passive_data)
        self.manager.current = 'passive_data_inspector'
