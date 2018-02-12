import argparse
import os

from subprocess import run
from plugins import SFTP, imgur, ipfs
from handlers import config_handler
from helpers import misc_helper

misc = misc_helper.MiscHelper()
conf = config_handler.ConfigHandler()

# To setup a initial configuration file in case there is none
# TODO: Find out if there's a better way to handle this.

parser = argparse.ArgumentParser(prog="ShareL", description="Upload files to a remote host")
parser.add_argument("--edit-conf", help="Edit the configuration of the program (uses the $EDITOR variable)", dest="ec")
parser.add_argument("--sftp", help="Upload a file to an SFTP host", dest="sftp", nargs=1)
parser.add_argument("--imgur", help="Upload a file to imgur", dest="imgur", nargs=1)
parser.add_argument("--ipfs", help="Upload a file to IPFS", dest="ipfs", nargs=1)
parser.add_argument("--conf", help="Set what configuration to use.", dest="conf")

args = parser.parse_args()

if args.ec:
    print("Edit configuration")
    run([os.environ["EDITOR"], os.environ["HOME"] + "/.config/ShareL/config.ini"])
elif args.sftp:
    if misc.is_file(args.sftp[0]):
        sftp = SFTP.Sftp()
        if sftp.connect()[0]:
            result = sftp.upload(args.sftp[0])
            conf.apply_general_config_options(result[1])
    else:
        print("File does not exist.")
elif args.imgur:
    imgr = imgur.Imgur()
    print(imgr.upload(args.imgur[0]))
elif args.ipfs:
    ipfs = ipfs.Ipfs()
    ipfs.upload(args.ipfs[0])
elif args.conf:
    print("Set what config to use.")
