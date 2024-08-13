import os

from flask import request, flash, url_for
from python_helpers.ph_keys import PhKeys
from python_helpers.ph_util import PhUtil
from werkzeug.utils import secure_filename, redirect

from amenity_pj.helper.constants import Const
from amenity_pj.helper.util import Util


def handle_requests(apj_id, api, log, default_data, **kwargs):
    """

    :param apj_id:
    :param api:
    :param log:
    :param default_data:
    :param kwargs:
    :return:
    """
    #
    default_data_app = {
    }
    app_data = PhUtil.dict_merge(default_data, default_data_app)
    requested_data_dict = Util.request_pre(request=request, apj_id=apj_id, api=api, log=log)
    if request.method == PhKeys.GET:
        pass
    if request.method == PhKeys.POST:
        pass
    result = None
    if apj_id == Const.APJ_ID_EXPERIMENTS_1:
        result = experiments_1(apj_id=apj_id)
    if apj_id == Const.APJ_ID_EXPERIMENTS_2:
        result = experiments_2(apj_id=apj_id)
    if apj_id == Const.APJ_ID_EXPERIMENTS_3:
        result = experiments_3(apj_id=apj_id)
    if apj_id == Const.APJ_ID_EXPERIMENTS_4:
        result = experiments_4(apj_id=apj_id)
    if apj_id == Const.APJ_ID_EXPERIMENTS_5:
        result = experiments_5(apj_id=apj_id)
    return result if result else Util.request_post(request=request, apj_id=apj_id, api=api, log=log,
                                                   output_data=app_data)


def experiments_1(apj_id):
    if request.method == 'POST':
        # check if the post-request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = sanitize_file_name(file.filename)
            local_path = os.path.join(Const.UPLOAD_FOLDER_PERMANENT, filename)
            file.save(local_path)
            return redirect(url_for('experiments', apj_id=apj_id, name=filename))
    return '''
        <!doctype html>
        <title>Upload new File</title>
        <h1>Upload new File</h1>
        <form method=post enctype=multipart/form-data>
          <input type=file name=file>
          <input type=submit value=Upload>
        </form>
        '''


def experiments_2(apj_id):
    return None


def experiments_3(apj_id):
    return None


def experiments_4(apj_id):
    return Util.request_post(request=request, apj_id=apj_id)


def experiments_5(apj_id):
    return Util.request_post(request=request, apj_id=apj_id)


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in Const.UPLOAD_FILE_EXTENSIONS_ALLOWED


def sanitize_file_name(file_name):
    return secure_filename(file_name)
