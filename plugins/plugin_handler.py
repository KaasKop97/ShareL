from plugins.SFTP import Sftp


class PluginHandler:
    def __init__(self):
        self.plugins = [Sftp()]
