import os
from logging.config import dictConfig

from flask import Flask, request
from flask_sitemapper import Sitemapper
from python_helpers.ph_keys import PhKeys

from amenity_pj.handler import app_handler
from amenity_pj.helper.constants import Const
from amenity_pj.helper.constants_seo import ConstSeo
from amenity_pj.helper.util import Util

# from amenity_pj.helper.logger import dictConfig


app = Flask(__name__)
app.config['SECRET_KEY'] = 'Pj Test'
# app.config['SECRET_KEY'] = b'_5#y2L"F4Q8z\n\xec]/'
app.config['UPLOAD_FOLDER'] = Const.UPLOAD_FOLDER_PERMANENT

sitemapper = Sitemapper()
sitemapper.init_app(app)

host_name = None
# Default is Prod Env
prod_env = True

# @sitemap.register_generator
# def index():
# This function is Not needed if you set SITEMAP_INCLUDE_RULES_WITHOUT_PARAMS=True
# https://www.sitemaps.org/protocol.html
# yield Const.END_POINT_INDEX, {}
# yield Const.END_POINT_INDEX, {}, Const.DEPLOYMENT_DATE, 'monthly'

# TODO: Uncomment below for local execution
# prod_env = False

# Prod Logging
LOG_LEVEL = "INFO"
LOG_HANDLER = ["size-rotate"]
LOG_FILE_PATH = os.sep.join([Const.LOG_FOLDER_APPS, Const.LOG_FILE_NAME])
# TODO: Sitemap, Robot should work only for prod, beta, local; should not be allowed for alpha; past
sitemap_robot_needed = True
# Others
# LOG_HANDLER = ["console"]
# LOG_HANDLER = ["console", "file"]
# LOG_HANDLER = ["time-rotate"]


if prod_env is False:
    # localhost logging
    LOG_LEVEL = "INFO"
    # LOG_HANDLER = ["console", "size-rotate"]
    LOG_HANDLER = ["console", "file"]
    LOG_FILE_PATH = Const.LOG_FILE_NAME

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
                "filename": LOG_FILE_PATH,
                "formatter": "default",
            },
            "size-rotate": {
                "class": "logging.handlers.RotatingFileHandler",
                "filename": LOG_FILE_PATH,
                "maxBytes": Const.LOG_MAX_BYTES,
                "backupCount": Const.LOG_MAX_BACKUP_COUNT,
                "formatter": "default",
            },
            "time-rotate": {
                "class": "logging.handlers.TimedRotatingFileHandler",
                "filename": LOG_FILE_PATH,
                "when": "D",
                "interval": 10,
                "backupCount": Const.LOG_MAX_BACKUP_COUNT,
                "formatter": "default",
            },
        },
        "root":
            {
                "level": LOG_LEVEL,
                "handlers": LOG_HANDLER,
            },
    }
)

log = app.logger


@app.context_processor
def utility_processor_title_for():
    def title_for(end_point=None):
        return Util.get_apj_data(apj_id=None, specific_key=PhKeys.APP_TITLE, end_point=end_point)

    return dict(title_for=title_for)


@app.context_processor
def utility_processor_selected_input_format():
    def is_selected_input_format(input_format, selected_input_format):
        return Util.is_selected(input_format, selected_input_format)

    return dict(is_selected_input_format=is_selected_input_format)


@app.context_processor
def utility_processor_selected_output_format():
    def is_selected_output_format(output_format, selected_output_format):
        return Util.is_selected(output_format, selected_output_format)

    return dict(is_selected_output_format=is_selected_output_format)


@app.context_processor
def utility_processor_selected_asn1_schema():
    def is_selected_asn1_schema(asn1_schema, selected_asn1_schema):
        return Util.is_selected(asn1_schema, selected_asn1_schema)

    return dict(is_selected_asn1_schema=is_selected_asn1_schema)


@app.context_processor
def utility_processor_selected_sample():
    def is_selected_sample(sample, selected_sample):
        return Util.is_selected(sample, selected_sample)

    return dict(is_selected_sample=is_selected_sample)


@app.context_processor
def utility_processor_selected_qr_code_version():
    def is_selected_qr_code_version(sample, selected_qr_code_version):
        return Util.is_selected(sample, selected_qr_code_version)

    return dict(is_selected_qr_code_version=is_selected_qr_code_version)


@app.context_processor
def utility_processor_selected_url_time_out():
    def is_selected_url_time_out(sample, selected_url_time_out):
        return Util.is_selected(sample, selected_url_time_out)

    return dict(is_selected_url_time_out=is_selected_url_time_out)


