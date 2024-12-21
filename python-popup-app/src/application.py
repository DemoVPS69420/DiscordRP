import subprocess
from tkinter import filedialog, messagebox, Button, Tk
import os
import signal

class Application:
    def __init__(self, master):
        self.master = master
        self.master.title("Python File Runner")
        self.current_process = None
        self.history_file = "history.txt"

        self.run_button = Button(master, text="Select Python File", command=self.select_file)
        self.run_button.pack(pady=20)

        self.stop_button = Button(master, text="Stop Current File", command=self.stop_current_process)
        self.stop_button.pack(pady=20)

    def select_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Python Files", "*.py")])
        if file_path:
            self.run_file(file_path)

    def run_file(self, file_path):
        if self.current_process:
            self.stop_current_process()

        self.current_process = subprocess.Popen(['python', file_path], creationflags=subprocess.CREATE_NEW_PROCESS_GROUP)
        self.log_history(file_path)
        messagebox.showinfo("Running", f"Running: {file_path}")

    def stop_current_process(self):
        if self.current_process:
            self.current_process.send_signal(signal.CTRL_BREAK_EVENT)
            self.current_process.wait()
            self.current_process = None

    def log_history(self, file_path):
        with open(self.history_file, "a") as f:
            f.write(file_path + "\n")

if __name__ == "__main__":
    root = Tk()
    app = Application(root)
    root.mainloop()