from handlers import config_handler


class GfyCat:
    def __init__(self):
        self.conf = config_handler.ConfigHandler()
        self.GfyCat = self.conf.get_section("gfycat")

    def upload(self, file):

