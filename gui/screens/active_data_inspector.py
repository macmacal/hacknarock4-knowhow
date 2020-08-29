from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from data.ActiveData import ActiveData
from database.EntityDAO import DataDAO


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
                self.active_data.tutorial = i.tutorial
        self.text_input.text = self.active_data.tutorial
        self.btn_preview()

    def btn_preview(self):
        self.text_preview.text = self.text_input.text
        # TODO: add parsing for [ref] markup formatting

    def btn_save(self):
        pass

    def btn_delete(self):
        pass
