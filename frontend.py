import tkinter as tk


class MainWindow:
    def __init__(self):
        # Setting window on the FullHD screen
        self.window = tk.Tk()
        self.sc_width = self.window.winfo_screenwidth()
        self.sc_height = self.window.winfo_screenheight()
        self.x = ((self.sc_width / 2) - 200) + (self.sc_width / 4)
        self.y = ((self.sc_height / 2) - 200) - (self.sc_height / 4)
        self.window.geometry(('%dx%d+%d+%d' % (620, 280, self.x, self.y)))
        self.window.title("Lukas Rausa - TO-DO LIST")

        self.header = tk.Frame(self.window, width=600, height=280, bg="gray8")
        self.header.grid(row=0, column=0, sticky="WE", ipady=4)
        self.title = tk.Label(self.header, text=">> TO-DO LIST >>", font=("Source Code Pro", 12, "bold"), fg="green2", bg="gray8")
        self.title.grid(row=0, column=0)
        self.add_task = tk.Button(self.header, text="+", font=("Source Code Pro", 14, "bold"), fg="green2", bg="gray24")
        self.add_task.grid(row=0, column=1, sticky="E")

        self.columns_frame = tk.Frame(self.window, width=620, height=280, bg="gray8")
        self.columns_frame.grid(row=1, column=0, sticky="WE")

        self.tasks = tk.Label(self.columns_frame, text="Task", font=("Source Code Pro", 11, "bold"), fg="green2", bg="gray24")
        self.tasks.grid(row=0, column=0, ipadx=122, padx=1)
        self.deadline = tk.Label(self.columns_frame, text="Deadline", font=("Source Code Pro", 11, "bold"), fg="green2", bg="gray24")
        self.deadline.grid(row=0, column=1, ipadx=10, padx=1)
        self.progress = tk.Label(self.columns_frame, text="Progress", font=("Source Code Pro", 11, "bold"), fg="green2", bg="gray24")
        self.progress.grid(row=0, column=2, ipadx=30, padx=1)
        self.confirmation = tk.Label(self.columns_frame, text="Confirm", font=("Source Code Pro", 11, "bold"), fg="green2", bg="gray24")
        self.confirmation.grid(row=0, column=3, ipadx=10, padx=1)

        self.tasks_list = tk.Frame(self.window, width=640, height=280, bg="gray8")
        self.tasks_list.grid(row=2, column=0)

    def unpack_tasks(self):
        pass

    def run(self):
        self.window.mainloop()


gui = MainWindow()
gui.run()
