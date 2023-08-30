from asn1_play.main.data_type.data_type_master import DataTypeMaster
from asn1_play.main.helper.constants_config import ConfigConst
from asn1_play.main.helper.defaults import Defaults
from asn1_play.main.helper.formats import Formats
from asn1_play.main.helper.formats_group import FormatsGroup
from flask import render_template, request
from python_helpers.ph_modes_error_handling import PhErrorHandlingModes
from python_helpers.ph_util import PhUtil


def get_sample_data(key):
    sample_data = {
        'sample_1': {
            'remarks_list': 'SGP22; Der to Asn1',
            'raw_data': 'BF25335A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D652031',
            'asn1_element': 'StoreMetadataRequest',
            'input_format': Formats.DER,
            'output_format': Formats.ASN1,
            'tlv_parsing_of_output': False,
        },
        'sample_2': {
            'remarks_list': 'SGP22; Asn1 to Der; Tlv',
            'raw_data': """{
  iccid '989209012143658709F5'H,
  serviceProviderName "SP Name 1",
  profileName "Operational Profile Name 1"
}""",
            'asn1_element': 'StoreMetadataRequest',
            'input_format': Formats.ASN1,
            'output_format': Formats.DER,
            'tlv_parsing_of_output': True,
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
            'asn1_element': 'ProfileHeader',
            'input_format': Formats.ASN1,
            'output_format': Formats.DER,
            'tlv_parsing_of_output': False,
        },
        'sample_4': {
            'remarks_list': 'Der(Hex) to Base 64',
            'raw_data': 'BF25335A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D652031',
            'input_format': Formats.DER,
            'output_format': Formats.DER_64,
            'asn1_element': ' ',
            'tlv_parsing_of_output': False,

        },
        'sample_5': {
            'remarks_list': 'Ascii to Hex',
            'raw_data': 'Welcome To AsnPlay !!!',
            'input_format': Formats.ASCII,
            'output_format': Formats.HEX,
            'asn1_element': ' ',
            'tlv_parsing_of_output': False,

        },
        'sample_6': {
            'remarks_list': 'Hex to ASCII',
            'raw_data': '57656c636f6d6520546f2041736e506c617920212121',
            'input_format': Formats.HEX,
            'output_format': Formats.ASCII,
            'asn1_element': ' ',
            'tlv_parsing_of_output': False,
        }
    }
    return sample_data.get(key, None)


def handle_requests():
    """

    :return:
    """

    input_formats = FormatsGroup.INPUT_FORMATS
    input_formats.sort()
    output_formats = FormatsGroup.ALL_FORMATS
    output_formats.sort()
    page_url = 'asn1Play.html'
    default_data = {
        'version': f'v{ConfigConst.TOOL_VERSION}',
        'input_formats': input_formats,
        'output_formats': output_formats,
        'selected_input_format': Defaults.FORMAT_INPUT,
        'selected_output_format': Defaults.FORMAT_OUTPUT,
        'sample_processing': 'load_only',
        'output_data': '',
    }
    if request.method == 'GET':
        return render_template(page_url, **default_data)
    if request.method == 'POST':
        PhUtil.print_iter(request.form, header='request.form')
        sample_processing = request.form['sample_processing']
        # if not request.form['raw_data']:
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
                              not k.startswith('sample')}
            data_type = DataTypeMaster()
            data_type.set_data_pool(data_pool=dic_to_process)
            data_type.parse_safe(PhErrorHandlingModes.CONTINUE_ON_ERROR)
            default_data.update({'output_data': data_type.get_output_data()})
        if sample_data_dict:
            default_data.update({'raw_data': sample_data_dict.get('raw_data')})
            default_data.update({'selected_input_format': sample_data_dict.get('input_format')})
            default_data.update({'selected_output_format': sample_data_dict.get('output_format')})
            default_data.update({'asn1_element': sample_data_dict.get('asn1_element')})
            default_data.update({'remarks_list': sample_data_dict.get('remarks_list')})
            default_data.update({'tlv_parsing_of_output': sample_data_dict.get('tlv_parsing_of_output')})
        else:
            default_data.update({'raw_data': request.form['raw_data']})
            default_data.update({'selected_input_format': request.form['input_format']})
            default_data.update({'selected_output_format': request.form['output_format']})
            default_data.update({'asn1_element': request.form['asn1_element']})
            default_data.update({'remarks_list': request.form['remarks_list']})
            default_data.update(
                {'tlv_parsing_of_output': True if 'tlv_parsing_of_output' in request.form.keys() else False})
        default_data.update({'sample_processing': sample_processing})
        return render_template(page_url, **default_data)
    return render_template(page_url, **default_data)
