from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from database.EntityDAO import DataDAO
from gui.popup import information_poup
from gui.popup import confirmation_poup
from data.PDFData import PDFData
from database.DocumentDAO import DocumentDAO
import webbrowser
import os

class RelatedDocumentInspector(Screen):
    selected_item = 1
    related_doc = PDFData(name='GenericName', link='Generic document Path.')
    doc_name = ObjectProperty(None)
    doc_path = ObjectProperty(None)

    def on_enter(self, *args):
        self.related_doc.name = self.doc_name.text
        self.selected_item = int(self.manager.get_screen('passive_data_inspector').item_id.text)
        self.update_path()

    def update_path(self):
        for i in DataDAO.get_data_by_id(self.selected_item).documents:
            if i.name == self.related_doc.name:
                self.related_doc = i
        self.doc_path.text = self.related_doc.link
        self.doc_name.text = self.related_doc.name

    def btn_pdf_open(self):
        webbrowser.open('file://{}/{}'.format(os.getcwd(), self.related_doc.link))

    def btn_save(self):
        self.related_doc.link = DocumentDAO.save_document(self.selected_item, self.doc_path.text)
        passive_data = DataDAO.get_data_by_id(self.selected_item)
        index = 0
        if len(passive_data.documents):
            for i in passive_data.documents:
                if i.name == self.related_doc.name:
                    index = passive_data.documents.index(i)
            passive_data.documents.pop(index)
        self.related_doc.name = self.doc_name.text
        self.related_doc.documents = self.doc_path.text
        passive_data.documents.insert(index, self.related_doc)
        DataDAO.save_or_update_data(passive_data)
        information_poup(msg='The item has been saved!')
        self.update_path()

    def btn_delete(self):
        confirmation_poup(msg="Are you sure?", yes_action=self.delete_related_doc)

    def delete_related_doc(self, instance):
        passive_data = DataDAO.get_data_by_id(self.selected_item)
        index = 0
        for i in passive_data.documents:
            if i.name == self.related_doc.name:
                index = passive_data.documents.index(i)
        passive_data.documents.pop(index)
        DataDAO.save_or_update_data(passive_data)
        DocumentDAO.remove_document(self.selected_item, self.related_doc.name + ".pdf")
        self.manager.current = 'passive_data_inspector'
