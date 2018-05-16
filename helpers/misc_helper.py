import os
import pyperclip
import notify2


class MiscHelper:
    @staticmethod
    def is_file(file_location):
        return os.path.isfile(file_location)

    @staticmethod
    def is_dir(directory):
        return os.path.isdir(directory)

    @staticmethod
    def copy_to_clipboard(data):
        pyperclip.copy(data)

    @staticmethod
    def send_notification(text):
        if text:
            notify2.init("ShareL")
            notify = notify2.Notification("ShareL", text)
            notify.show()

    @staticmethod
    def send_stdout(text):
        print(text)

    @staticmethod
    def get_filename(file_location):
        return file_location.split("/")[-1]
