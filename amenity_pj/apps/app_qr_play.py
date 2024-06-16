from flask import render_template, request, jsonify
from python_helpers.ph_constants import PhConstants
from python_helpers.ph_keys import PhKeys
from python_helpers.ph_modes_error_handling import PhErrorHandlingModes
from python_helpers.ph_util import PhUtil
from qr_play.main.data_type.any_data import small_data, bulk_data_1, bulk_data_2
from qr_play.main.data_type.data_type_master import DataTypeMaster
from qr_play.main.helper.constants_config import GIT_SUMMARY
from qr_play.main.helper.defaults import Defaults
from qr_play.main.helper.formats import Formats

from amenity_pj.helper.constants import Const
from amenity_pj.helper.util import Util


def get_sample_data(key):
    sample_data = {
        PhKeys.SAMPLE_1: {
            PhKeys.REMARKS_LIST: 'Simple Qr',
            PhKeys.INPUT_DATA: small_data,
            PhKeys.SCALE: 8,
            PhKeys.SPLIT_QRS: False,
            PhKeys.QR_CODE_VERSION: 33
        },
        PhKeys.SAMPLE_2: {
            PhKeys.REMARKS_LIST: 'Bulk Data Single Qr',
            PhKeys.INPUT_DATA: bulk_data_1,
            PhKeys.SCALE: Defaults.SCALE,
            PhKeys.SPLIT_QRS: False,
            PhKeys.QR_CODE_VERSION: 40
        },
        PhKeys.SAMPLE_3: {
            PhKeys.REMARKS_LIST: 'Bulk Data Split Qrs',
            PhKeys.INPUT_DATA: bulk_data_2,
            PhKeys.SCALE: Defaults.SCALE,
            PhKeys.SPLIT_QRS: True,
            PhKeys.QR_CODE_VERSION: 40
        },
        PhKeys.SAMPLE_4: {
            PhKeys.REMARKS_LIST: 'Simple Qr (LPA)',
            PhKeys.INPUT_DATA: 'LPA:1$SMDP.EXAMPLE.COM$04386-AGYFT-A74Y8-3F815',
            PhKeys.SCALE: Defaults.SCALE,
            PhKeys.SPLIT_QRS: False,
            PhKeys.QR_CODE_VERSION: Defaults.QR_CODE_VERSION
        },
        PhKeys.SAMPLE_5: {
            PhKeys.REMARKS_LIST: 'Simple Qr (Google Pay/GPay)',
            PhKeys.INPUT_DATA: 'upi://pay?pa=impratikjaiswal@okicici&pn=Pratik%20Jaiswal&aid=uGICAgICw6tuJBw',
            PhKeys.SCALE: Defaults.SCALE,
            PhKeys.SPLIT_QRS: False,
            PhKeys.QR_CODE_VERSION: Defaults.QR_CODE_VERSION
        },
    }
    return sample_data.get(key, None)


