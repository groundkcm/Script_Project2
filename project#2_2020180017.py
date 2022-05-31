from tkinter import *
from tkinter.ttk import *
import tkinter.messagebox as messagebox
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


def select_game(event=None):
    text = Gameselect.get()
    print(text, 'is selected')


def select_nametype(event=None):
    text = Gameselect.get()
    print(text, 'is selected')
# def enter_item(event=None):
#     text = combobox.get()
#     print(text, 'is entered')


def make_nickname():
    pass

window = Tk()
window.title("Name is already taken")
window.geometry("+100+100")
window.resizable(False, False)
window.bind('<Escape>', stop)

# 게임 선택
label = Label(text="게임 선택")
label.pack(anchor="w", pady=10)
Gameselect = Combobox(width=50, height=5, values=['로스트아크', 'LoL', '배틀그라운드', '오버워치', '배틀필드', '콜오브듀티'])
Gameselect.current()
Gameselect.bind('<<ComboboxSelected>>', select_game)
# Gameselect.bind('<Return>', enter_item)
Gameselect.pack()

# 테마 선택
# label = Label(text="닉네임 컨셉 선택")
# label.pack(anchor="w")
history_frame = LabelFrame(text='닉네임 컨셉 선택')
history_frame.pack(fill=X)
history_listbox = Listbox(history_frame, selectmode='single', height=5)
history_listbox.insert(0, '개인정보')
history_listbox.insert(1, '랜덤')
history_listbox.insert(END, '[a-zA-z]+')
history_listbox.pack(side=LEFT, fill=X, expand=True)
history_listbox.bind('<<ListboxSelect>>', None)
scrollbar = Scrollbar(history_frame)
scrollbar.pack(side=RIGHT, fill=Y)
history_listbox.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=history_listbox.yview)

# 닉네임 조합 선택
label = Label(text="닉네임 구성 선택")
label.pack(anchor="w")
nametype = Combobox(width=50, height=5, values=['영어', '영어 + 숫자', '한글', '한글 + 숫자', '한글 + 영어', '한글 + 영어 + 숫자'])
nametype.current()
nametype.bind('<<ComboboxSelected>>', select_nametype)
# nametype.bind('<Return>', enter_item)
nametype.pack()


command_frame = LabelFrame(text='Command')
command_frame.pack(fill=BOTH, padx=5, pady=5)
Button(command_frame, command=make_nickname, text='Make Nickname').pack(side=LEFT, expand=True, fill=BOTH, padx=5, pady=5)
# Button(command_frame, command=make_normal_folders, text='make normal_folders').pack(side=LEFT, expand=True, fill=BOTH, padx=5, pady=5)
# Button(command_frame, command=move_files, text='move files').pack(side=LEFT, expand=True, fill=BOTH, padx=5, pady=5)

menu = Menu()

menu_File = Menu(menu, tearoff=False) # tearoff : menu 분리
menu_File.add_command(label="Quit", accelerator='Ctrl+Q', command=stop)
menu.add_cascade(label="Menu", underline=True, menu=menu_File)



window.bind_all('<Control-q>', stop)
window.config(menu=menu)

window.mainloop()