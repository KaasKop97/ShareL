import requests
from helpers import misc_helper


class WebApiHelper:
    def __init__(self, base_url, sub_path_check=""):
        self.base_url = base_url

        if not requests.get(self.base_url).status_code == 200 \
                or not requests.get(self.base_url + sub_path_check) == 200:
            print(self.base_url + sub_path_check + " Not resolvable, status code: " + str(
                requests.get(self.base_url).status_code))
            return
        self.misc = misc_helper.MiscHelper()

    def get(self, url):
        # TODO: Do I really need a get function?
        pass

    def post(self, path, data, headers=""):
        api_url = self.base_url + path
        r = requests.post(api_url, data=data, headers=headers)
        return r
