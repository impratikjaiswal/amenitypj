import uuid

from flask import jsonify, render_template
from python_helpers.ph_constants import PhConstants
from python_helpers.ph_keys import PhKeys
from python_helpers.ph_util import PhUtil

from amenity_pj.helper.constants import Const
from amenity_pj.helper.defaults import Defaults


class Util:

    @classmethod
    def get_common_data(cls, end_point, specific_key=None, fail_safe=False):
        data = Const.COMMON_DATA_MAPPING.get(end_point, None)
        if fail_safe:
            data = PhUtil.set_if_not_none(current_value=data, new_value=PhConstants.DICT_EMPTY)
        if specific_key is None:
            return data
        specific_value = data.get(specific_key, None)
        if fail_safe:
            specific_value = PhUtil.set_if_not_none(current_value=specific_value, new_value=PhConstants.STR_EMPTY)
        return specific_value

    @classmethod
    def get_github_url(cls, github_repo=None, github_pages=True):
        default_url = Const.GITHUB_PAGES if github_pages else Const.GITHUB_REPO
        return '/'.join(filter(None, [default_url, github_repo]))

    @classmethod
    def get_request_info(cls, request, template_id, api):
        return f'{template_id}; {request.method}; {"API" if api else "Form"} Request'

    @classmethod
    def request_pre(cls, request, end_point, api=Defaults.API, log=Defaults.LOG):
        template_id = cls.get_common_data(end_point=end_point, specific_key=PhKeys.APP_TEMPLATE)
        PhUtil.print_separator(
            main_text=f'{cls.get_request_info(request=request, template_id=template_id, api=api)} Received!!!', log=log)
        requested_data_dict = request.get_json() if request.is_json else request.form.to_dict()
        PhUtil.print_iter(requested_data_dict, header='Inputs', log=log)
        return requested_data_dict

    @classmethod
    def request_post(cls, request, end_point, api=Defaults.API, log=Defaults.LOG, output_data=PhConstants.DICT_EMPTY):
        template_id = cls.get_common_data(end_point=end_point, specific_key=PhKeys.APP_TEMPLATE)
        PhUtil.print_iter(output_data, header='Outputs', log=log)
        PhUtil.print_separator(
            main_text=f'{cls.get_request_info(request=request, template_id=template_id, api=api)} Completed!!!',
            log=log)
        return jsonify(**output_data) if api else render_template(template_id, **output_data)

    @classmethod
    # TODO: Custom Decorator
    # TODO: @requires_auth
    def user_visit(cls, request, log):
        """
        TODO: Handle this with Custom Decorator
        :param request:
        :param url:
        :return:

        TODO: To Validate:
        Ref: https://stackoverflow.com/questions/15974730/how-do-i-get-the-different-parts-of-a-flask-requests-url/15975041#15975041

        ============ Sample 1
        App:    http://www.example.com/myapplication
        User:   http://www.example.com/myapplication/foo/page.html?x=y

        path             /foo/page.html
        full_path        /foo/page.html?x=y
        script_root      /myapplication
        base_url         http://www.example.com/myapplication/foo/page.html
        url              http://www.example.com/myapplication/foo/page.html?x=y
        url_root         http://www.example.com/myapplication/
        ============ Sample 2
        curl -XGET http://127.0.0.1:5000/alert/dingding/test?x=y

        request.method:              GET
        request.url:                 http://127.0.0.1:5000/alert/dingding/test?x=y
        request.base_url:            http://127.0.0.1:5000/alert/dingding/test
        request.url_charset:         utf-8
        request.url_root:            http://127.0.0.1:5000/
        str(request.url_rule):       /alert/dingding/test
        request.host_url:            http://127.0.0.1:5000/
        request.host:                127.0.0.1:5000
        request.script_root:
        request.path:                /alert/dingding/test
        request.full_path:           /alert/dingding/test?x=y
        request.environ['RAW_URI']   /alert/dingding/test?x=y (full_path may return extra question mark:  alert/dingding/test?)

        request.args:                ImmutableMultiDict([('x', 'y')])
        request.args.get('x'):       y
        request.remote_addr         127.0.0.1
        request.query_string
        request.access_route[0]
        ---
        # As for nginx, it sends the real IP address under HTTP_X_FORWARDED_FOR so make sure you don't end up with localhost for each request
        ---
        The below code works if in e.g. nginx you set: proxy_set_header X-Real-IP $remote_addr
        request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
        -----
        request.environ['REMOTE_ADDR']
        -----
        Needs config ? https://calvin.me/forward-ip-addresses-when-using-nginx-proxy/
        if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
            print(request.environ['REMOTE_ADDR'])
        else:
            print(request.environ['HTTP_X_FORWARDED_FOR']) # if behind a proxy
        -----
        so we fetch the uploaded files with request.files and text with request.form
        file_name = request.files['file'].filename
        ref_id = request.form['referenceId']
        """
        PhUtil.print_separator(main_text=f'user_visit Received!!!', log=log)
        try:
            request_id = str(uuid.uuid4())
            # TODO: Error
            # dir(request)
            # request.__dict__
            # PhUtil.print_iter(header='request', the_iter=request.copy(), depth_level=1)
            # PhUtil.print_iter(header='request', the_iter=request, depth_level=1)
            #    PhUtil.print_iter(header='request.headers', the_iter=request.headers, log=log)
            log.info('request dict')
            log.info(request.__dict__)
            log.info(PhConstants.STR_EMPTY)
            log.info('request.headers dict')
            log.info(request.headers.__dict__)
            log.info(PhConstants.STR_EMPTY)
            log.info('request.environ dict')
            log.info(request.environ)
            log.info(PhConstants.STR_EMPTY)
            log.info('Other Param')
            # session["ctx"] = {"request_id": request_id}
            log.info(f'User Visit: {request_id}')
            log.info(f'request.url_root: {request.url_root}')
            log.info(f'request.path: {request.path}')  # "/antitop/pj"
            log.info(f'request.url_rule: {request.url_rule}')  # "/antitop/<username>"
            log.info(f'request.url_rule_rule: {request.url_rule.rule}')
            log.info(f'request.endpoint: {request.endpoint}')
            if 'Host' in request.headers:
                log.info(f'request.headers["Host"]: {request.headers["Host"]}')
            log.info(PhConstants.STR_EMPTY)
        except Exception as e:
            log.info(f'user_visit: {e}')
            log.info(PhConstants.STR_EMPTY)

    @classmethod
    def is_selected(cls, item, selected_item):
        return 'SELECTED' if item == selected_item else ''
