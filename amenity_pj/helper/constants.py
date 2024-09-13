import os

from asn1_play.main.helper.constants_config import ConfigConst as ConfigConst_Asn1Play
from cert_play.main.helper.constants_config import ConfigConst as ConfigConst_CertPlay
from excel_play.main.helper.constants_config import ConfigConst as ConfigConst_ExcelPlay
from python_helpers.ph_constants import PhConstants
from python_helpers.ph_keys import PhKeys
from python_helpers.ph_util import PhUtil
from qr_play.main.helper.constants_config import ConfigConst as ConfigConst_QrPlay
from tlv_play.main.helper.constants_config import ConfigConst as ConfigConst_TlvPlay

from amenity_pj.helper.constants_config import ConfigConst as ConfigConst_AmenityPj
from amenity_pj.helper.constants_seo import ConstSeo
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
    # IDs
    ####################
    APJ_ID_AMENITY_PJ = 0x11
    APJ_ID_LOGIN = 0x12
    APJ_ID_ABOUT_US = 0x13

    APJ_ID_TESTIMONIALS = 0x21
    APJ_ID_TESTIMONIALS_ID = 0x22
    APJ_ID_NEWS_COMMON = 0x23

    APJ_ID_CREDITS = 0x31
    APJ_ID_SPONSORSHIP = 0x32
    APJ_ID_404 = 0x33
    APJ_ID_STATS = 0x34
    APJ_ID_SETTINGS = 0x35

    APJ_ID_SEO_GROUP = 0x40
    APJ_ID_SITEMAP = 0x41
    APJ_ID_ROBOT_TXT = 0x42

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

    APJ_ID_APPS_API_GROUP = 0xE0
    APJ_ID_ASN1_PLAY_ASN1_OBJECTS = 0xE1
    APJ_ID_EXCEL_PLAY_INFO = 0xE2

    APJ_ID_DEV_API_GROUP = 0xF0
    APJ_ID_SERVER_DETAILS = 0xF1

    ####################
    # END_POINTS
    ####################
    END_POINT_AMENITY_PJ = 'index'
    END_POINT_LOGIN = 'login'
    END_POINT_TESTIMONIALS = 'testimonials'
    END_POINT_ABOUT_US = 'about_us'
    END_POINT_CREDITS = 'credits_'
    END_POINT_SPONSORSHIP = 'sponsorship'
    END_POINT_STATS = 'stats'
    END_POINT_SETTINGS = 'settings'
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

    DEFAULT_CANONICAL_URL = HOST_ADDRESS_PROD
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
    TITLE_EXPERIMENTS = 'Experiments'

    ####################
    # Common or without end points Constants
    ####################
    VERSION_AMENITY_PJ = ConfigConst_AmenityPj.TOOL_VERSION_DETAILED
    TEMPLATE_WIP = 'wip.html'
    DESCRIPTION_ONLY_FOR_ADMINS = '!!! Only For Admins !!!'

    ####################
    # Common Data APPS
    ####################
    COMMON_DATA_APPS = {
        PhKeys.APP_PARENT_TITLE: ConstSeo.TITLE_AMENITY_PJ,
        PhKeys.APP_PARENT_VERSION: f'{PhConstants.SEPERATOR_NAME_VERSION}{VERSION_AMENITY_PJ}',
        PhKeys.SAMPLE_OPTION: Defaults.SAMPLE_OPTION,
        PhKeys.INPUT_DATA: PhConstants.STR_EMPTY,
        PhKeys.OUTPUT_DATA: PhConstants.STR_EMPTY,
        PhKeys.INFO_DATA: PhConstants.STR_EMPTY,
    }

    COMMON_DATA_EXPERIMENTS = {
        PhKeys.APP_TITLE: TITLE_EXPERIMENTS,
        PhKeys.APP_DESCRIPTION: DESCRIPTION_ONLY_FOR_ADMINS,
        PhKeys.APP_END_POINT: END_POINT_EXPERIMENTS,
    }

    INDEX_LIST = [
        APJ_ID_AMENITY_PJ,
        APJ_ID_LOGIN,
        APJ_ID_ABOUT_US,
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
                PhKeys.APP_TITLE: ConstSeo.TITLE_AMENITY_PJ,
                PhKeys.APP_DESCRIPTION: ConstSeo.APP_DESCRIPTION_AMENITY_PJ,
                PhKeys.APP_VERSION: f'{PhConstants.SEPERATOR_NAME_VERSION}{VERSION_AMENITY_PJ}',
                PhKeys.APP_GITHUB_URL: 'amenitypj',
                PhKeys.APP_GIT_SUMMARY: ConfigConst_AmenityPj.TOOL_GIT_SUMMARY,
                PhKeys.APP_URL: '/',
                PhKeys.APP_URL_ALT: '/index.html',
                PhKeys.APP_TEMPLATE: 'index.html',
                PhKeys.APP_END_POINT: END_POINT_AMENITY_PJ,
                PhKeys.APP_META_DESCRIPTION: ConstSeo.APP_META_DESCRIPTION_AMENITY_PJ,
                PhKeys.APP_META_KEYWORDS: ConstSeo.APP_META_KEYWORDS_AMENITY_PJ,
                PhKeys.APP_META_AUTHOR: ConstSeo.APP_META_AUTHOR,
            },
        #
        APJ_ID_ASN1_PLAY:
            {
                PhKeys.APP_TITLE_PRE: Defaults.APP_WELCOME,
                PhKeys.APP_TITLE: ConstSeo.TITLE_ASN1_PLAY,
                PhKeys.APP_VERSION: f'{PhConstants.SEPERATOR_NAME_VERSION}{ConfigConst_Asn1Play.TOOL_VERSION_DETAILED}',
                PhKeys.APP_DESCRIPTION: ConstSeo.APP_DESCRIPTION_ASN1_PLAY,
                PhKeys.APP_GITHUB_URL: 'asn1Play',
                PhKeys.APP_GIT_SUMMARY: ConfigConst_Asn1Play.TOOL_GIT_SUMMARY,
                PhKeys.APP_URL: '/asn1Play',
                PhKeys.APP_URL_API: '/api/asn1Play',
                PhKeys.APP_TEMPLATE: '/apps/asn1Play.html',
                PhKeys.APP_END_POINT: END_POINT_ASN1_PLAY,
                PhKeys.APP_META_DESCRIPTION: ConstSeo.APP_META_DESCRIPTION_ASN1_PLAY,
                PhKeys.APP_META_KEYWORDS: ConstSeo.APP_META_KEYWORDS_ASN1_PLAY,
                PhKeys.APP_META_AUTHOR: ConstSeo.APP_META_AUTHOR,
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
                PhKeys.APP_TITLE: ConstSeo.TITLE_TLV_PLAY,
                PhKeys.APP_VERSION: f'{PhConstants.SEPERATOR_NAME_VERSION}{ConfigConst_TlvPlay.TOOL_VERSION}',
                PhKeys.APP_DESCRIPTION: ConstSeo.APP_DESCRIPTION_TLV_PLAY,
                PhKeys.APP_GITHUB_URL: 'tlvPlay',
                PhKeys.APP_GIT_SUMMARY: ConfigConst_TlvPlay.TOOL_GIT_SUMMARY,
                PhKeys.APP_URL: '/tlvPlay',
                PhKeys.APP_URL_API: '/api/tlvPlay',
                PhKeys.APP_TEMPLATE: '/apps/tlvPlay.html',
                PhKeys.APP_END_POINT: END_POINT_TLV_PLAY,
                PhKeys.APP_META_DESCRIPTION: ConstSeo.APP_META_DESCRIPTION_TLV_PLAY,
                PhKeys.APP_META_KEYWORDS: ConstSeo.APP_META_KEYWORDS_TLV_PLAY,
                PhKeys.APP_META_AUTHOR: ConstSeo.APP_META_AUTHOR,
            },
        #
        APJ_ID_QR_PLAY:
            {
                PhKeys.APP_TITLE_PRE: Defaults.APP_WELCOME,
                PhKeys.APP_TITLE: ConstSeo.TITLE_QR_PLAY,
                PhKeys.APP_VERSION: f'{PhConstants.SEPERATOR_NAME_VERSION}{ConfigConst_QrPlay.TOOL_VERSION_DETAILED}',
                PhKeys.APP_DESCRIPTION: ConstSeo.APP_DESCRIPTION_QR_PLAY,
                PhKeys.APP_GITHUB_URL: 'qrPlay',
                PhKeys.APP_GIT_SUMMARY: ConfigConst_QrPlay.TOOL_GIT_SUMMARY,
                PhKeys.APP_URL: '/qrPlay',
                PhKeys.APP_URL_API: '/api/qrPlay',
                PhKeys.APP_TEMPLATE: '/apps/qrPlay.html',
                PhKeys.APP_END_POINT: END_POINT_QR_PLAY,
                PhKeys.APP_META_DESCRIPTION: ConstSeo.APP_META_DESCRIPTION_QR_PLAY,
                PhKeys.APP_META_KEYWORDS: ConstSeo.APP_META_KEYWORDS_QR_PLAY,
                PhKeys.APP_META_AUTHOR: ConstSeo.APP_META_AUTHOR,
            },
        #
        APJ_ID_EXCEL_PLAY:
            {
                PhKeys.APP_TITLE_PRE: Defaults.APP_WELCOME,
                PhKeys.APP_TITLE: ConstSeo.TITLE_EXCEL_PLAY,
                PhKeys.APP_VERSION: f'{PhConstants.SEPERATOR_NAME_VERSION}{ConfigConst_ExcelPlay.TOOL_VERSION_DETAILED}',
                PhKeys.APP_DESCRIPTION: ConstSeo.APP_DESCRIPTION_EXCEL_PLAY,
                PhKeys.APP_GITHUB_URL: 'excelPlay',
                PhKeys.APP_GIT_SUMMARY: ConfigConst_ExcelPlay.TOOL_GIT_SUMMARY,
                PhKeys.APP_URL: '/excelPlay',
                PhKeys.APP_URL_API: '/api/excelPlay',
                PhKeys.APP_TEMPLATE: '/apps/excelPlay.html',
                PhKeys.APP_END_POINT: END_POINT_EXCEL_PLAY,
                PhKeys.APP_META_DESCRIPTION: ConstSeo.APP_META_DESCRIPTION_EXCEL_PLAY,
                PhKeys.APP_META_KEYWORDS: ConstSeo.APP_META_KEYWORDS_EXCEL_PLAY,
                PhKeys.APP_META_AUTHOR: ConstSeo.APP_META_AUTHOR,
            },
        #
        APJ_ID_CERT_PLAY:
            {
                PhKeys.APP_TITLE_PRE: Defaults.APP_WELCOME,
                PhKeys.APP_TITLE: ConstSeo.TITLE_CERT_PLAY,
                PhKeys.APP_VERSION: f'{PhConstants.SEPERATOR_NAME_VERSION}{ConfigConst_CertPlay.TOOL_VERSION_DETAILED}',
                PhKeys.APP_DESCRIPTION: ConstSeo.APP_DESCRIPTION_CERT_PLAY,
                PhKeys.APP_GITHUB_URL: 'certPlay',
                PhKeys.APP_GIT_SUMMARY: ConfigConst_CertPlay.TOOL_GIT_SUMMARY,
                PhKeys.APP_URL: '/certPlay',
                PhKeys.APP_URL_API: '/api/certPlay',
                PhKeys.APP_TEMPLATE: '/apps/certPlay.html',
                PhKeys.APP_END_POINT: END_POINT_CERT_PLAY,
                PhKeys.APP_META_DESCRIPTION: ConstSeo.APP_META_DESCRIPTION_CERT_PLAY,
                PhKeys.APP_META_KEYWORDS: ConstSeo.APP_META_KEYWORDS_CERT_PLAY,
                PhKeys.APP_META_AUTHOR: ConstSeo.APP_META_AUTHOR,
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
                PhKeys.APP_DESCRIPTION: ConstSeo.APP_DESCRIPTION_ABOUT_US,
                PhKeys.APP_URL: '/aboutUs',
                PhKeys.APP_TEMPLATE: 'aboutus.html',
                # Empty Value is necessary, so that default value can be set here
                PhKeys.APP_GITHUB_URL: '',
                PhKeys.APP_END_POINT: END_POINT_ABOUT_US,
                PhKeys.APP_META_DESCRIPTION: ConstSeo.APP_META_DESCRIPTION_ABOUT_US,
                PhKeys.APP_META_KEYWORDS: ConstSeo.APP_META_KEYWORDS_ABOUT_US,
                PhKeys.APP_META_AUTHOR: ConstSeo.APP_META_AUTHOR,
            },
        #
        APJ_ID_CREDITS:
            {
                PhKeys.APP_TITLE: 'Credits',
                PhKeys.APP_DESCRIPTION: f'{ConstSeo.TITLE_AMENITY_PJ} is Thankful to its day to day users, feedback providers '
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
                PhKeys.APP_DESCRIPTION: ConstSeo.APP_DESCRIPTION_LOGIN,
                PhKeys.APP_URL: '/login',
                PhKeys.APP_TEMPLATE: 'login.html',
                PhKeys.APP_END_POINT: END_POINT_LOGIN,
                PhKeys.APP_META_DESCRIPTION: ConstSeo.APP_META_DESCRIPTION_LOGIN,
                PhKeys.APP_META_KEYWORDS: ConstSeo.APP_META_KEYWORDS_LOGIN,
                PhKeys.APP_META_AUTHOR: ConstSeo.APP_META_AUTHOR,
            },
        #
        APJ_ID_STATS:
            {
                PhKeys.APP_TITLE: 'Stats',
                PhKeys.APP_DESCRIPTION: DESCRIPTION_ONLY_FOR_ADMINS,
                PhKeys.APP_URL: '/stats',
                PhKeys.APP_TEMPLATE: 'stats.html',
                PhKeys.APP_END_POINT: END_POINT_STATS,
            },
        #
        APJ_ID_SETTINGS:
            {
                PhKeys.APP_TITLE: 'Settings',
                PhKeys.APP_DESCRIPTION: DESCRIPTION_ONLY_FOR_ADMINS,
                PhKeys.APP_URL: '/settings',
                PhKeys.APP_URL_API: '/api/settings',
                PhKeys.APP_TEMPLATE: 'settings.html',
                PhKeys.APP_END_POINT: END_POINT_SETTINGS,
            },
        #
        APJ_ID_SITEMAP:
            {
                PhKeys.APP_URL: '/sitemap.xml',
            },
        #
        APJ_ID_ROBOT_TXT:
            {
                PhKeys.APP_URL: '/robots.txt',
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
                PhKeys.APP_DESCRIPTION: f"I'm afraid you've found a page that doesn't exist on {ConstSeo.TITLE_AMENITY_PJ}.",
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
                PhKeys.APP_TEMPLATE: '/experiments/4_text_area_line_number.html',
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
                PhKeys.APP_TEMPLATE: '/experiments/12_404_cave_man_apj.html',
            },
        #
        APJ_ID_EXPERIMENTS_13:
            {
                PhKeys.APP_URL: '/exp13',
                PhKeys.APP_TEMPLATE: '/experiments/13_404_fear_eyes_apj.html',
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
        END_POINT_STATS: APJ_ID_STATS,
        END_POINT_SETTINGS: APJ_ID_SETTINGS,
        END_POINT_ASN1_PLAY: APJ_ID_ASN1_PLAY,
        END_POINT_ASN1_PLAY_ASN1_OBJECTS: APJ_ID_ASN1_PLAY_ASN1_OBJECTS,
        END_POINT_TLV_PLAY: APJ_ID_TLV_PLAY,
        END_POINT_QR_PLAY: APJ_ID_QR_PLAY,
        END_POINT_EXCEL_PLAY: APJ_ID_EXCEL_PLAY,
        END_POINT_CERT_PLAY: APJ_ID_CERT_PLAY,
    }

    ####################
    # Stats Counter IDs
    ####################
    COUNTER_STATS_ID_MAPPING = {
        APJ_ID_AMENITY_PJ: 'f173817c110232e690615804a2fe4fe6975163db',
        APJ_ID_LOGIN: 'f48c06c2f0ba4c0b5288cda4359cb098271d712a',
        APJ_ID_ABOUT_US: '5344ba753f658c5fc34e0bb93f1ef7db9455ccab',
        APJ_ID_ASN1_PLAY: 'c28ad7357e9fa5df51ec1083a1efe5cd515df5ab',
        APJ_ID_TLV_PLAY: '66f375724d749e5e276c5d20017829690adc66f7',
        APJ_ID_QR_PLAY: 'e75f3460e58f2a32a1b7ab3ffab1b70e3466abe6',
        APJ_ID_EXCEL_PLAY: '6539579995b2458ab23fc5b6c4ceebd7c17a9b47',
        APJ_ID_CERT_PLAY: '5a8556bb1deb0161e2e8d4261fcc5c9cd190791a',
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
                f'{ConstSeo.TITLE_ASN1_PLAY} now supports GSMA SGP.32 v1.1 & v1.2 (GSMA_SGP_32_v1_1, GSMA_SGP_32_v1_2).',
                #
                f'{ConstSeo.TITLE_ASN1_PLAY} will auto trim the Quotation marks \"\" or \'\' if present.',
                #
                f'To convert any APDU in {ConstSeo.TITLE_ASN1_PLAY}, please trim the last 2 bytes of SW/Status Word (e.g: 9000).',
                #
            ],
        #
        APJ_ID_TLV_PLAY:
            [
                #
                f'{ConstSeo.TITLE_TLV_PLAY} now supports Base 64 data.',
                #
                f'if "Value In Ascii" is selected, {ConstSeo.TITLE_TLV_PLAY} converts hex data to ascii where ever possible.',
                #
                f'if "Non TLV Neighbor" is selected, {ConstSeo.TITLE_TLV_PLAY} will handle scenarios where non TLV data is '
                f'placed after TLV(s)',
                #
            ],
        #
        APJ_ID_QR_PLAY:
            [
                #
                f'if "Auto Split Qrs" is selected, {ConstSeo.TITLE_QR_PLAY} breaks data in multiple chunks if data does not '
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
                f'{ConstSeo.TITLE_CERT_PLAY} Automatically takes care of Open SSL format (-----BEGIN CERTIFICATE-----, '
                f'-----END CERTIFICATE-----).',
                #
            ],
    }

    @classmethod
    def print_versions(cls):
        """

        :return:
        """
        PhUtil.print_heading()
        PhUtil.print_version(ConfigConst_AmenityPj.TOOL_NAME, ConfigConst_AmenityPj.TOOL_VERSION)
        config_const_pool = [
            ConfigConst_Asn1Play,
            ConfigConst_TlvPlay,
            ConfigConst_QrPlay,
            ConfigConst_ExcelPlay,
            ConfigConst_CertPlay,
        ]
        for config_const in config_const_pool:
            PhUtil.print_version(config_const.TOOL_NAME, config_const.TOOL_VERSION, no_additional_info=True)
