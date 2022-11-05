#Coding Activity 1
from sys import exit

appointment_time = str(input("Enter the appointment-time in the format (hh:mm am/hh:mm pm): "))
current_time = str(input("Enter current-time in the format (hh:mm am/hh:mm pm): "))
hour_difference = 0
minute_difference = 0

"""
Suppose:
    
    appointment_time: 10:30 am
    current_time: 9:30 am
"""

at_split = appointment_time.split(" ")          #['10:30', 'am']
at_time = at_split[0]                           #10:30
at_am_pm = at_split[1]                          #am
at_hour_min = at_time.split(":")                #['10', '30']
at_hour = at_hour_min[0]                        #10
at_min = at_hour_min[1]                         #30


ct_split = current_time.split(" ")              #['9:30', 'am']
ct_time = ct_split[0]                           #9:30
ct_am_pm = ct_split[1]                          #am
ct_hour_min = ct_time.split(":")                #['9', '30']
ct_hour = ct_hour_min[0]                        #9
ct_min = ct_hour_min[1]                         #30

if (at_am_pm == "pm"):
    at_hour = int(at_hour) + 12
    at_total_minutes = (at_hour * 60) + int(at_min)

elif(at_am_pm == "am"):
    at_total_minutes = (int(at_hour) * 60) + int(at_min) 

if (ct_am_pm == "pm"):
    ct_hour = int(ct_hour) + 12
    ct_total_minutes = (ct_hour * 60) + int(ct_min)

elif(ct_am_pm == "am"):
    ct_total_minutes = (int(ct_hour) * 60) + int(ct_min) 


total_minutes_difference = abs(at_total_minutes - ct_total_minutes)

if (total_minutes_difference % 60 == 0):
    hour_difference = total_minutes_difference / 60
    if (hour_difference == 1):
        print(f"My appointment is at {appointment_time} and it is {current_time}.")
        print("You have 1 hour.")
        exit()
    else:
        print(f"My appointment is at {appointment_time} and it is {current_time}.")
        print(f"You have {hour_difference} hours.")
        exit()

if (float(total_minutes_difference / 60) < 1.0):
    if (total_minutes_difference == 1):
        print(f"My appointment is at {appointment_time} and it is {current_time}.")
        print("You have 1 minute")
        exit()
    else:
        print(f"My appointment is at {appointment_time} and it is {current_time}.")
        print(f"You have {total_minutes_difference} minutes.")
        exit()

if ((total_minutes_difference / 60) > 1):
    hours = int(total_minutes_difference / 60)
    minutes = int(((total_minutes_difference / 60) - 1) * 60)
    print(f"My appointment is at {appointment_time} and it is {current_time}.")
    print(f"You have {hours} hours and {minutes} minutes.")
    exit()

