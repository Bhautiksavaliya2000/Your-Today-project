from win10toast import ToastNotifier
import webbrowser
from datetime import datetime
import time
import os
import csv

day = datetime.today().strftime('%A')
toast = ToastNotifier()

# To check if file is already exists.
if os.path.isfile("timetable.csv"):
    lines = [line for line in open(r"timetable.csv")]
else:
    try:
        lines = [line for line in open("timetable.csv", 'a+')]
    except Exception as e:
        print("The issue is:", e)

# 
def input_getter():
    no = int(input("Enter total slots."))
    slot_list = []

    print("Enter starting time of each session. In hh:mm 24 hour or 12 hour format according to your PC time.")
    for i in range(no):
        starting_time = input(f"slot : {i+1} ")
        slot_list.append(starting_time)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']

    # storing user input into csv file when user first time enters timetable.
    fwriter =  open("timetable.csv", 'a+', newline='')
    thewriter = csv.writer(fwriter)
    thewriter.writerow(slot_list)
    thewriter.writerow(days)

    print("Enter 'NA' for any time slot that not having lecture or permanent link.")
    for day in days:
        # to get time:msg dict for each day of week.
        time_link_list = []
        time_msg_list = []
        print("For ",day, ":")
        for slot in slot_list:
            msg = input(f"enter msg for {slot} :")
            time_msg_list.append(msg)   
            linkaddress = input(f"enter link for {slot} :")
            time_link_list.append(linkaddress)

        thewriter.writerow(time_msg_list)    # message list
        thewriter.writerow(time_link_list)   # list of link. 

# To check if file exist but empty.
if not lines:
    input_getter()
    
# to read from the file if timetable is already entered.
final_time_msg_dict = {}
final_time_link_dict = {}

# preparing both the directories from the lines list.
slotlist = lines[0].strip().split(',')
daylist = lines[1].strip().split(',')

idx = 0
for i in range(2,len(lines),2):
    temp_msgdict =  dict(zip(slotlist, lines[i].strip().split(',')))  
    final_time_msg_dict[daylist[idx]] = temp_msgdict
    temp_linkdict = dict(zip(slotlist,lines[i+1].strip().split(',')))
    final_time_link_dict[daylist[idx]] = temp_linkdict
    idx += 1

def openlink(day,currenttime):
    try:
        webbrowser.open(final_time_link_dict[day][currenttime])
    except Exception as e:
        pass

def show_notification(day,currenttime):
    # To behave according to 'NA'
    if final_time_msg_dict[day][currenttime] != "NA" and final_time_link_dict[day][currenttime] != "NA":
        toast.show_toast( title="Notification", msg=final_time_msg_dict[day][currenttime],
                        icon_path=None, duration=10, threaded=False, callback_on_click=openlink(day,currenttime))

    elif final_time_msg_dict[day][currenttime] != "NA" and final_time_link_dict[day][currenttime] == "NA":
        toast.show_toast( title="Notification", msg=final_time_msg_dict[day][currenttime], icon_path=None,      duration=10, threaded=False)
    
    else:
        toast.show_toast( title="Notification", msg="Free slot", icon_path=None, duration=10, threaded=False)

# user interaction starts. 
reenter = input("Do you wanto to re-enter timetable? (y/n)")
if reenter == 'y' or reenter == 'Y':
    verify = input("Are you sure? (y/n)")
    if verify == 'y' or verify == 'Y':
        open("timetable.csv","w").close()
        input_getter()
    
ans = input("Start now? (y/n) :")
if ans == 'Y' or ans=='y':
    currenttime = time.strftime("%H:%M")
    print("Your today is started....")

    for lec_time in slotlist:
        if lec_time<currenttime:
            pass
        else:
            while currenttime != lec_time:
                time.sleep(1)
                currenttime = time.strftime("%H:%M")
            show_notification(day,currenttime)
            print("The  ",final_time_msg_dict[day][currenttime]," is started")
        
else:
    print("Ok")


