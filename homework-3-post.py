import pandas as pd
import re
import sys
import copy
import requests
import json

'''
Insert multiple devices info into web api,by means of request
'''
'''
url = 'http://127.0.0.1:8000/add_devices/'
#data_json = json.dumps({'dev_name': 'A-HHA3A-2LA-AS01', 'ip': '11.121.240.135','vendor':'Cisco'})
data = {'dev_name': 'A-HHA3A-2LA-AS01', 'ip': '11.121.240.135','vendor':'Cisco'}
devnamel = ['A-HHA3D-2LA-AS0'+ chr(i+ord('0')) for i in range(10)]
ipl = ['11.121.240.14'+ chr(i+ord('0')) for i in range(10)]
vendorl = ['Cisco' for i in range(10)]
modell = ['N9K' for i in range(10)]
series = ['Nexus' for i in range(10)]

datal = []
for i in range(10):
    cu_dev = {}
    cu_dev['dev_name'] = devnamel[i]
    cu_dev['ip'] = ipl[i]
    cu_dev['vendor'] = vendorl[i]
    cu_dev['model'] = modell[i]
    cu_dev['series'] = series[i]
    response = requests.post(url, cu_dev)
    #datal.append(cu_dev)

#response = requests.post(url, cu_dev)
print(response)
'''
'''
url = 'http://127.0.0.1:9000/device/'
data = {'dev_name': 'A-HHA3A-2LA-AS01', 'ip': '11.121.240.135','vendor':'Cisco','model':'N5K','series':'SW'}
response = requests.post(url, data)
print(response)

'''
url = 'http://127.0.0.1:9000/device/'
devnamel = ['A-HHA3D-2LA-AS0'+ chr(i+ord('0')) for i in range(10)]
ipl = ['11.121.240.14'+ chr(i+ord('0')) for i in range(10)]
vendorl = ['Cisco' for i in range(10)]
modell = ['N9K' for i in range(10)]
series = ['Nexus' for i in range(10)]

datal = []
for i in range(10):
    cu_dev = {}
    cu_dev['dev_name'] = devnamel[i]
    cu_dev['ip'] = ipl[i]
    cu_dev['vendor'] = vendorl[i]
    cu_dev['model'] = modell[i]
    cu_dev['series'] = series[i]
    response = requests.post(url, cu_dev)
