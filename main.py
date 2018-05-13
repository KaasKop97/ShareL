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
parser.add_argument("--conf", help="Set what configuration to use.", dest="conf")

args = parser.parse_args()

if args.sftp or args.imgur:
    service = None
    file = None
    returns = None

    if args.sftp:
        service = "sftp"
        returns = "plain"
        file = args.sftp[0]
    elif args.imgur:
        service = "imgur"
        returns = "json"
        file = args.imgur[0]

    if file and misc.is_file(file):
        if conf.get_key_value("general", "show_notification_on_upload_initiation"):
            misc.send_notification("Started upload to " + service)
        plugin_handler = plugin_handler.PluginHandler(service)
        if returns == "json":
            plugin_handler.handle_upload_json(file)
        else:
            plugin_handler.handle_upload(file)

if args.ec:
    print("Edit configuration")
    run([os.environ["EDITOR"], os.environ["HOME"] + "/.config/ShareL/config.ini"])
elif args.conf:
    print("Set what config to use.")
