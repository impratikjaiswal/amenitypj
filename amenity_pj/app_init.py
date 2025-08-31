import json
import os
import sqlite3

from python_helpers.ph_util import PhUtil

from amenity_pj.helper.constants import Const


def init_directories(running_from_pycharm=False):
    """

    :param running_from_pycharm:
    :return:
    """
    PhUtil.print_heading()
    folders_list_relative = [
        Const.LOG_FOLDER_APPS,
        Const.LOG_FOLDER_OTHER,
        Const.UPLOAD_FOLDER_PERMANENT,
        Const.UPLOAD_FOLDER_TEMPORARY,
    ]
    folders_list_absolute = [
        PhUtil.path_default_out_folder,
    ]
    adjustment_path = os.pardir if running_from_pycharm is True else None
    for folder in folders_list_relative:
        target_path = os.sep.join(filter(None, [adjustment_path, folder]))
        PhUtil.make_dirs(target_path, absolute_path_needed=True)
    for folder in folders_list_absolute:
        PhUtil.make_dirs(folder)


def init_contributors_offline_data_and_generate_json(running_from_pycharm=False):
    """

    :param running_from_pycharm:
    :return:
    """
    """
    Structure:

    items: [
        user: {
            "login": "",
            "avatar_url": "",
            "html_url": "",
        }
        "created_at": "",
    ]
    """
    folder = os.sep.join(['data', 'issues'])
    adjustment_path = os.pardir if running_from_pycharm is True else None
    path_src = os.sep.join(filter(None, [adjustment_path, folder]))
    path_dest = os.sep.join(['static', 'issues_data'])
    PhUtil.make_dirs(path_dest, absolute_path_needed=True)
    file_name_raw = 'combined_raw.json'
    file_name = 'combined.json'
    file_path_src = os.path.join(path_src, file_name)
    file_path_dest = os.path.join(path_dest, file_name)
    file_path_dest_raw = os.path.join(path_dest, file_name_raw)
    # Open the orders.json file
    data = None
    with open(file_path_src) as file:
        data = json.load(file)
    if not data:
        return None
    items = data.get('items', None)
    if not items:
        return None
    feedback_providers_data_raw = []
    for item in items:
        user = item.get('user', None)
        if not user:
            continue
        feedback_providers_data_raw.append({
            "login": user.get("login", ""),
            "avatar_url": user.get("avatar_url", ""),
            "html_url": user.get("html_url", ""),
            "created_at": item.get("created_at", ""),
        })
    feedback_providers_data = feedback_providers_data_raw
    # feedback_providers_data = sorted(feedback_providers_data_raw, key=itemgetter('login'), reverse=True)
    with open(file_path_dest_raw, 'w') as file:
        json.dump(feedback_providers_data_raw, file, indent=4)
    with open(file_path_dest, 'w') as file:
        json.dump(feedback_providers_data, file, indent=4)
    PhUtil.print_iter(feedback_providers_data_raw, depth_level=1)


def init_db():
    """

    :return:
    """
    connection = sqlite3.connect('../db/database.db')

    with open('../db/schema.sql') as f:
        connection.executescript(f.read())

    cur = connection.cursor()

    cur.execute("INSERT INTO posts (title, content, publisher) VALUES (?, ?, ?)",
                ('Open Source Tools', 'All the Tools provided here are open source. Code can be found at Github.',
                 'Admin')
                )

    cur.execute("INSERT INTO posts (title, content, publisher) VALUES (?, ?, ?)",
                ('Asn1Play', 'I am using this tool from couple of years & it helps me boost my Productivity', 'Pratik')
                )

    cur.execute("INSERT INTO posts (title, content, publisher) VALUES (?, ?, ?)",
                ('TlvPlay', 'Great Tool, able to parse any TLV for known as well as unknown Tools', 'Pj')
                )

    cur.execute("INSERT INTO posts (title, content, publisher) VALUES (?, ?, ?)",
                ('QrPlay', 'Wow !!!, Variety of Qr versions are supported under one roof', 'Amrit')
                )

    connection.commit()
    connection.close()


def main():
    """

    :return:
    """
    running_from_pycharm = False
    #
    init_directories(running_from_pycharm)
    #
    init_contributors_offline_data_and_generate_json(running_from_pycharm)
    #
    init_db()
    #
    PhUtil.print_done()


if __name__ == '__main__':
    main()
