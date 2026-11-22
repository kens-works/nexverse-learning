class APIEndpoint:
    def __init__(self, base_url, port, auth_token):
        self.base_url = base_url
        self.port = port
        self.auth_token = auth_token

    def get_full_url(self):
        return f"{self.base_url}:{self.port}"

    def get_auth_header(self):
        return f"Bearer<{self.auth_token}>"

api1 = APIEndpoint("https://api.internal", 8443, "tok_sec_1")
api2 = APIEndpoint("http://log.internal", 8080, "tok_log_2")

#Print both full URLs and their headers
print(f"Full url for api1 - {api1.get_full_url()}")
print(f"Header for api1 - {api1.get_auth_header()}")

print(f"Full url for api2 - {api2.get_full_url()}")
print(f"Header for api2 - {api2.get_auth_header()}")