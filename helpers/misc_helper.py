import os
import pyperclip
import subprocess


class MiscHelper:
    @staticmethod
    def is_file(file_location):
        return os.path.isfile(file_location)

    @staticmethod
    def is_dir(dir):
        return os.path.isdir(dir)

    @staticmethod
    def copy_to_clipboard(data):
        pyperclip.copy(data)

    @staticmethod
    def send_notification(text):
        subprocess.run(["notify-send", text])
