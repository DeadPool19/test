# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 12:28:40 2018

@author: wangyuping
"""

import requests
#import json
#检查某个电脑室里面的有多少电脑，有多少台可用。用户需给出一个时间段，以及电脑室的地址
def check_pc_status(riqi,start_time,end_time,dbuilding,droom_no):
   #url='https://api.data.umac.mo/service/facilities/computer_room_pc_status/v1.0.0/all?date_from=2018-03-23T15:05:00&date_to=2018-03-23T15:15:00'

    url='https://api.data.umac.mo/service/facilities/computer_room_pc_status/v1.0.0/all?date_from='+riqi+'T'+start_time+'&date_to='+riqi+'T'+end_time

    args={'Accept':'application/json','Authorization':'Bearer 1e8ca74b-97c8-33c1-af96-05a04b79a93d'}
    r=requests.get(url,headers=args)
    r_dict=r.json()
    #print(len(r_dict))
    #print(r_dict)
    noh=r_dict['_returned']#有多少间房提供电脑
    print('the number of computer rooms is: '+str(noh))
    
    room_state=r_dict['_embedded']#room_state is a list一个元素是一个房间的情况
    for i in range(noh):
        rs_one_room=room_state[i]#rs_one_room is a dictionary
        building=rs_one_room['buildingCode']
        room_num=rs_one_room['roomNo']
        #print('building: '+ building+' room_no: '+room_num)
        if building==dbuilding and room_num==droom_no:
            print('building: '+ building+' room_no: '+room_num)
            pc_state=rs_one_room['pc']#pc_state is a list 一个元素是一个电脑的情况
            npc=len(pc_state) #the number of computers
            print('#computers: '+str(npc))
            count_available=0
            for j in range(npc):
                a_pcs=pc_state[j]
                if a_pcs['available']:
                    count_available=count_available+1
            print('#available: '+str(count_available))
            break


def check_pc_status_2(riqi,start_time,end_time):
   #url='https://api.data.umac.mo/service/facilities/computer_room_pc_status/v1.0.0/all?date_from=2018-03-23T15:05:00&date_to=2018-03-23T15:15:00'

    url='https://api.data.umac.mo/service/facilities/computer_room_pc_status/v1.0.0/all?date_from='+riqi+'T'+start_time+'&date_to='+riqi+'T'+end_time

    args={'Accept':'application/json','Authorization':'Bearer 1e8ca74b-97c8-33c1-af96-05a04b79a93d'}
    r=requests.get(url,headers=args)
    r_dict=r.json()
    #print(len(r_dict))
    #print(r_dict)
    noh=r_dict['_returned']#有多少间房提供电脑
    print('the number of computer rooms is: '+str(noh))
    
    room_state=r_dict['_embedded']#room_state is a list一个元素是一个房间的情况
    for i in range(noh):
        rs_one_room=room_state[i]#rs_one_room is a dictionary
        building=rs_one_room['buildingCode']
        room_num=rs_one_room['roomNo']
        print('building: '+ building+' room_no: '+room_num)
        pc_state=rs_one_room['pc']#pc_state is a list 一个元素是一个电脑的情况
        npc=len(pc_state) #the number of computers
        print('#computers: '+str(npc))
        count_available=0
        for j in range(npc):
            a_pcs=pc_state[j]
            if a_pcs['available']:
                count_available=count_available+1
        print('#available: '+str(count_available))
            

check_pc_status('2018-03-23','15:05:00','15:15:00','E6','3093')