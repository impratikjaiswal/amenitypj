from flask import request
from python_helpers.ph_keys import PhKeys
from python_helpers.ph_util import PhUtil

from amenity_pj.helper.util import Util


def handle_requests(apj_id, api, log, default_data, **kwargs):
    """

    :return:
    """
    #
    default_data_app = {
    }
    app_data = PhUtil.dict_merge(default_data, default_data_app)
    requested_data_dict = Util.request_pre(request=request, apj_id=apj_id, api=api, log=log)
    if request.method == PhKeys.GET:
        pass
    if request.method == PhKeys.POST:
        pass
    return Util.request_post(request=request, apj_id=apj_id, api=api, log=log, output_data=app_data)
