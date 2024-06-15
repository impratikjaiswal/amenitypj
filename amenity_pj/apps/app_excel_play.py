# from excel_play.main.data_type.data_type_master import DataTypeMaster
# from python_helpers.ph_modes_error_handling import PhErrorHandlingModes
# from excel_play.main.helper.defaults import Defaults
from excel_play.main.helper.constants_config import GIT_SUMMARY
from flask import render_template, request, jsonify
from python_helpers.ph_constants import PhConstants
from python_helpers.ph_keys import PhKeys
from python_helpers.ph_util import PhUtil

from amenity_pj.helper.constants import Const
from amenity_pj.helper.util import Util


def get_sample_data(key):
    sample_data = {
        PhKeys.SAMPLE_1: {
        },
    }
    return sample_data.get(key, None)


def handle_requests(api=False):
    """

    :return:
    """

    default_data = {
        PhKeys.APP_TITLE: Const.TITLE_EXCEL_PLAY,
        PhKeys.APP_DESCRIPTION: Const.DESCRIPTION_EXCEL_PLAY,
        PhKeys.APP_VERSION: Const.VERSION_EXCEL_PLAY,
        PhKeys.APP_GITHUB_URL: Util.get_github_url(github_repo=Const.GITHUB_REPO_EXCEL_PLAY, github_pages=False),
        PhKeys.APP_GITHUB_PAGES_URL: Util.get_github_url(github_repo=Const.GITHUB_REPO_EXCEL_PLAY, github_pages=True),
        PhKeys.APP_GIT_SUMMARY: GIT_SUMMARY,
        PhKeys.SAMPLE_PROCESSING: PhKeys.SAMPLE_LOAD_ONLY,
        PhKeys.OUTPUT_DATA: PhConstants.STR_EMPTY,
    }
    log_req = f'{Const.TEMPLATE_EXCEL_PLAY}; {request.method}; {"API" if api else "Form"} Request'
    PhUtil.print_separator(main_text=f'{log_req} Received!!!')
    requested_data_dict = request.get_json() if request.is_json else request.form.to_dict()
    PhUtil.print_iter(requested_data_dict, header='Inputs')
    if request.method == PhKeys.GET:
        pass
    if request.method == PhKeys.POST:
        sample_processing = requested_data_dict.get(PhKeys.SAMPLE_PROCESSING, False)
        # When submitting an HTML form,
        # 1) unchecked checkboxes do not send any data, however checked checkboxes do send False (may send True as well)
        pass
        # 2) Everything is converted to String; below needs to be typecasted
        pass
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
            PhUtil.print_iter(dic_to_process, header='dic_to_process')
            # data_type = DataTypeMaster()
            # data_type.set_data_pool(data_pool=dic_to_process)
            # data_type.parse_safe(PhErrorHandlingModes.CONTINUE_ON_ERROR)
            # output_data = data_type.get_output_data()
            # default_data.update({PhKeys.OUTPUT_DATA: output_data})
        # if sample_data_dict:
        #     if PhKeys.RAW_DATA in sample_data_dict:
        #         default_data.update({PhKeys.RAW_DATA: sample_data_dict.get(PhKeys.RAW_DATA)})
        #     if 'length_in_decimal' in sample_data_dict:
        #         default_data.update({'length_in_decimal': sample_data_dict.get('length_in_decimal')})
        #     if 'value_in_ascii' in sample_data_dict:
        #         default_data.update({'value_in_ascii': sample_data_dict.get('value_in_ascii')})
        #     if 'one_liner' in sample_data_dict:
        #         default_data.update({'one_liner': sample_data_dict.get('one_liner')})
        #     if PhKeys.REMARKS_LIST in sample_data_dict:
        #         default_data.update({PhKeys.REMARKS_LIST: sample_data_dict.get(PhKeys.REMARKS_LIST)})
        # else:
        #     if PhKeys.RAW_DATA in requested_data_dict:
        #         default_data.update({PhKeys.RAW_DATA: requested_data_dict[PhKeys.RAW_DATA]})
        #     if 'length_in_decimal' in requested_data_dict:
        #         default_data.update({'length_in_decimal': requested_data_dict['length_in_decimal']})
        #     if 'value_in_ascii' in requested_data_dict:
        #         default_data.update({'value_in_ascii': requested_data_dict['value_in_ascii']})
        #     if 'one_liner' in requested_data_dict:
        #         default_data.update({'one_liner': requested_data_dict['one_liner']})
        #     if PhKeys.REMARKS_LIST in requested_data_dict:
        #         default_data.update({PhKeys.REMARKS_LIST: requested_data_dict[PhKeys.REMARKS_LIST]})
        default_data.update({PhKeys.SAMPLE_PROCESSING: sample_processing})
        PhUtil.print_iter(default_data, header='Outputs')
    PhUtil.print_separator(main_text=f'{log_req} Completed!!!')
    return jsonify(**default_data) if api else render_template(Const.TEMPLATE_EXCEL_PLAY, **default_data)
