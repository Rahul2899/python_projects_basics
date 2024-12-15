import tkinter as tk
from tkinter import messagebox

# Function to add a task
def add_task():
    task = task_entry.get()
    if task.strip():  # Ensure the task isn't empty
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

# Function to delete the selected task
def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete!")

# Function to clear all tasks
def clear_tasks():
    task_listbox.delete(0, tk.END)

# Initialize the main window
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x400")

# Task entry field and add button
task_entry = tk.Entry(root, font=("Arial", 14))
task_entry.pack(pady=10)

add_task_button = tk.Button(root, text="Add Task", command=add_task, font=("Arial", 12), bg="green", fg="white")
add_task_button.pack(pady=5)

# Listbox to display tasks
task_listbox = tk.Listbox(root, font=("Arial", 14), width=35, height=10)
task_listbox.pack(pady=10)

# Buttons for actions: Delete and Clear All
delete_task_button = tk.Button(root, text="Delete Task", command=delete_task, font=("Arial", 12), bg="red", fg="white")
delete_task_button.pack(pady=5)

clear_tasks_button = tk.Button(root, text="Clear All Tasks", command=clear_tasks, font=("Arial", 12), bg="orange", fg="black")
clear_tasks_button.pack(pady=5)

# Run the main event loop
root.mainloop()
