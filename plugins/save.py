import datetime
from os import mkdir

from handlers import config_handler
from helpers import misc_helper
from shutil import copyfile


class Save:
    def __init__(self):
        self.conf = config_handler.ConfigHandler()
        self.misc = misc_helper.MiscHelper()
        self.configuration = self.conf.get_section("save")
        self.always_save_to_disk_mode = False

        self.save_location = self.configuration["save_location"]
        self.per_month_basis = bool(self.configuration["per_month_basis"])

    def upload(self, file):
        filename = self.misc.get_filename(file)

        if self.per_month_basis:
            if not self.misc.is_dir(self.save_location):
                mkdir(self.save_location)

            if not self.misc.is_dir(self.save_location + datetime.date.strftime(datetime.date.today(), "%Y-%m")):
                mkdir(self.save_location + datetime.date.strftime(datetime.date.today(), "%Y-%m"))
                save_path = self.save_location + datetime.date.strftime(datetime.date.today(),
                                                                        "%Y-%m") + "/" + filename
            else:
                save_path = self.save_location + datetime.date.strftime(datetime.date.today(),
                                                                        "%Y-%m") + "/" + filename
        else:
            save_path = self.save_location + "/" + filename

        copyfile(file, save_path)

        if self.misc.is_file(save_path):
            return [True, ""]
        else:
            return [False, "Something went wrong, does the directory exist that you set in the config file?"]