@sitemapper.include(lastmod=ConstSeo.LAST_MODIFY_DATE_INDEX)
@app.route(Util.get_apj_data(apj_id=Const.APJ_ID_AMENITY_PJ, specific_key=PhKeys.APP_URL))
# Due to alias=True, URL_ALT will be redirected to URL
@app.route(Util.get_apj_data(apj_id=Const.APJ_ID_AMENITY_PJ, specific_key=PhKeys.APP_URL_ALT), alias=True)
def index():
    return app_handler.handle_requests(apj_id=Const.APJ_ID_AMENITY_PJ, log=log)


@sitemapper.include(lastmod=ConstSeo.LAST_MODIFY_DATE_ASN1_PLAY)
@app.route(Util.get_apj_data(apj_id=Const.APJ_ID_ASN1_PLAY, specific_key=PhKeys.APP_URL_API), methods=('GET', 'POST'),
           defaults={'api': True})
@app.route(Util.get_apj_data(apj_id=Const.APJ_ID_ASN1_PLAY, specific_key=PhKeys.APP_URL), methods=('GET', 'POST'),
           defaults={'api': False})
def asn1_play(api):
    return app_handler.handle_requests(apj_id=Const.APJ_ID_ASN1_PLAY, api=api, log=log)


@app.route(Util.get_apj_data(apj_id=Const.APJ_ID_ASN1_PLAY_ASN1_OBJECTS, specific_key=PhKeys.APP_URL))
def asn1_play_asn1_objects():
    return app_handler.handle_requests(apj_id=Const.APJ_ID_ASN1_PLAY_ASN1_OBJECTS, api=True, log=log,
                                       internal=True)


@sitemapper.include(lastmod=ConstSeo.LAST_MODIFY_DATE_TLV_PLAY)
@app.route(Util.get_apj_data(apj_id=Const.APJ_ID_TLV_PLAY, specific_key=PhKeys.APP_URL_API), methods=('GET', 'POST'),
           defaults={'api': True})
@app.route(Util.get_apj_data(apj_id=Const.APJ_ID_TLV_PLAY, specific_key=PhKeys.APP_URL), methods=('GET', 'POST'),
           defaults={'api': False})
def tlv_play(api):
    return app_handler.handle_requests(apj_id=Const.APJ_ID_TLV_PLAY, api=api, log=log)


@sitemapper.include(lastmod=ConstSeo.LAST_MODIFY_DATE_QR_PLAY)
@app.route(Util.get_apj_data(apj_id=Const.APJ_ID_QR_PLAY, specific_key=PhKeys.APP_URL_API), methods=('GET', 'POST'),
           defaults={'api': True})
@app.route(Util.get_apj_data(apj_id=Const.APJ_ID_QR_PLAY, specific_key=PhKeys.APP_URL), methods=('GET', 'POST'),
           defaults={'api': False})
def qr_play(api):
    return app_handler.handle_requests(apj_id=Const.APJ_ID_QR_PLAY, api=api, log=log, root_path=app.root_path)


@sitemapper.include(lastmod=ConstSeo.LAST_MODIFY_DATE_EXCEL_PLAY)
@app.route(Util.get_apj_data(apj_id=Const.APJ_ID_EXCEL_PLAY, specific_key=PhKeys.APP_URL_API), methods=('GET', 'POST'),
           defaults={'api': True})
@app.route(Util.get_apj_data(apj_id=Const.APJ_ID_EXCEL_PLAY, specific_key=PhKeys.APP_URL), methods=('GET', 'POST'),
           defaults={'api': False})
def excel_play(api):
    return app_handler.handle_requests(apj_id=Const.APJ_ID_EXCEL_PLAY, api=api, log=log, root_path=app.root_path)


@app.route(Util.get_apj_data(apj_id=Const.APJ_ID_EXCEL_PLAY_INFO, specific_key=PhKeys.APP_URL))
def excel_play_info():
    return app_handler.handle_requests(apj_id=Const.APJ_ID_EXCEL_PLAY_INFO, api=True, log=log,
                                       internal=True)


@sitemapper.include(lastmod=ConstSeo.LAST_MODIFY_DATE_CERT_PLAY)
@app.route(Util.get_apj_data(apj_id=Const.APJ_ID_CERT_PLAY, specific_key=PhKeys.APP_URL_API), methods=('GET', 'POST'),
           defaults={'api': True})
@app.route(Util.get_apj_data(apj_id=Const.APJ_ID_CERT_PLAY, specific_key=PhKeys.APP_URL), methods=('GET', 'POST'),
           defaults={'api': False})
def cert_play(api):
    return app_handler.handle_requests(apj_id=Const.APJ_ID_CERT_PLAY, api=api, log=log)


