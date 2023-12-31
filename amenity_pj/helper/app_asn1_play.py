from asn1_play.generated_code.asn1.GSMA.SGP_22 import asn1_mapping
from asn1_play.generated_code.asn1.asn1_versions import Asn1Versions
from asn1_play.main.data_type.data_type_master import DataTypeMaster
from asn1_play.main.helper.defaults import Defaults
from asn1_play.main.helper.formats import Formats
from asn1_play.main.helper.formats_group import FormatsGroup
from flask import render_template, request
from python_helpers.ph_constants import PhConstants
from python_helpers.ph_modes_error_handling import PhErrorHandlingModes
from python_helpers.ph_util import PhUtil

from amenity_pj.helper.constants import Const


def get_sample_data(key):
    # TODO: Remove usage of asn1_object_alternate once list is populated
    sample_data = {
        'sample_1': {
            'remarks_list': 'GSMA_SGP22_v3_0_0; Der to Asn1;',
            'raw_data': 'BF25335A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D652031',
            'asn1_schema': Asn1Versions.GSMA_SGP_22_v3_0_0.get_name(),
            'asn1_object': Defaults.ASN1_OBJECT,
            'asn1_object_alternate': Defaults.ASN1_OBJECT,
            'input_format': Formats.DER,
            'output_format': Formats.ASN1,
        },
        'sample_1_1': {
            'remarks_list': 'GSMA_SGP22_v2_4; Der to Asn1;',
            'raw_data': 'BF25335A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D652031',
            'asn1_schema': Asn1Versions.GSMA_SGP_22_v2_4.get_name(),
            'asn1_object': Defaults.ASN1_OBJECT,
            'asn1_object_alternate': Defaults.ASN1_OBJECT,
            'input_format': Formats.DER,
            'output_format': Formats.ASN1,
        },
        'sample_2': {
            'remarks_list': 'SGP22; Asn1 to Der; Tlv',
            'raw_data': """{
  iccid '989209012143658709F5'H,
  serviceProviderName "SP Name 1",
  profileName "Operational Profile Name 1"
}""",
            'asn1_schema': Asn1Versions.GSMA_SGP_22_v3_0_0.get_name(),
            'asn1_object': Defaults.ASN1_OBJECT,
            'asn1_object_alternate': Defaults.ASN1_OBJECT,
            'input_format': Formats.ASN1,
            'output_format': Formats.DER,
            'tlv_parsing_of_output': True,
        },
        'sample_2_1': {
            'remarks_list': 'SGP22; Asn1 to Der; Tlv',
            'raw_data': """{
      iccid '989209012143658709F5'H,
      serviceProviderName "SP Name 1",
      profileName "Operational Profile Name 1"
    }""",
            'asn1_schema': Asn1Versions.GSMA_SGP_22_v3_0_0.get_name(),
            'asn1_object': Defaults.ASN1_OBJECT,
            'asn1_object_alternate': Defaults.ASN1_OBJECT,
            'input_format': Formats.ASN1,
            'output_format': Formats.DER,
        },
        'sample_3': {
            'remarks_list': 'TCA; Asn1 to Der',
            'raw_data': """{
    major-version 2,
    minor-version 1,
    profileType "GSMA Profile Package",
    iccid '8929901012345678905F'H,
    eUICC-Mandatory-services {
        usim NULL
    },
    eUICC-Mandatory-GFSTEList {
        {2 23 143 1 2 1}
    }
}""",
            'asn1_schema': Asn1Versions.TCA_EPP_v3_2.get_name(),
            'asn1_object': 'ProfileHeader',
            'asn1_object_alternate': 'ProfileHeader',
            'input_format': Formats.ASN1,
            'output_format': Formats.DER,
        },
        'sample_4': {
            'remarks_list': 'Der(Hex) to Base 64',
            'raw_data': 'BF25335A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D652031',
            'input_format': Formats.DER,
            'output_format': Formats.DER_64,
        },
        'sample_5': {
            'remarks_list': 'Ascii to Hex',
            'raw_data': 'Welcome To AsnPlay !!!',
            'input_format': Formats.ASCII,
            'output_format': Formats.HEX,
        },
        'sample_6': {
            'remarks_list': 'Hex to ASCII',
            'raw_data': '57656c636f6d6520546f2041736e506c617920212121',
            'input_format': Formats.HEX,
            'output_format': Formats.ASCII,
        },
        'sample_7': {
            'remarks_list': 'PKIX1Explicit88; Der to Asn1; Certificate',
            'raw_data': '308201ff308201a6a0030201020209020000000000000001300a06082a8648ce3d0403023037310b300906035504061302455331153013060355040a0c0c52535020546573742045554d3111300f06035504030c0845554d20546573743020170d3230303430313039343835385a180f37343936303132343039343835385a3064310b300906035504061302455331153013060355040a0c0c52535020546573742045554d312930270603550405132038393034393033323132333435313233343531323334353637383930313233353113301106035504030c0a54657374206555494343305a301406072a8648ce3d020106092b2403030208010107034200043e590c38a9c256315ecff3291416dd335409a666fd41b3b51e5e5114f343abf0a26774c6c26c48753afe283643227bb6608cd261cc972d374a479124ebf27722a36b3069301f0603551d230418301680146fa1e5217363a822bded988a1a0d0ff5d7620db7301d0603551d0e04160414c8a64f343b85b7b0578dc57f8f13586dc804ed84300e0603551d0f0101ff04040302078030170603551d200101ff040d300b3009060767811201020101300a06082a8648ce3d040302034700304402205673c0fe8ff495ae93ae37a13296b2cb1b1017d7697053ed6920e987928699d70220059c7fec056869f24b548ac64757e4cb14d3a08609752c79a5b872a4980e338b',
            'asn1_schema': Asn1Versions.GSMA_SGP_22_v3_0_0.get_name(),
            'asn1_object': 'Certificate',
            'asn1_object_alternate': 'Certificate',
            'input_format': Formats.DER,
            'output_format': Formats.ASN1,
        },
    }
    return sample_data.get(key, None)


