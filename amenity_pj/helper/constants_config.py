from amenity_pj._git_info import GIT_SUMMARY
from amenity_pj._tool_name import TOOL_NAME
from amenity_pj._version import __version__


class ConfigConst:
    TOOL_VERSION = __version__.public()
    TOOL_VERSION_DETAILED = f'v{TOOL_VERSION}'
    TOOL_NAME = TOOL_NAME
    TOOL_TITLE = 'Amenity Pj'
    TOOL_GIT_SUMMARY = GIT_SUMMARY
