class Popup:
    def __init__(self, master, run_file_callback):
        self.master = master
        self.run_file_callback = run_file_callback
        self.selected_file = None
        self.create_popup()

    def create_popup(self):
        self.popup = Toplevel(self.master)
        self.popup.title("Select Python File")
        
        self.file_listbox = Listbox(self.popup)
        self.file_listbox.pack(fill=BOTH, expand=True)

        self.load_files()

        self.run_button = Button(self.popup, text="Run", command=self.run_selected_file)
        self.run_button.pack()

        self.popup.protocol("WM_DELETE_WINDOW", self.on_close)

    def load_files(self):
        # Load Python files from a specified directory
        import os
        for file in os.listdir('.'):
            if file.endswith('.py'):
                self.file_listbox.insert(END, file)

    def run_selected_file(self):
        selected_index = self.file_listbox.curselection()
        if selected_index:
            self.selected_file = self.file_listbox.get(selected_index)
            self.run_file_callback(self.selected_file)
            self.popup.destroy()

    def on_close(self):
        self.popup.destroy()