from tkinter import *
from tkinter.ttk import *
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def stop():
    window.quit()


window = Tk()
window.geometry("+0+0")
window.resizable(False, False)
window.bind('<Escape>', stop)

label = Label(text="File Management")
label.pack()
command_frame = LabelFrame(text='Command')
command_frame.pack(fill=BOTH, padx=5, pady=5)

# Button(command_frame, command=make_lecture_folders, text='make lecture_folders').pack(side=LEFT, expand=True, fill=BOTH, padx=5, pady=5)
# Button(command_frame, command=make_normal_folders, text='make normal_folders').pack(side=LEFT, expand=True, fill=BOTH, padx=5, pady=5)
# Button(command_frame, command=move_files, text='move files').pack(side=LEFT, expand=True, fill=BOTH, padx=5, pady=5)

menu = Menu()
menu_File = Menu(menu, tearoff=False) # tearoff : menu 분리
menu_File.add_command(label="Quit", accelerator='Ctrl+Q', command=stop)
menu.add_cascade(label="Menu", underline=True, menu=menu_File)
menu_Colors = Menu(menu, tearoff=False)
window.bind_all('<Control-q>', stop)
window.config(menu=menu)

window.mainloop()