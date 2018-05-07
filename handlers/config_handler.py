import os
import configparser

from helpers import misc_helper


class ConfigHandler:
    def __init__(self):
        self.confparser = configparser.ConfigParser()
        self.misc = misc_helper.MiscHelper()
        self.config_location = os.path.expanduser("~/.config/ShareL/config.ini")

        if not os.path.isdir(self.config_location[0:-10]):
            os.mkdir(self.config_location[0:-10])
        if not os.path.isfile(self.config_location):
            print(
                "There was no configuration found, I made one in " + os.path.expanduser("~/.config/ShareL/config.ini") +
                " make sure to edit the configuration if you want to use SFTP or any other service that requires" +
                " authentication. Imgur and gfycat are already conifgured and use an anonymous client-id")
            self.init_config()
        elif os.path.isfile(self.config_location):
            self.config_file_exists()

        self.read_file = self.confparser.read(self.config_location)

    def init_config(self):
        self.confparser["general"] = {
            "copy_link_to_clipboard": True,
            "show_notification_on_upload_initiation": True,
            "show_notification_on_upload_completed": True,
            "output_location_to_stdout": True
        }

        self.confparser["SFTP"] = {
            "domain": "example.com",
            "username": "root(plsdont)",
            "password": "SuperSecretPassword",
            "port": "22",
            "use_pub_key_authentication": True,
            "remote_dir": "/var/www/example.com/files",
            "http_path": "http://example.com/files/",
            "notification_clipboard_content": "http_path"
        }

        self.confparser["imgur"] = {
            "client-id": "b0b233b63c847b4",
            "Username": "optional",
            "Password": "optional"
        }

        self.confparser["gfycat"] = {
            "client-id": "2_7_DzuB",
        }

        self.confparser["save"] = {
            "save_location": "/home/xxx/memes!",
        }

        with open(self.config_location, "w") as f:
            self.confparser.write(f)

    def does_section_exist(self, section):
        if self.confparser.has_section(section):
            return True
        else:
            return False

    def does_key_exist_in_section(self, section, key):
        if self.does_section_exist(section) and key in self.confparser[section].keys():
            return self.confparser[section][key]
        else:
            return False

    def get_section(self, section):
        if self.does_section_exist(section):
            return self.confparser[section]
        else:
            return False

    def get_key_value(self, section, key):
        if self.does_section_exist(section) and key in self.confparser[section].keys():
            return self.confparser[section][key]
        elif not self.does_section_exist(section):
            print("Section " + section + " does not exist.")
        elif not self.does_key_exist_in_section(section, key):
            print("Key " + key + " does not exist in section " + section)

    def set_key_value(self, section, key, value):
        # you'll be able to set settings in the config file in the future.
        pass

    # The key show_notification_on_upload setting is handled in main.py
    def apply_general_config_options(self, data):
        if bool(self.get_key_value("general", "copy_link_to_clipboard")):
            self.misc.copy_to_clipboard(data)

        if bool(self.get_key_value("general", "show_notification_on_upload_completed")):
            self.misc.send_notification(data)

        if bool(self.get_key_value("general", "output_location_to_stdout")):
            self.misc.send_stdout(data)

    def config_file_exists(self):
        pass
