from python_helpers.ph_keys import PhKeys


class AppSettings:
    def __init__(self, settings=None):
        if settings is None:
            self.initiate_settings()
            self.set_default_settings()
        else:
            self.settings = settings

    def set_default_settings(self):
        self.settings.update({PhKeys.CFG_HIGHLIGHT_SYNTAX: False})
        self.settings.update({PhKeys.CFG_HIGHLIGHT_SYNTAX_LANGUAGE: 'javascript'})
        self.settings.update({PhKeys.CFG_HIGHLIGHT_SYNTAX_STYLE: 'tokyo-night-dark'})
        self.settings.update({PhKeys.CFG_COUNTERS_STATS: True})
        self.settings.update({PhKeys.CFG_COUNTERS_STATS_FORMAT: '1232638/t/2'})

    def get_setting(self):
        return self.settings

    def set_setting(self, key, value):
        if key in self.settings.keys():
            self.settings[key] = value
        else:
            self.settings.update({key: value})

    def initiate_settings(self):
        self.settings = dict()
