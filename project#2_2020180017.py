from tkinter import *
from tkinter.ttk import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import csv
import re
import logging

# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


# options = webdriver.ChromeOptions()
# user_agent = {
#     'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36'
# }
# options.add_experimental_option('excludeSwitches', ['enable-automation'])
# options.add_argument(f'user-agent={user_agent}')
# browser = webdriver.Chrome(options=options)

# url = 'https://flyasiana.com/I/KR/KO/RevenueRegistTravel.do'
# browser.get(url)
# browser.refresh()
#
#
# keyword = '신라면'
# url = f'https://search.naver.com/search.naver?where=image&sm=tab_jum&query={keyword}'
#
# browser = webdriver.Chrome()
# browser.get(url)
# browser.refresh()
#
# soup = BeautifulSoup(browser.page_source, features='lxml')
# elms = soup.find_all(class_='_image _listImage')
#
# for i, e in enumerate(elms):
#     caption = e['alt']
#     image_url = e['data-lazy-src'] if e.has_attr('data-lazy-src') else e['src']
#     print(f'No: {i:3}, Caption: {caption}, URL: {image_url}')


def stop():
    window.quit()


window = Tk()
window.geometry("+100+100")
window.resizable(False, False)
window.bind('<Escape>', stop)

label = Label(text="Name is already taken")
label.pack()

history_frame = LabelFrame(text='History')
history_frame.pack(fill=X)
history_listbox = Listbox(history_frame, selectmode='single', height=5)
history_listbox.insert(0, 'Python')
history_listbox.insert(1, '\d\d')
history_listbox.insert(END, '[a-zA-z]+')
history_listbox.pack(side=LEFT, fill=X, expand=True)
history_listbox.bind('<<ListboxSelect>>', None)
scrollbar = Scrollbar(history_frame)
scrollbar.pack(side=RIGHT, fill=Y)
history_listbox.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=history_listbox.yview)

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