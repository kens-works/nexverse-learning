class DBConnection:
    def __init__(self, host, port, database):
        self.host = host
        self.port = port
        self.database = database
        print (f"{self.host}:{self.port}/{self.database}")

    def get_dsn(self):
        return f"postgresql://{self.host}:{self.port}/{self.database}"

conn = DBConnection("db-primary.internal", 5432, "telemetry")
print(conn.get_dsn())