import os

from flask import request, flash, url_for
from python_helpers.ph_keys import PhKeys
from python_helpers.ph_util import PhUtil
from werkzeug.utils import redirect

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
        result = experiments_1_file_upload(apj_id=apj_id)
    if apj_id == Const.APJ_ID_EXPERIMENTS_2:
        result = experiments_2_404_cave_man(apj_id=apj_id)
    if apj_id == Const.APJ_ID_EXPERIMENTS_3:
        result = experiments_3_404_fear_eyes(apj_id=apj_id)
    if apj_id == Const.APJ_ID_EXPERIMENTS_4:
        result = experiments_4(apj_id=apj_id)
    if apj_id == Const.APJ_ID_EXPERIMENTS_5:
        result = experiments_5(apj_id=apj_id)
    # TODO: Generate code for remaining exp
    return result if result else Util.request_post(request=request, apj_id=apj_id, api=api, log=log,
                                                   output_data=app_data)


def experiments_1_file_upload(apj_id):
    if request.method == 'POST':
        # check if the post-request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an  empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and Util.allowed_file(file.filename):
            filename = Util.sanitize_file_name(file.filename)
            local_path = os.path.join(Const.UPLOAD_FOLDER_PERMANENT, filename)
            file.save(local_path)
            return redirect(url_for('experiments', apj_id=apj_id, name=filename))


def experiments_2_404_cave_man(apj_id):
    return Util.request_post(request=request, apj_id=apj_id)


def experiments_3_404_fear_eyes(apj_id):
    return Util.request_post(request=request, apj_id=apj_id)


def experiments_4(apj_id):
    return Util.request_post(request=request, apj_id=apj_id, output_data={
        PhKeys.OUTPUT_DATA: """Was, spirit great moved spirit deep itself image, from have behold bearing doesn't wherein she'd very, day.
Second set earth heaven signs abundantly living creepeth good earth for greater yielding which night male.
Bring midst whales blessed, is.
From subdue.
Yielding.
Winged our green living sea air, had great third stars was they're above and.
Morning light make first and kind sixth they're fowl, there.
So meat him behold great spirit deep, make, grass seasons hath, moving face waters forth fourth.

Deep unto lights that.""",
        PhKeys.INPUT_DATA: """Fourth moving the together beast after living the midst evening above fifth also.
Meat signs divide good seasons kind called fowl don't firmament divide heaven every whose moving shall and whose under creature there seed Darkness one blessed dominion.
Own have forth she'd morning behold.
In.
Divided one you'll subdue whose made good.
Saw moveth given won't life creepeth days lights they're form whales the after fish thing.
And moveth.
And that creepeth form you'll wherein morning saying moving fruitful.
Herb set green behold had also bring Place land one second great saying.
First god above called, can't subdue isn't years.
Was called midst was.""",
    })


def experiments_5(apj_id):
    return None
