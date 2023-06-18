import tkinter as tk
from tkinter import ttk
from time import strftime
from tkcalendar import DateEntry
from functools import partial

from datetime import datetime

import db
import backend as be


class MainWindow:
    def __init__(self):
        # Setting window on the FullHD screen
        self.window = tk.Tk()
        self.sc_width = self.window.winfo_screenwidth()
        self.sc_height = self.window.winfo_screenheight()
        self.x = ((self.sc_width / 2) - 220) + (self.sc_width / 4)
        self.y = ((self.sc_height / 2) - 260) - (self.sc_height / 4)
        self.window.geometry(('%dx%d+%d+%d' % (690, 280, self.x, self.y)))
        self.window.title("Lukas Rausa - TO-DO LIST")

        self.date = strftime('%d-%B-%Y')  # use in new task window

        self.header = tk.Frame(self.window, width=600, height=300, bg="gray8")
        self.header.grid(row=0, column=0, sticky="WE")
        self.title = tk.Label(self.header, text=">> TO-DO LIST >>", font=("Source Code Pro", 12, "bold"), fg="green2", bg="gray8", anchor="w")
        self.title.grid(row=0, column=0, ipadx=224)
        self.add_task = tk.Button(self.header, width=4, text="+", command=self.open_new_task, font=("Source Code Pro", 12, "bold"), fg="green2",
                                  bg="gray40")
        self.add_task.grid(row=0, column=1)

        self.columns_frame = tk.Frame(self.window, width=620, height=280, bg="gray8")
        self.columns_frame.grid(row=1, column=0, sticky="WE")

        self.tasks = tk.Label(self.columns_frame, width=33, text="Task", font=("Source Code Pro", 11, "bold"), fg="green2", bg="gray24")
        self.tasks.grid(row=0, column=0, padx=1, sticky="W")
        self.deadlines = tk.Label(self.columns_frame, width=13, text="Deadline", font=("Source Code Pro", 11, "bold"), fg="green2", bg="gray24")
        self.deadlines.grid(row=0, column=1, padx=1, sticky="W")
        self.progresses = tk.Label(self.columns_frame, width=16, text="Progress", font=("Source Code Pro", 11, "bold"), fg="green2", bg="gray24")
        self.progresses.grid(row=0, column=2, padx=1, sticky="W")
        self.confirmations = tk.Label(self.columns_frame, width=11, text="Confirm", font=("Source Code Pro", 11, "bold"), fg="green2",
                                      bg="gray24")
        self.confirmations.grid(row=0, column=3, padx=1, sticky="W")

        # Default variables
        # TopLevel
        self.nt_window = None
        self.sctop_width = None
        self.sctop_height = None
        self.top_x = None
        self.top_y = None
        self.top_task = None
        self.top_deadline = None
        self.top_task_entry = None
        self.top_deadline_entry = None
        self.accept_new_task = None
        # Task datas
        self.task_info = None
        self.deadline = None
        self.progress = None
        self.remained = None
        self.db_content = None
        self.row_move = 1
        self.task_container = []
        # Task widgets
        self.task_widget = None
        self.deadline_widget = None
        self.progress_widget = None
        self.confirmation_widget = None

    def open_new_task(self):
        self.nt_window = tk.Toplevel()
        self.nt_window.title("Add new task")
        self.nt_window.resizable(width=False, height=False)
        self.sctop_width = self.nt_window.winfo_screenwidth()
        self.sctop_height = self.nt_window.winfo_screenheight()
        self.top_x = ((self.sctop_width / 2) - 310) + (self.sctop_width / 4)
        self.top_y = ((self.sctop_height / 2) - 580) + (self.sctop_height / 4)
        self.nt_window.geometry(('%dx%d+%d+%d' % (400, 80, self.top_x, self.top_y)))
        #self.nt_window.protocol("WM_DELETE_WINDOW", self.save_new_task)
        self.top_task = tk.Label(self.nt_window, width=20, text="Task text", font=("Source Code Pro", 11), fg="white", bg="gray44")
        self.top_task.grid(row=0, column=0, sticky="WE")
        self.top_deadline = tk.Label(self.nt_window, width=10, text="Deadline", font=("Source Code Pro", 11), fg="white", bg="gray20")
        self.top_deadline.grid(row=0, column=1, columnspan=2, sticky="WE")
        self.top_task_entry = tk.Entry(self.nt_window, width=50)
        self.top_task_entry.grid(row=1, column=0, padx=1, sticky="NS")
        self.top_deadline_entry = DateEntry(self.nt_window, date_pattern='yyyy/mm/dd')
        self.top_deadline_entry.grid(row=1, column=1, sticky="WE")
        self.accept_new_task = tk.Button(self.nt_window, text="ACCEPT", command=self.save_new_task, font=("Source Code Pro", 8), fg="white", bg="gray44")
        self.accept_new_task.grid(row=2, column=0, columnspan=2, sticky="WE", ipadx=20)

    def save_new_task(self):
        self.task_info = self.top_task_entry.get()
        self.deadline = self.top_deadline_entry.get()
        self.progress = int(be.refresh_progress(self.deadline))
        self.remained = self.progress
        db.add_new_task(self.task_info, self.deadline, self.progress, self.remained)
        # Refreshing workspace
        self.unpack_tasks()
        self.nt_window.destroy()

    def unpack_tasks(self):
        self.refresh_workspace()
        self.db_content = db.get_tasks()
        for record in self.db_content:
            self.task_widget = tk.Label(self.columns_frame, width=37, text=record.task, font=("Source Code Pro", 8), fg="white", bg="gray44")
            self.task_widget.grid(row=self.row_move, column=0, padx=1, sticky="WE")
            self.deadline_widget = tk.Label(self.columns_frame, width=14, text=record.deadline, font=("Source Code Pro", 8), fg="white", bg="gray44")
            self.deadline_widget.grid(row=self.row_move, column=1, padx=1, sticky="WE", ipadx=1)
            self.progress_widget = ttk.Progressbar(self.columns_frame, orient="horizontal", mode="determinate", length=150, maximum=4)
            self.progress_widget.grid(row=self.row_move, column=2, padx=1, sticky="WE")
            self.confirmation_widget = tk.Button(self.columns_frame, command=partial(self.confirm_task, record.id), width=10, text="√", font=("Source Code Pro", 8), fg="white", bg="gray44")
            self.confirmation_widget.grid(row=self.row_move, column=3, padx=1, sticky="WE")
            self.task_container.append([self.task_widget, self.deadline_widget, self.progress_widget, self.confirmation_widget])
            self.row_move += 1

    def refresh_workspace(self):
        if len(self.task_container) != 0:
            for widget_dump in self.task_container:
                for widget in widget_dump:
                    widget.destroy()

    def confirm_task(self, task_id):
        db.remove_task(task_id)
        self.unpack_tasks()

    def run(self):
        self.unpack_tasks()
        self.window.mainloop()


gui = MainWindow()
gui.run()
