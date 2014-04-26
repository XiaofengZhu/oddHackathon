from bs4 import BeautifulSoup
import re;
import requests;
import datetime;
import icalendar;
from datetime import datetime;
import pytz
from icalendar import vCalAddress, vText
from icalendar import vDatetime
from icalendar import Calendar, Event
from datetime import timedelta

dayNumber={
'mo':0,
'tu':1,
'we':2,
'th':3,
'fr':4,
'sa':5,
'su':6}

def convert_meeting_days(days):
    i=0;
    dayList = [];
    while i+1<=len(days):
        day = days[i:i+2]
        dayList.append(dayNumber[day.lower()])
        i+=2
    return dayList;
def last_weekday(day,weekday):
    lastday = day - timedelta(days=day.weekday()) + timedelta(days=weekday, weeks=-1)
    return lastday;
def next_weekday(d, weekday):
    days_ahead = weekday - d.weekday()
    if days_ahead <= 0: # Target day already happened this week
        days_ahead += 7
    return d + timedelta(days_ahead)

####################################
#d = datetime.date(2011, 7, 2)
#next_monday = next_weekday(d, 0) # 0 = Monday, 1=Tuesday, 2=Wednesday...
#print(next_monday)
#####################################
option = input('options:\n \t type a if you have your html file in this folder\n \t type b if you have a list of course nums to input\n');
if(option.lower()=='a'):
    fileDirectory = input('please enter your html file name with no .html extention. Example: \'enrollment\' \n');
    if fileDirectory==None:
        fileDirectory='enrollment'
    soup = BeautifulSoup(open('./'+fileDirectory+'_files/SA_LEARNER_SERVICES.SSS_STUDENT_CENTER.html'))
    classes = soup.findAll("span", { "class" : "PSHYPERLINKDISABLED" })
    classIds = [];
    for c in classes:
        print "processing:",c
        classnumtemp = re.findall(r'\([0-9]+\)',str(c))
        if(len(classnumtemp)>=1):
            classnum = classnumtemp[0][1:-1];
        #if(re.findall('id=".*?"',str(c))[0][4]=='E'):
            classIds.append(classnum);
else:
    classIds = input('Please enter the list of course nums here. Example: [40613,40615]\n');#those are just examples for classIds
print classIds;

classIds = [40613,40615]
print "skipped original course numbers", "new course number: ",classIds
classesInfo = {};
#creating calendar
cal = Calendar();
for classId in classIds:
    data = requests.get('http://vazzak2.ci.northwestern.edu/courses/?class_num='+str(classId))
    classesInfo[classId] = {};
    if(len(data.json())==0):
        print "no information was found for course num ",classId
        continue;
    classesInfo[classId] = data.json()[0];
    classesInfo[classId]['meeting_days'] = convert_meeting_days(classesInfo[classId]['meeting_days'])
    for meetDay in classesInfo[classId]['meeting_days']:
        startDate = classesInfo[classId]['start_date']+' 00:00:00';
        startDate = datetime.strptime(startDate, '%Y-%m-%d %H:%M:%S')
        startDate = next_weekday(startDate,meetDay) 
        startDate = startDate.strftime("%Y-%m-%d") 
        startTime = classesInfo[classId]['start_time'];
        tempStartDate = startDate;
        endTime = classesInfo[classId]['end_time'];
        endTime = tempStartDate+ ' '+ endTime;
        endTime = datetime.strptime(endTime, '%Y-%m-%d %H:%M:%S')
        startTime = tempStartDate + ' '+startTime;
        startTime = datetime.strptime(startTime, '%Y-%m-%d %H:%M:%S')
        endDate = classesInfo[classId]['end_date']+' 00:00:00';
        endDate = datetime.strptime(endDate, '%Y-%m-%d %H:%M:%S')
        days = (endDate - startTime).days
        print 'startDate:',startTime
        print 'startDateEndTime',endTime
        print 'endDate:',endDate
        print 'days:', days;
        weeks = days/7+1  
        event = Event();
        event.add('summary', classesInfo[classId]['title']);
        event.add('dtstart',startTime)
        event.add('dtend',endTime)
        event.add('rrule',{'freq':'weekly','count':weeks});
        event.add('location',classesInfo[classId]['room']);
        cal.add_component(event)
        
        
print cal;        
f = open('test.ics','wb')
f.write(cal.to_ical());
f.close(); 
