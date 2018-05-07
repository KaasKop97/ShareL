import os
from handlers import config_handler
from helpers import misc_helper

class Save:
    def __init__(self):
        self.conf = config_handler.ConfigHandler()
        self.misc = misc_helper.MiscHelper()
        self.configuration = self.conf.get_section("save")

    def upload(self, file):
        filename = self.misc.get_filename(file)
        os.rename(file, self.configuration["save_location"] + filename)
        if self.misc.is_file(self.configuration["save_location"] + filename):
            return [True, ""]
        else:
            return [False, "Something went wrong, does the directory exist that you set in the config file?"]


