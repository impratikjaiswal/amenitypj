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
    APP_DESCRIPTION_AMENITY_PJ = f'{TITLE_AMENITY_PJ} is a collection of FREE & Open Source Apps. This extended family offers various playgrounds which are nurtured to enhance users\'s day to day productivity.'
    APP_META_DESCRIPTION_AMENITY_PJ = f'{TITLE_AMENITY_PJ} is a collection of FREE & Open Source Apps including asn1Play, tlvPlay, qrPlay, excelPlay, certPlay.'
    APP_META_KEYWORDS_AMENITY_PJ = f'ASN1 Play, TLV Play, QR Play, Excel Play, Cert Play, asn1Play, tlvPlay, qrPlay, excelPlay, certPlay'

    APP_DESCRIPTION_ASN1_PLAY = f'ASN.1 Encoder, Decoder & validator. Supports various versions of GSMA SGP.22, GSMA SGP.32, TCA eUICC Profile Package (SAIP) specifications along with their inherited specs.'
    APP_META_DESCRIPTION_ASN1_PLAY = f'{APP_DESCRIPTION_ASN1_PLAY} Supports large variety of encoding-decoding rules (DER, JER, JSON, BER, CER, APER, COER, OER, UPER etc).'
    APP_META_KEYWORDS_ASN1_PLAY = f'ASN.1, ASN1, ASN, ASN 1, ASN1 der, Abstract Syntax Notation One, GSMA, TCA, SGP22, SGP.22, SGP32, SGP.32, asn1 encoder, asn1 decoder, asn1 validator,'

    APP_DESCRIPTION_TLV_PLAY = f'Generic TLV Parser based on TLV and related standards. Can parse any Simple or BER TLV upto *nth Level* automatically. Multi byte Tag, Multi byte Length are also Supported.'
    APP_META_DESCRIPTION_TLV_PLAY = APP_DESCRIPTION_TLV_PLAY
    APP_META_KEYWORDS_TLV_PLAY = f'TLV, Tag Length Value, Type Length Value, length value, tlv encoder, tlv decoder, multi byte tag, multi byte length, simple tlv, ber tlv'

    APP_DESCRIPTION_QR_PLAY = f'Qr Code Generator. Multiple Qr codes can be generated automatically when input text does not fit in one.'
    APP_META_DESCRIPTION_QR_PLAY = APP_DESCRIPTION_QR_PLAY
    APP_META_KEYWORDS_QR_PLAY = f'qr, qr code, qr code generator, quick response code, qrcode generator, qrcode, multiple qrcode generator, multiple qr code generator'

    APP_DESCRIPTION_EXCEL_PLAY = f'Split Microsoft Excel file to individual CSV file(s) containing one sheet per file. Multiple input files can be fed in one shot.'
    APP_META_DESCRIPTION_EXCEL_PLAY = APP_DESCRIPTION_EXCEL_PLAY
    APP_META_KEYWORDS_EXCEL_PLAY = f'excel, microsoft excel, excel export,excel export csv, xlsx, xls, csv, comma seperated values'

    APP_DESCRIPTION_CERT_PLAY = f'Generic Certificate Parser based on X.509 and related standards. Can fetch (& parse) TLS certificate of any live website.'
    APP_META_DESCRIPTION_CERT_PLAY = APP_DESCRIPTION_CERT_PLAY
    APP_META_KEYWORDS_CERT_PLAY = f'certificate parser, cert, certificate, tls, transport layer security, tls certificate, ssl, x509, ssl certificate, openssl'

    APP_DESCRIPTION_ABOUT_US = f'As the word AMENITY refers to an additional feature or service that elevates convenience and comfort. {TITLE_AMENITY_PJ} also intends to offer various day to day tools which are crafted with the purpose to enhance productivity.'
    APP_META_DESCRIPTION_ABOUT_US = APP_DESCRIPTION_ABOUT_US
    APP_META_KEYWORDS_ABOUT_US = f'{TITLE_AMENITY_PJ}'

    APP_DESCRIPTION_LOGIN = '!!! Currently only Admin Login is supported !!!'
    APP_META_DESCRIPTION_LOGIN = APP_DESCRIPTION_ABOUT_US
    APP_META_KEYWORDS_LOGIN = f'{TITLE_AMENITY_PJ}'
