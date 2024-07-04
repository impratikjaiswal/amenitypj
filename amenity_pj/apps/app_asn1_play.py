from asn1_play.generated_code.asn1.asn1 import Asn1
from asn1_play.generated_code.asn1.asn1_versions import Asn1Versions
from asn1_play.main.data_type.data_type_master import DataTypeMaster
from asn1_play.main.data_type.sample import Sample
from asn1_play.main.helper.constants_config import GIT_SUMMARY
from asn1_play.main.helper.defaults import Defaults
from asn1_play.main.helper.formats_group import FormatsGroup
from flask import request, jsonify
from python_helpers.ph_constants import PhConstants
from python_helpers.ph_keys import PhKeys
from python_helpers.ph_modes_error_handling import PhErrorHandlingModes
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

    samples_dict = Sample().get_sample_data_pool_for_web()
    samples_list = PhUtil.generalise_list(list(samples_dict.keys()), sort=False)
    input_formats = PhUtil.generalise_list(FormatsGroup.INPUT_FORMATS_SUPPORTED)
    output_formats = PhUtil.generalise_list(FormatsGroup.OUTPUT_FORMATS_SUPPORTED)
    asn1_schemas = PhUtil.generalise_list(Asn1Versions._get_list_of_supported_versions())
    default_selected_asn1_schema = Defaults.ASN1_SCHEMA.get_name()
    asn1_objects = get_asn1_objects_list(default_selected_asn1_schema)
    template_id = aConstants.TEMPLATE_ASN1_PLAY
    default_data = {
        # TODO Implement dic in const
        PhKeys.APP_PARENT_TITLE: aConstants.TITLE_AMENITY_PJ,
        PhKeys.APP_PARENT_VERSION: aConstants.VERSION_AMENITY_PJ,
        PhKeys.APP_TITLE: aConstants.TITLE_ASN1_PLAY,
        PhKeys.APP_VERSION: aConstants.VERSION_ASN1_PLAY,
        PhKeys.APP_DESCRIPTION: aConstants.DESCRIPTION_ASN1_PLAY,
        PhKeys.APP_GITHUB_URL: aUtil.get_github_url(github_repo=aConstants.GITHUB_REPO_ASN1_PLAY, github_pages=False),
        PhKeys.APP_GITHUB_PAGES_URL: aUtil.get_github_url(github_repo=aConstants.GITHUB_REPO_ASN1_PLAY,
                                                          github_pages=True),
        PhKeys.APP_GIT_SUMMARY: GIT_SUMMARY,
        PhKeys.SAMPLES: samples_list,
        PhKeys.SAMPLE_SELECTED: samples_list[1] if len(samples_list) > 1 else None,
        PhKeys.SAMPLE_OPTION: aDefaults.SAMPLE_OPTION,
        PhKeys.INPUT_DATA: PhConstants.STR_EMPTY,
        PhKeys.OUTPUT_DATA: PhConstants.STR_EMPTY,
        PhKeys.INFO_DATA: PhConstants.STR_EMPTY,
        PhKeys.INPUT_FORMATS: input_formats,
        PhKeys.INPUT_FORMAT_SELECTED: Defaults.FORMAT_INPUT,
        PhKeys.OUTPUT_FORMATS: output_formats,
        PhKeys.OUTPUT_FORMAT_SELECTED: Defaults.FORMAT_OUTPUT,
        PhKeys.ASN1_SCHEMAS: asn1_schemas,
        PhKeys.ASN1_SCHEMA_SELECTED: default_selected_asn1_schema,
        PhKeys.ASN1_OBJECTS: asn1_objects,
        PhKeys.ASN1_OBJECT_SELECTED: PhConstants.STR_EMPTY,
        PhKeys.FETCH_ASN1_OBJECTS_LIST: False,
        # Delete?
        PhKeys.ASN1_OBJECT_ALTERNATE: PhConstants.STR_EMPTY,
        PhKeys.TLV_PARSING_OF_OUTPUT: False,
    }
    requested_data_dict = aUtil.request_pre(request=request, template_id=template_id, api=api, log=log)
    if request.method == PhKeys.GET:
        pass
    if request.method == PhKeys.POST:
        # if not requested_data_dict[PhKeys.INPUT_DATA]:
        #     flash('input_data is required!')
        process_sample = True if PhKeys.PROCESS_SAMPLE in requested_data_dict else None
        sample_option = requested_data_dict.get(PhKeys.SAMPLE_OPTION, None)
        sample_name = requested_data_dict.get(PhKeys.SAMPLE, None)
        sample_dict = None
        # When submitting an HTML form,
        # 1) unchecked checkboxes do not send any data, however checked checkboxes do send False (may send True as well)
        update_checked_item(PhKeys.TLV_PARSING_OF_OUTPUT)
        update_checked_item(PhKeys.FETCH_ASN1_OBJECTS_LIST)
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
            data_type = DataTypeMaster()
            data_type.set_data_pool(data_pool=dic_to_process)
            data_type.parse_safe(PhErrorHandlingModes.CONTINUE_ON_ERROR)
            output_data, info_data = data_type.get_output_data(only_output=False)
            default_data.update({PhKeys.OUTPUT_DATA: output_data})
            default_data.update({PhKeys.INFO_DATA: info_data})
        # Conditional Updates
        update_default_data(PhKeys.INPUT_DATA)
        update_default_data(PhKeys.INPUT_FORMAT, PhKeys.INPUT_FORMAT_SELECTED)
        update_default_data(PhKeys.OUTPUT_FORMAT, PhKeys.OUTPUT_FORMAT_SELECTED)
        selected_asn1_schema = update_default_data(PhKeys.ASN1_SCHEMA, PhKeys.ASN1_SCHEMA_SELECTED)
        if selected_asn1_schema:
            default_data.update({PhKeys.ASN1_OBJECTS: get_asn1_objects_list(selected_asn1_schema)})
        update_default_data(PhKeys.ASN1_OBJECT, PhKeys.ASN1_OBJECT_SELECTED)
        update_default_data(PhKeys.ASN1_OBJECT_ALTERNATE)
        update_default_data(PhKeys.TLV_PARSING_OF_OUTPUT)
        update_default_data(PhKeys.FETCH_ASN1_OBJECTS_LIST)
        update_default_data(PhKeys.REMARKS)
        # Fixed Updates
        default_data.update({PhKeys.SAMPLE_SELECTED: sample_name})
        default_data.update({PhKeys.SAMPLE_OPTION: sample_option})
    return aUtil.request_post(default_data=default_data, request=request, template_id=template_id, api=api, log=log)


