import calendar
from datetime import datetime
from datetime import date

today = date.today()
year = today.year
month = today.month
day = today.day

list_of_tasks = [
    [True, "October", 15, "Sunday", "Homework", "Homework due every Sunday!"], 
    [False, "October", 31, "Tuesday", "Halloween", "It's Halloween!"], 
    [False, "August", 24, "Thursday", "Birthday", "My Birthday!"] ]

# Task example: [[Repeats (Bool), Month of Task (if not repeatable), Day of Task, Name of Day of Week, Task Name, Task Description]]

def print_calender(_year, _month, _day):
    cal = calendar.TextCalendar()
    cal_str = cal.formatmonth(_year, _month)
    current_day = " " + str(_day) + " "
    if cal_str.__contains__(current_day):
        cal_str = cal_str.replace(current_day, f"[{day}]")
    print(cal_str)

def print_tasks(_month):
    print("Task List:\n")
    month_name = calendar.month_name[_month]
    tasks_for_month = [
        task for task in list_of_tasks
        if task[0] or task[1] == month_name ]
    remaining_tasks = [ task for task in list_of_tasks
                        if task[0] or task[1] != month_name ]

    if not tasks_for_month:
        print("No tasks for this month.\n")
        return

    for task in tasks_for_month:
        repeats, task_month, task_day, day_name, task_name, description = task
        print(f"Task Name: {task_name} \nTask Description: {description}")
        if repeats:
            print(f"Next Occurrence of Task: {day_name}\n")
        else:
            print(f"Date of Task: {task_month} {task_day}, {day_name}\n")

    if len(remaining_tasks) != 0:
         print("Future Tasks:\n")
         for task in remaining_tasks:
               repeats, task_month, task_day, day_name, task_name, description = task
               print(f"Task Name: {task_name} \nTask Description: {description}")
               if repeats:
                      print(f"Next Occurrence of Task: {day_name}, {task_day}\n")
               else:
                      print(f"Date of Task: {task_month} {task_day}, {day_name}\n")

print_calender(year, month, day)
print_tasks(month)

def new_task():
     taskname = input("What task would you like to add? \n")
     taskdescription = input("What description would you give your taks? \n")
     taskmonth = input("What month is your task due? \n")
     taskday = int(input("What day is your task due? \n"))
     isrepeatable = input("Is the task repeatable? (Y/N) \n")

     monthnumber = list(calendar.month_name).index(taskmonth)

     date_obj = datetime.strptime(f"{today.year}-{monthnumber}-{taskday}", "%Y-%m-%d")


     list_of_tasks.append([isrepeatable == "Y", taskmonth, taskday, date_obj.strftime("%A"), taskname, taskdescription])
     print_tasks(month)


new_task()
