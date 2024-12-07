from data_play.main.data_type.data_type_master import DataTypeMaster
from data_play.main.data_type.sample import Sample
from data_play.main.helper.defaults import Defaults
from flask import request
from python_helpers.ph_keys import PhKeys
from python_helpers.ph_modes_error_handling import PhErrorHandlingModes
from python_helpers.ph_util import PhUtil

from amenity_pj.helper.util import Util


def handle_requests(apj_id, api, log, default_data, **kwargs):
    """

    :return:
    """

    def update_app_data(source_key, target_key=None):
        """

        :param source_key:
        :param target_key:
        :return:
        """
        target_key = source_key if target_key is None else target_key
        source_dict = sample_dict if sample_dict else requested_data_dict
        if source_key in source_dict:
            app_data.update({target_key: source_dict.get(source_key)})
        return app_data.get(target_key, None)

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
    default_data_app = {
        PhKeys.SAMPLES: samples_list,
        PhKeys.SAMPLE_SELECTED: samples_list[1] if len(samples_list) > 1 else None,
        PhKeys.CONTENT_MAPPINGS: Defaults.CONTENT_MAPPINGS,
        PhKeys.NAME_MAPPINGS: Defaults.NAME_MAPPINGS,
    }
    app_data = PhUtil.dict_merge(default_data, default_data_app)
    requested_data_dict = Util.request_pre(request=request, apj_id=apj_id, api=api, log=log)
    if request.method == PhKeys.GET:
        pass
    if request.method == PhKeys.POST:
        process_sample_random = True if PhKeys.PROCESS_SAMPLE_RANDOM in requested_data_dict else False
        if process_sample_random:
            process_sample = True
            sample_option = PhKeys.SAMPLE_LOAD_AND_SUBMIT
            sample_name = PhUtil.get_random_item_from_iter(samples_dict, skip_generalise_item=True)
        else:
            process_sample = True if PhKeys.PROCESS_SAMPLE in requested_data_dict else None
            sample_option = requested_data_dict.get(PhKeys.SAMPLE_OPTION, None)
            sample_name = requested_data_dict.get(PhKeys.SAMPLE, None)
        sample_dict = None
        # When submitting an HTML form,
        # 1) unchecked check-boxes do not send any data, however checked checkboxes do send False (may send True as well)
        pass
        # 2) Everything is converted to String; below needs to be typecast, TODO: should be handled in parse_config; int
        pass
        PhUtil.print(f'process_sample is {process_sample}', log=log)
        if process_sample:
            sample_dict = samples_dict.get(sample_name, None)
            if sample_dict:
                PhUtil.print_iter(sample_dict, header='sample_dict', log=log)
        if sample_dict and sample_option == PhKeys.SAMPLE_LOAD_ONLY:
            PhUtil.print('Data Processing is not needed', log=log)
            pass
        else:
            PhUtil.print('Data Processing is needed', log=log)
            dic_received = sample_dict if sample_dict else requested_data_dict
            # Filter All Processing Related Keys
            dic_to_process = PhUtil.filter_processing_related_keys(dic_received)
            PhUtil.print_iter(dic_to_process, header='dic_to_process', log=log)
            data_type = DataTypeMaster()
            data_type.set_data_pool(data_pool=dic_to_process)
            data_type.process_safe(PhErrorHandlingModes.CONTINUE_ON_ERROR)
            output_data, info_data = data_type.get_output_data(only_output=False)
            app_data.update({PhKeys.OUTPUT_DATA: output_data})
            app_data.update({PhKeys.INFO_DATA: info_data})
            app_data.update({PhKeys.TRANSACTION_ID: Util.fetch_transaction_id_from_info_data(info_data)})
        # Conditional Updates
        update_app_data(PhKeys.INPUT_DATA)
        update_app_data(PhKeys.CONTENT_MAPPINGS)
        update_app_data(PhKeys.NAME_MAPPINGS)
        update_app_data(PhKeys.REMARKS)
        # Fixed Updates
        app_data.update({PhKeys.SAMPLE_SELECTED: sample_name})
        app_data.update({PhKeys.SAMPLE_OPTION: sample_option})
    return Util.request_post(request=request, apj_id=apj_id, api=api, log=log, output_data=app_data)