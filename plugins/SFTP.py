import paramiko
from handlers import config_handler


class Sftp:
    def __init__(self):
        self.conf = config_handler.ConfigHandler()

        self.domain = self.conf.get_key_value("SFTP", "domain")
        self.port = int(self.conf.get_key_value("SFTP", "port"))
        self.username = self.conf.get_key_value("SFTP", "username")
        self.password = self.conf.get_key_value("SFTP", "password")
        self.remote_dir = self.conf.get_key_value("SFTP", "remote_dir")
        self.use_pub_key = bool(self.conf.get_key_value("SFTP", "use_pub_key_authentication"))
        self.ssh_conn = paramiko.SSHClient()

        if self.use_pub_key:
            self.ssh_conn.load_system_host_keys()
            self.ssh_conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.ssh_conn.connect(self.domain, self.port)
        else:
            self.ssh_conn.connect(self.domain, self.port, self.username, self.password)

    def upload(self, file):
        filename = file.split("/")[-1]
        sftp = self.ssh_conn.open_sftp()
        sftp.put(file, self.remote_dir + "/" + filename)

