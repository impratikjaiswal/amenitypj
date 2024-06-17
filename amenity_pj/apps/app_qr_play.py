from flask import render_template, request, jsonify
from python_helpers.ph_constants import PhConstants
from python_helpers.ph_keys import PhKeys
from python_helpers.ph_modes_error_handling import PhErrorHandlingModes
from python_helpers.ph_util import PhUtil
from qr_play.main.data_type.data_type_master import DataTypeMaster
from qr_play.main.data_type.sample import Sample
from qr_play.main.helper.constants_config import GIT_SUMMARY
from qr_play.main.helper.defaults import Defaults
from qr_play.main.helper.formats import Formats
from qr_play.main.helper.formats_group import FormatsGroup

from amenity_pj.helper.constants import Const
from amenity_pj.helper.util import Util


def handle_requests(api=False):
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
        requested_data_dict.update({target_key: int(requested_data_dict.get(target_key))})

    samples_dict = Sample().get_sample_data_pool_for_web()
    samples_list = PhUtil.generalise_list(list(samples_dict.keys()), sort=False)
    qr_code_versions = PhUtil.generalise_list(FormatsGroup.QR_CODE_VERSIONS_SUPPORTED)
    image_formats = PhUtil.generalise_list(FormatsGroup.IMAGE_FORMATS_SUPPORTED)
    default_data = {
        PhKeys.APP_TITLE: Const.TITLE_QR_PLAY,
        PhKeys.APP_DESCRIPTION: Const.DESCRIPTION_QR_PLAY,
        PhKeys.APP_VERSION: Const.VERSION_QR_PLAY,
        PhKeys.APP_GITHUB_URL: Util.get_github_url(github_repo=Const.GITHUB_REPO_QR_PLAY, github_pages=False),
        PhKeys.APP_GITHUB_PAGES_URL: Util.get_github_url(github_repo=Const.GITHUB_REPO_QR_PLAY, github_pages=True),
        PhKeys.APP_GIT_SUMMARY: GIT_SUMMARY,
        PhKeys.SAMPLES: samples_list,
        PhKeys.SAMPLE_SELECTED: samples_list[1] if len(samples_list) > 1 else None,
        PhKeys.SAMPLE_OPTION: PhKeys.SAMPLE_LOAD_ONLY,
        PhKeys.INPUT_DATA: PhConstants.STR_EMPTY,
        PhKeys.OUTPUT_DATA: PhConstants.STR_EMPTY,
        PhKeys.QR_CODE_VERSIONS: qr_code_versions,
        PhKeys.QR_CODE_VERSION_SELECTED: Defaults.QR_CODE_VERSION,
        PhKeys.IMAGE_FORMATS: image_formats,
        PhKeys.IMAGE_FORMAT_SELECTED: Defaults.IMAGE_FORMAT,
        PhKeys.SPLIT_QRS: Defaults.SPLIT_QRS,
        PhKeys.SCALE: Defaults.SCALE,
    }
    log_req = f'{Const.TEMPLATE_QR_PLAY}; {request.method}; {"API" if api else "Form"} Request'
    PhUtil.print_separator(main_text=f'{log_req} Received!!!')
    requested_data_dict = request.get_json() if request.is_json else request.form.to_dict()
    PhUtil.print_iter(requested_data_dict, header='Inputs')
    if request.method == PhKeys.GET:
        pass
    if request.method == PhKeys.POST:
        process_sample = True if PhKeys.PROCESS_SAMPLE in requested_data_dict else None
        sample_option = requested_data_dict.get(PhKeys.SAMPLE_OPTION, None)
        sample_name = requested_data_dict.get(PhKeys.SAMPLE, None)
        sample_dict = None
        # When submitting an HTML form,
        # 1) unchecked checkboxes do not send any data, however checked checkboxes do send False (may send True as well)
        update_checked_item(PhKeys.SPLIT_QRS)
        # 2) Everything is converted to String; below needs to be typecasted
        # XXX: This should be handled in parse_config; integer
        update_integer_item(PhKeys.QR_CODE_VERSION)
        update_integer_item(PhKeys.SCALE)
        print(f'process_sample is {process_sample}')
        if process_sample:
            sample_dict = samples_dict.get(sample_name, None)
            if sample_dict:
                print('sample_dict is available')
        if sample_dict and sample_option == PhKeys.SAMPLE_LOAD_ONLY:
            # Data Processing is not needed
            pass
        else:
            # Data Processing is needed in all other cases
            dic_received = sample_dict if sample_dict else requested_data_dict
            # PhUtil.print_iter(dic_received, header='dic_received')
            # Filter All Processing Related Keys
            dic_to_process = PhUtil.filter_processing_related_keys(dic_received)
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
        # Conditional Updates
        update_default_data(PhKeys.INPUT_DATA)
        update_default_data(PhKeys.SPLIT_QRS)
        update_default_data(PhKeys.QR_CODE_VERSION, PhKeys.QR_CODE_VERSION_SELECTED)
        update_default_data(PhKeys.IMAGE_FORMAT, PhKeys.IMAGE_FORMAT_SELECTED)
        update_default_data(PhKeys.SCALE)
        update_default_data(PhKeys.REMARKS)
        # Fixed Updates
        default_data.update({PhKeys.SAMPLE_SELECTED: sample_name})
        default_data.update({PhKeys.SAMPLE_OPTION: sample_option})
        PhUtil.print_iter(default_data, header='Outputs')
    PhUtil.print_separator(main_text=f'{log_req} Completed!!!')
    return jsonify(**default_data) if api else render_template(Const.TEMPLATE_QR_PLAY, **default_data)
