
import re
import sys
import copy
import requests
import json
import pandas as pd
import csv
'''
Insert multiple devices info into web api,by means of request
'''
#convert html to excel with pandas

#url = 'http://127.0.0.1:8000/dev_list/'
#resp = requests.get(url)
#tb = pd.read_html(url,skiprows = 1)[0] 
#tb.columns = ['Device Name','IP','Vendor','Model','Series']
#data = json.loads(resp.text).get('projectStatus').get('status')
#tb.to_excel('devices_info.xlsx', sheet_name='Sheet1', index=False, header=True)

'''
    <tr>
        <td>Device Name</td>
        <td>IP</td>
        <td>Vendor</td>
        <td>Model</td>
        <td>Series</td>
    </tr>

'''

#get result from json data
'''
url = 'http://127.0.0.1:9000/device/'
resp = requests.get(url)
text = resp.json()['results']

print(help(text))
for k,v in text.items():
    print(k,v)

df = pd.DataFrame(text)
print(df)
df.to_excel('devices_info_from_DRF.xlsx', sheet_name='Sheet1', index=False, header=True)
'''

#get items from json
url = 'http://127.0.0.1:9000/device/'
resp = requests.get(url)
lendev = int(resp.json()['count'])
dev_list = []
for i in range(1,lendev+1):
    url_single = url + str(i)
    resp_single = requests.get(url_single)
    dev = resp_single.json()
    dev_list.append(dev)

#print(dev_list)
df = pd.DataFrame(dev_list)
print(df)
df.to_excel('devices_info_from_DRF.xlsx', sheet_name='Sheet1', index=False, header=True)
