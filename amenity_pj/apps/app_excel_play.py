# from excel_play.main.data_type.data_type_master import DataTypeMaster
# from python_helpers.ph_modes_error_handling import PhErrorHandlingModes
# from excel_play.main.helper.defaults import Defaults
import os

from excel_play.main.excelPlay import process_input
from excel_play.main.helper.formats import Formats
from flask import request, redirect, flash, send_file
from python_helpers.ph_constants import PhConstants
from python_helpers.ph_keys import PhKeys
from python_helpers.ph_util import PhUtil

from amenity_pj.helper.constants import Const
from amenity_pj.helper.util import Util


def handle_requests(apj_id, api, log, root_path, default_data, **kwargs):
    """

    :return:
    """

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
    default_data_app = {
        PhKeys.SAMPLES: samples_list,
        PhKeys.SAMPLE_SELECTED: samples_list[1] if len(samples_list) > 1 else None,
    }
    app_data = PhUtil.dict_merge(default_data, default_data_app)
    requested_data_dict = Util.request_pre(request=request, apj_id=apj_id, api=api, log=log)
    if request.method == PhKeys.GET:
        pass
    if request.method == PhKeys.POST:
        process_sample = True if PhKeys.PROCESS_SAMPLE in requested_data_dict else None
        sample_option = requested_data_dict.get(PhKeys.SAMPLE_OPTION, None)
        sample_name = requested_data_dict.get(PhKeys.SAMPLE, None)
        sample_dict = None
        # When submitting an HTML form,
        # 1) unchecked checkboxes do not send any data, however checked checkboxes do send False (may send True as well)
        pass
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
            # Check if the post-request has the file part
            if 'file' not in request.files:
                flash('File Object is not received !!!', PhKeys.ALERT_CSS_CLASS_DANGER)
                return redirect(request.url)
            # Get List of FileStorage Objects (Multiple)
            files = request.files.getlist('file')
            # ImmutableMultiDict([('file', <FileStorage: 'Finance.csv' ('text/csv')>), ('file', <FileStorage:
            # 'House.csv' ('text/csv')>), ('file', <FileStorage: 'OrderData.csv' ('text/csv')>)])
            valid_files_count = 0
            files_list = []
            transaction_id = PhUtil.generate_transaction_id()
            target_directory_path = os.sep.join([root_path, Const.UPLOAD_FOLDER_TEMPORARY, transaction_id])
            PhUtil.print_(f'target_directory_path is {target_directory_path}', log=log)
            PhUtil.makedirs(target_directory_path)
            for file in files:
                if not file.filename:
                    # If the user does not select a file, the browser submits an empty file without a filename.
                    continue
                if Util.allowed_file(file.filename, ext_list=Const.UPLOAD_FILE_EXTENSIONS_ALLOWED_EXCEL_PLAY):
                    valid_files_count += 1
                    input_file_name = Util.sanitize_file_name(file.filename)
                    input_file_path = os.sep.join([target_directory_path, input_file_name])
                    file.save(input_file_path)
                    files_list.append(input_file_path)
                    flash(f'{file.filename} uploaded')
            if valid_files_count == 0:
                flash('No uploaded files', PhKeys.ALERT_CSS_CLASS_DANGER)
                return redirect(request.url)
            PhUtil.print_iter(files_list, header='files_list', log=log)
            output_files_paths = []
            for file in files_list:
                output_file_path = process_input(input_file_or_folder=file, output_archive_format=Formats.ZIP)
                PhUtil.print_(f'output_file_path is {output_file_path}', log=log)
                output_files_paths.append(output_file_path)
                break
            if output_files_paths:
                for file_set in output_files_paths:
                    for file in file_set:
                        return send_file(path_or_file=file, as_attachment=True
                                         # , download_name=PhUtil.get_file_name_and_extn(file_path=file)
                                         )
            # return send_from_directory(local_folder_path, 'Sheet1.csv')
        # Conditional Updates
        update_app_data(PhKeys.INPUT_DATA)
        # Fixed Updates
        app_data.update({PhKeys.SAMPLE_OPTION: sample_option})
    return Util.request_post(request=request, apj_id=apj_id, api=api, log=log, output_data=app_data)
