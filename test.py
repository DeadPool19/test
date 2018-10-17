# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 20:46:03 2018

@author: wangyuping
"""
'''
from urllib import request

response=request.urlopen('https://baidu.com')

html=response.read()
print(html)
'''


import requests
#import json
def check_holiday(start,end):
    #url='https://api.data.umac.mo/service/aboutum/public_holidays/v1.0.0/all?format&date_from=2018-03-01&date_to=2018-03-31'
    url='https://api.data.umac.mo/service/aboutum/public_holidays/v1.0.0/all?format&date_from='+start+'&date_to='+end
    args={'Accept':'application/json','Authorization':'Bearer 1e8ca74b-97c8-33c1-af96-05a04b79a93d'}
    r=requests.get(url,headers=args)
    r_dict=r.json()
    #print(len(r_dict))
    #print(r_dict)
    noh=r_dict['_returned']  #the number of holidays 假期的数量
    #print(noh)
    #print(type(noh))
    if noh==0:
        print('There is no holidays in the designated period')
    if noh>0:
        v=r_dict['_embedded'] #the dates and the session of the holidays 假期的日期和时间段
        for i in range(noh):
             
              v_dict=v[i]# 某一个假期
              if v_dict['holiday']=='W':
                  print('holiday is: '+v_dict['date']+'and the session is the whole day')
              if v_dict['holiday']=='1':
                  print('holiday is: '+v_dict['date']+'and the session is the morning')
              if v_dict['holiday']=='2':
                  print('holiday is: '+v_dict['date']+'and the session is the afternoon')
   
