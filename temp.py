# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 16:47:17 2018

@author: wangyuping
"""

import tkinter as tk
import requests

#import test
window=tk.Tk()
window.title('Show Holidays Window')
window.geometry('460x300')


riqi=tk.Label(window,text='Dates').place(x=10,y=13)
jiaqi=tk.Label(window,text='Holidays').place(x=10,y=60)
zhongjian=tk.Label(window,text='to').place(x=217,y=13)

riqientry1_var=tk.StringVar()
riqientry2_var=tk.StringVar()
riqientry1=tk.Entry(window,width=15,textvariable=riqientry1_var).place(x=60,y=10)
riqientry2=tk.Entry(window,width=15,textvariable=riqientry2_var).place(x=240,y=10)

holiday_show=tk.Text(window,width=30,height=18)
holiday_show.place(x=80,y=40)


#import json
#检查某个时间段的放假情况。用户需给出时间段
def check_holiday():
    #url='https://api.data.umac.mo/service/aboutum/public_holidays/v1.0.0/all?format&date_from=2018-03-01&date_to=2018-03-31'
    start=riqientry1_var.get()
    end=riqientry2_var.get()
    url='https://api.data.umac.mo/service/aboutum/public_holidays/v1.0.0/all?format&date_from='+start+'&date_to='+end
    args={'Accept':'application/json','Authorization':'Bearer 1e8ca74b-97c8-33c1-af96-05a04b79a93d'}
    r=requests.get(url,headers=args)
    r_dict=r.json()
    #print(len(r_dict))
    #print(r_dict)
    noh=r_dict['_returned']
    #print(noh)
    #print(type(noh))
    if noh==0:
        holiday_show.delete(0.0,tk.END)
        holiday_show.insert(tk.INSERT,'Therer is no hoidays in the designated period'+'\n')

        #print('There is no holidays in the designated period')
    if noh>0:
        holiday_show.delete(0.0,tk.END)
        v=r_dict['_embedded']
        for i in range(noh):
            
              v_dict=v[i]
              if v_dict['holiday']=='W':
                  holiday_show.insert(tk.INSERT,'holiday is: '+v_dict['date']+'and the session is the whole day'+'\n')
                 # print('holiday is: '+v_dict['date']+'and the session is the whole day')
              if v_dict['holiday']=='1':
                  holiday_show.insert(tk.INSERT,'holiday is: '+v_dict['date']+'and the session is the morning'+'\n')

                  #print('holiday is: '+v_dict['date']+'and the session is the morning')
              if v_dict['holiday']=='2':
                  holiday_show.insert(tk.INSERT,'holiday is: '+v_dict['date']+'and the session is the afternoon'+'\n')

                  #print('holiday is: '+v_dict['date']+'and the session is the afternoon')

cb=tk.Button(window,text='Check',command=check_holiday).place(x=400,y=13)

window.mainloop()