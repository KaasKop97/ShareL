import os
import pyperclip


class MiscHelper:
    def is_file(self, file_location):
        return os.path.isfile(file_location)

    def is_dir(self, dir):
        return os.path.isdir(dir)

    def copy_to_clipboard(self, data):
        pyperclip.copy(data)
