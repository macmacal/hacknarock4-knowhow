import pickle


class PassiveDataDAO:
    def __init__(self, path):
        self.path = path

    def get_passive_data_by_id(self, passive_data_id):
        with open(self.path + '\\' + str(passive_data_id), 'rb') as f:
            passive_data = pickle.load(f)
        return passive_data

    def save_passive_data(self, passive_data):
        with open(self.path + '\\' + str(passive_data.id), 'wb+') as f:
            pickle.dump(passive_data, f)
