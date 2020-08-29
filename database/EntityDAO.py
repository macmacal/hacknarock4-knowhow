import pickle
from os import listdir, remove
from os.path import isfile, join
import constants
import glob


class EntityDAO:
    def __init__(self, path):
        self.path = path

    def get_data_by_id(self, data_id):
        paths = glob.glob(self.path + '\\' + str(data_id) + '*')
        with open(paths[0], 'rb') as f:
            passive_data = pickle.load(f)
        return passive_data

    def get_data_by_name(self, data_name):
        paths = glob.glob(self.path + '\\?_' + str(data_name))
        if len(paths) != 0:
            with open(paths[0], 'rb') as f:
                passive_data = pickle.load(f)
            return passive_data

    def id_exists(self, data_id):
        paths = glob.glob(self.path + '\\' + str(data_id) + '*')
        return len(paths) != 0

    def name_exists(self, data_name):
        paths = glob.glob(self.path + '\\?_' + str(data_name))
        return len(paths) != 0

    def remove_data_by_id(self, data_id):
        paths = glob.glob(self.path + '\\' + str(data_id) + '*')
        if len(paths) == 1:
            remove(paths[0])

    def get_all_data(self):
        datafiles = [f for f in listdir(self.path) if isfile(join(self.path, f))]

        data_list = []
        for datafile in datafiles:
            data_list.append(self.get_data_by_id(datafile))

        return data_list

    def save_or_update_data(self, data):
        paths = glob.glob(self.path + '\\' + str(data.id) + '*')
        if len(paths) != 0:
            self.remove_data_by_id(data.id)
        with open(self.path + '\\' + str(data.id) + '_' + data.name, 'wb+') as f:
            pickle.dump(data, f)


DataDAO = EntityDAO(constants.DATABASE_PATH)
