class SSHConnection:
  def __init__(self,host):
    self.host = host
    self.connected = False

  def __enter__(self):
    self.connected = True
    print(f"Opening SSH socket to {self.host}")
    return self

  def run(self, command):
    print(f"[{self.host}] Running : {command}")

  #When the with block finishes cleanly, Python passes None for all three. 
  # If the code inside the with block crashes, Python automatically passes the exception's class (exc_type), error message (exc_val), and traceback (exc_tb) into __exit__ so your teardown logic knows a failure happened.
  def __exit__(self, exc_type, exc_val, exc_tb):
    self.connected = False
    print(f"Closing the SSH socket to {self.host}")

with SSHConnection("10.0.1.5") as conn:
  conn.run("uptime")





  