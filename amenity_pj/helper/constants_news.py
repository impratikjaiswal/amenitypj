####################
# News Data All
####################
from python_helpers.ph_keys import PhKeys

from amenity_pj.helper.constants import Const
from amenity_pj.helper.constants_seo import ConstSeo


class ConstNews:
    NEWS_DATA_MAPPING = {
        #
        Const.APJ_ID_NEWS_COMMON:
            [
                #
                # f'{PhKeys.APP_TITLE} now supports "Copy Input Data", "Copy Output Data" & "Copy Info".',
                #
                f'{PhKeys.APP_TITLE} is now equipped with essential copy/paste functionality. '
                f'Try "Copy" icon available with various field(s).',
                #
                # f'{PhKeys.APP_TITLE} now supports "Download Input Data", "Download Output Data" and "Download Info".'
                #
                f'{PhKeys.APP_TITLE} is now equipped with essential download functionality. '
                f'Try "Download" icon available with various field(s).',
                #
                # f'{PhKeys.APP_TITLE} now supports "Upload Input Data".'
                #
                f'{PhKeys.APP_TITLE} is now equipped with essential upload functionality. '
                f'Try "Upload" icon available with Input Data field.'
                #
                f'Checkout our new offering {ConstSeo.TITLE_DATA_PLAY}".'
            ],
        #
        Const.APJ_ID_ASN1_PLAY:
            [
                #
                f'{ConstSeo.TITLE_ASN1_PLAY} now supports GSMA SGP.32 v1.1 & v1.2 (GSMA_SGP_32_v1_1, GSMA_SGP_32_v1_2).',
                #
                f'{ConstSeo.TITLE_ASN1_PLAY} now supports GSMA SGP.22 v2.6 (GSMA_SGP_22_v2_6).',
                #
                f'{ConstSeo.TITLE_ASN1_PLAY} will auto trim the Quotation marks \"\" or \'\' if present.',
                #
                f'To convert any APDU in {ConstSeo.TITLE_ASN1_PLAY}, please trim the last 2 bytes of SW/Status Word (e.g: 9000).',
                #
            ],
        #
        Const.APJ_ID_TLV_PLAY:
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
        Const.APJ_ID_QR_PLAY:
            [
                #
                f'if "Auto Split Qrs" is selected, {ConstSeo.TITLE_QR_PLAY} breaks data in multiple chunks if data does not '
                f'fit in one QR.',
                #
            ],
        #
        Const.APJ_ID_EXCEL_PLAY:
            [
                #
                f'{ConstSeo.TITLE_EXCEL_PLAY} now supports various encoding Formats.',
                #
            ],
        #
        Const.APJ_ID_CERT_PLAY:
            [
                #
                f'{ConstSeo.TITLE_CERT_PLAY} Automatically takes care of Open SSL format (-----BEGIN CERTIFICATE-----, '
                f'-----END CERTIFICATE-----).',
                #
                f'Now {ConstSeo.TITLE_CERT_PLAY} can fetch "All Certs" (Full Certificate Chain) for a URL',
                #
                f'{ConstSeo.TITLE_CERT_PLAY}, Support "Fetch only" (Don\'t Parse) for a URL',
                #
            ],
        #
        Const.APJ_ID_DATA_PLAY:
            [
                #
                f'{ConstSeo.TITLE_DATA_PLAY} now supports various encoding Formats.',
                #
            ],
        #
    }
