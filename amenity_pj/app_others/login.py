from flask import request, flash, redirect, url_for
from python_helpers.ph_crypto import PhCrypto
from python_helpers.ph_keys import PhKeys
from python_helpers.ph_util import PhUtil

from amenity_pj.helper.constants import Const
from amenity_pj.helper.util import Util


def __validate_credentials(user_name_actual, pass_word_actual):
    """

    :return:
    """
    # user_id = lower(user_name)
    __user_db = {
        'admin': {
            'user_name': 'Admin',
            'pass_word': '8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918',
        },
        'pj': {
            'user_name': 'Pj',
            'pass_word': 'fb8868acd9cbbd68964baa1cfa6b893a6269e01569183474e6c1c4242a0071a9',
        }
    }
    if not user_name_actual:
        return False, 'Missing User Name', PhKeys.ALERT_CSS_CLASS_INFO
    if not pass_word_actual:
        return False, 'Missing Password', PhKeys.ALERT_CSS_CLASS_INFO
    user_data = __user_db.get(user_name_actual.lower(), None)
    if user_data is None:
        return False, 'Unknown User Name', PhKeys.ALERT_CSS_CLASS_DANGER
    user_name_expected = user_data.get('user_name')
    pass_word_expected = user_data.get('pass_word')
    if PhCrypto.hash_str_sha256(pass_word_actual) != pass_word_expected:
        return False, 'Invalid Password', PhKeys.ALERT_CSS_CLASS_DANGER
    return True, f'Welcome {user_name_expected}', PhKeys.ALERT_CSS_CLASS_PRIMARY


def handle_requests(apj_id, api, log, default_data, **kwargs):
    """

    :return:
    """
    #
    default_data_app = {
    }
    app_data = PhUtil.dict_merge(default_data, default_data_app)
    Util.request_pre(request=request, apj_id=apj_id, api=api, log=log)
    #
    if request.method == PhKeys.GET:
        pass
    if request.method == PhKeys.POST:
        result, msg, msg_category = __validate_credentials(request.form['username'], request.form['password'])
        flash(msg, msg_category)
        if result is True:
            return redirect(
                url_for(Util.get_apj_data(apj_id=Const.APJ_ID_AMENITY_PJ, specific_key=PhKeys.APP_END_POINT)))
    return Util.request_post(request=request, apj_id=Const.APJ_ID_LOGIN, api=api, log=log,
                             output_data=app_data)