def get_asn1_objects_list(asn1_schema_str):
    asn1_objects_list = []
    if not PhUtil.is_generalised_item(asn1_schema_str):
        asn1_schema = Asn1Versions._get_asn1_version(asn1_schema_str)
        asn1 = Asn1(asn1_schema=asn1_schema)
        asn1_objects_list = asn1.get_asn1_object_list()
    asn1_objects_list = PhUtil.generalise_list(asn1_objects_list)
    return asn1_objects_list


def handle_asn1_objects():
    """

    :return:
    """
    selected_asn1_schema_js = request.args.get('selected_asn1_schema_js', type=str)
    selected_asn1_object_js = request.args.get('selected_asn1_object_js', type=str)
    print(f'selected_asn1_schema_js: {selected_asn1_schema_js}')
    print(f'selected_asn1_object_js: {selected_asn1_object_js}')
    updated_values = get_asn1_objects_list(selected_asn1_schema_js)
    html_string_selected = ''
    for entry in updated_values:
        if entry == selected_asn1_object_js:
            html_string_selected += '<option value="{}" SELECTED>{}</option>'.format(entry, entry)
        else:
            html_string_selected += '<option value="{}">{}</option>'.format(entry, entry)
    print(f'html_string_selected: {html_string_selected}')
    return jsonify(html_string_selected=html_string_selected)
