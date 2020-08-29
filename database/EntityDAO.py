import pickle
from os import listdir, remove
from os.path import isfile, join
import constants
import glob


class EntityDAO:
    def __init__(self, path):
        self.path = path

    def get_data_by_id(self, passive_data_id):
        paths = glob.glob(self.path + '\\' + str(passive_data_id) + '*')
        with open(paths[0], 'rb') as f:
            passive_data = pickle.load(f)
        return passive_data

    def id_exists(self, passive_data_id):
        paths = glob.glob(self.path + '\\' + str(passive_data_id) + '*')
        return len(paths) != 0

    def remove_data_by_id(self, passive_data_id):
        paths = glob.glob(self.path + '\\' + str(passive_data_id) + '*')
        if len(paths) == 1:
            remove(paths[0])

    def get_all_data(self):
        datafiles = [f for f in listdir(self.path) if isfile(join(self.path, f))]

        passive_data_list = []
        for datafile in datafiles:
            passive_data_list.append(self.get_data_by_id(datafile))

        return passive_data_list

    def save_or_update_data(self, passive_data):
        paths = glob.glob(self.path + '\\' + str(passive_data.id) + '*')
        if len(paths) == 1:
            with open(paths[0], 'wb+') as f:
                pickle.dump(passive_data, f)


DataDAO = EntityDAO(constants.DATABASE_PATH)
