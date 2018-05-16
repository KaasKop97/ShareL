import paramiko
import socket
from handlers import config_handler
from helpers import misc_helper


class Sftp:
    def __init__(self):
        self.conf = config_handler.ConfigHandler()
        self.misc = misc_helper.MiscHelper()
        self.sftp_section = self.conf.get_section("SFTP")

        self.domain = self.sftp_section["domain"]
        self.port = int(self.sftp_section["port"])
        self.username = self.sftp_section["username"]
        self.password = self.sftp_section["password"]
        self.remote_dir = self.sftp_section["remote_dir"]
        self.use_pub_key = bool(self.sftp_section["use_pub_key_authentication"])
        self.http_path = self.sftp_section["http_path"]
        self.notification_content = self.sftp_section["notification_clipboard_content"]

        self.ssh_conn = paramiko.SSHClient()

    def connect(self):
        if self.use_pub_key:
            self.ssh_conn.load_system_host_keys()
            self.ssh_conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            try:
                self.ssh_conn.connect(self.domain, self.port)
                return [True, ""]
            except socket.gaierror:
                return [False, "ERROR: " + self.domain + " is not resolvable."]
        else:
            try:
                self.ssh_conn.connect(self.domain, self.port, self.username, self.password)

                return [True, ""]
            except socket.gaierror:
                return [False, "ERROR: " + self.domain + " is not resolvable."]

    def upload(self, file):
        filename = file.split("/")[-1]
        remote_dir = self.remote_dir + "/" + filename
        sftp_session = self.ssh_conn.open_sftp()
        sftp_session.put(file, remote_dir)

        if self.notification_content == "http_path":
            location = self.http_path + filename
        elif self.notification_content == "remote_dir":
            location = remote_dir
        else:
            location = "ERROR"

        return [True, location]