@sitemapper.include(lastmod=ConstSeo.LAST_MODIFY_DATE_DATA_PLAY)
@app.route(Util.get_apj_data(apj_id=Const.APJ_ID_DATA_PLAY, specific_key=PhKeys.APP_URL_API), methods=('GET', 'POST'),
           defaults={'api': True})
@app.route(Util.get_apj_data(apj_id=Const.APJ_ID_DATA_PLAY, specific_key=PhKeys.APP_URL), methods=('GET', 'POST'),
           defaults={'api': False})
def data_play(api):
    return app_handler.handle_requests(apj_id=Const.APJ_ID_DATA_PLAY, api=api, log=log)


@app.route(Util.get_apj_data(apj_id=Const.APJ_ID_TESTIMONIALS, specific_key=PhKeys.APP_URL), methods=('GET', 'POST'))
def testimonials():
    return app_handler.handle_requests(apj_id=Const.APJ_ID_TESTIMONIALS, log=log)


@app.route(Util.get_apj_data(apj_id=Const.APJ_ID_TESTIMONIALS_ID, specific_key=PhKeys.APP_URL), methods=('GET', 'POST'))
def testimonials_post(testimonial_post_id):
    return app_handler.handle_requests(apj_id=Const.APJ_ID_TESTIMONIALS_ID, log=log,
                                       testimonial_post_id=testimonial_post_id)


@sitemapper.include(lastmod=ConstSeo.LAST_MODIFY_DATE_ABOUT_US)
@app.route(Util.get_apj_data(apj_id=Const.APJ_ID_ABOUT_US, specific_key=PhKeys.APP_URL), methods=('GET', 'POST'))
def about_us():
    return app_handler.handle_requests(apj_id=Const.APJ_ID_ABOUT_US, log=log)


@app.route(Util.get_apj_data(apj_id=Const.APJ_ID_CREDITS, specific_key=PhKeys.APP_URL), methods=('GET', 'POST'))
def credits_():
    return app_handler.handle_requests(apj_id=Const.APJ_ID_CREDITS, log=log)


@app.route(Util.get_apj_data(apj_id=Const.APJ_ID_SPONSORSHIP, specific_key=PhKeys.APP_URL), methods=('GET', 'POST'))
def sponsorship():
    return app_handler.handle_requests(apj_id=Const.APJ_ID_SPONSORSHIP, log=log)


@sitemapper.include(lastmod=ConstSeo.LAST_MODIFY_DATE_LOGIN)
@app.route(Util.get_apj_data(apj_id=Const.APJ_ID_LOGIN, specific_key=PhKeys.APP_URL), methods=('GET', 'POST'))
def login():
    return app_handler.handle_requests(apj_id=Const.APJ_ID_LOGIN, log=log)


@app.route(Util.get_apj_data(apj_id=Const.APJ_ID_STATS, specific_key=PhKeys.APP_URL), methods=('GET', 'POST'))
def stats():
    return app_handler.handle_requests(apj_id=Const.APJ_ID_STATS, log=log)


@app.route(Util.get_apj_data(apj_id=Const.APJ_ID_SETTINGS, specific_key=PhKeys.APP_URL_API), methods=('GET', 'POST'),
           defaults={'api': True})
@app.route(Util.get_apj_data(apj_id=Const.APJ_ID_SETTINGS, specific_key=PhKeys.APP_URL), methods=('GET', 'POST'),
           defaults={'api': False})
def settings(api):
    return app_handler.handle_requests(apj_id=Const.APJ_ID_SETTINGS, api=api, log=log)


@app.errorhandler(Util.get_apj_data(apj_id=Const.APJ_ID_404, specific_key=PhKeys.APP_CODE))
def not_found(e):
    return app_handler.handle_requests(apj_id=Const.APJ_ID_404, log=log)


@app.route(Util.get_apj_data(apj_id=Const.APJ_ID_SERVER_DETAILS, specific_key=PhKeys.APP_URL), methods=('GET', 'POST'))
def server_details():
    return app_handler.handle_requests(apj_id=Const.APJ_ID_SERVER_DETAILS, api=True, log=log, internel=True)


@app.route(Util.get_apj_data(apj_id=Const.APJ_ID_SITEMAP, specific_key=PhKeys.APP_URL))
def sitemap():
    if sitemap_robot_needed:
        Util.user_visit(request=request, log=log)
        return sitemapper.generate()


@app.route(Util.get_apj_data(apj_id=Const.APJ_ID_ROBOT_TXT, specific_key=PhKeys.APP_URL))
def robot():
    if sitemap_robot_needed:
        return app_handler.handle_requests(apj_id=Const.APJ_ID_ROBOT_TXT, log=log)



