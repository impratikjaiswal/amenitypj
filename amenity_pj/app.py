import os
import sqlite3
import uuid
from logging.config import dictConfig

from flask import Flask, render_template, request, url_for, flash, redirect
from flask_sitemapper import Sitemapper
from python_helpers.ph_keys import PhKeys
from python_helpers.ph_util import PhUtil
from werkzeug.exceptions import abort

from amenity_pj._git_info import GIT_SUMMARY
from amenity_pj.apps import app_qr_play, app_tlv_play, app_asn1_play, app_cert_play, app_excel_play
from amenity_pj.helper.constants import Const
from amenity_pj.helper.util import Util

app = Flask(__name__)

sitemapper = Sitemapper()
sitemapper.init_app(app)

app.config['SECRET_KEY'] = 'Pj Test'

dictConfig(
    {
        "version": 1,
        "formatters": {
            "default": {
                "format": "[%(asctime)s] [%(levelname)s | %(module)s] %(message)s",
                "datefmt": "%B %d, %Y %H:%M:%S %Z",
            }
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "stream": "ext://sys.stdout",
                "formatter": "default",
            },
            "file": {
                "class": "logging.FileHandler",
                "filename": "amenitypj.log",
                "formatter": "default",
            },
            "size-rotate": {
                "class": "logging.handlers.RotatingFileHandler",
                "filename": "amenitypj.log",
                "maxBytes": 1000000,
                "backupCount": 5,
                "formatter": "default",
            },
            "time-rotate": {
                "class": "logging.handlers.TimedRotatingFileHandler",
                "filename": "amenitypj.log",
                "when": "D",
                "interval": 10,
                "backupCount": 5,
                "formatter": "default",
            },
        },
        # "root": {"level": "INFO", "handlers": ["console"]},
        # "root": {"level": "INFO", "handlers": ["console", "file"]},
        "root": {"level": "INFO", "handlers": ["size-rotate"]},
        # "root": {"level": "INFO", "handlers": ["time-rotate"]},
    }
)


def get_db_connection():
    # conn = sqlite3.connect(r'database.db')
    path = os.sep.join([os.path.dirname(os.path.realpath(__file__)), 'db', 'database.db'])
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    return conn


