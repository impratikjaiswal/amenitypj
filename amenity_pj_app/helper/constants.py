from amenity_pj_app.helper.constants_config import ConfigConst


class Const:
    END_POINT_INDEX = 'index'
    URL_INDEX = '/'
    TEMPLATE_INDEX = 'index.html'

    TITLE_TESTIMONIALS = 'Testimonials'
    END_POINT_TESTIMONIALS = 'testimonials'
    URL_TESTIMONIALS = '/testimonials'
    TEMPLATE_TESTIMONIALS = 'testimonials.html'

    TITLE_ABOUT_US = 'About Us'
    END_POINT_ABOUT_US = 'about_us'
    URL_ABOUT_US = '/aboutUs'
    TEMPLATE_ABOUT_US = 'aboutus.html'

    TEMPLATE_WIP = 'wip.html'
    TEMPLATE_POST = 'post.html'

    TITLE_SPONSORSHIP = 'Sponsorship'
    END_POINT_SPONSORSHIP = 'sponsorship'
    URL_SPONSORSHIP = '/sponsorship'

    GITHUB_URL_DEFAULT = 'https://impratikjaiswal.github.io'
    VERSION_DEFAULT = ''

    TITLE_EXCEL_PLAY = 'Excel Play'
    END_POINT_EXCEL_PLAY = 'excel_play'
    URL_EXCEL_PLAY = '/excelPlay'
    TEMPLATE_EXCEL_PLAY = 'excelPlay.html'
    GITHUB_URL_EXCEL_PLAY = 'https://impratikjaiswal.github.io/excelPlay/'

    TITLE_ASN1_PLAY = 'ASN1 Play'
    END_POINT_ASN1_PLAY = 'asn1_play'
    URL_ASN1_PLAY = '/asn1Play'
    TEMPLATE_ASN1_PLAY = 'asn1Play.html'
    GITHUB_URL_ASN1_PLAY = 'https://impratikjaiswal.github.io/asn1play/'

    TITLE_TLV_PLAY = 'TLV Play'
    END_POINT_TLV_PLAY = 'tlv_play'
    URL_TLV_PLAY = '/tlvPlay'
    TEMPLATE_TLV_PLAY = 'tlvPlay.html'
    GITHUB_URL_TLV_PLAY = 'https://impratikjaiswal.github.io/tlvPlay/'

    TITLE_QR_PLAY = 'QR Play'
    END_POINT_QR_PLAY = 'qr_play'
    URL_QR_PLAY = '/qrPlay'
    TEMPLATE_QR_PLAY = 'qrPlay.html'
    GITHUB_URL_QR_PLAY = 'https://impratikjaiswal.github.io/qrPlay/'

    END_POINT_AND_TITLE_MAPPING = {
        END_POINT_INDEX : ConfigConst.TOOL_TITLE,
        END_POINT_TESTIMONIALS: TITLE_TESTIMONIALS,
        END_POINT_ABOUT_US: TITLE_ABOUT_US,
        END_POINT_SPONSORSHIP: TITLE_SPONSORSHIP,
        END_POINT_EXCEL_PLAY: TITLE_EXCEL_PLAY,
        END_POINT_ASN1_PLAY: TITLE_ASN1_PLAY,
        END_POINT_TLV_PLAY: TITLE_TLV_PLAY,
        END_POINT_QR_PLAY: TITLE_QR_PLAY,
    }