import requests
from helpers import misc_helper


class WebApiHelper:
    def __init__(self, base_url):
        self.base_url = base_url
        self.misc = misc_helper.MiscHelper()

    def get(self, url):
        # TODO Do I really need a get?
        pass

    def post(self, url, data, headers=""):
        api_url = self.base_url + url
        r = requests.post(api_url, data=data, headers=headers)
        return r