@app.route(Util.get_apj_data(apj_id=Const.APJ_ID_FAV_ICON, specific_key=PhKeys.APP_URL))
def favicon():
    return app_handler.handle_requests(apj_id=Const.APJ_ID_FAV_ICON, log=log)


@app.route(Util.get_apj_data(apj_id=Const.APJ_ID_EXPERIMENTS_1, specific_key=PhKeys.APP_URL), methods=('GET', 'POST'),
           defaults={'apj_id': Const.APJ_ID_EXPERIMENTS_1})
@app.route(Util.get_apj_data(apj_id=Const.APJ_ID_EXPERIMENTS_2, specific_key=PhKeys.APP_URL), methods=('GET', 'POST'),
           defaults={'apj_id': Const.APJ_ID_EXPERIMENTS_2})
@app.route(Util.get_apj_data(apj_id=Const.APJ_ID_EXPERIMENTS_3, specific_key=PhKeys.APP_URL), methods=('GET', 'POST'),
           defaults={'apj_id': Const.APJ_ID_EXPERIMENTS_3})
@app.route(Util.get_apj_data(apj_id=Const.APJ_ID_EXPERIMENTS_4, specific_key=PhKeys.APP_URL), methods=('GET', 'POST'),
           defaults={'apj_id': Const.APJ_ID_EXPERIMENTS_4})
@app.route(Util.get_apj_data(apj_id=Const.APJ_ID_EXPERIMENTS_5, specific_key=PhKeys.APP_URL), methods=('GET', 'POST'),
           defaults={'apj_id': Const.APJ_ID_EXPERIMENTS_5})
@app.route(Util.get_apj_data(apj_id=Const.APJ_ID_EXPERIMENTS_6, specific_key=PhKeys.APP_URL), methods=('GET', 'POST'),
           defaults={'apj_id': Const.APJ_ID_EXPERIMENTS_6})
@app.route(Util.get_apj_data(apj_id=Const.APJ_ID_EXPERIMENTS_7, specific_key=PhKeys.APP_URL), methods=('GET', 'POST'),
           defaults={'apj_id': Const.APJ_ID_EXPERIMENTS_7})
@app.route(Util.get_apj_data(apj_id=Const.APJ_ID_EXPERIMENTS_8, specific_key=PhKeys.APP_URL), methods=('GET', 'POST'),
           defaults={'apj_id': Const.APJ_ID_EXPERIMENTS_8})
@app.route(Util.get_apj_data(apj_id=Const.APJ_ID_EXPERIMENTS_9, specific_key=PhKeys.APP_URL), methods=('GET', 'POST'),
           defaults={'apj_id': Const.APJ_ID_EXPERIMENTS_9})
@app.route(Util.get_apj_data(apj_id=Const.APJ_ID_EXPERIMENTS_10, specific_key=PhKeys.APP_URL), methods=('GET', 'POST'),
           defaults={'apj_id': Const.APJ_ID_EXPERIMENTS_10})
@app.route(Util.get_apj_data(apj_id=Const.APJ_ID_EXPERIMENTS_11, specific_key=PhKeys.APP_URL), methods=('GET', 'POST'),
           defaults={'apj_id': Const.APJ_ID_EXPERIMENTS_11})
@app.route(Util.get_apj_data(apj_id=Const.APJ_ID_EXPERIMENTS_12, specific_key=PhKeys.APP_URL), methods=('GET', 'POST'),
           defaults={'apj_id': Const.APJ_ID_EXPERIMENTS_12})
@app.route(Util.get_apj_data(apj_id=Const.APJ_ID_EXPERIMENTS_13, specific_key=PhKeys.APP_URL), methods=('GET', 'POST'),
           defaults={'apj_id': Const.APJ_ID_EXPERIMENTS_13})
@app.route(Util.get_apj_data(apj_id=Const.APJ_ID_EXPERIMENTS_14, specific_key=PhKeys.APP_URL), methods=('GET', 'POST'),
           defaults={'apj_id': Const.APJ_ID_EXPERIMENTS_14})
@app.route(Util.get_apj_data(apj_id=Const.APJ_ID_EXPERIMENTS_15, specific_key=PhKeys.APP_URL), methods=('GET', 'POST'),
           defaults={'apj_id': Const.APJ_ID_EXPERIMENTS_15})
def experiments(apj_id):
    return app_handler.handle_requests(apj_id=apj_id, log=log)


if __name__ == "__main__":
    Const.print_versions()
    app.run(host='0.0.0.0', port='8080')
