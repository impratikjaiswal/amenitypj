from flask import render_template, request
from python_helpers.ph_modes_error_handling import PhErrorHandlingModes
from python_helpers.ph_util import PhUtil
from tlv_play.main.data_type.data_type_master import DataTypeMaster
from tlv_play.main.helper.defaults import Defaults

from amenity_pj_app.helper.constants import Const


def get_sample_data(key):
    sample_data = {
        'sample_1': {
            'remarks_list': 'Simple TLV',
            'raw_data': '86020102',
        },
        'sample_2': {
            'remarks_list': 'Parallel Simple TLVs',
            'raw_data': '81020105820106830209AB',
        },
        'sample_3': {
            'remarks_list': 'Multi Byte Tag; EID',
            'raw_data': 'BF3E125A1089049032123451234512345678901235',
        },
        'sample_4': {
            'remarks_list': 'Nested BER TLV; Ascii Values',
            'raw_data': '064B21220D2048656C6C6F2C204275792031204742204461746120666F7220302E3520555344210F0D0D41726520596F7520537572653F151431107777772E66616365626F6F6B2E636F6D0500',
            'value_in_ascii': True,
        },
        'sample_5': {
            'remarks_list': 'Nested BER TLV; Length In Decimal',
            'raw_data': '064B21220D2048656C6C6F2C204275792031204742204461746120666F7220302E3520555344210F0D0D41726520596F7520537572653F151431107777772E66616365626F6F6B2E636F6D0500',
            'length_in_decimal': True,
        },
        'sample_6': {
            'remarks_list': 'Complex Nested Ber TLVs; ESIM Profile',
            'raw_data': 'A042800102810101821447534D412050726F66696C65205061636B616765830A8929901012345678905FA506810084008B00A610060667810F010201060667810F010204B08201F8A0058000810101810667810F010201A207A105C60301020AA305A1038B010FA40C830A989209012143658709F5A527A109820442210026800198831A61184F10A0000000871002FF33FF01890000010050045553494DA682019EA10A8204422100258002022B831B8001019000800102A406830101950108800158A40683010A95010882010A8316800101A40683010195010880015AA40683010A95010882010F830B80015BA40683010A95010882011A830A800101900080015A970082011B8316800103A406830101950108800158A40683010A95010882010F8316800111A40683010195010880014AA40683010A95010882010F8321800103A406830101950108800158A40683010A950108840132A4068301019501088201048321800101A406830101950108800102A406830181950108800158A40683010A950108820104831B800101900080011AA406830101950108800140A40683010A95010882010A8310800101900080015AA40683010A95010882011583158001019000800118A40683010A95010880014297008201108310800101A40683010195010880015A97008201158316800113A406830101950108800148A40683010A95010882010F830B80015EA40683010A95010882011A83258001019000800102A010A406830101950108A406830102950108800158A40683010A950108A33FA0058000810102A13630118001018108303030303030303082020099300D800102810831323334353637383012800200818108393239343536373882020088A244A0058000810103A13BA0393013800101810831323334FFFFFFFF8201018301063010800102810830303030FFFFFFFF820102301080010A810835363738FFFFFFFF830101B381C3A0058000810104810667810F010204A21DA11B83027FF18410A0000000871002FF33FF018900000100C60301810AA30B8309082999181132547698A406A104C7022F06A80F830D0A2E148CE73204000000000000AB45A10D82044221003483026F428001688334534D53433120FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF1FFFFFFFFFFFFFFFFFFFFFFFF07916427417900F4FFFFFFFFFFFFFFAD1383110247534D41206555494343FFFFFFFFFFFFAE03830100B20483020040B606830419F1FF01A225A0058000810105A11CA01A301880020081810839323338FFFFFFFF82020081830101840122A43AA0058000810106A131A12F8001018101018210000102030405060708090A0B0C0D0E0F83100102030405060708090A0B0C0D0E0F008603010203A681BBA0058000810107A1444F07A00000015153504F08A0000001515350414F08A000000151000000820382DC0083010FC90A810280008201F08701F0EA11800F0100000100000002011203B2010000A26C302295013882010183010130173015800180861066778899AABBCCDD1122334455EEFF103022950134820102830101301730158001808610112233445566778899AABBCCDDEEFF1030229501C882010383010130173015800180861099AABBCCDDEEFF101122334455667788A681C0A0058000810108A1494F07A00000015153504F08A0000001515350414F10A00000055910100102736456616C7565820380800083010FC907810280008201F0EA11800F01000001000000020112036C756500A26C30229501388201018301013017301580018086101122334455667788112233445566778830229501348201028301013017301580018086101122334455667788112233445566778830229501C882010383010130173015800180861011223344556677881122334455667788A720A00381010B4F09A00000055910100001A0050403B00000810112040100040100A740A00381010C4F09A00000055910100002A0050403B00020810112040100040100301E8010A0000000871002FF33FF018900000100810402000100820402000100AA07A0058000810163',
            'value_in_ascii': True,
            'length_in_decimal': True,
            'one_liner': True,
        },
    }
    return sample_data.get(key, None)


def handle_requests():
    """

    :return:
    """

    default_data = {
        'app_title': Const.TITLE_TLV_PLAY,
        'app_description': Const.DESCRIPTION_TLV_PLAY,
        'app_version': Const.VERSION_TLV_PLAY,
        'app_github_url': Const.GITHUB_URL_TLV_PLAY,
        'sample_processing': 'load_only',
        'length_in_decimal': Defaults.LENGTH_IN_DECIMAL,
        'value_in_ascii': Defaults.VALUE_IN_ASCII,
        'one_liner': Defaults.ONE_LINER,
        'output_data': '',
    }
    if request.method == 'GET':
        return render_template(Const.TEMPLATE_TLV_PLAY, **default_data)
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
            if 'length_in_decimal' in sample_data_dict:
                default_data.update({'length_in_decimal': sample_data_dict.get('length_in_decimal')})
            if 'value_in_ascii' in sample_data_dict:
                default_data.update({'value_in_ascii': sample_data_dict.get('value_in_ascii')})
            if 'one_liner' in sample_data_dict:
                default_data.update({'one_liner': sample_data_dict.get('one_liner')})
            default_data.update({'remarks_list': sample_data_dict.get('remarks_list')})
        else:
            default_data.update({'raw_data': request.form['raw_data']})
            default_data.update({'length_in_decimal': True if 'length_in_decimal' in request.form.keys() else False})
            default_data.update({'value_in_ascii': True if 'value_in_ascii' in request.form.keys() else False})
            default_data.update({'one_liner': True if 'one_liner' in request.form.keys() else False})
            default_data.update({'remarks_list': request.form['remarks_list']})
        default_data.update({'sample_processing': sample_processing})
        return render_template(Const.TEMPLATE_TLV_PLAY, **default_data)
    return render_template(Const.TEMPLATE_TLV_PLAY, **default_data)
