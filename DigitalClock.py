import tkinter as tk
from tkinter import messagebox
from time import strftime
import threading
import time

# We create a function to update the clock display
def UpdateClock():
    CurrentTime = strftime('%H:%M:%S %p')
    ClockLabel.config(text=CurrentTime)
    ClockLabel.after(1000, UpdateClock)

# Now we write a function to set an alarm in our clock
def SetAlarm():
    AlarmTime = AlarmEntry.get()
    if AlarmTime:
        threading.Thread(target=CheckAlarm, args=(AlarmTime,), daemon=True).start()  # Added parentheses here
        messagebox.showinfo("Alarm Set", f"Alarm set for {AlarmTime}")

# Now we write a function to check if the current time is same as the alarm time
def CheckAlarm(AlarmTime):
    while True:
        CurrentTime = strftime('%H:%M:%S %p')
        # print(f"Current Time: {CurrentTime}, Alarm Time: {AlarmTime}")
        if CurrentTime == AlarmTime:
            messagebox.showinfo("Alarm", "Time to wake up!")
            break
        time.sleep(1)

# Now we write code for creating the Graphical User Interface (GUI)
root = tk.Tk()
root.title("Digital Alarm Clock")
root.geometry("400x200")

# Writing code to create clock label
ClockLabel = tk.Label(root, font=("calibri", 40, "bold"), background="black", foreground="white")
ClockLabel.pack(anchor="center")

# Creating entry field for Alarm Time
AlarmEntry = tk.Entry(root, font=("calibri", 20))
AlarmEntry.pack(pady=10)
AlarmEntry.insert(0, "HH:MM:SS AM/PM")

# Creating a button for setting the Alarm
SetAlarmButton = tk.Button(root, text="Set Alarm", command=SetAlarm, font=("calibri", 15))
SetAlarmButton.pack(pady=10)

# Starting to update the clock
UpdateClock()

# Run Tkinter event main loop
root.mainloop()