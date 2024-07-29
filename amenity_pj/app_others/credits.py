import json
import os

from flask import request
from python_helpers.ph_util import PhUtil

from amenity_pj.helper.util import Util


def handle_requests(apj_id, api, log, default_data, **kwargs):
    """

    :param apj_id:
    :param api:
    :param log:
    :param default_data:
    :param kwargs:
    :return:
    """
    #

    default_data_app = {
        'issue_contributors': extract_data_and_generate_json_pre_deployment()
    }
    app_data = PhUtil.dict_merge(default_data, default_data_app)
    requested_data_dict = Util.request_pre(request=request, apj_id=apj_id, api=api, log=log)
    return Util.request_post(request=request, apj_id=apj_id, api=api, log=log, output_data=app_data)


def extract_data_and_generate_json_pre_deployment():
    # Open the orders.json file
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, os.pardir, 'static', 'issues_data', 'combined.json')
    data = {}
    with open(json_url) as file:
        data = json.load(file)
    return data
