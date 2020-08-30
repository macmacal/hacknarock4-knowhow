from os import remove
import constants
import glob

from utils.pdf_utils import copy_pdf


class DocumentDAO:
    def __init__(self, documents_path):
        self.documents_path = documents_path

    def remove_document(self, id, name):
        paths = glob.glob(self.documents_path + '\\' + str(id) + '_' + name)
        if len(paths) == 1:
            remove(paths[0])

    def save_document(self, id, path):
        copy_pdf(path, id)


DocumentDAO = DocumentDAO(constants.DOCUMENTS_PATH)
