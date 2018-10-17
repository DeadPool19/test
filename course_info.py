# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 19:11:22 2018

@author: wangyuping
"""
import requests
#查询某个课程的时间地点以及讲师的情况。用户需给出课程代码以及查询年份学期。
def check_course_info(courseCode,year,sem):
    
    #1. Example to retrieve information of course section EDPC602 001 in academic year 2017/2018 and semester 1:
    #https://api.data.umac.mo/service/academic/courses/v1.0.0/EDPC602-2017-1/001
    
    #2. Example to retrieve all courses offered in academic year 2017/2018 and semester 1:

    #https://api.data.umac.mo/service/academic/courses/v1.0.0/all?year=2017&sem=1
    
    #3. Example to retrieve information of course EDPC602 in academic year 2017/2018 and semester 1:

    #https://api.data.umac.mo/service/academic/courses/v1.0.0/EDPC602-2017-1
    
    url='https://api.data.umac.mo/service/academic/courses/v1.0.0/'+courseCode+'-'+year+'-'+sem
    
    args={'Accept':'application/json','Authorization':'Bearer 1e8ca74b-97c8-33c1-af96-05a04b79a93d'}
    r=requests.get(url,headers=args)
    #print(r.reason)
    r_dict=r.json()
    #print(r_dict)
    noh=r_dict['_returned']#有多少条返回的课程情况
    #print(noh)
    course_state=r_dict['_embedded']#room_state is a list一个元素是一个课程的情况
    for i in range(noh):
        rs_one_course=course_state[i]#rs_one_course is a dictionary
        course=rs_one_course['courseCode']
        nianfen=rs_one_course['year']
        s_nianfen=str(nianfen)

        #print('building: '+ building+' room_no: '+room_num)
        if s_nianfen==year and course==courseCode:
            
            print('course_code: '+courseCode)
           
            print('year: '+str(rs_one_course['year'])+' sem: '+str(rs_one_course['sem']))
            print('course_name: '+rs_one_course['courseTitleEng']+' '+rs_one_course['courseTitleChi'])
            section_state=rs_one_course['sections']
            for j in range(len(section_state)):
                section_state_one=section_state[j]
                print('section: '+str(section_state_one['sectionCode']))
                instructor_state=section_state_one['instructors']
                schedule_state=section_state_one['schedules']
                for k in range(len(instructor_state)):
                    instructor_state_one=instructor_state[k]
                    print('instructor: '+instructor_state_one['salutation']+' '+instructor_state_one['name'])
                for m in range(len(schedule_state)):
                    schedule_state_one=schedule_state[m]
                    print('schedule: day'+str(schedule_state_one['day'])+' type: '+schedule_state_one['componentType']+' time: '
                          +schedule_state_one['timeFrom']+'-'+schedule_state_one['timeTo'])
                    print('location: '+schedule_state_one['room1'])

check_course_info('EDPC602','2017','1')