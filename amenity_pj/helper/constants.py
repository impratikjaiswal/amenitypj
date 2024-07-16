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
    APJ_ID_TESTIMONIALS = 20
    APJ_ID_TESTIMONIALS_ID = 21
    APJ_ID_ABOUT_US = 30
    APJ_ID_CREDITS = 40
    APJ_ID_SPONSORSHIP = 50
    APJ_ID_SITEMAP = 60
    APJ_ID_SERVER_DETAILS = 70
    APJ_ID_404 = 80
    APJ_ID_ASN1_PLAY = 200
    APJ_ID_ASN1_PLAY_ASN1_OBJECTS = 201
    APJ_ID_TLV_PLAY = 210
    APJ_ID_QR_PLAY = 220
    APJ_ID_EXCEL_PLAY = 230
    APJ_ID_CERT_PLAY = 240

    ####################
    # END_POINTS
    ####################
    END_POINT_AMENITY_PJ = 'index'
    END_POINT_LOGIN = 'login'
    END_POINT_TESTIMONIALS = 'testimonials'
    END_POINT_ABOUT_US = 'about_us'
    END_POINT_CREDITS = 'credits_'
    END_POINT_SPONSORSHIP = 'sponsorship'
    END_POINT_ASN1_PLAY = 'asn1_play'
    END_POINT_TLV_PLAY = 'tlv_play'
    END_POINT_QR_PLAY = 'qr_play'
    END_POINT_EXCEL_PLAY = 'excel_play'
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
    # Common or without end points Constants
    ####################
    TITLE_AMENITY_PJ = ConfigConst_AmenityPj.TOOL_TITLE
    VERSION_AMENITY_PJ = ConfigConst_AmenityPj.TOOL_VERSION_DETAILED
    TEMPLATE_WIP = 'wip.html'

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

    APPS_LIST = [
        APJ_ID_ASN1_PLAY,
        APJ_ID_TLV_PLAY,
        APJ_ID_QR_PLAY,
        APJ_ID_EXCEL_PLAY,
        APJ_ID_CERT_PLAY,
    ]

    WHATS_NEW_LIST = [
        APJ_ID_AMENITY_PJ,
        APJ_ID_ASN1_PLAY,
        APJ_ID_TLV_PLAY,
    ]

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
                PhKeys.APP_END_POINT: END_POINT_ABOUT_US,
            },
        #
        APJ_ID_CREDITS:
            {
                PhKeys.APP_TITLE: 'Credits',
                PhKeys.APP_DESCRIPTION: f'{TITLE_AMENITY_PJ} is Thankful to: ',
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
        APJ_ID_ASN1_PLAY:
            {
                PhKeys.APP_TITLE_PRE: Defaults.APP_WELCOME,
                PhKeys.APP_TITLE: 'ASN1 Play',
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
            },
        #
        APJ_ID_TLV_PLAY:
            {
                PhKeys.APP_TITLE_PRE: Defaults.APP_WELCOME,
                PhKeys.APP_TITLE: 'TLV Play',
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
                PhKeys.APP_TITLE: 'QR Play',
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
                # PhKeys.APP_TITLE_PRE: Defaults.APP_WELCOME,
                PhKeys.APP_TITLE: 'Excel Play',
                PhKeys.APP_VERSION: ConfigConst_ExcelPlay.TOOL_VERSION_DETAILED,
                PhKeys.APP_DESCRIPTION: 'Export one or more Excel file(s) with single or multiple sheets to several files each containing one sheet.',
                PhKeys.APP_GITHUB_URL: 'excelPlay',
                PhKeys.APP_GIT_SUMMARY: ConfigConst_ExcelPlay.TOOL_GIT_SUMMARY,
                PhKeys.APP_URL: '/excelPlay',
                PhKeys.APP_URL_API: '/api/excelPlay',
                # PhKeys.APP_TEMPLATE:  'excelPlay.html',
                PhKeys.APP_TEMPLATE: TEMPLATE_WIP,
                PhKeys.APP_DESCRIPTION_LEVEL_2: Defaults.DESCRIPTION_WIP,
                PhKeys.APP_END_POINT: END_POINT_EXCEL_PLAY,
            },
        #
        APJ_ID_CERT_PLAY:
            {
                PhKeys.APP_TITLE_PRE: Defaults.APP_WELCOME,
                PhKeys.APP_TITLE: 'Cert Play',
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
        END_POINT_TLV_PLAY: APJ_ID_TLV_PLAY,
        END_POINT_QR_PLAY: APJ_ID_QR_PLAY,
        END_POINT_EXCEL_PLAY: APJ_ID_EXCEL_PLAY,
        END_POINT_CERT_PLAY: APJ_ID_CERT_PLAY,
    }
