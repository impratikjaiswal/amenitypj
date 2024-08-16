import json
import os

from python_helpers.ph_util import PhUtil


def extract_data_and_generate_json_pre_deployment():
    """

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
    path_src = os.sep.join([os.pardir, 'data', 'issues_data'])
    path_dest = os.sep.join(['static', 'issues_data'])
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


def main():
    extract_data_and_generate_json_pre_deployment()
    PhUtil.print_done()


if __name__ == '__main__':
    main()
