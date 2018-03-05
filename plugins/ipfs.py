from handlers import config_handler
from helpers import misc_helper, web_api_helper
import os


class Ipfs:
    def __init__(self):
        self.conf = config_handler.ConfigHandler()
        self.misc = misc_helper.MiscHelper()
        self.wapi = web_api_helper.WebApiHelper("http://localhost:5001/api/v0/")

    def upload(self, file):
        # data = {
        #     'path': os.path.abspath(file),
        #     'Content-Encoding': "multipart/form-data"
        # }
        # req = self.wapi.post("add", data)

        return [True, req]