def handle_requests():
    """

    :return:
    """

    input_formats = PhUtil.generalise_list(FormatsGroup.INPUT_FORMATS)
    output_formats = PhUtil.generalise_list(FormatsGroup.ALL_FORMATS)
    asn1_objects = PhUtil.generalise_list(asn1_mapping)
    asn1_schemas = PhUtil.generalise_list(PhUtil.get_obj_list(Asn1Versions, clean_name=True))
    default_data = {
        'app_title': Const.TITLE_ASN1_PLAY,
        'app_description': Const.DESCRIPTION_ASN1_PLAY,
        'app_version': Const.VERSION_ASN1_PLAY,
        'app_github_url': Const.GITHUB_URL_ASN1_PLAY,
        'input_formats': input_formats,
        'output_formats': output_formats,
        'asn1_schemas': asn1_schemas,
        'asn1_objects': asn1_objects,
        'asn1_object_alternate': PhConstants.STR_EMPTY,
        'selected_input_format': Defaults.FORMAT_INPUT,
        'selected_output_format': Defaults.FORMAT_OUTPUT,
        'selected_asn1_schema': Defaults.ASN1_SCHEMA.get_name(),
        'selected_asn1_object': Defaults.ASN1_OBJECT,
        'tlv_parsing_of_output': False,
        'sample_processing': 'load_only',
        'output_data': '',
    }
    if request.method == 'GET':
        return render_template(Const.TEMPLATE_ASN1_PLAY, **default_data)
    if request.method == 'POST':
        PhUtil.print_iter(request.form, header='request.form')
        sample_processing = request.form['sample_processing']
        # if not request.form[PhKeys.RAW_DATA]:
        #     flash('raw_data is required!')
        sample_data_dict = None
        for key in request.form.keys():
            if not key.startswith('sample'):
                continue
            sample_data_dict = get_sample_data(key)
            if sample_data_dict:
                break
        if sample_data_dict and sample_processing == 'load_only':
            # Data Processing is not needed
            pass
        else:
            # Data Processing is needed in all other cases
            # Filter All Sample Keys
            dic_to_process = {k: v for k, v in
                              (sample_data_dict if sample_data_dict else request.form.to_dict()).items() if
                              not (k.startswith('sample') or k.startswith('process'))}
            data_type = DataTypeMaster()
            data_type.set_data_pool(data_pool=dic_to_process)
            data_type.parse_safe(PhErrorHandlingModes.CONTINUE_ON_ERROR)
            default_data.update({'output_data': data_type.get_output_data()})
        if sample_data_dict:
            # Mandatory Objects
            default_data.update({'raw_data': sample_data_dict.get('raw_data')})
            default_data.update({'selected_input_format': sample_data_dict.get('input_format')})
            default_data.update({'selected_output_format': sample_data_dict.get('output_format')})
            # Optional Objects
            if 'asn1_schema' in sample_data_dict:
                default_data.update({'selected_asn1_schema': sample_data_dict.get('asn1_schema')})
            if 'asn1_object' in sample_data_dict:
                default_data.update({'selected_asn1_object': sample_data_dict.get('asn1_object')})
            if 'asn1_object_alternate' in sample_data_dict:
                default_data.update({'asn1_object_alternate': sample_data_dict.get('asn1_object_alternate')})
            if 'tlv_parsing_of_output' in sample_data_dict:
                default_data.update({'tlv_parsing_of_output': sample_data_dict.get('tlv_parsing_of_output')})
            if 'remarks_list' in sample_data_dict:
                default_data.update({'remarks_list': sample_data_dict.get('remarks_list')})
        else:
            default_data.update({'raw_data': request.form['raw_data']})
            default_data.update({'selected_input_format': request.form['input_format']})
            default_data.update({'selected_output_format': request.form['output_format']})
            default_data.update({'selected_asn1_schema': request.form['asn1_schema']})
            default_data.update({'selected_asn1_object': request.form['asn1_object']})
            default_data.update({'asn1_schema': request.form['asn1_schema']})
            default_data.update({'asn1_object': request.form['asn1_object']})
            default_data.update({'asn1_object_alternate': request.form['asn1_object_alternate']})
            if 'tlv_parsing_of_output' in request.form.keys():
                default_data.update({'tlv_parsing_of_output': True})
            default_data.update({'remarks_list': request.form['remarks_list']})
        default_data.update({'sample_processing': sample_processing})
        return render_template(Const.TEMPLATE_ASN1_PLAY, **default_data)
    return render_template(Const.TEMPLATE_ASN1_PLAY, **default_data)
