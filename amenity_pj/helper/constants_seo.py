from asn1_play.main.helper.constants_config import ConfigConst as ConfigConst_Asn1Play
from cert_play.main.helper.constants_config import ConfigConst as ConfigConst_CertPlay
from data_play.main.helper.constants_config import ConfigConst as ConfigConst_DataPlay
from excel_play.main.helper.constants_config import ConfigConst as ConfigConst_ExcelPlay
from qr_play.main.helper.constants_config import ConfigConst as ConfigConst_QrPlay
from tlv_play.main.helper.constants_config import ConfigConst as ConfigConst_TlvPlay

from amenity_pj.helper.constants_config import ConfigConst as ConfigConst_AmenityPj
from amenity_pj.helper.defaults import Defaults


class ConstSeo:
    """

    """
    ####################
    # Deployment Dates
    ####################
    DEPLOYMENT_DATE = '2023-11-11'
    LAST_MODIFY_DATE_INDEX = '2024-11-01'
    LAST_MODIFY_DATE_ASN1_PLAY = '2024-11-01'
    LAST_MODIFY_DATE_TLV_PLAY = '2024-11-01'
    LAST_MODIFY_DATE_QR_PLAY = '2024-11-01'
    LAST_MODIFY_DATE_EXCEL_PLAY = '2024-11-01'
    LAST_MODIFY_DATE_CERT_PLAY = '2024-11-01'
    LAST_MODIFY_DATE_DATA_PLAY = '2024-11-01'
    LAST_MODIFY_DATE_ABOUT_US = '2024-11-01'
    LAST_MODIFY_DATE_LOGIN = '2024-11-01'

    ####################
    # Titles
    ####################
    TITLE_AMENITY_PJ = ConfigConst_AmenityPj.TOOL_TITLE
    TITLE_ASN1_PLAY = ConfigConst_Asn1Play.TOOL_TITLE
    TITLE_TLV_PLAY = ConfigConst_TlvPlay.TOOL_TITLE
    TITLE_QR_PLAY = ConfigConst_QrPlay.TOOL_TITLE
    TITLE_EXCEL_PLAY = ConfigConst_ExcelPlay.TOOL_TITLE
    TITLE_CERT_PLAY = ConfigConst_CertPlay.TOOL_TITLE
    # TITLE_DATA_PLAY = ConfigConst_DataPlay.TOOL_TITLE
    TITLE_DATA_PLAY = None
    TITLE_ABOUT_US = 'About US'
    TITLE_LOGIN = 'Login'
    TITLE_CREDITS = 'Credits'
    TITLE_SPONSORSHIP = 'Sponsorship'
    TITLE_TESTIMONIALS = 'Testimonials'

    ####################
    # Author
    ####################
    APP_META_AUTHOR = TITLE_AMENITY_PJ

    ####################
    # Descriptions, Keywords
    ####################
    APP_DESCRIPTION_AMENITY_PJ = f'{TITLE_AMENITY_PJ} is a collection of FREE & Open Source Apps. This extended family offers various playgrounds which are nurtured to enhance users\'s day to day productivity.'
    APP_META_DESCRIPTION_AMENITY_PJ = f'{TITLE_AMENITY_PJ} is a collection of FREE & Open Source Apps including asn1Play, tlvPlay, qrPlay, excelPlay, certPlay, dataPlay.'
    APP_META_KEYWORDS_AMENITY_PJ = f'{TITLE_AMENITY_PJ}, {TITLE_ASN1_PLAY}, {TITLE_TLV_PLAY}, {TITLE_QR_PLAY}, {TITLE_EXCEL_PLAY}, {TITLE_CERT_PLAY}, {TITLE_DATA_PLAY}, amenityPj, asn1Play, tlvPlay, qrPlay, excelPlay, certPlay, dataPlay'

    APP_DESCRIPTION_ASN1_PLAY = ConfigConst_Asn1Play.TOOL_DESCRIPTION
    APP_META_DESCRIPTION_ASN1_PLAY = ConfigConst_Asn1Play.TOOL_META_DESCRIPTION
    APP_META_KEYWORDS_ASN1_PLAY = ConfigConst_Asn1Play.TOOL_META_KEYWORDS

    APP_DESCRIPTION_TLV_PLAY = ConfigConst_TlvPlay.TOOL_DESCRIPTION
    APP_META_DESCRIPTION_TLV_PLAY = ConfigConst_TlvPlay.TOOL_META_DESCRIPTION
    APP_META_KEYWORDS_TLV_PLAY = ConfigConst_TlvPlay.TOOL_META_KEYWORDS

    APP_DESCRIPTION_QR_PLAY = ConfigConst_QrPlay.TOOL_DESCRIPTION
    APP_META_DESCRIPTION_QR_PLAY = ConfigConst_QrPlay.TOOL_META_DESCRIPTION
    APP_META_KEYWORDS_QR_PLAY = ConfigConst_QrPlay.TOOL_META_KEYWORDS

    APP_DESCRIPTION_EXCEL_PLAY = ConfigConst_ExcelPlay.TOOL_DESCRIPTION
    APP_META_DESCRIPTION_EXCEL_PLAY = ConfigConst_ExcelPlay.TOOL_META_DESCRIPTION
    APP_META_KEYWORDS_EXCEL_PLAY = ConfigConst_ExcelPlay.TOOL_META_KEYWORDS

    APP_DESCRIPTION_CERT_PLAY = ConfigConst_ExcelPlay.TOOL_DESCRIPTION
    APP_META_DESCRIPTION_CERT_PLAY = ConfigConst_ExcelPlay.TOOL_META_DESCRIPTION
    APP_META_KEYWORDS_CERT_PLAY = ConfigConst_ExcelPlay.TOOL_META_KEYWORDS

    APP_DESCRIPTION_DATA_PLAY = ConfigConst_ExcelPlay.TOOL_DESCRIPTION
    APP_META_DESCRIPTION_DATA_PLAY = ConfigConst_ExcelPlay.TOOL_META_DESCRIPTION
    APP_META_KEYWORDS_DATA_PLAY = ConfigConst_ExcelPlay.TOOL_META_KEYWORDS

    APP_DESCRIPTION_ABOUT_US = f'As the word AMENITY refers to an additional feature or service that elevates convenience and comfort. {TITLE_AMENITY_PJ} also intends to offer various day to day tools which are crafted with the purpose to enhance productivity.'
    APP_META_DESCRIPTION_ABOUT_US = APP_DESCRIPTION_ABOUT_US
    APP_META_KEYWORDS_ABOUT_US = f'{TITLE_ABOUT_US}, {TITLE_AMENITY_PJ}'

    APP_DESCRIPTION_LOGIN = '!!! Currently only Admin Login is supported !!!'
    APP_META_DESCRIPTION_LOGIN = APP_DESCRIPTION_LOGIN
    APP_META_KEYWORDS_LOGIN = f'{TITLE_LOGIN}, {TITLE_AMENITY_PJ}'

    APP_DESCRIPTION_CREDITS = f'{TITLE_AMENITY_PJ} is Thankful to its day to day users, feedback providers (online as well as offline), validators, 3rd Party products. Couple of names are: '
    APP_META_DESCRIPTION_CREDITS = APP_DESCRIPTION_CREDITS
    APP_META_KEYWORDS_CREDITS = f'{TITLE_CREDITS}, {TITLE_AMENITY_PJ}'

    APP_DESCRIPTION_SPONSORSHIP = Defaults.DESCRIPTION
    APP_META_DESCRIPTION_SPONSORSHIP = APP_DESCRIPTION_SPONSORSHIP
    APP_META_KEYWORDS_SPONSORSHIP = f'{TITLE_SPONSORSHIP}, {TITLE_AMENITY_PJ}'

    APP_DESCRIPTION_TESTIMONIALS = 'Read What others feel about us'
    APP_META_DESCRIPTION_TESTIMONIALS = APP_DESCRIPTION_TESTIMONIALS
    APP_META_KEYWORDS_TESTIMONIALS = f'{TITLE_TESTIMONIALS}, {TITLE_AMENITY_PJ}'
