from cert_play.main.data_type.data_type_master import DataTypeMaster
from cert_play.main.data_type.sample import Sample
from cert_play.main.helper.constants_config import GIT_SUMMARY
from cert_play.main.helper.defaults import Defaults
from cert_play.main.helper.formats import Formats
from cert_play.main.helper.formats_group import FormatsGroup
from flask import render_template, request, jsonify
from python_helpers.ph_constants import PhConstants
from python_helpers.ph_keys import PhKeys
from python_helpers.ph_modes_error_handling import PhErrorHandlingModes
from python_helpers.ph_util import PhUtil

from amenity_pj.helper.constants import Const
from amenity_pj.helper.util import Util


def handle_requests(api=False):
    """

    :return:
    """

    SAMPLE_LOAD_ONLY = 'Load Only'
    SAMPLE_LOAD_AND_SUBMIT = 'Load & Submit'
    samples_dic = Sample().get_sample_data_pool_for_web()
    samples_list = PhUtil.generalise_list(list(samples_dic.keys()), sort=False)
    input_formats = PhUtil.generalise_list(FormatsGroup.INPUT_FORMATS_SUPPORTED)
    default_data = {
        PhKeys.APP_TITLE: Const.TITLE_CERT_PLAY,
        PhKeys.APP_DESCRIPTION: Const.DESCRIPTION_CERT_PLAY,
        PhKeys.APP_VERSION: Const.VERSION_CERT_PLAY,
        PhKeys.APP_GITHUB_URL: Util.get_github_url(github_repo=Const.GITHUB_REPO_CERT_PLAY, github_pages=False),
        PhKeys.APP_GITHUB_PAGES_URL: Util.get_github_url(github_repo=Const.GITHUB_REPO_CERT_PLAY, github_pages=True),
        PhKeys.APP_GIT_SUMMARY: GIT_SUMMARY,
        PhKeys.INPUT_DATA: PhConstants.STR_EMPTY,
        PhKeys.OUTPUT_DATA: PhConstants.STR_EMPTY,
        PhKeys.INPUT_FORMATS: input_formats,
        PhKeys.INPUT_FORMAT_SELECTED: Defaults.FORMAT_INPUT,
        PhKeys.SAMPLES: samples_list,
        PhKeys.SAMPLE_SELECTED: samples_list[1] if len(samples_list) > 1 else None,
        PhKeys.SAMPLE_PROCESSING: PhKeys.SAMPLE_LOAD_ONLY,
    }
    log_req = f'{Const.TEMPLATE_CERT_PLAY}; {request.method}; {"API" if api else "Form"} Request'
    PhUtil.print_separator(main_text=f'{log_req} Received!!!')
    requested_data_dict = request.get_json() if request.is_json else request.form.to_dict()
    PhUtil.print_iter(requested_data_dict, header='Inputs')
    if request.method == PhKeys.GET:
        pass
    if request.method == PhKeys.POST:
        sample_processing = True if 'sample_process' in requested_data_dict else False
        # When submitting an HTML form,
        # 1) unchecked checkboxes do not send any data, however checked checkboxes do send False (may send True as well)
        pass
        # 2) Everything is converted to String; below needs to be typecasted
        pass
        sample_data_dict = None
        if sample_processing is True:
            print('sample_processing is needed')
            sample_option = requested_data_dict.get('sample_option', None)
            sample_data = requested_data_dict.get('sample_data', None)
            sample_data_dict = samples_dic.get(sample_data)
            if sample_data_dict:
                print('sample_data_dict is available')
        if sample_data_dict and sample_option == SAMPLE_LOAD_ONLY:
            # Data Processing is not needed
            pass
        else:
            # Data Processing is needed in all other cases
            dic_received = sample_data_dict if sample_data_dict else requested_data_dict
            # PhUtil.print_iter(dic_received, header='dic_received')
            # Filter All Processing Related Keys
            dic_to_process = filter_processing_related_keys(dic_received)
            PhUtil.print_iter(dic_to_process, header='dic_to_process')
            data_type = DataTypeMaster()
            data_type.set_data_pool(data_pool=dic_to_process)
            data_type.parse_safe(PhErrorHandlingModes.CONTINUE_ON_ERROR)
            output_data = data_type.get_output_data()
            default_data.update({PhKeys.OUTPUT_DATA: output_data})
        if sample_data_dict:
            if PhKeys.RAW_DATA in sample_data_dict:
                default_data.update({PhKeys.RAW_DATA: sample_data_dict.get(PhKeys.RAW_DATA)})
            if 'input_format' in sample_data_dict:
                default_data.update({PhKeys.INPUT_FORMAT_SELECTED: sample_data_dict.get('input_format')})
            if PhKeys.REMARKS_LIST in sample_data_dict:
                default_data.update({PhKeys.REMARKS_LIST: sample_data_dict.get(PhKeys.REMARKS_LIST)})
        else:
            if PhKeys.RAW_DATA in requested_data_dict:
                default_data.update({PhKeys.RAW_DATA: requested_data_dict[PhKeys.RAW_DATA]})
            if 'input_format' in requested_data_dict:
                default_data.update({PhKeys.INPUT_FORMAT_SELECTED: requested_data_dict['input_format']})
            if PhKeys.REMARKS_LIST in requested_data_dict:
                default_data.update({PhKeys.REMARKS_LIST: requested_data_dict[PhKeys.REMARKS_LIST]})
        if sample_processing is True:
            default_data.update({'selected_sample_option': sample_option})
            default_data.update({'selected_sample': sample_data})
        PhUtil.print_iter(default_data, header='Outputs')
    PhUtil.print_separator(main_text=f'{log_req} Completed!!!')
    return jsonify(**default_data) if api else render_template(Const.TEMPLATE_CERT_PLAY, **default_data)
