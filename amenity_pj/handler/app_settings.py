class AppSettings:
    def __init__(self, settings=None):
        if settings is None:
            self.initiate_settings()
            self.set_default_settings()
        else:
            self.settings = settings

    def set_default_settings(self):
        self.settings.update({'setting_highlight_js': True})
        self.settings.update({'setting_stats_counter': True})

    def get_setting(self):
        return self.settings

    def set_setting(self, key, value):
        if key in self.settings.keys():
            self.settings[key] = value
        else:
            self.settings.update({key: value})

    def initiate_settings(self):
        self.settings = dict()
