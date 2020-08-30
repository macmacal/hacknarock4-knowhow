import shutil

import constants


def copy_pdf(path_from, asset_id):
    split_path = path_from.split('\\')
    print(split_path[len(split_path)-1])
    shutil.copyfile(path_from, constants.DOCUMENTS_PATH + '\\' + str(asset_id) + '_' + split_path[len(split_path)-1])
