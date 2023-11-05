from flask import render_template, request
from python_helpers.ph_keys import PhKeys
from python_helpers.ph_modes_error_handling import PhErrorHandlingModes
from python_helpers.ph_util import PhUtil
from qr_play.main.data_type.any_data import small_data, bulk_data_1, bulk_data_2
from qr_play.main.data_type.data_type_master import DataTypeMaster
from qr_play.main.helper.constants_config import ConfigConst
from qr_play.main.helper.defaults import Defaults
from qr_play.main.helper.formats import Formats


def get_sample_data(key):
    sample_data = {
        PhKeys.SAMPLE_1: {
            PhKeys.REMARKS_LIST: 'Simple Qr',
            PhKeys.RAW_DATA: small_data,
            PhKeys.SCALE: 8,
            PhKeys.SPLIT_QRS: False,
            PhKeys.QR_CODE_VERSION: 33
        },
        PhKeys.SAMPLE_2: {
            PhKeys.REMARKS_LIST: 'Bulk Data Single Qr',
            PhKeys.RAW_DATA: bulk_data_1,
            PhKeys.SCALE: Defaults.SCALE,
            PhKeys.SPLIT_QRS: False,
            PhKeys.QR_CODE_VERSION: Defaults.QR_CODE_VERSION
        },
        PhKeys.SAMPLE_3: {
            PhKeys.REMARKS_LIST: 'Bulk Data Split Qrs',
            PhKeys.RAW_DATA: bulk_data_2,
            PhKeys.SCALE: Defaults.SCALE,
            PhKeys.SPLIT_QRS: True,
            PhKeys.QR_CODE_VERSION: Defaults.QR_CODE_VERSION
        },
    }
    return sample_data.get(key, None)


def handle_requests():
    """

    :return:
    """

    page_url = 'qrPlay.html'
    default_data = {
        PhKeys.VERSION: f'v{ConfigConst.TOOL_VERSION}',
        PhKeys.QR_CODE_VERSIONS: list(range(40, 0, -1)),
        PhKeys.SELECTED_QR_CODE_VERSION: Defaults.QR_CODE_VERSION,
        PhKeys.SPLIT_QRS: Defaults.SPLIT_QRS,
        PhKeys.SCALE: Defaults.SCALE,
        PhKeys.SAMPLE_PROCESSING: PhKeys.SAMPLE_LOAD_ONLY,
        PhKeys.OUTPUT_DATA: '',
    }
    if request.method == PhKeys.GET:
        return render_template(page_url, **default_data)
    if request.method == PhKeys.POST:
        PhUtil.print_separator(main_text=f'{page_url} Post Request Started')
        PhUtil.print_iter(request.form, header='Request Input')
        # if not request.form[PhKeys.RAW_DATA]:
        #     flash('raw_data is required!')
        requested_data_dict = request.form.to_dict()
        sample_processing = requested_data_dict[PhKeys.SAMPLE_PROCESSING]
        # When submitting an HTML form,
        # 1) unchecked checkboxes do not send any data
        if PhKeys.SPLIT_QRS not in requested_data_dict:
            requested_data_dict.update({PhKeys.SPLIT_QRS: False})
        # 2) Integer is converted to String
        requested_data_dict.update({PhKeys.QR_CODE_VERSION: int(requested_data_dict.get(PhKeys.QR_CODE_VERSION))})
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
                              not k.startswith(PhKeys.SAMPLE)}
            dic_to_process.update({PhKeys.IMAGE_FORMAT: Formats.PNG_URI})
            dic_to_process.update({PhKeys.PRINT_INPUT: True})
            PhUtil.print_iter(dic_to_process, header='Request to Process')
            data_type = DataTypeMaster()
            data_type.set_data_pool(data_pool=dic_to_process)
            data_type.parse_safe(PhErrorHandlingModes.CONTINUE_ON_ERROR)
            temp_output_data = []
            output_data = data_type.get_output_data()
            if isinstance(output_data, list):
                temp_output_data = output_data
            else:
                temp_output_data.append(output_data)
            default_data.update({PhKeys.OUTPUT_DATA: temp_output_data})
        if sample_data_dict:
            # PhUtil.print_iter(sample_data_dict, header='Request Output for sample_data_dict')
            default_data.update({PhKeys.RAW_DATA: sample_data_dict.get(PhKeys.RAW_DATA)})
            if PhKeys.SPLIT_QRS in sample_data_dict:
                default_data.update({PhKeys.SPLIT_QRS: sample_data_dict.get(PhKeys.SPLIT_QRS)})
            if PhKeys.QR_CODE_VERSION in sample_data_dict:
                default_data.update({PhKeys.SELECTED_QR_CODE_VERSION: sample_data_dict.get(PhKeys.QR_CODE_VERSION)})
            if PhKeys.SCALE in sample_data_dict:
                default_data.update({PhKeys.SCALE: sample_data_dict.get(PhKeys.SCALE)})
            default_data.update({PhKeys.REMARKS_LIST: sample_data_dict.get(PhKeys.REMARKS_LIST)})
        else:
            # PhUtil.print_iter(requested_data_dict, header='Request Output for requested_data_dict')
            default_data.update({PhKeys.RAW_DATA: requested_data_dict[PhKeys.RAW_DATA]})
            default_data.update({PhKeys.SPLIT_QRS: requested_data_dict[PhKeys.SPLIT_QRS]})
            default_data.update({PhKeys.SELECTED_QR_CODE_VERSION: requested_data_dict[PhKeys.QR_CODE_VERSION]})
            default_data.update({PhKeys.SCALE: requested_data_dict[PhKeys.SCALE]})
            default_data.update({PhKeys.REMARKS_LIST: requested_data_dict[PhKeys.REMARKS_LIST]})
        default_data.update({PhKeys.SAMPLE_PROCESSING: sample_processing})
        PhUtil.print_iter(default_data, header='Request Output')
        PhUtil.print_separator(main_text=f'{page_url} Post Request Completed')
        return render_template(page_url, **default_data)
    return render_template(page_url, **default_data)