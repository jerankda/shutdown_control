import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import threading
import time
import os

# Function to validate and start the timer
def start_timer():
    try:
        hours = int(hour_entry.get()) if hour_entry.get() else 0
        minutes = int(min_entry.get()) if min_entry.get() else 0
        seconds = int(sec_entry.get()) if sec_entry.get() else 0
        total_seconds = hours * 3600 + minutes * 60 + seconds

        if total_seconds <= 0:
            raise ValueError("Time must be greater than zero.")

        action = action_var.get()
        warnings = warning_var.get()
        warning_time = int(warning_time_entry.get()) * 60 if warning_var.get() == "Yes" else None

        confirm = messagebox.askyesno("Confirmation", f"Are you sure you want to schedule a {action.lower()} in {hours}h {minutes}m {seconds}s?")
        if confirm:
            countdown_label.config(text=f"Time remaining: {hours:02d}:{minutes:02d}:{seconds:02d}")
            start_button.config(state='disabled')
            cancel_button.config(state='normal')
            threading.Thread(target=timer_thread, args=(total_seconds, action, warnings, warning_time), daemon=True).start()
    except ValueError as ve:
        messagebox.showerror("Invalid Input", str(ve))

# Function to handle the countdown and execute the command
def timer_thread(total_seconds, action, warnings, warning_time):
    global shutdown_process
    for remaining in range(total_seconds, 0, -1):
        mins, secs = divmod(remaining, 60)
        hrs, mins = divmod(mins, 60)
        countdown_label.config(text=f"Time remaining: {hrs:02d}:{mins:02d}:{secs:02d}")
        time.sleep(1)
        if warnings == "Yes" and warning_time and remaining == warning_time:
            messagebox.showwarning("Warning", f"The system will {action.lower()} in {warning_time//60} minutes.")

        if shutdown_cancelled:
            return

    execute_action(action)

# Function to execute the chosen action
def execute_action(action):
    commands = {
        "Shutdown": "shutdown -s -f -t 0",
        "Restart": "shutdown -r -f -t 0",
        "Log Off": "shutdown -l -f",
        "Hibernate": "shutdown -h"
    }
    os.system(commands[action])

# Function to cancel the shutdown
def cancel_shutdown():
    global shutdown_cancelled
    shutdown_cancelled = True
    os.system("shutdown -a")
    countdown_label.config(text="Shutdown cancelled.")
    start_button.config(state='normal')
    cancel_button.config(state='disabled')

# Initialize the main window
root = tk.Tk()
root.title("Windows Shutdown Timer")

# Variables
action_var = tk.StringVar(value="Shutdown")
warning_var = tk.StringVar(value="No")
shutdown_cancelled = False

# Time input frame
time_frame = ttk.LabelFrame(root, text="Set Time")
time_frame.pack(padx=10, pady=5, fill="x")

ttk.Label(time_frame, text="Hours:").grid(row=0, column=0, padx=5, pady=5)
hour_entry = ttk.Entry(time_frame, width=5)
hour_entry.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(time_frame, text="Minutes:").grid(row=0, column=2, padx=5, pady=5)
min_entry = ttk.Entry(time_frame, width=5)
min_entry.grid(row=0, column=3, padx=5, pady=5)

ttk.Label(time_frame, text="Seconds:").grid(row=0, column=4, padx=5, pady=5)
sec_entry = ttk.Entry(time_frame, width=5)
sec_entry.grid(row=0, column=5, padx=5, pady=5)

# Action selection frame
action_frame = ttk.LabelFrame(root, text="Choose Action")
action_frame.pack(padx=10, pady=5, fill="x")

actions = ["Shutdown", "Restart", "Log Off", "Hibernate"]
for idx, act in enumerate(actions):
    ttk.Radiobutton(action_frame, text=act, variable=action_var, value=act).grid(row=0, column=idx, padx=5, pady=5)

# Warning options frame
warning_frame = ttk.LabelFrame(root, text="Warning Notifications")
warning_frame.pack(padx=10, pady=5, fill="x")

ttk.Label(warning_frame, text="Enable Warnings:").grid(row=0, column=0, padx=5, pady=5)
ttk.Radiobutton(warning_frame, text="Yes", variable=warning_var, value="Yes").grid(row=0, column=1, padx=5, pady=5)
ttk.Radiobutton(warning_frame, text="No", variable=warning_var, value="No").grid(row=0, column=2, padx=5, pady=5)

ttk.Label(warning_frame, text="Warn before (minutes):").grid(row=0, column=3, padx=5, pady=5)
warning_time_entry = ttk.Entry(warning_frame, width=5)
warning_time_entry.insert(0, "5")
warning_time_entry.grid(row=0, column=4, padx=5, pady=5)

# Countdown label
countdown_label = ttk.Label(root, text="Time remaining: 00:00:00", font=("Helvetica", 12))
countdown_label.pack(pady=10)

# Start and Cancel buttons
button_frame = ttk.Frame(root)
button_frame.pack(pady=5)

start_button = ttk.Button(button_frame, text="Start Timer", command=start_timer)
start_button.grid(row=0, column=0, padx=5)

cancel_button = ttk.Button(button_frame, text="Cancel Shutdown", command=cancel_shutdown, state='disabled')
cancel_button.grid(row=0, column=1, padx=5)

# Run the main event loop
root.mainloop()
