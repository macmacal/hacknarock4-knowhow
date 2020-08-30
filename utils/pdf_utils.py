import shutil

import constants


def copy_pdf(path_from, asset_id, name):
    new_path = constants.DOCUMENTS_PATH + '\\' + str(asset_id) + '_' + name + '.pdf'
    shutil.copyfile(path_from, new_path)
    return new_path
