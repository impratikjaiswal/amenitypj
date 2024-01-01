from asn1_play.generated_code.asn1.GSMA.SGP_22 import asn1_mapping
from asn1_play.generated_code.asn1.asn1_versions import Asn1Versions
from asn1_play.main.data_type.data_type_master import DataTypeMaster
from asn1_play.main.helper.defaults import Defaults
from asn1_play.main.helper.formats import Formats
from asn1_play.main.helper.formats_group import FormatsGroup
from flask import render_template, request
from python_helpers.ph_constants import PhConstants
from python_helpers.ph_keys import PhKeys
from python_helpers.ph_modes_error_handling import PhErrorHandlingModes
from python_helpers.ph_util import PhUtil

from amenity_pj.helper.constants import Const


def get_sample_data(key):
    # TODO: Remove usage of asn1_object_alternate once list is populated
    sample_data = {
        PhKeys.SAMPLE_1: {
            PhKeys.REMARKS_LIST: 'GSMA_SGP22_v3_0_0; Der to Asn1;',
            PhKeys.RAW_DATA: 'BF2582031C5A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D6520319301019482029089504E470D0A1A0A0000000D49484452000000400000004008040000000060B9550000000774494D4507E00B091007364C956F97000000097048597300000B1200000B1201D2DD7EFC0000000467414D410000B18F0BFC61050000021F4944415478DAED99CD1583200C803D32000B3004ABB00ECBB0822338578AF559223F49B0A8175F2EC023E1238410DB09A667E5E1E55F80BF00F686060B1E66B80420C02A32550D0E966E8CC6F0128D193460635FA66A3B7D511DB48DD94788B655D7815071BA26E61B9000ACC711841085EB398D84C0CD94F921EBE2DDAB18DB6B5005B055C3BC752B4038745C5339449CD4950248100E1D4528FAC207B228E3101A4BD4AE52BA96A603808B05D44C27ADAB2AF8807A00A6184B228014807566ECA13538E5008AC890BF06BE809E4DBEBE0B808A842A009FFD7B010436AF06B04F034C8D47EA46004703E034E4D95B90A98A447300DC353C9F07A843404D9B2D904BCA84F62480A7013C39351431225B722DE9F6AD591A0047C194E5AE19BD865AFC1A26976F088603C0A7AC9117FCE131F64200BCDFED8E290EE058906C46F2FAD09DAC885AB1550C68D2A8B426DCF69B8E71F76D195B15CD368207463513FD2DEA6648476B2500EB999B6250FA5DC0499E0B88B921F2BBAF782E877588930370724E4D3F0DD01D49DBE7E92CB940423172008F3ED3C6011C03B1396BCE6EC24800C703B862682480A20142250B8C05C081385186CD65009607D059DD772B80AE3CB963010205B054436414808ABB0FF237752480A996FB3702D8334FDA0BF002BC002FC0488053B5F5380005DC0A1703F03FFDFDC433A6FA010CF1EF4165C831E602B40134844C66E67FA4C1000618E5AB8F6008C03FAAB7028C9117E0036BAF44917035AF0E0000000049454E44AE426082B621301F800204F0811974657374736D6470706C7573312E6578616D706C652E636F6DB705800392F91899020640BF220F300D8003883710A1060404C1020304BF230F300D8003883711A106040402020202',
            'asn1_schema': Asn1Versions.GSMA_SGP_22_v3_0_0.get_name(),
            'asn1_object': Defaults.ASN1_OBJECT,
            'asn1_object_alternate': Defaults.ASN1_OBJECT,
            'input_format': Formats.DER,
            'output_format': Formats.ASN1,
        },
        'sample_1_1': {
            PhKeys.REMARKS_LIST: 'GSMA_SGP22_v2_4; Der to Asn1;',
            PhKeys.RAW_DATA: 'BF2582031C5A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D6520319301019482029089504E470D0A1A0A0000000D49484452000000400000004008040000000060B9550000000774494D4507E00B091007364C956F97000000097048597300000B1200000B1201D2DD7EFC0000000467414D410000B18F0BFC61050000021F4944415478DAED99CD1583200C803D32000B3004ABB00ECBB0822338578AF559223F49B0A8175F2EC023E1238410DB09A667E5E1E55F80BF00F686060B1E66B80420C02A32550D0E966E8CC6F0128D193460635FA66A3B7D511DB48DD94788B655D7815071BA26E61B9000ACC711841085EB398D84C0CD94F921EBE2DDAB18DB6B5005B055C3BC752B4038745C5339449CD4950248100E1D4528FAC207B228E3101A4BD4AE52BA96A603808B05D44C27ADAB2AF8807A00A6184B228014807566ECA13538E5008AC890BF06BE809E4DBEBE0B808A842A009FFD7B010436AF06B04F034C8D47EA46004703E034E4D95B90A98A447300DC353C9F07A843404D9B2D904BCA84F62480A7013C39351431225B722DE9F6AD591A0047C194E5AE19BD865AFC1A26976F088603C0A7AC9117FCE131F64200BCDFED8E290EE058906C46F2FAD09DAC885AB1550C68D2A8B426DCF69B8E71F76D195B15CD368207463513FD2DEA6648476B2500EB999B6250FA5DC0499E0B88B921F2BBAF782E877588930370724E4D3F0DD01D49DBE7E92CB940423172008F3ED3C6011C03B1396BCE6EC24800C703B862682480A20142250B8C05C081385186CD65009607D059DD772B80AE3CB963010205B054436414808ABB0FF237752480A996FB3702D8334FDA0BF002BC002FC0488053B5F5380005DC0A1703F03FFDFDC433A6FA010CF1EF4165C831E602B40134844C66E67FA4C1000618E5AB8F6008C03FAAB7028C9117E0036BAF44917035AF0E0000000049454E44AE426082B621301F800204F0811974657374736D6470706C7573312E6578616D706C652E636F6DB705800392F91899020640BF220F300D8003883710A1060404C1020304BF230F300D8003883711A106040402020202',
            'asn1_schema': Asn1Versions.GSMA_SGP_22_v2_4.get_name(),
            'asn1_object': Defaults.ASN1_OBJECT,
            'asn1_object_alternate': Defaults.ASN1_OBJECT,
            'input_format': Formats.DER,
            'output_format': Formats.ASN1,
        },
        PhKeys.SAMPLE_2: {
            PhKeys.REMARKS_LIST: 'SGP22; Asn1 to Der',
            PhKeys.RAW_DATA: """{
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
        'sample_2_1': {
            PhKeys.REMARKS_LIST: 'SGP22; Asn1 to Der; Tlv',
            PhKeys.RAW_DATA: """{
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
        PhKeys.SAMPLE_3: {
            PhKeys.REMARKS_LIST: 'TCA; Asn1 to Der',
            PhKeys.RAW_DATA: """{
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
        'sample_3_1': {
            PhKeys.REMARKS_LIST: 'PKIX1Explicit88; Der to Asn1; Certificate',
            PhKeys.RAW_DATA: '308201ff308201a6a0030201020209020000000000000001300a06082a8648ce3d0403023037310b300906035504061302455331153013060355040a0c0c52535020546573742045554d3111300f06035504030c0845554d20546573743020170d3230303430313039343835385a180f37343936303132343039343835385a3064310b300906035504061302455331153013060355040a0c0c52535020546573742045554d312930270603550405132038393034393033323132333435313233343531323334353637383930313233353113301106035504030c0a54657374206555494343305a301406072a8648ce3d020106092b2403030208010107034200043e590c38a9c256315ecff3291416dd335409a666fd41b3b51e5e5114f343abf0a26774c6c26c48753afe283643227bb6608cd261cc972d374a479124ebf27722a36b3069301f0603551d230418301680146fa1e5217363a822bded988a1a0d0ff5d7620db7301d0603551d0e04160414c8a64f343b85b7b0578dc57f8f13586dc804ed84300e0603551d0f0101ff04040302078030170603551d200101ff040d300b3009060767811201020101300a06082a8648ce3d040302034700304402205673c0fe8ff495ae93ae37a13296b2cb1b1017d7697053ed6920e987928699d70220059c7fec056869f24b548ac64757e4cb14d3a08609752c79a5b872a4980e338b',
            'asn1_schema': Asn1Versions.GSMA_SGP_22_v3_0_0.get_name(),
            'asn1_object': 'Certificate',
            'asn1_object_alternate': 'Certificate',
            'input_format': Formats.DER,
            'output_format': Formats.ASN1,
        },
        'sample_3_2': {
            PhKeys.REMARKS_LIST: 'Asn1 Objects Static List; v3_1',
            'asn1_schema': Asn1Versions.GSMA_SGP_22_v3_1.get_name(),
            PhKeys.FETCH_ASN1_OBJECTS_LIST: True
        },
        PhKeys.SAMPLE_4: {
            PhKeys.REMARKS_LIST: 'Der(Hex) to Base 64',
            PhKeys.RAW_DATA: 'BF25335A0A989209012143658709F591095350204E616D652031921A4F7065726174696F6E616C2050726F66696C65204E616D652031',
            'input_format': Formats.DER,
            'output_format': Formats.DER_64,
            'asn1_schema': PhConstants.STR_SELECT_OPTION,
        },
        PhKeys.SAMPLE_5: {
            PhKeys.REMARKS_LIST: 'Ascii to Hex',
            PhKeys.RAW_DATA: 'Welcome To AsnPlay !!!',
            'input_format': Formats.ASCII,
            'output_format': Formats.HEX,
            'asn1_schema': PhConstants.STR_SELECT_OPTION,
        },
        PhKeys.SAMPLE_6: {
            PhKeys.REMARKS_LIST: 'Hex to ASCII',
            PhKeys.RAW_DATA: '57656c636f6d6520546f2041736e506c617920212121',
            'input_format': Formats.HEX,
            'output_format': Formats.ASCII,
            'asn1_schema': PhConstants.STR_SELECT_OPTION,
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
        PhKeys.RAW_DATA: PhConstants.STR_EMPTY,
        'input_formats': input_formats,
        'output_formats': output_formats,
        'tlv_parsing_of_output': False,
        'asn1_schemas': asn1_schemas,
        'asn1_objects': asn1_objects,
        'asn1_object_alternate': PhConstants.STR_EMPTY,
        'selected_input_format': Defaults.FORMAT_INPUT,
        'selected_output_format': Defaults.FORMAT_OUTPUT,
        'selected_asn1_schema': Defaults.ASN1_SCHEMA.get_name(),
        'selected_asn1_object': Defaults.ASN1_OBJECT,
        PhKeys.FETCH_ASN1_OBJECTS_LIST: False,
        'sample_processing': 'load_only',
        'output_data': PhConstants.STR_EMPTY,
    }
    if request.method == PhKeys.GET:
        return render_template(Const.TEMPLATE_ASN1_PLAY, **default_data)
    if request.method == PhKeys.POST:
        PhUtil.print_separator(main_text=f'{Const.TEMPLATE_QR_PLAY} Post Request Started')
        PhUtil.print_iter(request.form, header='Request Input')
        requested_data_dict = request.form.to_dict()
        # if not requested_data_dict[PhKeys.RAW_DATA]:
        #     flash('raw_data is required!')
        sample_processing = requested_data_dict[PhKeys.SAMPLE_PROCESSING]
        # When submitting an HTML form,
        # 1) unchecked checkboxes do not send any data, however checked checkboxes do send False (may send True as well)
        requested_data_dict.update({'tlv_parsing_of_output': True if 'tlv_parsing_of_output' in requested_data_dict else False})
        requested_data_dict.update({PhKeys.FETCH_ASN1_OBJECTS_LIST: True if PhKeys.FETCH_ASN1_OBJECTS_LIST in requested_data_dict else False})
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
            # Filter All Sample Keys
            # if sample_data_dict:
            #     PhUtil.print_iter(sample_data_dict, header='Request Input for sample_data_dict')
            # else:
            #     PhUtil.print_iter(requested_data_dict, header='Request Input for requested_data_dict')
            dic_to_process = {k: v for k, v in
                              (sample_data_dict if sample_data_dict else requested_data_dict).items() if
                              not (k.startswith(PhKeys.SAMPLE) or k.startswith('process'))}
            PhUtil.print_iter(dic_to_process, header='Request to Process')
            data_type = DataTypeMaster()
            data_type.set_data_pool(data_pool=dic_to_process)
            data_type.parse_safe(PhErrorHandlingModes.CONTINUE_ON_ERROR)
            output_data = data_type.get_output_data()
            default_data.update({PhKeys.OUTPUT_DATA: output_data})
        if sample_data_dict:
            # PhUtil.print_iter(sample_data_dict, header='Request Output for sample_data_dict')
            if PhKeys.RAW_DATA in sample_data_dict:
                default_data.update({PhKeys.RAW_DATA: sample_data_dict.get(PhKeys.RAW_DATA)})
            if 'input_format' in sample_data_dict:
                default_data.update({'selected_input_format': sample_data_dict.get('input_format')})
            if 'output_format' in sample_data_dict:
                default_data.update({'selected_output_format': sample_data_dict.get('output_format')})
            if 'asn1_schema' in sample_data_dict:
                default_data.update({'selected_asn1_schema': sample_data_dict.get('asn1_schema')})
            if 'asn1_object' in sample_data_dict:
                default_data.update({'selected_asn1_object': sample_data_dict.get('asn1_object')})
            if 'asn1_object_alternate' in sample_data_dict:
                default_data.update({'asn1_object_alternate': sample_data_dict.get('asn1_object_alternate')})
            if 'tlv_parsing_of_output' in sample_data_dict:
                default_data.update({'tlv_parsing_of_output': sample_data_dict.get('tlv_parsing_of_output')})
            if PhKeys.FETCH_ASN1_OBJECTS_LIST in sample_data_dict:
                default_data.update(
                    {PhKeys.FETCH_ASN1_OBJECTS_LIST: sample_data_dict.get(PhKeys.FETCH_ASN1_OBJECTS_LIST)})
            if PhKeys.REMARKS_LIST in sample_data_dict:
                default_data.update({PhKeys.REMARKS_LIST: sample_data_dict.get(PhKeys.REMARKS_LIST)})
        else:
            # PhUtil.print_iter(requested_data_dict, header='Request Output for requested_data_dict')
            if PhKeys.RAW_DATA in requested_data_dict:
                default_data.update({PhKeys.RAW_DATA: requested_data_dict[PhKeys.RAW_DATA]})
            if 'input_format' in requested_data_dict:
                default_data.update({'selected_input_format': requested_data_dict['input_format']})
            if 'output_format' in requested_data_dict:
                default_data.update({'selected_output_format': requested_data_dict['output_format']})
            if 'asn1_schema' in requested_data_dict:
                default_data.update({'selected_asn1_schema': requested_data_dict['asn1_schema']})
            if 'asn1_object' in requested_data_dict:
                default_data.update({'selected_asn1_object': requested_data_dict['asn1_object']})
            if 'asn1_object_alternate' in requested_data_dict:
                default_data.update({'asn1_object_alternate': requested_data_dict['asn1_object_alternate']})
            if 'tlv_parsing_of_output' in requested_data_dict:
                default_data.update({'tlv_parsing_of_output': requested_data_dict['tlv_parsing_of_output']})
            if PhKeys.FETCH_ASN1_OBJECTS_LIST in requested_data_dict:
                default_data.update(
                    {PhKeys.FETCH_ASN1_OBJECTS_LIST: requested_data_dict[PhKeys.FETCH_ASN1_OBJECTS_LIST]})
            if PhKeys.REMARKS_LIST in requested_data_dict:
                default_data.update({PhKeys.REMARKS_LIST: requested_data_dict[PhKeys.REMARKS_LIST]})
        default_data.update({PhKeys.SAMPLE_PROCESSING: sample_processing})
        PhUtil.print_iter(default_data, header='Request Output')
        PhUtil.print_separator(main_text=f'{Const.TEMPLATE_ASN1_PLAY} Post Request Completed')
        return render_template(Const.TEMPLATE_ASN1_PLAY, **default_data)
    return render_template(Const.TEMPLATE_ASN1_PLAY, **default_data)
