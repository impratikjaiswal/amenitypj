from asn1_play.generated_code.asn1.asn1 import Asn1
from asn1_play.generated_code.asn1.asn1_versions import Asn1Versions
from asn1_play.main.data_type.data_type_master import DataTypeMaster
from asn1_play.main.data_type.sample import Sample
from asn1_play.main.helper.constants_config import GIT_SUMMARY
from asn1_play.main.helper.defaults import Defaults
from asn1_play.main.helper.formats_group import FormatsGroup
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

    samples_dict = Sample().get_sample_data_pool_for_web()
    samples_list = PhUtil.generalise_list(list(samples_dict.keys()), sort=False)
    input_formats = PhUtil.generalise_list(FormatsGroup.INPUT_FORMATS_SUPPORTED)
    output_formats = PhUtil.generalise_list(FormatsGroup.OUTPUT_FORMATS_SUPPORTED)
    asn1_schemas = PhUtil.generalise_list(Asn1Versions._get_list_of_supported_versions())
    default_selected_asn1_schema = Defaults.ASN1_SCHEMA.get_name()
    asn1_objects = get_asn1_objects_list(default_selected_asn1_schema)
    default_data = {
        PhKeys.APP_TITLE: Const.TITLE_ASN1_PLAY,
        PhKeys.APP_DESCRIPTION: Const.DESCRIPTION_ASN1_PLAY,
        PhKeys.APP_VERSION: Const.VERSION_ASN1_PLAY,
        PhKeys.APP_GITHUB_URL: Util.get_github_url(github_repo=Const.GITHUB_REPO_ASN1_PLAY, github_pages=False),
        PhKeys.APP_GITHUB_PAGES_URL: Util.get_github_url(github_repo=Const.GITHUB_REPO_ASN1_PLAY, github_pages=True),
        PhKeys.APP_GIT_SUMMARY: GIT_SUMMARY,
        PhKeys.SAMPLES: samples_list,
        PhKeys.SAMPLE_SELECTED: samples_list[1] if len(samples_list) > 1 else None,
        PhKeys.SAMPLE_OPTION: PhKeys.SAMPLE_LOAD_ONLY,
        PhKeys.INPUT_DATA: PhConstants.STR_EMPTY,
        PhKeys.OUTPUT_DATA: PhConstants.STR_EMPTY,
        PhKeys.INPUT_FORMATS: input_formats,
        PhKeys.INPUT_FORMAT_SELECTED: Defaults.FORMAT_INPUT,
        PhKeys.OUTPUT_FORMATS: output_formats,
        PhKeys.OUTPUT_FORMAT_SELECTED: Defaults.FORMAT_OUTPUT,
        PhKeys.ASN1_SCHEMAS: asn1_schemas,
        PhKeys.ASN1_SCHEMA_SELECTED: default_selected_asn1_schema,
        PhKeys.ASN1_OBJECTS: asn1_objects,
        PhKeys.ASN1_OBJECT_SELECTED: PhConstants.STR_EMPTY,
        PhKeys.FETCH_ASN1_OBJECTS_LIST: False,
        # Delete
        PhKeys.ASN1_OBJECT_ALTERNATE: PhConstants.STR_EMPTY,
        PhKeys.TLV_PARSING_OF_OUTPUT: False,
    }
    log_req = f'{Const.TEMPLATE_ASN1_PLAY}; {request.method}; {"API" if api else "Form"} Request'
    PhUtil.print_separator(main_text=f'{log_req} Received!!!')
    requested_data_dict = request.get_json() if request.is_json else request.form.to_dict()
    PhUtil.print_iter(requested_data_dict, header='Inputs')
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
        # 2) Everything is converted to String; below needs to be typecasted
        pass
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
            default_data.update({PhKeys.OUTPUT_DATA: output_data})
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
        PhUtil.print_iter(default_data, header='Outputs')
    PhUtil.print_separator(main_text=f'{log_req} Completed!!!')
    return jsonify(**default_data) if api else render_template(Const.TEMPLATE_ASN1_PLAY, **default_data)


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
