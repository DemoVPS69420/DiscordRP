from tkinter import Tk, Button, filedialog, messagebox
import subprocess
import os
import signal

class Application:
    def __init__(self, master):
        self.master = master
        self.master.title("Python File Runner")
        self.current_process = None

        self.run_button = Button(master, text="Select Python File", command=self.select_file)
        self.run_button.pack(pady=20)

    def select_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Python Files", "*.py")])
        if file_path:
            self.run_file(file_path)

    def run_file(self, file_path):
        if self.current_process:
            self.stop_current_process()

        self.current_process = subprocess.Popen(['python', file_path], preexec_fn=os.setsid)
        messagebox.showinfo("Running", f"Running: {file_path}")

    def stop_current_process(self):
        os.killpg(os.getpgid(self.current_process.pid), signal.SIGTERM)
        self.current_process = None
        messagebox.showinfo("Stopped", "Previous process has been stopped.")

if __name__ == "__main__":
    root = Tk()
    app = Application(root)
    root.mainloop()