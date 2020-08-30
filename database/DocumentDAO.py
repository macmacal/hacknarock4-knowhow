from os import remove
import constants
import glob

from utils.pdf_utils import copy_pdf


class DocumentDAO:
    def __init__(self, documents_path):
        self.documents_path = documents_path

    def remove_all_documents_from_id(self, id):
        paths = glob.glob(self.documents_path + '\\' + str(id) + '*')
        for path in paths:
            remove(path)

    def remove_document(self, id, name):
        paths = glob.glob(self.documents_path + '\\' + str(id) + '_' + name)
        if len(paths) == 1:
            remove(paths[0])

    def save_document(self, id, path):
        return copy_pdf(path, id)


DocumentDAO = DocumentDAO(constants.DOCUMENTS_PATH)
