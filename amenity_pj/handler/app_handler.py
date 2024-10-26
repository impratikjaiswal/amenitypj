import copy
import random
from datetime import datetime

from flask import request, flash, url_for, send_from_directory
from python_helpers.ph_keys import PhKeys
from python_helpers.ph_util import PhUtil

from amenity_pj.app_others import testimonial, login, experiments, credits, stats, settings
from amenity_pj.apps import app_asn1_play, app_tlv_play, app_qr_play, app_excel_play, app_cert_play
from amenity_pj.handler.app_settings import AppSettings
from amenity_pj.helper.constants import Const
from amenity_pj.helper.defaults import Defaults
from amenity_pj.helper.util import Util

host_name = None
nav_bar_app_items = None

app_settings = AppSettings()


def set_server_name(host_name_passed=None):
    """

    :param host_name_passed:
    :return:
    """
    global host_name, nav_bar_app_items
    """
    request dict
    'headers': EnvironHeaders([('Host', 'localhost:5000'),
    'HTTP_HOST': 'localhost:5000'
    'host': 'localhost:5000', 'url': 'http://localhost:5000/asn1Play'
    request.url_root: http://localhost:5000/
    request.headers["Host"]: localhost:5000
    """
    if host_name_passed is None:
        if 'Host' in request.headers:
            host_name_request = request.headers['Host']
        else:
            # TODO: Alternate needs to check
            host_name_request = ''
    else:
        host_name_request = host_name_passed
    key = None
    if host_name_request:
        if any(x in host_name_request for x in ['127.0.0.1', 'localhost']):
            key = 'local'
            host_name = host_name_request
        for _ in ['beta', 'alpha', 'past']:
            if _ in host_name_request:
                key = _
                host_name = key
        if key not in Const.NAV_ITEMS_MAPPING.keys():
            # None as well as All unknown hosts will be treated as prod
            key = 'prod'
            host_name = ''
        nav_bar_app_items = Const.NAV_ITEMS_MAPPING.get(key, None)
    return host_name, nav_bar_app_items


