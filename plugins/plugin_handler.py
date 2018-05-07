import plugins.SFTP, plugins.imgur, plugins.save, plugins.ipfs
from handlers import config_handler
import json


class PluginHandler:
    def __init__(self, service):
        self.conf_handler = config_handler.ConfigHandler()
        self.plugin_list = ["sftp", "imgur", "save", "ipfs"]

        if service.lower() in self.plugin_list:
            if service.lower() == self.plugin_list[0]:
                self.plugin = plugins.SFTP.Sftp()
                self.plugin.connect()
            elif service.lower() == self.plugin_list[1]:
                self.plugin = plugins.imgur.Imgur()
            elif service.lower() == self.plugin_list[2]:
                self.plugin = plugins.save.Save()
            elif service.lower() == self.plugin_list[3]:
                self.plugin = plugins.ipfs.Ipfs()

    def handle_upload_json(self, file):
        upload = self.plugin.upload(file)
        if upload[0]:
            self.conf_handler.apply_general_config_options(json.loads(upload[1].content)["data"]["link"])
        else:
            print(json.loads(upload[1].content))

    def handle_upload(self, file):
        upload = self.plugin.upload(file)
        if upload[0]:
            self.conf_handler.apply_general_config_options(upload[1])
        else:
            print(upload[1])
