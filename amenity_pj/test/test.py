from python_helpers.ph_keys import PhKeys
from python_helpers.ph_util import PhUtil

from amenity_pj.app_handler import set_server_name
from amenity_pj.helper.constants import Const
from amenity_pj.helper.util import Util


def test_set_server_name():
    PhUtil.print_heading()
    hosts_pool = [
        'localhost:5000',
        '127.0.0.1:5000',
        'beta.amenitypj.in',
        'alpha.amenitypj.in',
        'past.amenitypj.in',
        'amenitypj.in',
        'www.amenitypj.in',
        'www.beta.amenitypj.in',
    ]
    for _host in hosts_pool:
        host_name, nav_items = set_server_name(_host)
        print(f'{_host}: {host_name}; {nav_items} ')


def test_versions():
    PhUtil.print_heading()
    PhUtil.print_version(Const.TITLE_AMENITY_PJ, Const.VERSION_AMENITY_PJ)
    for apj_id in Const.APPS_LIST:
        PhUtil.print_version(Util.get_apj_data(apj_id=apj_id, specific_key=PhKeys.APP_TITLE),
                             Util.get_apj_data(apj_id=apj_id, specific_key=PhKeys.APP_VERSION),
                             no_additional_info=True)


def main():
    test_versions()
    test_set_server_name()


if __name__ == '__main__':
    main()
