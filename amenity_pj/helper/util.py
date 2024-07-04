from flask import jsonify, render_template
from python_helpers.ph_util import PhUtil

from amenity_pj.helper.constants import Const


class Util:

    @classmethod
    def get_github_url(cls, github_repo=None, github_pages=True):
        default_url = Const.GITHUB_PAGES if github_pages else Const.GITHUB_REPO
        return '/'.join(filter(None, [default_url, github_repo]))

    @classmethod
    def get_request_info(cls, request, template_id, api):
        return f'{template_id}; {request.method}; {"API" if api else "Form"} Request'

    @classmethod
    def request_pre(cls, request, template_id, api, log):
        PhUtil.print_separator(
            main_text=f'{cls.get_request_info(request=request, template_id=template_id, api=api)} Received!!!', log=log)
        requested_data_dict = request.get_json() if request.is_json else request.form.to_dict()
        PhUtil.print_iter(requested_data_dict, header='Inputs', log=log)
        return requested_data_dict

    @classmethod
    def request_post(cls, default_data, request, template_id, api, log):
        PhUtil.print_iter(default_data, header='Outputs', log=log)
        PhUtil.print_separator(
            main_text=f'{cls.get_request_info(request=request, template_id=template_id, api=api)} Completed!!!',
            log=log)
        return jsonify(**default_data) if api else render_template(template_id, **default_data)
