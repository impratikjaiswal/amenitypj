from asn1_play.main.helper.constants_config import ConfigConst as asn1_play_config
from qr_play.main.helper.constants_config import ConfigConst as qr_play_config
from tlv_play.main.helper.constants_config import ConfigConst as tlv_play_config

from amenity_pj.helper.constants_config import ConfigConst as amenity_pj_config


class Const:
    DEPLOYMENT_DATE = '2023-11-11'
    URL_SITEMAP = '/sitemap.xml'
    TEMPLATE_WIP = 'wip.html'
    TEMPLATE_POST = 'post.html'

    GITHUB_URL_DEFAULT = 'https://impratikjaiswal.github.io'
    VERSION_DEFAULT = ''
    DESCRIPTION_DEFAULT = ''

    TITLE_AMENITY_PJ = amenity_pj_config.TOOL_TITLE
    DESCRIPTION_AMENITY_PJ = ('Amenity Pj offers a playground for various open source tools (amenities) such as ASN1 '
                              'Play, TLV Play, QR Play which are crafted with the purpose of enhancing productivity.')
    VERSION_AMENITY_PJ = f'v{amenity_pj_config.TOOL_VERSION}'
    END_POINT_AMENITY_PJ = 'index'
    URL_AMENITY_PJ = '/'
    TEMPLATE_AMENITY_PJ = 'index.html'
    GITHUB_URL_AMENITY_PJ = 'https://impratikjaiswal.github.io/amenitypj/'

    TITLE_ASN1_PLAY = 'ASN1 Play'
    DESCRIPTION_ASN1_PLAY = 'ASN1 Encoder & Decoder based on pycrate.'
    VERSION_ASN1_PLAY = f'v{asn1_play_config.TOOL_VERSION}'
    END_POINT_ASN1_PLAY = 'asn1_play'
    URL_ASN1_PLAY = '/asn1Play'
    TEMPLATE_ASN1_PLAY = 'asn1Play.html'
    GITHUB_URL_ASN1_PLAY = 'https://impratikjaiswal.github.io/asn1play/'

    TITLE_EXCEL_PLAY = 'Excel Play'
    DESCRIPTION_EXCEL_PLAY = 'Export one or more Excel file(s) with single or multiple sheets to several files each containing one sheet.'
    # VERSION_EXCEL_PLAY = f'v{excel_play_config.TOOL_VERSION}'
    VERSION_EXCEL_PLAY = VERSION_DEFAULT
    END_POINT_EXCEL_PLAY = 'excel_play'
    URL_EXCEL_PLAY = '/excelPlay'
    # TEMPLATE_EXCEL_PLAY = 'excelPlay.html'
    TEMPLATE_EXCEL_PLAY = TEMPLATE_WIP
    GITHUB_URL_EXCEL_PLAY = 'https://impratikjaiswal.github.io/excelPlay/'

    TITLE_TLV_PLAY = 'TLV Play'
    DESCRIPTION_TLV_PLAY = 'Generic TLV Parser. Will parse any TLV upto nth Level.'
    VERSION_TLV_PLAY = f'v{tlv_play_config.TOOL_VERSION}'
    END_POINT_TLV_PLAY = 'tlv_play'
    URL_TLV_PLAY = '/tlvPlay'
    TEMPLATE_TLV_PLAY = 'tlvPlay.html'
    GITHUB_URL_TLV_PLAY = 'https://impratikjaiswal.github.io/tlvPlay/'

    TITLE_QR_PLAY = 'QR Play'
    DESCRIPTION_QR_PLAY = 'Qr Code Generator based on Segno. Can Generate Single as well as Multiple Qr codes.'
    VERSION_QR_PLAY = f'v{qr_play_config.TOOL_VERSION}'
    END_POINT_QR_PLAY = 'qr_play'
    URL_QR_PLAY = '/qrPlay'
    TEMPLATE_QR_PLAY = 'qrPlay.html'
    GITHUB_URL_QR_PLAY = 'https://impratikjaiswal.github.io/qrPlay/'

    TITLE_TESTIMONIALS = 'Testimonials'
    DESCRIPTION_TESTIMONIALS = 'Read What others feel about us'
    VERSION_TESTIMONIALS = VERSION_DEFAULT
    END_POINT_TESTIMONIALS = 'testimonials'
    URL_TESTIMONIALS = '/testimonials'
    TEMPLATE_TESTIMONIALS = 'testimonials.html'
    GITHUB_URL_TESTIMONIALS = GITHUB_URL_DEFAULT

    TITLE_ABOUT_US = 'About Us'
    DESCRIPTION_ABOUT_US = ('As the word Amenity refers to an additional feature or service that elevates convenience '
                            'and comfort. Amenity Pj also intends to offer some day to day tools which can elevates '
                            'productivity.')

    VERSION_ABOUT_US = VERSION_DEFAULT
    END_POINT_ABOUT_US = 'about_us'
    URL_ABOUT_US = '/aboutUs'
    TEMPLATE_ABOUT_US = 'aboutus.html'
    GITHUB_URL_ABOUT_US = GITHUB_URL_DEFAULT

    TITLE_SPONSORSHIP = 'Sponsorship'
    DESCRIPTION_SPONSORSHIP = DESCRIPTION_DEFAULT
    VERSION_SPONSORSHIP = VERSION_DEFAULT
    END_POINT_SPONSORSHIP = 'sponsorship'
    URL_SPONSORSHIP = '/sponsorship'
    TEMPLATE_SPONSORSHIP = TEMPLATE_WIP
    GITHUB_URL_SPONSORSHIP = GITHUB_URL_DEFAULT

    END_POINT_AND_TITLE_MAPPING = {
        END_POINT_AMENITY_PJ: TITLE_AMENITY_PJ,
        END_POINT_TESTIMONIALS: TITLE_TESTIMONIALS,
        END_POINT_ABOUT_US: TITLE_ABOUT_US,
        END_POINT_SPONSORSHIP: TITLE_SPONSORSHIP,
        END_POINT_EXCEL_PLAY: TITLE_EXCEL_PLAY,
        END_POINT_ASN1_PLAY: TITLE_ASN1_PLAY,
        END_POINT_TLV_PLAY: TITLE_TLV_PLAY,
        END_POINT_QR_PLAY: TITLE_QR_PLAY,
    }
