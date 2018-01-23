import os
import configparser


class ConfigHandler:
    def __init__(self):
        self.confparser = configparser.ConfigParser()
        self.config_location = os.path.join(os.environ["HOME"], ".config/ShareL/config.ini")
        if not os.path.isdir(self.config_location[0:-10]):
            os.mkdir(self.config_location[0:-10])
        if not os.path.isfile(self.config_location):
            self.init_config()

    def init_config(self):
        self.confparser["general"] = {
            "copy_link_to_clipboard": True,
            "save_file_locally": True,
            "show_notification_on_upload": True
        }
        self.confparser["SFTP"] = {
            "domain": "domain_to_upload_to",
            "multiple_domains": "False",
            "username": "your_username",
            "password": "your_password",
            "port": "your_port",
            "use_pub_key_authentication": "",
            "remote_dir": "where_should_the_files_be_placed"
        }

        self.confparser["imgur"] = {
            "client-id": "your client-id. Get it from the imgur site.",
            "Username": "optional",
            "Password": "optional"
        }

        with open(self.config_location, "w") as f:
            self.confparser.write(f)

    def get_key_value(self, section, key):
        self.confparser.read(self.config_location)

        if self.confparser.has_section(section) and key in self.confparser[section].keys():
            return self.confparser[section][key]
        else:
            print("Key or section does not exist.")
