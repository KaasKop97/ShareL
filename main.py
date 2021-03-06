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
parser.add_argument("--sftp", help="Uploads a file to an SFTP host", dest="sftp", nargs=1)
parser.add_argument("--imgur", help="Uploads a file to imgur", dest="imgur", nargs=1)
parser.add_argument("--ipfs", help="Uploads a file to IPFS", dest="ipfs", nargs=1)
parser.add_argument("--save", help="Save the file locally and nothing else.", dest="save", nargs=1)
parser.add_argument("--conf", help="Set what configuration to use.", dest="conf")

args = parser.parse_args()

if args.sftp or args.imgur or args.save or args.ipfs:
    service = None
    file = None
    returns = None

    if args.sftp:
        service = "sftp"
        returns = "plain"
        file = args.sftp[0]
        if conf.get_section("SFTP")["domain"] == "sftp-is-not-configured":
            misc.send_notification(
                "SFTP is not configured in your config.ini (" + os.path.expanduser("~/.config/ShareL/config.ini") + ")")
            exit(1)
    elif args.imgur:
        service = "imgur"
        returns = "json"
        file = args.imgur[0]
    elif args.save:
        service = "save"
        returns = "plain"
        file = args.save[0]
    elif args.ipfs:
        service = "ipfs"
        returns = "plain"
        file = args.ipfs[0]
    if file and misc.is_file(file):
        pluginHandler = plugin_handler.PluginHandler(service)
        if conf.get_key_value("general", "show_notification_on_upload_initiation"):
            misc.send_notification("Started upload to " + service)

        if returns == "json":
            pluginHandler.handle_upload_json(file)
        else:
            pluginHandler.handle_upload(file)

        if bool(conf.get_key_value("general", "always_save_image_to_local_disk")):
            plugin_handler_save = plugin_handler.PluginHandler("save")
            plugin_handler_save.handle_upload(file)
    else:
        print("ERROR not a file.")

if args.ec:
    print("Edit configuration")
    run([os.environ["EDITOR"], os.path.expanduser("~/.config/ShareL/config.ini")])
elif args.conf:
    print("Set what config to use.")
