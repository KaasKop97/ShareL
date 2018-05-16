from handlers import config_handler
from helpers import misc_helper
import subprocess


class Ipfs:
    def __init__(self):
        self.conf = config_handler.ConfigHandler()
        self.misc = misc_helper.MiscHelper()

    def upload(self, file):
        upload = subprocess.run(["ipfs", "add", file], stdout=subprocess.PIPE)
        if upload.returncode == 1:
            return [False, "Error check euhm something?"]
        else:
            ipfs_hash = str(upload.stdout.decode("utf-8"))[6:52]
            return [True, "https://ipfs.io/ipfs/" + ipfs_hash[0:59]]

