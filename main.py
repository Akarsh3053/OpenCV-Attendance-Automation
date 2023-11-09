import tkinter as tk
from tkinter import ttk, messagebox

class Application(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        style = ttk.Style()
        style.configure("TButton",
                        foreground="midnight blue",
                        background="white",
                        font=("Helvetica", 16, "bold"),
                        padding=10)

        self.hi_there = ttk.Button(self, style="TButton")
        self.hi_there["text"] = "Start Face Recognition"
        self.hi_there["command"] = self.start_face_recognition
        self.hi_there.pack(side="top")

        self.quit = ttk.Button(self, text="QUIT", style="TButton",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def start_face_recognition(self):
        # Here you can add the code to start the face recognition process
        messagebox.showinfo("Info","Face recognition started")

root = tk.Tk()
app = Application(master=root)
app.mainloop()
