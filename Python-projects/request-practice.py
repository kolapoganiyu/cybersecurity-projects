import requests
from requests.auth import HTTPBasicAuth

site = input("Name of the site -")


response = requests.get(site)
print(response.content)

# printing
# printing
# printing only the status code