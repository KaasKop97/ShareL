import os
import pyperclip
import notify2


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
        notify2.init("ShareL")
        notify = notify2.Notification("ShareL - Upload succesfull!", text)
        notify.show()

    def check_file_type(self, file, desired_type):
        pass

    @staticmethod
    def send_stdout(text):
        print(text)
