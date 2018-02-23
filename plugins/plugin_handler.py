import plugins.SFTP, plugins.imgur
from handlers import config_handler


class PluginHandler:
    def __init__(self, service):
        self.conf_handler = config_handler.ConfigHandler()
        self.plugin_list = ["sftp", "imgur"]

        if service.lower() in self.plugin_list:
            if service.lower() == self.plugin_list[0]:
                self.plugin = plugins.SFTP.Sftp()
                self.plugin.connect()
            elif service.lower() == self.plugin_list[1]:
                self.plugin = plugins.imgur.Imgur()

    def handle_upload(self, file):
        upload = self.plugin.upload(file)
        if upload[0]:
            print("Welp its there")
            self.conf_handler.apply_general_config_options(upload[1])
        else:
            print(upload[1])
