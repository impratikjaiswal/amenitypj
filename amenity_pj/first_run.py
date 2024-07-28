import os

from python_helpers.ph_util import PhUtil

from amenity_pj.helper.constants import Const

runningFromPycharm = False


def folders_setup():
    PhUtil.print_heading()
    folders_list_relative = [
        Const.LOG_FOLDER_APPS,
        Const.LOG_FOLDER_OTHER,
        Const.UPLOAD_FOLDER_PERMANENT,
        Const.UPLOAD_FOLDER_TEMP,
    ]
    folders_list_absolute = [
        PhUtil.path_default_out_folder,
    ]
    adjustment_path = os.pardir if runningFromPycharm is True else None
    for folder in folders_list_relative:
        target_path = os.sep.join(filter(None, [adjustment_path, folder]))
        print(f'folder {folder}')
        PhUtil.makedirs(target_path)
    for folder in folders_list_absolute:
        print(f'folder {folder}')
        PhUtil.makedirs(folder)


def main():
    folders_setup()
    PhUtil.print_done()


if __name__ == '__main__':
    main()
