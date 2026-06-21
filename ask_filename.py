import tkinter.filedialog

def get_ask_filename(title, filetypes):
    return tkinter.filedialog.askopenfilename(title=title, filetypes=filetypes)