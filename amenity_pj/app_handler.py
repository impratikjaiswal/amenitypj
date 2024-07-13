import copy
from datetime import datetime

from flask import request
from python_helpers.ph_keys import PhKeys
from python_helpers.ph_util import PhUtil

from amenity_pj.app_others import testimonial, login
from amenity_pj.apps import app_asn1_play, app_tlv_play, app_qr_play, app_excel_play, app_cert_play
from amenity_pj.helper.constants import Const
from amenity_pj.helper.defaults import Defaults
from amenity_pj.helper.util import Util

host_name = None
nav_bar_app_items = None


def set_server_name():
    global host_name, nav_bar_app_items
    """
    request dict
    'headers': EnvironHeaders([('Host', 'localhost:5000'),
    'HTTP_HOST': 'localhost:5000'
    'host': 'localhost:5000', 'url': 'http://localhost:5000/asn1Play'
    request.url_root: http://localhost:5000/
    request.headers["Host"]: localhost:5000
    """
    if 'Host' in request.headers:
        host_name = request.headers['Host']
    else:
        host_name = ''
    if host_name:
        # TODO: Optimize it
        host_name = host_name.replace('.amenitypj.in', '')
        host_name = host_name.replace('amenitypj.in', '')
        data = None
        if not host_name:
            data = Const.NAV_ITEMS_MAPPING.get('prod', None)
        elif host_name in ['beta', 'alpha', 'past']:
            data = Const.NAV_ITEMS_MAPPING.get(host_name, None)
        else:
            data = Const.NAV_ITEMS_MAPPING.get('local', None)
        if data:
            nav_bar_app_items = data


def handle_requests(apj_id, **kwargs):
    global host_name, nav_bar_app_items
    """
    :param apj_id:
    :param kwargs:
    :return:
    """
    # Handle kwargs
    api = kwargs.get(PhKeys.API, Defaults.API)
    log = kwargs.get(PhKeys.LOG, Defaults.LOG)
    internal = kwargs.get(PhKeys.INTERNAL, Defaults.INTERNAL)
    testimonial_post_id = kwargs.get(PhKeys.TESTIMONIAL_POST_ID, -1)
    #
    request_path = request.path
    #
    if not internal:
        Util.user_visit(request=request, log=log)
    if apj_id == Const.APJ_ID_AMENITY_PJ:
        set_server_name()
    common_data = Util.get_apj_data(apj_id=apj_id).copy()
    if common_data:
        github_url = common_data.get(PhKeys.APP_GITHUB_URL, Defaults.GITHUB_REPO)
        if github_url:
            common_data.update({PhKeys.APP_GITHUB_URL: Util.get_github_url(github_repo=github_url, github_pages=False)})
            common_data.update(
                {PhKeys.APP_GITHUB_PAGES_URL: Util.get_github_url(github_repo=github_url, github_pages=True)})
        if host_name:
            common_data.update({PhKeys.APP_HOST: f'({host_name})'})
            if apj_id in Const.APPS_LIST:
                # data = nav_bar_app_items.copy()
                data = copy.deepcopy(nav_bar_app_items)
                for nav_bar_app_item in data:
                    nav_bar_app_item['url'] = nav_bar_app_item['url'] + request_path
                common_data.update({PhKeys.NAV_BAR_APP_ITEMS: data})
    # TODO: Migrate to 3.10 or above for Switch Statement
    # def number_to_string(argument):
    #     match argument:
    #         case 0:
    #             return "zero"
    #         case 1:
    #             return "one"
    #         case 2:
    #             return "two"
    #         case default:
    #             return "something"
    # head = number_to_string(2)

    func_mapping = {
        # #################
        # Imported Apps
        # #################
        Const.APJ_ID_ASN1_PLAY: app_asn1_play.handle_requests,
        Const.APJ_ID_TLV_PLAY: app_tlv_play.handle_requests,
        Const.APJ_ID_QR_PLAY: app_qr_play.handle_requests,
        Const.APJ_ID_EXCEL_PLAY: app_excel_play.handle_requests,
        Const.APJ_ID_CERT_PLAY: app_cert_play.handle_requests,
        # #################
        # Imported Apps/APIs
        # #################
        Const.APJ_ID_ASN1_PLAY_ASN1_OBJECTS: app_asn1_play.handle_asn1_objects,
        # #################
        # AmenityPj Apps/APIs
        # #################
        Const.APJ_ID_LOGIN: login.handle_requests,
        Const.APJ_ID_TESTIMONIALS: testimonial.handle_requests,
        Const.APJ_ID_TESTIMONIALS_ID: testimonial.handle_posts,
    }
    func = func_mapping.get(apj_id, None)
    if func is not None:
        return func(
            apj_id=apj_id,
            api=api,
            log=log,
            default_data=PhUtil.dict_merge(common_data,
                                           Const.COMMON_DATA_APPS) if apj_id in Const.APPS_LIST else common_data,
            testimonial_post_id=testimonial_post_id,
        )
    if apj_id == Const.APJ_ID_SERVER_DETAILS:
        set_server_name()
    if apj_id == Const.APJ_ID_404:
        with open("./404.csv", "a") as f:
            f.write(f'{datetime.now()},{request.__dict__}\n')
        # return send_file('static/images/Darknet-404-Page-Concept.png', mimetype='image/png')
    # ######################
    # AmenityPj Apps
    # ######################
    Util.request_pre(request=request, apj_id=apj_id, api=api, log=log)
    return Util.request_post(request=request, apj_id=apj_id, api=api, log=log, output_data=common_data)
