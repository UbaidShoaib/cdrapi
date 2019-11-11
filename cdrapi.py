
from urllib3.exceptions import InsecureRequestWarning

import requests ,ssl, json
from requests.auth import HTTPDigestAuth
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)


username = 'cdrapi'
password = 'cdrapi1231'
url = 'https://72.137.146.94:8443/cdrapi?format=JSON&caller=1000&numRecords=10'
r = requests.get(url,auth=HTTPDigestAuth(username,password) ,verify=False)
data=json.loads(r.text)
print(json.loads(r.content))