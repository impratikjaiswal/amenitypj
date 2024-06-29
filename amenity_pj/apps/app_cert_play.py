from cert_play.main.data_type.data_type_master import DataTypeMaster
from cert_play.main.data_type.sample import Sample
from cert_play.main.helper.constants_config import GIT_SUMMARY
from cert_play.main.helper.defaults import Defaults
from cert_play.main.helper.formats_group import FormatsGroup
from flask import render_template, request, jsonify
from python_helpers.ph_constants import PhConstants
from python_helpers.ph_keys import PhKeys
from python_helpers.ph_modes_error_handling import PhErrorHandlingModes
from python_helpers.ph_util import PhUtil

from amenity_pj.helper.constants import Const
from amenity_pj.helper.util import Util


def handle_requests(api=False, log=None):
    """

    :return:
    """

    def update_default_data(source_key, target_key=None):
        """

        :param source_key:
        :param target_key:
        :return:
        """
        target_key = source_key if target_key is None else target_key
        source_dict = sample_dict if sample_dict else requested_data_dict
        if source_key in source_dict:
            default_data.update({target_key: source_dict.get(source_key)})
        return default_data.get(target_key, None)

    def update_checked_item(target_key):
        """

        :param target_key:
        :return:
        """
        requested_data_dict.update({target_key: True if target_key in requested_data_dict else False})

    def update_integer_item(target_key):
        """

        :param target_key:
        :return:
        """
        requested_data_dict.update(
            {target_key: int(requested_data_dict.get(target_key) if target_key in requested_data_dict else -1)})

    samples_dict = Sample().get_sample_data_pool_for_web()
    samples_list = PhUtil.generalise_list(list(samples_dict.keys()), sort=False)
    input_formats = PhUtil.generalise_list(FormatsGroup.INPUT_FORMATS_SUPPORTED)
    utl_time_outs = PhUtil.generalise_list(FormatsGroup.URL_TIME_OUT_SUPPORTED)
    template_id = Const.TEMPLATE_CERT_PLAY
    default_data = {
        PhKeys.APP_PARENT_TITLE: Const.TITLE_AMENITY_PJ,
        PhKeys.APP_PARENT_VERSION: Const.VERSION_AMENITY_PJ,
        PhKeys.APP_TITLE: Const.TITLE_CERT_PLAY,
        PhKeys.APP_VERSION: Const.VERSION_CERT_PLAY,
        PhKeys.APP_DESCRIPTION: Const.DESCRIPTION_CERT_PLAY,
        PhKeys.APP_GITHUB_URL: Util.get_github_url(github_repo=Const.GITHUB_REPO_CERT_PLAY, github_pages=False),
        PhKeys.APP_GITHUB_PAGES_URL: Util.get_github_url(github_repo=Const.GITHUB_REPO_CERT_PLAY, github_pages=True),
        PhKeys.APP_GIT_SUMMARY: GIT_SUMMARY,
        PhKeys.SAMPLES: samples_list,
        PhKeys.SAMPLE_SELECTED: samples_list[1] if len(samples_list) > 1 else None,
        PhKeys.SAMPLE_OPTION: PhKeys.SAMPLE_LOAD_ONLY,
        PhKeys.INPUT_DATA: PhConstants.STR_EMPTY,
        PhKeys.OUTPUT_DATA: PhConstants.STR_EMPTY,
        PhKeys.INFO_DATA: PhConstants.STR_EMPTY,
        PhKeys.INPUT_FORMATS: input_formats,
        PhKeys.INPUT_FORMAT_SELECTED: Defaults.FORMAT_INPUT,
        PhKeys.URL_TIME_OUTS: utl_time_outs,
        PhKeys.URL_TIME_OUT_SELECTED: Defaults.URL_TIME_OUT,
        PhKeys.URL_PRE_ACCESS: Defaults.URL_PRE_ACCESS,
    }
    log_req = f'{template_id}; {request.method}; {"API" if api else "Form"} Request'
    PhUtil.print_separator(main_text=f'{log_req} Received!!!', log=log)
    requested_data_dict = request.get_json() if request.is_json else request.form.to_dict()
    PhUtil.print_iter(requested_data_dict, header='Inputs', log=log)
    if request.method == PhKeys.GET:
        pass
    if request.method == PhKeys.POST:
        process_sample = True if PhKeys.PROCESS_SAMPLE in requested_data_dict else None
        sample_option = requested_data_dict.get(PhKeys.SAMPLE_OPTION, None)
        sample_name = requested_data_dict.get(PhKeys.SAMPLE, None)
        sample_dict = None
        # When submitting an HTML form,
        # 1) unchecked checkboxes do not send any data, however checked checkboxes do send False (may send True as well)
        update_checked_item(PhKeys.URL_PRE_ACCESS)
        # 2) Everything is converted to String; below needs to be typecast, TODO: should be handled in parse_config; int
        update_integer_item(PhKeys.URL_TIME_OUT)
        PhUtil.print_(f'process_sample is {process_sample}', log=log)
        if process_sample:
            sample_dict = samples_dict.get(sample_name, None)
            if sample_dict:
                PhUtil.print_iter(sample_dict, header='sample_dict', log=log)
        if sample_dict and sample_option == PhKeys.SAMPLE_LOAD_ONLY:
            PhUtil.print_('Data Processing is not needed', log=log)
            pass
        else:
            PhUtil.print_('Data Processing is needed', log=log)
            dic_received = sample_dict if sample_dict else requested_data_dict
            # Filter All Processing Related Keys
            dic_to_process = PhUtil.filter_processing_related_keys(dic_received)
            PhUtil.print_iter(dic_to_process, header='dic_to_process', log=log)
            data_type = DataTypeMaster()
            data_type.set_data_pool(data_pool=dic_to_process)
            data_type.parse_safe(PhErrorHandlingModes.CONTINUE_ON_ERROR)
            output_data, info_data = data_type.get_output_data(only_output=False)
            default_data.update({PhKeys.OUTPUT_DATA: output_data})
            default_data.update({PhKeys.INFO_DATA: info_data})
        # Conditional Updates
        update_default_data(PhKeys.INPUT_DATA)
        update_default_data(PhKeys.INPUT_FORMAT, PhKeys.INPUT_FORMAT_SELECTED)
        update_default_data(PhKeys.URL_PRE_ACCESS)
        update_default_data(PhKeys.URL_TIME_OUT, PhKeys.URL_TIME_OUT_SELECTED)
        update_default_data(PhKeys.REMARKS)
        # Fixed Updates
        default_data.update({PhKeys.SAMPLE_SELECTED: sample_name})
        default_data.update({PhKeys.SAMPLE_OPTION: sample_option})
        PhUtil.print_iter(default_data, header='Outputs', log=log)
    PhUtil.print_separator(main_text=f'{log_req} Completed!!!', log=log)
    return jsonify(**default_data) if api else render_template(template_id, **default_data)
