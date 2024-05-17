from cert_play.main.data_type.data_type_master import DataTypeMaster
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


def get_sample_data(key):
    sample_data = {
        PhKeys.SAMPLE_1: {
            PhKeys.REMARKS_LIST: 'AmenityPj; Home Page',
            PhKeys.RAW_DATA: 'amenitypj.in',
            'input_format': Formats.URL,
        },
        PhKeys.SAMPLE_2: {
            PhKeys.REMARKS_LIST: 'AmenityPj; www; https;',
            PhKeys.RAW_DATA: 'https://www.amenitypj.in/',
            'input_format': Formats.URL,
        },
        PhKeys.SAMPLE_3: {
            PhKeys.REMARKS_LIST: 'AmenityPj; Sub Domain',
            PhKeys.RAW_DATA: 'beta.amenitypj.in',
            'input_format': Formats.URL,
        },
        PhKeys.SAMPLE_4: {
            PhKeys.REMARKS_LIST: 'Google',
            PhKeys.RAW_DATA: 'google.com',
            'input_format': Formats.URL,
        },
        PhKeys.SAMPLE_5: {
            PhKeys.REMARKS_LIST: 'Google; https; www;',
            PhKeys.RAW_DATA: 'https://www.google.com/',
            'input_format': Formats.URL,
        },
        PhKeys.SAMPLE_6: {
            PhKeys.REMARKS_LIST: 'WikiPedia; Sub Pages',
            PhKeys.RAW_DATA: 'https://en.wikipedia.org/wiki/Main_Page',
            'input_format': Formats.URL,
        },
        PhKeys.SAMPLE_7: {
            PhKeys.REMARKS_LIST: 'AmenityPj',
            PhKeys.RAW_DATA: r"""-----BEGIN CERTIFICATE-----
MIIErzCCA5egAwIBAgISA8caMPaDk56P1v8RvxkQdgxpMA0GCSqGSIb3DQEBCwUA
MDIxCzAJBgNVBAYTAlVTMRYwFAYDVQQKEw1MZXQncyBFbmNyeXB0MQswCQYDVQQD
EwJSMzAeFw0yNDA1MTEwNzM0MThaFw0yNDA4MDkwNzM0MTdaMBcxFTATBgNVBAMT
DGFtZW5pdHlwai5pbjBZMBMGByqGSM49AgEGCCqGSM49AwEHA0IABL74hi/pJ2op
qu+36ppYNCt65tD3B2Kq5u1C3n/QqlofA2tdW1MXMxTPX2x66cEuMWYH0eTi0EZW
v0tRB18Hy0ajggKjMIICnzAOBgNVHQ8BAf8EBAMCB4AwHQYDVR0lBBYwFAYIKwYB
BQUHAwEGCCsGAQUFBwMCMAwGA1UdEwEB/wQCMAAwHQYDVR0OBBYEFNPucKQzTDVM
jhjQEASfE1Gh44fWMB8GA1UdIwQYMBaAFBQusxe3WFbLrlAJQOYfr52LFMLGMFUG
CCsGAQUFBwEBBEkwRzAhBggrBgEFBQcwAYYVaHR0cDovL3IzLm8ubGVuY3Iub3Jn
MCIGCCsGAQUFBzAChhZodHRwOi8vcjMuaS5sZW5jci5vcmcvMIGrBgNVHREEgaMw
gaCCEmFscGhhLmFtZW5pdHlwai5pboIMYW1lbml0eXBqLmlughFiZXRhLmFtZW5p
dHlwai5pboIRcGFzdC5hbWVuaXR5cGouaW6CFnd3dy5hbHBoYS5hbWVuaXR5cGou
aW6CEHd3dy5hbWVuaXR5cGouaW6CFXd3dy5iZXRhLmFtZW5pdHlwai5pboIVd3d3
LnBhc3QuYW1lbml0eXBqLmluMBMGA1UdIAQMMAowCAYGZ4EMAQIBMIIBBAYKKwYB
BAHWeQIEAgSB9QSB8gDwAHYASLDja9qmRzQP5WoC+p0w6xxSActW3SyB2bu/qznY
hHMAAAGPZsnk6QAABAMARzBFAiEA5YpmM1dVtOW7SH2/SVEHpi9TdDv1j1+SMbia
w1CrqN4CIH/ulMV5ItLuRMyvz63qdkPHuesahzkNUNe1lJax8mlPAHYA3+FW66oF
r7WcD4ZxjajAMk6uVtlup/WlagHRwTu+UlwAAAGPZsnmAAAABAMARzBFAiEA5z82
NzuMuMPKl7z2lthCsSGZkNvO4VKHYJbMfrFwCAYCIDOTKLX5p+9CS8rF38jM0JZi
6Gh2GwoH04oEk6lIbdpGMA0GCSqGSIb3DQEBCwUAA4IBAQCYYN6K+WblpJXB3VDp
oaxJB/raiD5m4B0Yr4b0SFdBRNac/N+dBxxBTSizlW+2DkqU4j0Ni7DrudwpqZWM
e9pSTRtnIgUdAs9TqpwMszUuCrToDzIbBdxYyI+4cDbMpdJtRcJLBUvBrp38b6oF
p3hLs34VruS+SyXGIcnCzhJjSfUIMM51VCyyO+qbLWWRGPxz231lB6pktznflJtC
llqPaOGifLBa7it2I7chuMW00GuZ4MDytqmRtWu704KKy6jiuqp+c7+je6L+B63m
Vry1cZlWhDm4Mhs3wpJ2k8xjzOPiHHqGCAvjLZtXkx1y1T2Y1Si62lB1iGx939uc
rYhF
-----END CERTIFICATE-----""",
            'input_format': Formats.DER,
        },
    }
    return sample_data.get(key, None)