def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?',
                        (post_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post


def is_selected(item, selected_item):
    return 'SELECTED' if item == selected_item else ''


# @sitemap.register_generator
# def index():
# This function is Not needed if you set SITEMAP_INCLUDE_RULES_WITHOUT_PARAMS=True
# https://www.sitemaps.org/protocol.html
# yield Const.END_POINT_INDEX, {}
# yield Const.END_POINT_INDEX, {}, Const.DEPLOYMENT_DATE, 'monthly'


@app.context_processor
def utility_processor_title_for():
    def title_for(end_point=None):
        return Const.END_POINT_AND_TITLE_MAPPING.get(end_point, Const.TITLE_AMENITY_PJ)

    return dict(title_for=title_for)


@app.context_processor
def utility_processor_selected_input_format():
    def is_selected_input_format(input_format, selected_input_format):
        return is_selected(input_format, selected_input_format)

    return dict(is_selected_input_format=is_selected_input_format)


@app.context_processor
def utility_processor_selected_output_format():
    def is_selected_output_format(output_format, selected_output_format):
        return is_selected(output_format, selected_output_format)

    return dict(is_selected_output_format=is_selected_output_format)


@app.context_processor
def utility_processor_selected_asn1_schema():
    def is_selected_asn1_schema(asn1_schema, selected_asn1_schema):
        return is_selected(asn1_schema, selected_asn1_schema)

    return dict(is_selected_asn1_schema=is_selected_asn1_schema)


@app.context_processor
def utility_processor_selected_sample():
    def is_selected_sample(sample, selected_sample):
        return is_selected(sample, selected_sample)

    return dict(is_selected_sample=is_selected_sample)


@app.context_processor
def utility_processor_selected_qr_code_version():
    def is_selected_qr_code_version(sample, selected_qr_code_version):
        return is_selected(sample, selected_qr_code_version)

    return dict(is_selected_qr_code_version=is_selected_qr_code_version)


@app.context_processor
def utility_processor_selected_url_time_out():
    def is_selected_url_time_out(sample, selected_url_time_out):
        return is_selected(sample, selected_url_time_out)

    return dict(is_selected_url_time_out=is_selected_url_time_out)


@app.context_processor
def utility_processor_selected_image_format():
    def is_selected_image_format(sample, selected_image_format):
        return is_selected(sample, selected_image_format)

    return dict(is_selected_image_format=is_selected_image_format)


@app.route(Const.URL_SITEMAP)
def sitemap():
    user_visit()
    return sitemapper.generate()


# Custom Decorator
# @requires_auth
def user_visit(url=None):
    """
    TODO: Handle this with Custom Decorator
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
    PhUtil.print_separator(main_text=f'user_visit Received!!!', log=app.logger)
    try:
        request_id = str(uuid.uuid4())
        # TODO: Error
        # dir(request)
        # request.__dict__
        # PhUtil.print_iter(header='request', the_iter=request)
        # TODO: Error
        # PhUtil.print_iter(header='request', the_iter=request, depth_level=1)
        #    PhUtil.print_iter(header='request.headers', the_iter=request.headers, log=app.logger)
        app.logger.info('request dict')
        app.logger.info(request.__dict__)
        app.logger.info('request.headers dict')
        app.logger.info(request.headers.__dict__)
        app.logger.info('request.environ dict')
        app.logger.info(request.environ)
        app.logger.info('Other Param')
        # session["ctx"] = {"request_id": request_id}
        app.logger.info(f'User Visit: {request_id}')
        app.logger.info(f'request.url_root: {request.url_root}')
        app.logger.info(f'request.path: {request.path}')  # "/antitop/pj"
        app.logger.info(f'request.url_rule: {request.url_rule}')  # "/antitop/<username>"
        app.logger.info(f'request.url_rule_rule: {request.url_rule.rule}')
        app.logger.info(f'request.endpoint: {request.endpoint}')
        if 'Host' in request.headers:
            app.logger.info(f'request.headers["Host"]: {request.headers["Host"]}')
    except:
        # Nothing to Do
        pass


@sitemapper.include(lastmod=Const.DEPLOYMENT_DATE)
@app.route(Const.URL_AMENITY_PJ)
def index():
    user_visit()
    default_data = {
        PhKeys.APP_TITLE: Const.TITLE_AMENITY_PJ,
        PhKeys.APP_DESCRIPTION: Const.DESCRIPTION_AMENITY_PJ,
        PhKeys.APP_VERSION: Const.VERSION_AMENITY_PJ,
        PhKeys.APP_GITHUB_URL: Util.get_github_url(github_repo=Const.GITHUB_REPO_AMENITY_PJ, github_pages=False),
        PhKeys.APP_GITHUB_PAGES_URL: Util.get_github_url(github_repo=Const.GITHUB_REPO_AMENITY_PJ, github_pages=True),
        PhKeys.APP_GIT_SUMMARY: GIT_SUMMARY,
    }
    PhUtil.print_iter(the_iter=default_data, header='default_data', log=app.logger)
    return render_template(Const.TEMPLATE_AMENITY_PJ, **default_data)


@app.route(Const.URL_ASN1_PLAY_ASN1_OBJECTS)
def asn1_play_asn1_objects():
    # user_visit()
    return app_asn1_play.handle_asn1_objects()


@sitemapper.include(lastmod=Const.DEPLOYMENT_DATE)
@app.route(Const.URL_API_ASN1_PLAY, methods=('GET', 'POST'), defaults={'_api': True})
@app.route(Const.URL_ASN1_PLAY, methods=('GET', 'POST'), defaults={'_api': False})
def asn1_play(_api):
    user_visit()
    return app_asn1_play.handle_requests(api=_api, log=app.logger)


@sitemapper.include(lastmod=Const.DEPLOYMENT_DATE_CERT_PLAY)
@app.route(Const.URL_API_CERT_PLAY, methods=('GET', 'POST'), defaults={'_api': True})
@app.route(Const.URL_CERT_PLAY, methods=('GET', 'POST'), defaults={'_api': False})
def cert_play(_api):
    user_visit()
    return app_cert_play.handle_requests(api=_api, log=app.logger)


@sitemapper.include(lastmod=Const.DEPLOYMENT_DATE)
@app.route(Const.URL_API_TLV_PLAY, methods=('GET', 'POST'), defaults={'_api': True})
@app.route(Const.URL_TLV_PLAY, methods=('GET', 'POST'), defaults={'_api': False})
def tlv_play(_api):
    user_visit()
    return app_tlv_play.handle_requests(api=_api, log=app.logger)


@sitemapper.include(lastmod=Const.DEPLOYMENT_DATE)
@app.route(Const.URL_API_QR_PLAY, methods=('GET', 'POST'), defaults={'_api': True})
@app.route(Const.URL_QR_PLAY, methods=('GET', 'POST'), defaults={'_api': False})
def qr_play(_api):
    user_visit()
    return app_qr_play.handle_requests(api=_api, log=app.logger)


@sitemapper.include(lastmod=Const.DEPLOYMENT_DATE)
@app.route(Const.URL_API_EXCEL_PLAY, methods=('GET', 'POST'), defaults={'_api': True})
@app.route(Const.URL_EXCEL_PLAY, methods=('GET', 'POST'), defaults={'_api': False})
def excel_play(_api):
    user_visit()
    return app_excel_play.handle_requests(api=_api, log=app.logger)


@sitemapper.include(lastmod=Const.DEPLOYMENT_DATE)
@app.route(Const.URL_SPONSORSHIP, methods=('GET', 'POST'))
def sponsorship():
    user_visit()
    default_data = {
        PhKeys.APP_TITLE: Const.TITLE_SPONSORSHIP,
        PhKeys.APP_DESCRIPTION: Const.DESCRIPTION_SPONSORSHIP,
        PhKeys.APP_VERSION: Const.VERSION_SPONSORSHIP,
        PhKeys.APP_GITHUB_URL: Util.get_github_url(github_repo=Const.GITHUB_REPO_SPONSORSHIP, github_pages=False),
        PhKeys.APP_GITHUB_PAGES_URL: Util.get_github_url(github_repo=Const.GITHUB_REPO_SPONSORSHIP, github_pages=True),
    }
    return render_template(Const.TEMPLATE_SPONSORSHIP, **default_data)


@sitemapper.include(lastmod=Const.DEPLOYMENT_DATE)
@app.route(Const.URL_ABOUT_US, methods=('GET', 'POST'))
def about_us():
    user_visit()
    default_data = {
        PhKeys.APP_TITLE: Const.TITLE_ABOUT_US,
        PhKeys.APP_DESCRIPTION: Const.DESCRIPTION_ABOUT_US,
        PhKeys.APP_VERSION: Const.VERSION_ABOUT_US,
        PhKeys.APP_GITHUB_URL: Util.get_github_url(github_repo=Const.GITHUB_REPO_ABOUT_US, github_pages=False),
        PhKeys.APP_GITHUB_PAGES_URL: Util.get_github_url(github_repo=Const.GITHUB_REPO_ABOUT_US, github_pages=True),
    }
    return render_template(Const.TEMPLATE_ABOUT_US, **default_data)


@sitemapper.include(lastmod=Const.DEPLOYMENT_DATE_CREDITS)
@app.route(Const.URL_CREDITS, methods=('GET', 'POST'))
def credits():
    user_visit()
    default_data = {
        PhKeys.APP_TITLE: Const.TITLE_CREDITS,
        PhKeys.APP_DESCRIPTION: Const.DESCRIPTION_CREDITS,
        PhKeys.APP_VERSION: Const.VERSION_CREDITS,
        PhKeys.APP_GITHUB_URL: Util.get_github_url(github_repo=Const.GITHUB_REPO_CREDITS, github_pages=False),
        PhKeys.APP_GITHUB_PAGES_URL: Util.get_github_url(github_repo=Const.GITHUB_REPO_CREDITS, github_pages=True),
    }
    return render_template(Const.TEMPLATE_CREDITS, **default_data)


@sitemapper.include(lastmod=Const.DEPLOYMENT_DATE)
@app.route(Const.URL_TESTIMONIALS, methods=('GET', 'POST'))
def testimonials():
    user_visit()
    default_data = {
        PhKeys.APP_TITLE: Const.TITLE_TESTIMONIALS,
        PhKeys.APP_DESCRIPTION: Const.DESCRIPTION_TESTIMONIALS,
        PhKeys.APP_VERSION: Const.VERSION_TESTIMONIALS,
        PhKeys.APP_GITHUB_URL: Util.get_github_url(github_repo=Const.GITHUB_REPO_TESTIMONIAL, github_pages=False),
        PhKeys.APP_GITHUB_PAGES_URL: Util.get_github_url(github_repo=Const.GITHUB_REPO_TESTIMONIAL, github_pages=True),
    }
    if request.method == 'GET':
        conn = get_db_connection()
        posts = conn.execute('SELECT * FROM posts').fetchall()
        conn.close()
        return render_template(Const.TEMPLATE_TESTIMONIALS, posts=posts, **default_data)
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        publisher = request.form['publisher']

        if not title:
            flash('Title is required!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO posts (title, content, publisher) VALUES (?, ?, ?)',
                         (title, content, publisher))
            conn.commit()
            conn.close()
            return redirect(url_for(Const.END_POINT_TESTIMONIALS))
    return render_template(Const.TEMPLATE_TESTIMONIALS, **default_data)


@app.route(Const.URL_TESTIMONIALS_ID)
def post(post_id):
    post = get_post(post_id)
    return render_template(Const.TEMPLATE_POST, post=post)


# TODO: Error handling
# @app.errorhandler(404)
# def not_found(e):
#     with open("./404.csv", "a") as f:
#         f.write(f'{datetime.datetime.now()},{request.__dict__}\n')
#     return send_file('static/images/Darknet-404-Page-Concept.png', mimetype='image/png')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8080')
