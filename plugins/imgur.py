from helpers import web_api_helper
from handlers import config_handler
import os


class Imgur:
    def __init__(self):
        self.api_helper = web_api_helper.WebApiHelper("https://api.imgur.com/3/")
        self.conf = config_handler.ConfigHandler()
        self.imgur_section = self.conf.get_section("imgur")

    def upload(self, file):
        # Imgur actually accepts 10.x mb file sizes, it only denies them when they hit 11mb.
        if not os.path.getsize(file) >= 11000000:
            binary_file = open(file, "rb").read()
            data = {'image': binary_file}
            header = {"Authorization": "Client-ID " + self.imgur_section["client-id"]}

            req = self.api_helper.post("image", data, header)
            return [True, req]
        else:
            return "File exceeds imgur's maximum upload size of <10mb."
