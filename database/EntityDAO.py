import pickle
from os import listdir, remove, getcwd
from os.path import isfile, join
import constants
import glob

from data.PDFData import PDFData


class EntityDAO:
    def __init__(self, path, documents_path):
        self.path = path
        self.documents_path = documents_path

    def get_data_by_id(self, data_id):
        paths = glob.glob(self.path + '\\' + str(data_id) + '*')
        with open(paths[0], 'rb') as f:
            passive_data = pickle.load(f)

        file_documents = []
        file_document_paths = glob.glob(self.documents_path + '\\' + str(data_id) + '*')
        for file_document_path in file_document_paths:
            file_documents.append(PDFData(file_document_path.split('_')[1], getcwd()+"\\"+file_document_path))
        passive_data.documents = file_documents

        return passive_data

    def get_data_by_name(self, data_name):
        paths = glob.glob(self.path + '\\?_' + str(data_name))
        if len(paths) != 0:
            with open(paths[0], 'rb') as f:
                passive_data = pickle.load(f)

            file_documents = []
            file_document_paths = glob.glob(self.documents_path + '\\' + str(passive_data.id) + '*')
            for file_document_path in file_document_paths:
                file_documents.append(PDFData(file_document_path.split('_')[1], getcwd() + "\\" + file_document_path))
            passive_data.documents = file_documents

            return passive_data

    def id_exists(self, data_id):
        paths = glob.glob(self.path + '\\' + str(data_id) + '*')
        return len(paths) != 0

    def name_exists(self, data_name):
        paths = glob.glob(self.path + '\\?_' + str(data_name))
        return len(paths) != 0

    def remove_data_by_id(self, data_id, pdf=True):
        paths = glob.glob(self.path + '\\' + str(data_id) + '*')
        if len(paths) == 1:
            remove(paths[0])
            if pdf:
                paths = glob.glob(self.documents_path + '\\' + str(data_id) + '*')
                for path in paths:
                    remove(path)

    def get_all_data(self):
        datafiles = [f for f in listdir(self.path) if isfile(join(self.path, f))]

        data_list = []
        for datafile in datafiles:
            data_list.append(self.get_data_by_id(datafile))

        return data_list

    def save_or_update_data(self, data):
        paths = glob.glob(self.path + '\\' + str(data.id) + '*')
        if len(paths) != 0:
            self.remove_data_by_id(data.id, False)
        with open(self.path + '\\' + str(data.id) + '_' + data.name, 'wb+') as f:
            pickle.dump(data, f)


DataDAO = EntityDAO(constants.DATABASE_PATH, constants.DOCUMENTS_PATH)
