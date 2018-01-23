from plugins.SFTP import Sftp

# TODO: Load the plugins dynamically and provide a list of em to main.py

class PluginHandler:
    def __init__(self):
        self.plugins = [Sftp()]
