import argparse
import os

from subprocess import run
from plugins import plugin_handler
from handlers import config_handler
from helpers import misc_helper

misc = misc_helper.MiscHelper()
conf = config_handler.ConfigHandler()

# To setup a initial configuration file in case there is none
# TODO: Find out if there's a better way to handle this.
if not misc.is_file(os.path.expanduser("~/.config/ShareL/config.ini")):
    conf = config_handler.ConfigHandler()

parser = argparse.ArgumentParser(prog="ShareL", description="Upload files to a remote host")
parser.add_argument("--edit-conf", help="Edit the configuration of the program (uses the $EDITOR variable)", dest="ec")
parser.add_argument("--sftp", help="Upload a file to an SFTP host", dest="sftp", nargs=1)
parser.add_argument("--imgur", help="Upload a file to imgur", dest="imgur", nargs=1)
parser.add_argument("--gfycat", help="Upload a file to gfycat", dest="gfycat", nargs=1)
parser.add_argument("--conf", help="Set what configuration to use.", dest="conf")

args = parser.parse_args()

if args.sftp or args.imgur or args.gfycat:
    service = None
    file = None
    returns = None

    if args.sftp:
        service = "sftp"
        returns = "plain"
        file = args.sftp[0]
        if conf.get_section("SFTP")["domain"] == "example.com":
            print(
                "SFTP is not configured in your config.ini (" + os.path.expanduser("~/.config/ShareL/config.ini") + ")")
            exit(1)
    elif args.imgur:
        service = "imgur"
        returns = "json"
        file = args.imgur[0]
    elif args.gfycat:
        service = "gfycat"
        returns = "json"
        file = args.gfycat[0]

    if misc.is_file(file):
        plugin_handler = plugin_handler.PluginHandler(service)
        if returns == "json":
            plugin_handler.handle_upload_json(file)
        else:
            plugin_handler.handle_upload(file)

if args.ec:
    print("Edit configuration")
    run([os.environ["EDITOR"], os.path.expanduser("~/.config/ShareL/config.ini")])
elif args.conf:
    print("Set what config to use.")