def handle_requests(api=False):
    """

    :return:
    """

    input_formats = PhUtil.generalise_list(FormatsGroup.INPUT_FORMATS_SUPPORTED)
    default_data = {
        'app_title': Const.TITLE_CERT_PLAY,
        'app_description': Const.DESCRIPTION_CERT_PLAY,
        'app_version': Const.VERSION_CERT_PLAY,
        'app_github_url': Util.get_github_url(github_repo=Const.GITHUB_REPO_CERT_PLAY, github_pages=False),
        'app_github_pages_url': Util.get_github_url(github_repo=Const.GITHUB_REPO_CERT_PLAY, github_pages=True),
        'app_git_summary': GIT_SUMMARY,
        PhKeys.RAW_DATA: PhConstants.STR_EMPTY,
        'input_formats': input_formats,
        'selected_input_format': Defaults.INPUT_FORMAT,
        PhKeys.SAMPLE_PROCESSING: PhKeys.SAMPLE_LOAD_ONLY,
        PhKeys.OUTPUT_DATA: PhConstants.STR_EMPTY,
    }
    log_req = f'{Const.TEMPLATE_CERT_PLAY}; {request.method}; {"API" if api else "Form"} Request'
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
            data_type = DataTypeMaster()
            data_type.set_data_pool(data_pool=dic_to_process)
            data_type.parse_safe(PhErrorHandlingModes.CONTINUE_ON_ERROR)
            output_data = data_type.get_output_data()
            default_data.update({PhKeys.OUTPUT_DATA: output_data})
        if sample_data_dict:
            if PhKeys.RAW_DATA in sample_data_dict:
                default_data.update({PhKeys.RAW_DATA: sample_data_dict.get(PhKeys.RAW_DATA)})
            if 'input_format' in sample_data_dict:
                default_data.update({'selected_input_format': sample_data_dict.get('input_format')})
            if PhKeys.REMARKS_LIST in sample_data_dict:
                default_data.update({PhKeys.REMARKS_LIST: sample_data_dict.get(PhKeys.REMARKS_LIST)})
        else:
            if PhKeys.RAW_DATA in requested_data_dict:
                default_data.update({PhKeys.RAW_DATA: requested_data_dict[PhKeys.RAW_DATA]})
            if 'input_format' in requested_data_dict:
                default_data.update({'selected_input_format': requested_data_dict['input_format']})
            if PhKeys.REMARKS_LIST in requested_data_dict:
                default_data.update({PhKeys.REMARKS_LIST: requested_data_dict[PhKeys.REMARKS_LIST]})
        default_data.update({PhKeys.SAMPLE_PROCESSING: sample_processing})
        PhUtil.print_iter(default_data, header='Outputs')
    PhUtil.print_separator(main_text=f'{log_req} Completed!!!')
    return jsonify(**default_data) if api else render_template(Const.TEMPLATE_CERT_PLAY, **default_data)
