import os

from asn1_play.main.helper.constants_config import ConfigConst as ConfigConst_Asn1Play
from cert_play.main.helper.constants_config import ConfigConst as ConfigConst_CertPlay
from excel_play.main.helper.constants_config import ConfigConst as ConfigConst_ExcelPlay
from python_helpers.ph_constants import PhConstants
from python_helpers.ph_keys import PhKeys
from qr_play.main.helper.constants_config import ConfigConst as ConfigConst_QrPlay
from tlv_play.main.helper.constants_config import ConfigConst as ConfigConst_TlvPlay

from amenity_pj.helper.constants_config import ConfigConst as ConfigConst_AmenityPj
from amenity_pj.helper.defaults import Defaults


class Const:
    """

    """
    LOG_FOLDER_APPS = os.sep.join(['logs', 'apps'])
    LOG_FOLDER_OTHER = os.sep.join(['logs', 'others'])
    LOG_FILE_NAME = 'amenitypj.log'
    LOG_404_FILE_NAME = '404.csv'
    # LOG_FILE_PATH = os.sep.join([LOG_FOLDER_APPS, LOG_FILE_NAME])
    LOG_FILE_404_PATH = os.sep.join([LOG_FOLDER_APPS, LOG_404_FILE_NAME])
    LOG_MAX_BYTES = 1000000
    LOG_MAX_BACKUP_COUNT = 1000
    UPLOAD_FOLDER_PERMANENT = os.sep.join([os.pardir, 'data', 'user', 'uploads_permanent'])
    UPLOAD_FOLDER_TEMPORARY = os.sep.join([os.pardir, 'data', 'user', 'uploads_temporary'])
    UPLOAD_FILE_EXTENSIONS_ALLOWED_GENERIC = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'ahk'}
    UPLOAD_FILE_EXTENSIONS_ALLOWED_EXCEL_PLAY = {'xls', 'xlsx', 'csv'}
    UPLOAD_FILE_EXTENSIONS_BLOCKED = {'exe'}

    DOWNLOAD_MSG = 'Your Download will begin shortly !!!'
    DOWNLOAD_MSG_DEFAULT = f'Processing Initiated ... {DOWNLOAD_MSG}'

    ####################
    # Deployment Dates
    ####################
    DEPLOYMENT_DATE = '2023-11-11'
    DEPLOYMENT_DATE_CERT_PLAY = '2024-05-03'
    DEPLOYMENT_DATE_CREDITS = '2024-06-01'
    DEPLOYMENT_DATE_API = '2024-07-06'

    ####################
    # IDs
    ####################
    APJ_ID_AMENITY_PJ = 10
    APJ_ID_LOGIN = 11
    APJ_ID_NEWS_COMMON = 12
    APJ_ID_TESTIMONIALS = 20
    APJ_ID_TESTIMONIALS_ID = 21
    APJ_ID_ABOUT_US = 30
    APJ_ID_CREDITS = 40
    APJ_ID_SPONSORSHIP = 50
    APJ_ID_SITEMAP = 60
    APJ_ID_SERVER_DETAILS = 70
    APJ_ID_404 = 80
    APJ_ID_EXPERIMENTS_GROUP = 0x90
    APJ_ID_EXPERIMENTS_1 = 0x91
    APJ_ID_EXPERIMENTS_2 = 0x92
    APJ_ID_EXPERIMENTS_3 = 0x93
    APJ_ID_EXPERIMENTS_4 = 0x94
    APJ_ID_EXPERIMENTS_5 = 0x95
    APJ_ID_EXPERIMENTS_6 = 0x96
    APJ_ID_EXPERIMENTS_7 = 0x97
    APJ_ID_EXPERIMENTS_8 = 0x98
    APJ_ID_EXPERIMENTS_9 = 0x99
    APJ_ID_EXPERIMENTS_10 = 0x9A
    APJ_ID_EXPERIMENTS_11 = 0x9B
    APJ_ID_EXPERIMENTS_12 = 0x9C
    APJ_ID_EXPERIMENTS_13 = 0x9D
    APJ_ID_EXPERIMENTS_14 = 0x9E
    APJ_ID_EXPERIMENTS_15 = 0x9F
    APJ_ID_APPS_GROUP = 0xD0
    APJ_ID_ASN1_PLAY = 0xD1
    APJ_ID_TLV_PLAY = 0xD2
    APJ_ID_QR_PLAY = 0xD3
    APJ_ID_EXCEL_PLAY = 0xD4
    APJ_ID_CERT_PLAY = 0xD5
    APJ_ID_ASN1_PLAY_ASN1_OBJECTS = 0xE1
    APJ_ID_EXCEL_PLAY_INFO = 0xE2

    ####################
    # END_POINTS
    ####################
    END_POINT_AMENITY_PJ = 'index'
    END_POINT_LOGIN = 'login'
    END_POINT_TESTIMONIALS = 'testimonials'
    END_POINT_ABOUT_US = 'about_us'
    END_POINT_CREDITS = 'credits_'
    END_POINT_SPONSORSHIP = 'sponsorship'
    END_POINT_EXPERIMENTS = 'experiments'
    END_POINT_ASN1_PLAY = 'asn1_play'
    END_POINT_ASN1_PLAY_ASN1_OBJECTS = 'asn1_play_asn1_objects'
    END_POINT_TLV_PLAY = 'tlv_play'
    END_POINT_QR_PLAY = 'qr_play'
    END_POINT_EXCEL_PLAY = 'excel_play'
    END_POINT_EXCEL_PLAY_INFO = 'excel_play_info'
    END_POINT_CERT_PLAY = 'cert_play'

    ####################
    # External URLs
    ####################
    GITHUB_PAGES = 'https://impratikjaiswal.github.io'
    GITHUB_REPO = 'https://github.com/impratikjaiswal'
    HOST_ADDRESS_PROD = 'https://amenitypj.in'
    HOST_ADDRESS_BETA = 'https://beta.amenitypj.in'
    HOST_ADDRESS_ALPHA = 'https://alpha.amenitypj.in'
    HOST_ADDRESS_PAST = 'https://past.amenitypj.in'

    ####################
    # APIs
    ####################
    GET_API = 'Get API'
    GET_ASN1_OBJECTS = 'Get ASN1 Objects'
    DEFAULT_URL_FOR_API = ''

    NAV_ITEMS_MAPPING_URL_FOR = [
        {'text': GET_API, 'url': DEFAULT_URL_FOR_API}
    ]

    NAV_ITEMS_MAPPING_APP_SPECIFIC = {
        APJ_ID_ASN1_PLAY:
            [
                {'text': GET_ASN1_OBJECTS, 'url': DEFAULT_URL_FOR_API},
            ],
    }

    NAV_ITEMS_MAPPING = {
        'beta':
            [
                {'text': 'Prod Release', 'url': HOST_ADDRESS_PROD},
                {'text': 'Past Release', 'url': HOST_ADDRESS_PAST},
            ],
        'alpha':
            [
                {'text': 'Beta Release', 'url': HOST_ADDRESS_BETA},
                {'text': 'Prod Release', 'url': HOST_ADDRESS_PROD},
                {'text': 'Past Release', 'url': HOST_ADDRESS_PAST},
            ],
        'past':
            [
                {'text': 'Prod Release', 'url': HOST_ADDRESS_PROD},
                {'text': 'Beta Release', 'url': HOST_ADDRESS_BETA},
            ],
        'prod':
            [
                {'text': 'Beta Release', 'url': HOST_ADDRESS_BETA},
                {'text': 'Past Release', 'url': HOST_ADDRESS_PAST},
            ],
        'local':
            [
                {'text': 'Prod Release', 'url': HOST_ADDRESS_PROD},
                {'text': 'Alpha Release', 'url': HOST_ADDRESS_ALPHA},
                {'text': 'Beta Release', 'url': HOST_ADDRESS_BETA},
                {'text': 'Past Release', 'url': HOST_ADDRESS_PAST},
            ],
    }

    ####################
    # Titles
    ####################
    TITLE_AMENITY_PJ = ConfigConst_AmenityPj.TOOL_TITLE
    # TODO: Tool Title in every tools config
    TITLE_ASN1_PLAY = 'ASN1 Play'
    TITLE_TLV_PLAY = 'TLV Play'
    TITLE_QR_PLAY = 'QR Play'
    TITLE_EXCEL_PLAY = 'Excel Play'
    TITLE_CERT_PLAY = 'Cert Play'
    TITLE_EXPERIMENTS = 'Experiments'

    ####################
    # Common or without end points Constants
    ####################
    VERSION_AMENITY_PJ = ConfigConst_AmenityPj.TOOL_VERSION_DETAILED
    TEMPLATE_WIP = 'wip.html'
    DESCRIPTION_EXPERIMENTS = '!!! Only For Admins !!!'

    ####################
    # Common Data APPS
    ####################
    COMMON_DATA_APPS = {
        PhKeys.APP_PARENT_TITLE: TITLE_AMENITY_PJ,
        PhKeys.APP_PARENT_VERSION: VERSION_AMENITY_PJ,
        PhKeys.SAMPLE_OPTION: Defaults.SAMPLE_OPTION,
        PhKeys.INPUT_DATA: PhConstants.STR_EMPTY,
        PhKeys.OUTPUT_DATA: PhConstants.STR_EMPTY,
        PhKeys.INFO_DATA: PhConstants.STR_EMPTY,
    }

    COMMON_DATA_EXPERIMENTS = {
        PhKeys.APP_TITLE: TITLE_EXPERIMENTS,
        PhKeys.APP_DESCRIPTION: DESCRIPTION_EXPERIMENTS,
        PhKeys.APP_END_POINT: END_POINT_EXPERIMENTS,
    }

    INDEX_LIST = [
        APJ_ID_AMENITY_PJ,
        APJ_ID_LOGIN,
    ]

    APPS_LIST = [
        APJ_ID_ASN1_PLAY,
        APJ_ID_TLV_PLAY,
        APJ_ID_QR_PLAY,
        APJ_ID_EXCEL_PLAY,
        APJ_ID_CERT_PLAY,
    ]

    APPS_LIST_NEWS = [
        APJ_ID_ASN1_PLAY,
        APJ_ID_TLV_PLAY,
        APJ_ID_QR_PLAY,
        # APJ_ID_EXCEL_PLAY,
        APJ_ID_CERT_PLAY,
    ]

    APPS_LIST_W_INDEX = INDEX_LIST + APPS_LIST

    WHATS_NEW_LIST = INDEX_LIST + APPS_LIST_NEWS

    ####################
    # Common Data All
    ####################
    COMMON_DATA_MAPPING = {
        #
        APJ_ID_AMENITY_PJ:
            {
                PhKeys.APP_TITLE_PRE: Defaults.APP_WELCOME,
                PhKeys.APP_TITLE: TITLE_AMENITY_PJ,
                PhKeys.APP_DESCRIPTION: f'{TITLE_AMENITY_PJ} offers a playground for various open source tools ('
                                        f'amenities) such as ASN1 Play, TLV Play, QR Play, Cert Play, Excel Play '
                                        f'which are crafted with the purpose of enhancing productivity.',
                PhKeys.APP_VERSION: VERSION_AMENITY_PJ,
                PhKeys.APP_GITHUB_URL: 'amenitypj',
                PhKeys.APP_GIT_SUMMARY: ConfigConst_AmenityPj.TOOL_GIT_SUMMARY,
                PhKeys.APP_URL: '/',
                PhKeys.APP_URL_ALT: '/index.html',
                PhKeys.APP_TEMPLATE: 'index.html',
                PhKeys.APP_END_POINT: END_POINT_AMENITY_PJ,
            },
        #
        APJ_ID_TESTIMONIALS:
            {
                PhKeys.APP_TITLE: 'Testimonials',
                PhKeys.APP_DESCRIPTION: 'Read What others feel about us',
                PhKeys.APP_URL: '/testimonials',
                PhKeys.APP_TEMPLATE: 'testimonials.html',
                PhKeys.APP_END_POINT: END_POINT_TESTIMONIALS,
            },
        #
        APJ_ID_TESTIMONIALS_ID:
            {
                PhKeys.APP_URL: '/testimonials/<int:testimonial_post_id>',
                PhKeys.APP_TEMPLATE: 'testimonialPost.html',
            },
        #
        APJ_ID_ABOUT_US:
            {
                PhKeys.APP_TITLE: 'About Us',
                PhKeys.APP_DESCRIPTION: f'As the word Amenity refers to an additional feature or service that '
                                        f'elevates convenience and comfort. {TITLE_AMENITY_PJ} also intends to offer '
                                        f'various day to day tools which may elevates productivity.',
                PhKeys.APP_URL: '/aboutUs',
                PhKeys.APP_TEMPLATE: 'aboutus.html',
                # Empty Value is necessary, so that default value can be set here
                PhKeys.APP_GITHUB_URL: '',
                PhKeys.APP_END_POINT: END_POINT_ABOUT_US,
            },
        #
        APJ_ID_CREDITS:
            {
                PhKeys.APP_TITLE: 'Credits',
                PhKeys.APP_DESCRIPTION: f'{TITLE_AMENITY_PJ} is Thankful to its day to day users, feedback providers '
                                        f'(online as well as offline), validators, 3rd Party products. '
                                        f'Couple of names can be found below: ',
                PhKeys.APP_URL: '/credits',
                PhKeys.APP_TEMPLATE: 'credits.html',
                PhKeys.APP_END_POINT: END_POINT_CREDITS,
            },
        #
        APJ_ID_SPONSORSHIP:
            {
                PhKeys.APP_TITLE: 'Sponsorship',
                PhKeys.APP_DESCRIPTION: Defaults.DESCRIPTION,
                PhKeys.APP_URL: '/sponsorship',
                PhKeys.APP_TEMPLATE: TEMPLATE_WIP,
                PhKeys.APP_DESCRIPTION_LEVEL_2: Defaults.DESCRIPTION_WIP,
                PhKeys.APP_END_POINT: END_POINT_SPONSORSHIP,
            },
        #
        APJ_ID_LOGIN:
            {
                PhKeys.APP_TITLE: 'Login',
                PhKeys.APP_DESCRIPTION: '!!! Currently only Admin Login is supported !!!',
                PhKeys.APP_URL: '/login',
                PhKeys.APP_TEMPLATE: 'login.html',
                PhKeys.APP_END_POINT: END_POINT_LOGIN,
            },
        #
        APJ_ID_SITEMAP:
            {
                PhKeys.APP_URL: '/sitemap.xml',
            },
        #
        APJ_ID_SERVER_DETAILS:
            {
                PhKeys.APP_URL: '/api/serverDetails',
            },
        #
        APJ_ID_404:
            {
                PhKeys.APP_TITLE: '404',
                PhKeys.APP_DESCRIPTION: f"I'm afraid you've found a page that doesn't exist on {TITLE_AMENITY_PJ}.",
                PhKeys.APP_CODE: 404,
                PhKeys.APP_TEMPLATE: '404.html',
            },
        #
        APJ_ID_EXPERIMENTS_1:
            {
                PhKeys.APP_URL: '/exp1',
                PhKeys.APP_TEMPLATE: '/experiments/1_file_upload.html',
            },
        #
        APJ_ID_EXPERIMENTS_2:
            {
                PhKeys.APP_URL: '/exp2',
                PhKeys.APP_TEMPLATE: '/experiments/2_404_cave_man.html',
            },
        #
        APJ_ID_EXPERIMENTS_3:
            {
                PhKeys.APP_URL: '/exp3',
                PhKeys.APP_TEMPLATE: '/experiments/3_404_fear_eyes.html',
            },
        #
        APJ_ID_EXPERIMENTS_4:
            {
                PhKeys.APP_URL: '/exp4',
                PhKeys.APP_TEMPLATE: '/experiments/4.html',
            },
        #
        APJ_ID_EXPERIMENTS_5:
            {
                PhKeys.APP_URL: '/exp5',
                PhKeys.APP_TEMPLATE: '/experiments/5.html',
            },
        #
        APJ_ID_EXPERIMENTS_6:
            {
                PhKeys.APP_URL: '/exp6',
                PhKeys.APP_TEMPLATE: '/experiments/6.html',
            },
        #
        APJ_ID_EXPERIMENTS_7:
            {
                PhKeys.APP_URL: '/exp7',
                PhKeys.APP_TEMPLATE: '/experiments/7.html',
            },
        #
        APJ_ID_EXPERIMENTS_8:
            {
                PhKeys.APP_URL: '/exp8',
                PhKeys.APP_TEMPLATE: '/experiments/8.html',
            },
        #
        APJ_ID_EXPERIMENTS_9:
            {
                PhKeys.APP_URL: '/exp9',
                PhKeys.APP_TEMPLATE: '/experiments/9.html',
            },
        #
        APJ_ID_EXPERIMENTS_10:
            {
                PhKeys.APP_URL: '/exp10',
                PhKeys.APP_TEMPLATE: '/experiments/10.html',
            },
        #
        APJ_ID_EXPERIMENTS_11:
            {
                PhKeys.APP_URL: '/exp11',
                PhKeys.APP_TEMPLATE: '/experiments/11.html',
            },
        #
        APJ_ID_EXPERIMENTS_12:
            {
                PhKeys.APP_URL: '/exp12',
                PhKeys.APP_TEMPLATE: '/experiments/12.html',
            },
        #
        APJ_ID_EXPERIMENTS_13:
            {
                PhKeys.APP_URL: '/exp13',
                PhKeys.APP_TEMPLATE: '/experiments/13.html',
            },
        #
        APJ_ID_EXPERIMENTS_14:
            {
                PhKeys.APP_URL: '/exp14',
                PhKeys.APP_TEMPLATE: '/experiments/14.html',
            },
        #
        APJ_ID_EXPERIMENTS_15:
            {
                PhKeys.APP_URL: '/exp15',
                PhKeys.APP_TEMPLATE: '/experiments/15.html',
            },
        #
        APJ_ID_ASN1_PLAY:
            {
                PhKeys.APP_TITLE_PRE: Defaults.APP_WELCOME,
                PhKeys.APP_TITLE: TITLE_ASN1_PLAY,
                PhKeys.APP_VERSION: ConfigConst_Asn1Play.TOOL_VERSION_DETAILED,
                PhKeys.APP_DESCRIPTION: 'ASN1 Encoder & Decoder based on pycrate.',
                PhKeys.APP_GITHUB_URL: 'asn1Play',
                PhKeys.APP_GIT_SUMMARY: ConfigConst_Asn1Play.TOOL_GIT_SUMMARY,
                PhKeys.APP_URL: '/asn1Play',
                PhKeys.APP_URL_API: '/api/asn1Play',
                PhKeys.APP_TEMPLATE: '/apps/asn1Play.html',
                PhKeys.APP_END_POINT: END_POINT_ASN1_PLAY,
            },
        #
        APJ_ID_ASN1_PLAY_ASN1_OBJECTS:
            {
                PhKeys.APP_URL: '/asn1Play/asn1Objects',
                PhKeys.APP_END_POINT: END_POINT_ASN1_PLAY_ASN1_OBJECTS
            },
        #
        APJ_ID_EXCEL_PLAY_INFO:
            {
                PhKeys.APP_URL: '/excelPlay/info',
                PhKeys.APP_END_POINT: END_POINT_EXCEL_PLAY_INFO
            },
        #
        APJ_ID_TLV_PLAY:
            {
                PhKeys.APP_TITLE_PRE: Defaults.APP_WELCOME,
                PhKeys.APP_TITLE: TITLE_TLV_PLAY,
                PhKeys.APP_VERSION: ConfigConst_TlvPlay.TOOL_VERSION,
                PhKeys.APP_DESCRIPTION: 'Generic TLV Parser. Will parse any TLV upto nth Level.',
                PhKeys.APP_GITHUB_URL: 'tlvPlay',
                PhKeys.APP_GIT_SUMMARY: ConfigConst_TlvPlay.TOOL_GIT_SUMMARY,
                PhKeys.APP_URL: '/tlvPlay',
                PhKeys.APP_URL_API: '/api/tlvPlay',
                PhKeys.APP_TEMPLATE: '/apps/tlvPlay.html',
                PhKeys.APP_END_POINT: END_POINT_TLV_PLAY,
            },
        #
        APJ_ID_QR_PLAY:
            {
                PhKeys.APP_TITLE_PRE: Defaults.APP_WELCOME,
                PhKeys.APP_TITLE: TITLE_QR_PLAY,
                PhKeys.APP_VERSION: ConfigConst_QrPlay.TOOL_VERSION_DETAILED,
                PhKeys.APP_DESCRIPTION: 'Qr Code Generator based on Segno. Can Generate Single as well as Multiple Qr codes.',
                PhKeys.APP_GITHUB_URL: 'qrPlay',
                PhKeys.APP_GIT_SUMMARY: ConfigConst_QrPlay.TOOL_GIT_SUMMARY,
                PhKeys.APP_URL: '/qrPlay',
                PhKeys.APP_URL_API: '/api/qrPlay',
                PhKeys.APP_TEMPLATE: '/apps/qrPlay.html',
                PhKeys.APP_END_POINT: END_POINT_QR_PLAY,
            },
        #
        APJ_ID_EXCEL_PLAY:
            {
                PhKeys.APP_TITLE_PRE: Defaults.APP_WELCOME,
                PhKeys.APP_TITLE: TITLE_EXCEL_PLAY,
                PhKeys.APP_VERSION: ConfigConst_ExcelPlay.TOOL_VERSION_DETAILED,
                PhKeys.APP_DESCRIPTION: 'Export one or more Excel file(s) (with single or multiple sheets) to several '
                                        'csv files each containing one sheet.',
                PhKeys.APP_GITHUB_URL: 'excelPlay',
                PhKeys.APP_GIT_SUMMARY: ConfigConst_ExcelPlay.TOOL_GIT_SUMMARY,
                PhKeys.APP_URL: '/excelPlay',
                PhKeys.APP_URL_API: '/api/excelPlay',
                PhKeys.APP_TEMPLATE: '/apps/excelPlay.html',
                PhKeys.APP_END_POINT: END_POINT_EXCEL_PLAY,
            },
        #
        APJ_ID_CERT_PLAY:
            {
                PhKeys.APP_TITLE_PRE: Defaults.APP_WELCOME,
                PhKeys.APP_TITLE: TITLE_CERT_PLAY,
                PhKeys.APP_VERSION: ConfigConst_CertPlay.TOOL_VERSION_DETAILED,
                PhKeys.APP_DESCRIPTION: 'OpenSSL based Cert Parser. Will parse any TLS cert.',
                PhKeys.APP_GITHUB_URL: 'certPlay',
                PhKeys.APP_GIT_SUMMARY: ConfigConst_CertPlay.TOOL_GIT_SUMMARY,
                PhKeys.APP_URL: '/certPlay',
                PhKeys.APP_URL_API: '/api/certPlay',
                PhKeys.APP_TEMPLATE: '/apps/certPlay.html',
                PhKeys.APP_END_POINT: END_POINT_CERT_PLAY,
            },
    }

    ####################
    # END_POINTS, APJ MAPPING; Needed for Calling from HTML pages
    ####################
    END_POINT_APJ_MAPPING = {
        END_POINT_AMENITY_PJ: APJ_ID_AMENITY_PJ,
        END_POINT_LOGIN: APJ_ID_LOGIN,
        END_POINT_TESTIMONIALS: APJ_ID_TESTIMONIALS,
        END_POINT_ABOUT_US: APJ_ID_ABOUT_US,
        END_POINT_CREDITS: APJ_ID_CREDITS,
        END_POINT_SPONSORSHIP: APJ_ID_SPONSORSHIP,
        END_POINT_ASN1_PLAY: APJ_ID_ASN1_PLAY,
        END_POINT_ASN1_PLAY_ASN1_OBJECTS: APJ_ID_ASN1_PLAY_ASN1_OBJECTS,
        END_POINT_TLV_PLAY: APJ_ID_TLV_PLAY,
        END_POINT_QR_PLAY: APJ_ID_QR_PLAY,
        END_POINT_EXCEL_PLAY: APJ_ID_EXCEL_PLAY,
        END_POINT_CERT_PLAY: APJ_ID_CERT_PLAY,
    }

    ####################
    # News Data All
    ####################
    NEWS_DATA_MAPPING = {
        #
        APJ_ID_NEWS_COMMON:
            [
                #
                # f'{PhKeys.APP_TITLE} now supports "Copy Input Data", "Copy Output Data" & "Copy Info".',
                #
                f'{PhKeys.APP_TITLE} is now equipped with essential copy/paste functionality. '
                f'Try "Copy" icon available with various field(s).',
                #
                # f'{PhKeys.APP_TITLE} now supports "Download Input Data", "Download Output Data" & "Download Info".'
                #
                f'{PhKeys.APP_TITLE} is now equipped with essential download functionality. '
                f'Try "Download" icon available with various field(s).',
                #
                # f'{PhKeys.APP_TITLE} now supports "Upload Input Data".'
                #
                f'{PhKeys.APP_TITLE} is now equipped with essential upload functionality. '
                f'Try "Upload" icon available with Input Data field.'
                #
            ],
        #
        APJ_ID_ASN1_PLAY:
            [
                #
                f'{TITLE_ASN1_PLAY} now supports GSMA SGP.32 v1.1 & v1.2 (GSMA_SGP_32_v1_1, GSMA_SGP_32_v1_2).',
                #
                f'{TITLE_ASN1_PLAY} will auto trim the Quotation marks \"\" or \'\' if present.',
                #
                f'To convert any APDU in {TITLE_ASN1_PLAY}, please trim the last 2 bytes of SW/Status Word (e.g: 9000).',
                #
            ],
        #
        APJ_ID_TLV_PLAY:
            [
                #
                f'{TITLE_TLV_PLAY} now supports Base 64 data.',
                #
                f'if "Value In Ascii" is selected, {TITLE_TLV_PLAY} converts hex data to ascii where ever possible.',
                #
                f'if "Non TLV Neighbor" is selected, {TITLE_TLV_PLAY} will handle scenarios where non TLV data is '
                f'placed after TLV(s)',
                #
            ],
        #
        APJ_ID_QR_PLAY:
            [
                #
                f'if "Auto Split Qrs" is selected, {TITLE_QR_PLAY} breaks data in multiple chunks if data does not '
                f'fit in one QR.',
                #
            ],
        #
        APJ_ID_EXCEL_PLAY:
            [],
        #
        APJ_ID_CERT_PLAY:
            [
                #
                f'{TITLE_CERT_PLAY} Automatically takes care of Open SSL format (-----BEGIN CERTIFICATE-----, '
                f'-----END CERTIFICATE-----).',
                #
            ],
    }
