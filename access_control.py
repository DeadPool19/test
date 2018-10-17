# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 12:09:53 2018

@author: wangyuping
"""

import requests

    
url='https://api.data.umac.mo/service/facilities/access_control_records/v1.0.0/all'
    
args={'Accept':'application/json','Authorization':'Bearer 1e8ca74b-97c8-33c1-af96-05a04b79a93d'}
r=requests.get(url,headers=args)
print(r.reason)#'404'not found!!!!