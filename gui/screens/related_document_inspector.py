from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from database.EntityDAO import DataDAO
from gui.popup import information_poup
from gui.popup import confirmation_poup


class RelatedDocumentInspector(Screen):
    selected_item = 1
    related_doc = ActiveData(name='GenericName', tutorial='Generic tutorial text.')
    doc_name = ObjectProperty(None)
    doc_path = ObjectProperty(None)

    def on_enter(self, *args):
        self.related_doc.name = self.doc_name.text
        self.selected_item = int(self.manager.get_screen('passive_data_inspector').item_id.text)
        self.get_path()

    def get_path(self):
        for i in DataDAO.get_data_by_id(self.selected_item).pdflist:  # TODO fix
            if i.name == self.related_doc.name:
                self.related_doc = i
        self.doc_path.text = self.related_doc.path
        self.doc_name.text = self.related_doc.name

    def btn_save(self):
        information_poup(msg='The item has been saved!')
        pass
        # self.btn_preview()
        # passive_data = DataDAO.get_data_by_id(self.selected_item)
        # index = 0
        #
        # for i in passive_data.tutorials:
        #     if i.name == self.active_data.name:
        #        index = passive_data.tutorials.index(i)
        # passive_data.tutorials.pop(index)
        # self.active_data.name = self.text_title.text
        # self.active_data.tutorial = self.text_input.text
        # passive_data.tutorials.insert(index, self.active_data)
        # DataDAO.save_or_update_data(passive_data)

    def btn_delete(self):
        confirmation_poup(msg="Are you sure?", yes_action=self.delete_related_doc)

    def delete_related_doc(self, instance):
        passive_data = DataDAO.get_data_by_id(self.selected_item)
        index = 0
        for i in passive_data.pdflist:  # TODO fix
            if i.name == self.active_data.name:
                index = passive_data.pdflist.index(i)
        passive_data.pdflist.pop(index)
        DataDAO.save_or_update_data(passive_data)
        self.manager.current = 'passive_data_inspector'
