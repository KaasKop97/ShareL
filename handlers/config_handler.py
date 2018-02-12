import os
import configparser

from helpers import misc_helper


class ConfigHandler:
    def __init__(self):
        self.confparser = configparser.ConfigParser()
        self.misc = misc_helper.MiscHelper()
        self.config_location = os.path.join(os.environ["HOME"], ".config/ShareL/config.ini")

        if not os.path.isdir(self.config_location[0:-10]):
            os.mkdir(self.config_location[0:-10])
        if not os.path.isfile(self.config_location):
            self.init_config()

        self.read_file = self.confparser.read(self.config_location)

    def init_config(self):
        self.confparser["general"] = {
            "copy_link_to_clipboard": True,
            "show_notification_on_upload": True
        }

        self.confparser["SFTP"] = {
            "domain": "example.com",
            "username": "root",
            "password": "SuperSecretPassword",
            "port": "22",
            "use_pub_key_authentication": True,
            "remote_dir": "/var/www/example.com/files",
            "http_path": "http://example.com/files/",
            "notification_clipboard_content": "http_path"
        }

        self.confparser["imgur"] = {
            "client-id": "your client-id. Get it from the imgur site.",
            "Username": "optional",
            "Password": "optional"
        }

        with open(self.config_location, "w") as f:
            self.confparser.write(f)

    def does_section_exist(self, section):
        if self.confparser.has_section(section):
            return True

    def does_key_exist_in_section(self, section, key):
        if self.does_section_exist(section) and key in self.confparser[section].keys():
            return self.confparser[section][key]

    def get_section(self, section):
        if self.does_section_exist(section):
            return self.confparser[section]

    def get_key_value(self, section, key):
        if self.does_section_exist(section) and key in self.confparser[section].keys():
            return self.confparser[section][key]
        elif self.does_section_exist(section):
            print("Section does not exist.")
        elif self.does_key_exist_in_section(section, key):
            print("Key does not exist in section " + section)

    def set_key_value(self, section, key, value):
        # you'll be able to set settings in the config file in the future.
        pass

    def apply_general_config_options(self, data):
        if bool(self.get_key_value("general", "copy_link_to_clipboard")):
            self.misc.copy_to_clipboard(data)

        if bool(self.get_key_value("general", "send_notification_on_upload")):
            self.misc.send_notification(data)
