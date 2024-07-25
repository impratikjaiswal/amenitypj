import os

from python_helpers.ph_util import PhUtil

from amenity_pj.helper.constants import Const


def folders_setup():
    PhUtil.print_heading()
    folders_list = [
        Const.LOG_FOLDER_APPS,
        Const.LOG_FOLDER_OTHER,
        Const.UPLOAD_FOLDER_PERMANENT,
        Const.UPLOAD_FOLDER_TEMP,
        PhUtil.path_default_out_folder,
    ]
    adjustment_path = os.pardir
    for folder in folders_list:
        PhUtil.makedirs(os.sep.join([adjustment_path, folder]))


def main():
    folders_setup()
    PhUtil.print_done()


if __name__ == '__main__':
    main()
