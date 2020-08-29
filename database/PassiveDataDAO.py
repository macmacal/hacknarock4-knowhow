import pickle
from os import listdir, remove
from os.path import isfile, join


class PassiveDataDAO:
    def __init__(self, path):
        self.path = path

    def get_passive_data_by_id(self, passive_data_id):
        with open(self.path + '\\' + str(passive_data_id), 'rb') as f:
            passive_data = pickle.load(f)
        return passive_data

    def remove_passive_data_by_id(self, passive_data_id):
        remove(self.path + '\\' + str(passive_data_id))

    def get_passive_data(self):
        datafiles = [f for f in listdir(self.path) if isfile(join(self.path, f))]

        passive_data_list = []
        for datafile in datafiles:
            passive_data_list.append(self.get_passive_data_by_id(datafile))

        return passive_data_list

    def save_passive_data(self, passive_data):
        with open(self.path + '\\' + str(passive_data.id), 'wb+') as f:
            pickle.dump(passive_data, f)
