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
        PhKeys.SAMPLE_8: {
            PhKeys.REMARKS_LIST: 'Der (Hex); AmenityPj',
            PhKeys.RAW_DATA: '308204AF30820397A003020102021203C71A30F683939E8FD6FF11BF1910760C69300D06092A864886F70D01010B05003032310B300906035504061302555331163014060355040A130D4C6574277320456E6372797074310B3009060355040313025233301E170D3234303531313037333431385A170D3234303830393037333431375A3017311530130603550403130C616D656E697479706A2E696E3059301306072A8648CE3D020106082A8648CE3D03010703420004BEF8862FE9276A29AAEFB7EA9A58342B7AE6D0F70762AAE6ED42DE7FD0AA5A1F036B5D5B53173314CF5F6C7AE9C12E316607D1E4E2D04656BF4B51075F07CB46A38202A33082029F300E0603551D0F0101FF040403020780301D0603551D250416301406082B0601050507030106082B06010505070302300C0603551D130101FF04023000301D0603551D0E04160414D3EE70A4334C354C8E18D010049F1351A1E387D6301F0603551D23041830168014142EB317B75856CBAE500940E61FAF9D8B14C2C6305506082B0601050507010104493047302106082B060105050730018615687474703A2F2F72332E6F2E6C656E63722E6F7267302206082B060105050730028616687474703A2F2F72332E692E6C656E63722E6F72672F3081AB0603551D110481A33081A08212616C7068612E616D656E697479706A2E696E820C616D656E697479706A2E696E8211626574612E616D656E697479706A2E696E8211706173742E616D656E697479706A2E696E82167777772E616C7068612E616D656E697479706A2E696E82107777772E616D656E697479706A2E696E82157777772E626574612E616D656E697479706A2E696E82157777772E706173742E616D656E697479706A2E696E30130603551D20040C300A3008060667810C01020130820104060A2B06010401D6790204020481F50481F200F000760048B0E36BDAA647340FE56A02FA9D30EB1C5201CB56DD2C81D9BBBFAB39D884730000018F66C9E4E90000040300473045022100E58A66335755B4E5BB487DBF495107A62F53743BF58F5F9231B89AC350ABA8DE02207FEE94C57922D2EE44CCAFCFADEA7643C7B9EB1A87390D50D7B59496B1F2694F007600DFE156EBAA05AFB59C0F86718DA8C0324EAE56D96EA7F5A56A01D1C13BBE525C0000018F66C9E6000000040300473045022100E73F36373B8CB8C3CA97BCF696D842B1219990DBCEE152876096CC7EB17008060220339328B5F9A7EF424BCAC5DFC8CCD09662E868761B0A07D38A0493A9486DDA46300D06092A864886F70D01010B050003820101009860DE8AF966E5A495C1DD50E9A1AC4907FADA883E66E01D18AF86F448574144D69CFCDF9D071C414D28B3956FB60E4A94E23D0D8BB0EBB9DC29A9958C7BDA524D1B6722051D02CF53AA9C0CB3352E0AB4E80F321B05DC58C88FB87036CCA5D26D45C24B054BC1AE9DFC6FAA05A7784BB37E15AEE4BE4B25C621C9C2CE126349F50830CE75542CB23BEA9B2D659118FC73DB7D6507AA64B739DF949B42965A8F68E1A27CB05AEE2B7623B721B8C5B4D06B99E0C0F2B6A991B56BBBD3828ACBA8E2BAAA7E73BFA37BA2FE07ADE656BCB57199568439B8321B37C2927693CC63CCE3E21C7A86080BE32D9B57931D72D53D98D528BADA5075886C7DDFDB9CAD8845',
            'input_format': Formats.DER,
        },
        PhKeys.SAMPLE_9: {
            PhKeys.REMARKS_LIST: 'Der (Hex); GSMA NIST CI Cert (SGP.26_v1.x)',
            PhKeys.RAW_DATA: '30820250308201F7A003020102020900B874F3ABFA6C44D3300A06082A8648CE3D04030230443110300E06035504030C07546573742043493111300F060355040B0C0854455354434552543110300E060355040A0C0752535054455354310B30090603550406130249543020170D3230303430313038323735315A180F32303535303430313038323735315A30443110300E06035504030C07546573742043493111300F060355040B0C0854455354434552543110300E060355040A0C0752535054455354310B30090603550406130249543059301306072A8648CE3D020106082A8648CE3D03010703420004940657A673DC288F89D52EA8A47704992791F9C34B0036E633E2D0CBA9454D65DB32EB17981799D2F24388EE2B95C1094546C97901CEAEBA9650919A2E20D229A381CF3081CC301D0603551D0E04160414F54172BDF98A95D65CBEB88A38A1C11D800A85C3300F0603551D130101FF040530030101FF30170603551D200101FF040D300B3009060767811201020100300E0603551D0F0101FF040403020106300E0603551D1104073005880388370130610603551D1F045A3058302AA028A0268624687474703A2F2F63692E746573742E6578616D706C652E636F6D2F43524C2D412E63726C302AA028A0268624687474703A2F2F63692E746573742E6578616D706C652E636F6D2F43524C2D422E63726C300A06082A8648CE3D0403020347003044022052756AAFC2020A6CECBF2E5F3C20892510FF29751D298BD3B015D9605A4FE67D022057982836E4D205DDD2E6C3C1B455937F6B6E493B602FD1B66C357489A935F76B',
            'input_format': Formats.DER,
        },
    }
    return sample_data.get(key, None)


def handle_requests(api=False):
    """

    :return:
    """

    samples_dic = Sample().get_sample_data_pool_for_web()
    samples_list = PhUtil.generalise_list(list(samples_dic.keys()), sort=False)
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
        'samples': samples_list,
        'selected_sample': samples_list[1] if len(samples_list) > 1 else None,
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
