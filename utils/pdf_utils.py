import shutil

import constants


def copy_pdf(path_from, asset_id):
    split_path = path_from.split('\\')
    new_path = constants.DOCUMENTS_PATH + '\\' + str(asset_id) + '_' + split_path[len(split_path)-1]
    shutil.copyfile(path_from, new_path)
    return new_path
