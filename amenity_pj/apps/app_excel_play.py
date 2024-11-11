# from excel_play.main.data_type.data_type_master import DataTypeMaster
# from python_helpers.ph_modes_error_handling import PhErrorHandlingModes
# from excel_play.main.helper.defaults import Defaults
import os

from excel_play.main.data_type.data_type_master import DataTypeMaster
from excel_play.main.helper.defaults import Defaults
from flask import request, redirect, flash, send_file, jsonify
from python_helpers.ph_constants import PhConstants
from python_helpers.ph_keys import PhKeys
from python_helpers.ph_modes_error_handling import PhErrorHandlingModes
from python_helpers.ph_util import PhUtil

from amenity_pj.helper.constants import Const
from amenity_pj.helper.util import Util

info = None


def handle_requests(apj_id, api, log, root_path, default_data, **kwargs):
    """

    :return:
    """

    global info
    info = None

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

    samples_dict = PhConstants.DICT_EMPTY
    samples_list = PhUtil.generalise_list(list(samples_dict.keys()), sort=False)
    encoding_pool = PhUtil.generalise_list(PhConstants.CHAR_ENCODING_POOL)
    encoding_errors_pool = PhUtil.generalise_list(PhConstants.CHAR_ENCODING_ERRORS_POOL)
    default_data_app = {
        PhKeys.SAMPLES: samples_list,
        PhKeys.SAMPLE_SELECTED: samples_list[1] if len(samples_list) > 1 else None,
        PhKeys.ENCODING_POOL: encoding_pool,
        PhKeys.ENCODING_ERRORS_POOL: encoding_errors_pool,
        PhKeys.ENCODING_SELECTED: Defaults.ENCODING,
        PhKeys.ENCODING_ERRORS_SELECTED: Defaults.ENCODING_ERRORS
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
            # Check if the post-request has the file part
            if 'file' not in request.files:
                flash('File Object is not received !!!', PhKeys.ALERT_CSS_CLASS_DANGER)
                return redirect(request.url)
            # Get List of FileStorage Objects (Multiple)
            files = request.files.getlist('file')
            # ImmutableMultiDict([('file', <FileStorage: 'Finance.csv' ('text/csv')>), ('file', <FileStorage:
            # 'House.csv' ('text/csv')>), ('file', <FileStorage: 'OrderData.csv' ('text/csv')>)])
            valid_files_count = 0
            files_list_input = []
            transaction_id = PhUtil.generate_transaction_id()
            target_directory_path = os.sep.join([root_path, Const.UPLOAD_FOLDER_TEMPORARY, transaction_id])
            PhUtil.print(f'target_directory_path is {target_directory_path}', log=log)
            PhUtil.make_dirs(target_directory_path)
            for file in files:
                if not file.filename:
                    # If the user does not select a file, the browser submits an empty file without a filename.
                    continue
                if Util.allowed_file(file.filename, ext_list=Const.UPLOAD_FILE_EXTENSIONS_ALLOWED_EXCEL_PLAY):
                    valid_files_count += 1
                    input_file_name = Util.sanitize_file_name(file.filename)
                    input_file_path = os.sep.join([target_directory_path, input_file_name])
                    file.save(input_file_path)
                    files_list_input.append(input_file_path)
            if valid_files_count == 0:
                flash('No uploaded files', PhKeys.ALERT_CSS_CLASS_DANGER)
                return redirect(request.url)
            elif valid_files_count == 1:
                msg = f'{file.filename} uploaded successfully. {Const.DOWNLOAD_MSG}'
            else:
                msg = f'{valid_files_count} files uploaded successfully. {Const.DOWNLOAD_MSG}'
            info = msg
            # flash(f'{msg}')
            PhUtil.print_iter(files_list_input, header='files_list_input', log=log)
            dic_to_process.update({PhKeys.INPUT_DATA: files_list_input})
            PhUtil.print_iter(dic_to_process, header='dic_to_process', log=log)
            data_type = DataTypeMaster()
            data_type.set_data_pool(data_pool=dic_to_process)
            data_type.process_safe(PhErrorHandlingModes.CONTINUE_ON_ERROR)
            output_data, info_data = data_type.get_output_data(only_output=False)
            app_data.update({PhKeys.OUTPUT_DATA: output_data})
            app_data.update({PhKeys.INFO_DATA: info_data})
            app_data.update({PhKeys.TRANSACTION_ID: Util.fetch_transaction_id_from_info_data(info_data)})
            files_list_output = output_data
            PhUtil.print_iter(files_list_output, header='files_list_output', log=log)
            if files_list_output and len(files_list_output) > 1:
                single_zip_file = PhUtil.zip_and_clean_dir(source_files_dir=target_directory_path,
                                                           include_files=['*.zip'])
            else:
                single_zip_file = files_list_output[0]
            PhUtil.print(f'single_zip_file is {single_zip_file}', log=log)
            return send_file(path_or_file=single_zip_file, as_attachment=True
                             # , download_name=PhUtil.get_file_name_and_extn(file_path=file)
                             )
            # return send_from_directory(local_folder_path, 'Sheet1.csv')
        # Conditional Updates
        update_app_data(PhKeys.INPUT_DATA)
        # Fixed Updates
        app_data.update({PhKeys.SAMPLE_OPTION: sample_option})
    return Util.request_post(request=request, apj_id=apj_id, api=api, log=log, output_data=app_data)


def handle_info(**kwargs):
    """

    :return:
    """
    # time.sleep(0.005)
    global info
    return jsonify(html_string_selected=(info if info else Const.DOWNLOAD_MSG_DEFAULT))
