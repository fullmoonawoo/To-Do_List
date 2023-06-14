import tkinter as tk
from tkinter import ttk
from time import strftime
from tkcalendar import DateEntry


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

        #self.tasks_list = tk.Frame(self.window, width=640, height=250, bg="gray8")
        #self.tasks_list.grid(row=2, column=0, sticky="W")

        self.task = tk.Label(self.columns_frame, width=37, text="Pošli email do Gewisu teraz hned", font=("Source Code Pro", 8), fg="white",
                             bg="gray44")
        self.task.grid(row=1, column=0, padx=1, sticky="WE")
        self.deadline = tk.Label(self.columns_frame, width=14, text="2.6.2023", font=("Source Code Pro", 8), fg="white", bg="gray44")
        self.deadline.grid(row=1, column=1, padx=1, sticky="WE", ipadx=1)
        self.progress = ttk.Progressbar(self.columns_frame, orient="horizontal", mode="determinate", length=150)
        self.progress.grid(row=1, column=2, padx=1, sticky="WE")
        self.confirmation = tk.Button(self.columns_frame, width=10, text="√", font=("Source Code Pro", 8), fg="white", bg="gray44")
        self.confirmation.grid(row=1, column=3, padx=1, sticky="WE")

    def open_new_task(self):
        self.progress.step(1)

    def unpack_tasks(self):
        pass

    def run(self):
        self.window.mainloop()


gui = MainWindow()
gui.run()
