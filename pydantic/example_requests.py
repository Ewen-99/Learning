import requests

response = requests.get("https://coreyms.com", timeout=5)
status = response.status_code
status = "ok"