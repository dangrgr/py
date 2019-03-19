#F5 REST API playground
import requests
import json
from pprint import pprint
from getpass import getpass
from requests.auth import HTTPBasicAuth
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
username = "admin"
password = getpass() 

# examples

# update syslog (put)
#url = 'https://192.168.56.32/mgmt/tm/sys/syslog~Common~compress_pool'
sys_syslog_dict = {"remoteServers": [{"name": "remotesyslog1","host": "192.168.1.2","remotePort": 514}]}
sys_syslog_dict["remoteServers"][0]["local-ip"] = "192.168.1.2"

# create new pool (post, 200 if success, 409 if exists)
#url = 'https://192.168.56.32/mgmt/tm/ltm/pool'
ltm_new_pool_dict = {"name":"log_pool","partition":"Common","monitor":"udp","members":[{"name":"logsrvr01.local:514","address":"1.2.3.4"},{"name":"logsrvr02.local:514","address":"5.6.7.8"}]}
ltm_new_pool_dict["name"] = "%s_log_pool" % ("prod")

# update existing pool (put)
url = 'https://192.168.56.32/mgmt/tm/ltm/pool/prod_log_pool'
ltm_existing_pool_dict = {}
ltm_existing_pool_dict["members"] = [{"name":"logvip01.local:514","address":"9.10.11.12"}]

# ensure valid json
try:
    body = json.dumps(ltm_existing_pool_dict)
    print(body)
except ValueError as e:
        print(e)

# get, post, put
#response = requests.get(url, verify=False, auth=HTTPBasicAuth(username, password))
#response = requests.post(url, verify=False, data=body, auth=HTTPBasicAuth(username, password)) 
response = requests.put(url, verify=False, data=body, auth=HTTPBasicAuth(username, password)) 

try:
    print("Status: " + str(response.status_code))
except:
    pass

try:
    pprint(response.json())
except ValueError as e:
    if response.text:
        print(response.text)
    else:
        print(e)
