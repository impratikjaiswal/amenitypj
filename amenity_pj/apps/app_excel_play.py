# from excel_play.main.data_type.data_type_master import DataTypeMaster
# from python_helpers.ph_modes_error_handling import PhErrorHandlingModes
# from excel_play.main.helper.defaults import Defaults
from excel_play.main.helper.constants_config import GIT_SUMMARY
from flask import request
from python_helpers.ph_constants import PhConstants
from python_helpers.ph_keys import PhKeys
from python_helpers.ph_util import PhUtil

from amenity_pj.helper.constants import Const as aConstants
from amenity_pj.helper.defaults import Defaults as aDefaults
from amenity_pj.helper.util import Util as aUtil


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

    template_id = aConstants.TEMPLATE_EXCEL_PLAY
    default_data = {
        PhKeys.APP_PARENT_TITLE: aConstants.TITLE_AMENITY_PJ,
        PhKeys.APP_PARENT_VERSION: aConstants.VERSION_AMENITY_PJ,
        PhKeys.APP_TITLE: aConstants.TITLE_EXCEL_PLAY,
        PhKeys.APP_VERSION: aConstants.VERSION_EXCEL_PLAY,
        PhKeys.APP_DESCRIPTION: aConstants.DESCRIPTION_EXCEL_PLAY,
        PhKeys.APP_GITHUB_URL: aUtil.get_github_url(github_repo=aConstants.GITHUB_REPO_EXCEL_PLAY, github_pages=False),
        PhKeys.APP_GITHUB_PAGES_URL: aUtil.get_github_url(github_repo=aConstants.GITHUB_REPO_EXCEL_PLAY,
                                                          github_pages=True),
        PhKeys.APP_GIT_SUMMARY: GIT_SUMMARY,
        PhKeys.SAMPLE_OPTION: aDefaults.SAMPLE_OPTION,
        PhKeys.INPUT_DATA: PhConstants.STR_EMPTY,
        PhKeys.OUTPUT_DATA: PhConstants.STR_EMPTY,
        PhKeys.INFO_DATA: PhConstants.STR_EMPTY,
    }
    requested_data_dict = aUtil.request_pre(request=request, template_id=template_id, api=api, log=log)
    if request.method == PhKeys.GET:
        pass
    if request.method == PhKeys.POST:
        process_sample = True if PhKeys.PROCESS_SAMPLE in requested_data_dict else None
        sample_option = requested_data_dict.get(PhKeys.SAMPLE_OPTION, None)
        sample_name = requested_data_dict.get(PhKeys.SAMPLE, None)
        sample_dict = None
        # When submitting an HTML form,
        # 1) unchecked checkboxes do not send any data, however checked checkboxes do send False (may send True as well)
        pass
        # 2) Everything is converted to String; below needs to be typecast, TODO: should be handled in parse_config; int
        pass
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
        # Conditional Updates
        update_default_data(PhKeys.INPUT_DATA)
        # Fixed Updates
        default_data.update({PhKeys.SAMPLE_OPTION: sample_option})
    return aUtil.request_post(default_data=default_data, request=request, template_id=template_id, api=api, log=log)
