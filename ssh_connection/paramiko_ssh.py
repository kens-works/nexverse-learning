import paramiko


class SSHConnection:
    def __init__(self, host, username, key_filename=None, port=22):
        self.host = host
        self.username = username
        self.key_filename = key_filename
        self.port = port
        self.client = None

    def __enter__(self):
        self.client = paramiko.SSHClient()
        # Load ~/.ssh/known_hosts for host key verification
        self.client.load_system_host_keys()
        # AutoAddPolicy is convenient for ephemeral lab VMs;
        # omit this line in production to enforce strict host key checks
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        self.client.connect(
            hostname=self.host,
            port=self.port,
            username=self.username,
            key_filename=self.key_filename,
            timeout=10,
        )
        return self

    def run(self, command):
        if not self.client:
            raise RuntimeError("SSHConnection is closed. Use inside a 'with' block.")

        stdin, stdout, stderr = self.client.exec_command(command)
        output = stdout.read().decode("utf-8").strip()
        error = stderr.read().decode("utf-8").strip()
        exit_code = stdout.channel.recv_exit_status()

        return exit_code, output, error

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.client:
            self.client.close()
            self.client = None


with SSHConnection("10.0.1.5", username="ubuntu", key_filename="~/.ssh/id_ed25519") as conn:
    code, out, err = conn.run("uptime")
    print(f"Exit {code}: {out}")