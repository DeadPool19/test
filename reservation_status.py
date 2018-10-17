# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 11:28:22 2018

@author: wangyuping
"""

import requests
#import json
#检查某个房间的预定情况。用户需给出时间段和房间的位置。
def check_reservation_status(building_code,room_no,date_from,date_to):
   #https://api.data.umac.mo/service/facilities/computer_room_reservations/v1.0.0/all?date_from=2018-03-23&date_to=2018-04-01
   
    url='https://api.data.umac.mo/service/facilities/computer_room_reservations/v1.0.0/all?date_from='+date_from+'&date_to='+date_to

    args={'Accept':'application/json','Authorization':'Bearer 1e8ca74b-97c8-33c1-af96-05a04b79a93d'}
    r=requests.get(url,headers=args)
    print(r)
    r_dict=r.json()
    #print(len(r_dict))
    #print(r_dict)
    
    noh=r_dict['_returned']#有多少条返回的房间预定情况
  
    count=0
    reservation_status=r_dict['_embedded']#reservation_state is a list一个元素是一个房间预定的情况
    for i in range(noh):
        rs_one_reservation=reservation_status[i]#rs_one_reservation is a dictionary
        building=rs_one_reservation['buildingCode']
        room_num=rs_one_reservation['roomNo']
        #print('building: '+ building+' room_no: '+room_num)
        if building==building_code and room_num==room_no:
            count=count+1
            print('building: '+ building+' room_no: '+room_num)
            print('from: '+rs_one_reservation['dateFrom']+' to: '+rs_one_reservation['dateTo'])
            print('time from'+rs_one_reservation['timeFrom']+' to: '+rs_one_reservation['timeTo'])
            for j in rs_one_reservation['daysOfWeek']:
             print(str(j))
            print('status: '+ rs_one_reservation['status'])
           
    print('the number of reservations: '+str(count))       
 
        
#检查某个时间段有哪些房间可以预定available。用户需给出时间段？？？     
check_reservation_status('E6','2093','2018-03-23','2018-10-31')