from amenity_pj.helper.constants_config import ConfigConst as ConfigConst_AmenityPj


class ConstSeo:
    """

    """
    ####################
    # Deployment Dates
    ####################
    DEPLOYMENT_DATE = '2023-11-11'
    LAST_MODIFY_DATE_INDEX = '2024-09-08'
    LAST_MODIFY_DATE_ASN1_PLAY = '2024-09-08'
    LAST_MODIFY_DATE_TLV_PLAY = '2024-09-08'
    LAST_MODIFY_DATE_QR_PLAY = '2024-09-08'
    LAST_MODIFY_DATE_EXCEL_PLAY = '2024-09-08'
    LAST_MODIFY_DATE_CERT_PLAY = '2024-09-08'
    LAST_MODIFY_DATE_ABOUT_US = '2024-09-08'
    LAST_MODIFY_DATE_LOGIN = '2024-09-08'

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
    TITLE_ABOUT_US = 'About US'
    TITLE_LOGIN = 'Login'

    ####################
    # Author
    ####################
    APP_META_AUTHOR = TITLE_AMENITY_PJ

    ####################
    # Descriptions, Keywords
    ####################
    APP_META_AUTHOR = TITLE_AMENITY_PJ

    APP_DESCRIPTION_AMENITY_PJ = f'{TITLE_AMENITY_PJ} is a family of various Apps & Tools (amenities) where FREE (& Open Source) playgrounds are offered. This extended family is a collection of various tools such as ASN1 Play, TLV Play, QR Play, Cert Play, Excel Play; Which are crafted with the purpose of enhancing day to day productivity.',
    APP_META_DESCRIPTION_AMENITY_PJ = APP_DESCRIPTION_AMENITY_PJ
    APP_META_KEYWORDS_AMENITY_PJ = f''

    APP_DESCRIPTION_ASN1_PLAY = f'ASN1 Encoder & Decoder based on pycrate.'
    APP_META_DESCRIPTION_ASN1_PLAY = f'ASN.1 encoder, decoder and data validator. Supports GSMA complete ASN.1 and a big variety of encoding rules (BER, DER, PER, UPER, OER, COER, JSON, XML).'
    APP_META_KEYWORDS_ASN1_PLAY = f'ASN.1, ASN1, Converter, Encoder, Decoder '

    APP_DESCRIPTION_TLV_PLAY = f'Generic TLV Parser. Will parse any TLV upto nth Level.'
    APP_META_DESCRIPTION_TLV_PLAY = APP_DESCRIPTION_TLV_PLAY
    APP_META_KEYWORDS_TLV_PLAY = f''

    APP_DESCRIPTION_QR_PLAY = f'Qr Code Generator based on Segno. Can Generate Single as well as Multiple Qr codes.',
    APP_META_DESCRIPTION_QR_PLAY = APP_DESCRIPTION_QR_PLAY
    APP_META_KEYWORDS_QR_PLAY = f''

    APP_DESCRIPTION_EXCEL_PLAY = f'Export one or more Excel file(s) (with single or multiple sheets) to several csv files each containing one sheet.',
    APP_META_DESCRIPTION_EXCEL_PLAY = APP_DESCRIPTION_EXCEL_PLAY
    APP_META_KEYWORDS_EXCEL_PLAY = f''

    APP_DESCRIPTION_CERT_PLAY = f'OpenSSL based Cert Parser. Will parse any TLS cert.'
    APP_META_DESCRIPTION_CERT_PLAY = APP_DESCRIPTION_CERT_PLAY
    APP_META_KEYWORDS_CERT_PLAY = f''

    APP_DESCRIPTION_ABOUT_US = f'As the word Amenity refers to an additional feature or service that elevates convenience and comfort. {TITLE_AMENITY_PJ} also intends to offer various day to day tools which may elevates productivity.'
    APP_META_DESCRIPTION_ABOUT_US = APP_DESCRIPTION_ABOUT_US
    APP_META_KEYWORDS_ABOUT_US = f''

    APP_DESCRIPTION_LOGIN = '!!! Currently only Admin Login is supported !!!'
    APP_META_DESCRIPTION_LOGIN = APP_DESCRIPTION_LOGIN
    APP_META_KEYWORDS_LOGIN = f''
