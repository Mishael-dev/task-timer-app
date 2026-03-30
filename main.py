
option = input('''
Main Menu:
1 → Start New Task
2 → Exit
''')

number_option = int(option)

task_name = ""

if (number_option==1): 
    task_name = input("Enter task name: ")
elif(number_option==2):
    input("Exiting program...")
else:
    print("Please enter a valid option!")

import time

seconds = 0 

while True:
    secs = seconds % 60
    mins= secs // 60
    hrs = seconds // 360
    print(f"\r Task: {task_name} Status: RUNNING | Time: {hrs}:{mins}:{secs} | Controls: P = Pause | S = Stop", end="")
    seconds += 1
    time.sleep(1)