def handle_requests(api=False):
    """

    :return:
    """

    default_data = {
        PhKeys.APP_TITLE: Const.TITLE_QR_PLAY,
        PhKeys.APP_DESCRIPTION: Const.DESCRIPTION_QR_PLAY,
        PhKeys.APP_VERSION: Const.VERSION_QR_PLAY,
        PhKeys.APP_GITHUB_URL: Util.get_github_url(github_repo=Const.GITHUB_REPO_QR_PLAY, github_pages=False),
        PhKeys.APP_GITHUB_PAGES_URL: Util.get_github_url(github_repo=Const.GITHUB_REPO_QR_PLAY, github_pages=True),
        PhKeys.APP_GIT_SUMMARY: GIT_SUMMARY,
        PhKeys.QR_CODE_VERSIONS: list(range(40, 0, -1)),
        PhKeys.QR_CODE_VERSION_SELECTED: Defaults.QR_CODE_VERSION,
        PhKeys.SPLIT_QRS: Defaults.SPLIT_QRS,
        PhKeys.SCALE: Defaults.SCALE,
        PhKeys.SAMPLE_PROCESSING: PhKeys.SAMPLE_LOAD_ONLY,
        PhKeys.OUTPUT_DATA: PhConstants.STR_EMPTY,
    }
    log_req = f'{Const.TEMPLATE_QR_PLAY}; {request.method}; {"API" if api else "Form"} Request'
    PhUtil.print_separator(main_text=f'{log_req} Received!!!')
    requested_data_dict = request.get_json() if request.is_json else request.form.to_dict()
    PhUtil.print_iter(requested_data_dict, header='Inputs')
    if request.method == PhKeys.GET:
        pass
    if request.method == PhKeys.POST:
        sample_processing = requested_data_dict.get(PhKeys.SAMPLE_PROCESSING, False)
        # When submitting an HTML form,
        # 1) unchecked checkboxes do not send any data, however checked checkboxes do send False (may send True as well)
        requested_data_dict.update({PhKeys.SPLIT_QRS: True if PhKeys.SPLIT_QRS in requested_data_dict else False})
        # 2) Everything is converted to String; below needs to be typecasted
        # XXX: This should be handled in parse_config; integer
        requested_data_dict.update({PhKeys.QR_CODE_VERSION: int(requested_data_dict.get(PhKeys.QR_CODE_VERSION))})
        sample_data_dict = None
        for key in requested_data_dict.keys():
            if not key.startswith(PhKeys.SAMPLE):
                continue
            sample_data_dict = get_sample_data(key)
            if sample_data_dict:
                print('sample_data_dict is available')
                break
        if sample_data_dict and sample_processing == PhKeys.SAMPLE_LOAD_ONLY:
            # Data Processing is not needed
            pass
        else:
            # Data Processing is needed in all other cases
            dic_received = sample_data_dict if sample_data_dict else requested_data_dict
            # PhUtil.print_iter(dic_received, header='dic_received')
            # Filter All Processing Related Keys
            dic_to_process = {k: v for k, v in dic_received.items() if
                              not (k.startswith(PhKeys.SAMPLE) or k.startswith('process'))}
            dic_to_process.update({PhKeys.IMAGE_FORMAT: Formats.PNG_URI})
            dic_to_process.update({PhKeys.PRINT_INPUT: True})
            PhUtil.print_iter(dic_to_process, header='dic_to_process')
            data_type = DataTypeMaster()
            data_type.set_data_pool(data_pool=dic_to_process)
            data_type.parse_safe(PhErrorHandlingModes.CONTINUE_ON_ERROR)
            output_data = data_type.get_output_data()
            temp_output_data = []
            if isinstance(output_data, list):
                temp_output_data = output_data
            else:
                temp_output_data.append(output_data)
            default_data.update({PhKeys.OUTPUT_DATA: temp_output_data})
        if sample_data_dict:
            if PhKeys.INPUT_DATA in sample_data_dict:
                default_data.update({PhKeys.INPUT_DATA: sample_data_dict.get(PhKeys.INPUT_DATA)})
            if PhKeys.SPLIT_QRS in sample_data_dict:
                default_data.update({PhKeys.SPLIT_QRS: sample_data_dict.get(PhKeys.SPLIT_QRS)})
            if PhKeys.QR_CODE_VERSION in sample_data_dict:
                default_data.update({PhKeys.QR_CODE_VERSION_SELECTED: sample_data_dict.get(PhKeys.QR_CODE_VERSION)})
            if PhKeys.SCALE in sample_data_dict:
                default_data.update({PhKeys.SCALE: sample_data_dict.get(PhKeys.SCALE)})
            if PhKeys.REMARKS_LIST in sample_data_dict:
                default_data.update({PhKeys.REMARKS_LIST: sample_data_dict.get(PhKeys.REMARKS_LIST)})
        else:
            if PhKeys.INPUT_DATA in requested_data_dict:
                default_data.update({PhKeys.INPUT_DATA: requested_data_dict[PhKeys.INPUT_DATA]})
            if PhKeys.SPLIT_QRS in requested_data_dict:
                default_data.update({PhKeys.SPLIT_QRS: requested_data_dict[PhKeys.SPLIT_QRS]})
            if PhKeys.QR_CODE_VERSION in requested_data_dict:
                default_data.update({PhKeys.QR_CODE_VERSION_SELECTED: requested_data_dict[PhKeys.QR_CODE_VERSION]})
            if PhKeys.SCALE in requested_data_dict:
                default_data.update({PhKeys.SCALE: requested_data_dict[PhKeys.SCALE]})
            if PhKeys.REMARKS_LIST in requested_data_dict:
                default_data.update({PhKeys.REMARKS_LIST: requested_data_dict[PhKeys.REMARKS_LIST]})
        default_data.update({PhKeys.SAMPLE_PROCESSING: sample_processing})
        PhUtil.print_iter(default_data, header='Outputs')
    PhUtil.print_separator(main_text=f'{log_req} Completed!!!')
    return jsonify(**default_data) if api else render_template(Const.TEMPLATE_QR_PLAY, **default_data)