def handle_requests(apj_id, **kwargs):
    """

    :param apj_id:
    :param kwargs:
    :return:
    """
    global host_name, nav_bar_app_items, app_settings
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
    root_path = kwargs.get(PhKeys.ROOT_PATH, None)
    #
    # TODO: Alternative/Availability needs to check
    request_path = request.path
    # TODO: Alternative/Availability needs to check
    request_endpoint = request.endpoint
    # TODO: Alternative/Availability needs to check
    request_method = request.method
    #
    if not internal:
        Util.user_visit(request=request, log=log)
    if apj_id == Const.APJ_ID_AMENITY_PJ:
        set_server_name()
    if request_method == PhKeys.GET and api == Defaults.API and apj_id in Const.WHATS_NEW_LIST:
        whats_new(apj_id=apj_id, log=log)
    common_data = Util.get_apj_data(apj_id=apj_id).copy()
    if common_data:
        # Add GitHub URLs
        github_url = common_data.get(PhKeys.APP_GITHUB_URL, Defaults.GITHUB_REPO)
        if github_url is not None:
            common_data.update({PhKeys.APP_GITHUB_URL: Util.get_github_url(github_repo=github_url, github_pages=False)})
            common_data.update(
                {PhKeys.APP_GITHUB_PAGES_URL: Util.get_github_url(github_repo=github_url, github_pages=True)})
        # Add Hostname
        if host_name:
            common_data.update({PhKeys.APP_HOST: host_name})
        # Add STATS ID
        common_data.update({PhKeys.APP_STATS_ID: Util.get_stats_data(apj_id=apj_id)})
        # Add App Canonical URL
        app_url = common_data.get(PhKeys.APP_URL, None)
        if app_url:
            canonical_url = f'{Const.DEFAULT_CANONICAL_URL}' if apj_id == Const.APJ_ID_AMENITY_PJ else f'{Const.DEFAULT_CANONICAL_URL}{request_path}'
            common_data.update({PhKeys.APP_CANONICAL_URL: canonical_url})
        # Add AppSettings
        if app_settings:
            common_data = PhUtil.dict_merge(common_data, app_settings.get_setting())
            # for app_setting in app_settings.get_setting():
            #     common_data.update({dict(app_setting).ke   : f'({host_name})'})
        # Add Nav Data
        nav_data_url_for = []
        nav_data = []
        nav_data_app_specific = []
        if apj_id in Const.APPS_LIST:
            nav_data_url_for = copy.deepcopy(Const.NAV_ITEMS_MAPPING_URL_FOR)
            for nav_bar_app_item in nav_data_url_for:
                if nav_bar_app_item['text'] == Const.GET_API:
                    nav_bar_app_item['url'] = url_for(request_endpoint, api=True)
        if nav_bar_app_items and apj_id in Const.APPS_LIST_W_INDEX:
            nav_data = copy.deepcopy(nav_bar_app_items)
            for nav_bar_app_item in nav_data:
                nav_bar_app_item['url'] = nav_bar_app_item['url'] + request_path
        if apj_id in Const.APPS_LIST:
            if mapping_data := Const.NAV_ITEMS_MAPPING_APP_SPECIFIC.get(apj_id, None):
                nav_data_app_specific = copy.deepcopy(mapping_data)
                for nav_bar_app_item in nav_data_app_specific:
                    if nav_bar_app_item['text'] == Const.GET_ASN1_OBJECTS:
                        nav_bar_app_item['url'] = url_for(
                            Util.get_apj_data(apj_id=Const.APJ_ID_ASN1_PLAY_ASN1_OBJECTS,
                                              specific_key=PhKeys.APP_END_POINT))
        common_data.update({PhKeys.NAV_BAR_APP_ITEMS: nav_data_url_for + nav_data_app_specific + nav_data})
    # TODO: Migrate to python 3.10 or above for Switch Statement
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
        Const.APJ_ID_EXCEL_PLAY_INFO: app_excel_play.handle_info,
        # #################
        # AmenityPj Apps/APIs
        # #################
        Const.APJ_ID_LOGIN: login.handle_requests,
        Const.APJ_ID_TESTIMONIALS: testimonial.handle_requests,
        Const.APJ_ID_TESTIMONIALS_ID: testimonial.handle_posts,
        Const.APJ_ID_CREDITS: credits.handle_requests,
        Const.APJ_ID_STATS: stats.handle_requests,
        Const.APJ_ID_SETTINGS: settings.handle_requests,
    }
    if Util.get_apj_id_group(apj_id=apj_id) == Const.APJ_ID_EXPERIMENTS_GROUP:
        func = experiments.handle_requests
    else:
        func = func_mapping.get(apj_id, None)
    if func is not None:
        return func(
            apj_id=apj_id,
            api=api,
            log=log,
            default_data=common_data,
            testimonial_post_id=testimonial_post_id,
            root_path=root_path,
        )
    if apj_id == Const.APJ_ID_SERVER_DETAILS:
        set_server_name()
    if apj_id == Const.APJ_ID_404:
        with open(Const.LOG_FILE_404_PATH, "a") as f:
            f.write(f'{datetime.now()},{request.__dict__}\n')
        # return send_file('static/images/Darknet-404-Page-Concept.png', mimetype='image/png')
    if apj_id == Const.APJ_ID_ROBOT_TXT:
        return send_from_directory('static/txt', request.path[1:])
    # ######################
    # AmenityPj Apps
    # ######################
    Util.request_pre(request=request, apj_id=apj_id, api=api, log=log)
    return Util.request_post(request=request, apj_id=apj_id, api=api, log=log, output_data=common_data)


def whats_new(apj_id, log=None):
    """

    :param apj_id:
    :param log:
    :return:
    """
    news_data_pool_common = Const.NEWS_DATA_MAPPING.get(Const.APJ_ID_NEWS_COMMON, None)
    news_data_pool = Const.NEWS_DATA_MAPPING.get(apj_id, None)
    # TODO: Util
    for attempt in range(3):
        if news_data_pool and len(news_data_pool) > 0:
            break
        PhUtil.print_(f'Flash Data: News Not Found for apj_id: {apj_id}; Checking random #{attempt}', log=log)
        # TODO: Util
        # https://www.geeksforgeeks.org/random-numbers-in-python/
        apj_id = random.choice(Const.WHATS_NEW_LIST)
        news_data_pool = Const.NEWS_DATA_MAPPING.get(apj_id, None)
    if news_data_pool is None or not news_data_pool:
        # TODO: Util
        PhUtil.print_(f'Flash Data: News Not Found for apj_id: {apj_id}; Random Attempt Exhaust', log=log)
        return
    # News Pool Found
    news_data_pool_combined = news_data_pool_common + news_data_pool
    news_count = len(news_data_pool_combined)
    news_index = random.choice(range(news_count))
    flash_msg = news_data_pool_combined[news_index]
    if PhKeys.APP_TITLE in flash_msg:
        flash_msg = flash_msg.replace(PhKeys.APP_TITLE, Util.get_apj_data(apj_id=apj_id, specific_key=PhKeys.APP_TITLE))
    PhUtil.print_(f'Flash Msg: {flash_msg}', log=log)
    # session['_flashes'].clear()
    # session.pop('_flashes', None)
    flash(flash_msg)
