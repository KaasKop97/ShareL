import argparse
import os

from plugins import SFTP, imgur
from handlers import config_handler
from helpers import misc_helper

misc = misc_helper.MiscHelper()

# To setup a initial configuration file in case there is none
# TODO: Find out if there's a better way to handle this.
if not misc.is_file(os.environ["HOME"] + "/.config/ShareL/config.ini"):
    conf = config_handler.ConfigHandler()

# Here we check if file exists and shit

parser = argparse.ArgumentParser(prog="ShareL", description="Upload files to a remote host")
parser.add_argument("--edit-conf", help="Edit the configuration of the program", dest="ec")
parser.add_argument("--sftp", help="Upload a file to an SFTP host", dest="sftp", nargs=1)
parser.add_argument("--imgur", help="Upload a file to imgur", dest="imgur", nargs=1)
parser.add_argument("--conf", help="Set what configuration to use.", dest="conf")

args = parser.parse_args()

if args.ec:
    print("Edit configuration")
elif args.sftp:
    print("Uploading with SFTP")
    sftp = SFTP.Sftp()
    sftp.upload(args.sftp[0])
elif args.imgur:
    imgr = imgur.Imgur()
    print(imgr.upload(args.imgur[0]))
elif args.conf:
    print("Set what config to use.")
else:
    print("Argument provided does not exist.")
