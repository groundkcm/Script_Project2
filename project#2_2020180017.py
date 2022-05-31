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

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

user_agent = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36'
}

namelist = []
untaken_namelist = []

keyword = ''
lostark_url = f'https://lostark.game.onstove.com/Profile/Character/{keyword}'
maple_url = f'https://maple.gg/search?q={keyword}'
mincraft_url = f'https://ko.namemc.com/search?q={keyword}'
lol_url = f'https://www.op.gg/summoners/kr/{keyword}'
battleground_url = f'https://pubg.op.gg/user/{keyword}'
battlefield_url = f'https://battlefieldtracker.com/bfv/profile/origin/{keyword}/overview'

# options = webdriver.ChromeOptions()
# options.add_experimental_option('excludeSwitches', ['enable-automation'])
# options.add_argument(f'user-agent={user_agent}')
# browser = webdriver.Chrome(options=options)
#
# browser.get(url)
# browser.refresh()
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
    text = nametype.get()
    print(text, 'is selected')
# def enter_item(event=None):
#     text = combobox.get()
#     print(text, 'is entered')


def make_nickname():
    word.get()


def find_untaken_nickname():
    pass


window = Tk()
window.title("Name is already taken")
window.geometry("+100+100")
window.resizable(False, False)
window.bind('<Escape>', stop)
history_frame = LabelFrame(text='닉네임 컨셉 선택')
result_frame = LabelFrame(window)
command_frame = LabelFrame(text='Command')
command1_frame = LabelFrame(text='Command')


def Main():
    global Gameselect, nametype, word, history_frame, command_frame
    # 게임 선택

    result_frame.destroy()
    command1_frame.destroy()


    history_frame = LabelFrame(text='닉네임 컨셉 선택')
    history_frame.pack(fill=X, pady=7)

    label = Label(history_frame, text="게임 선택")
    label.pack(anchor="w", pady=7)
    Gameselect = Combobox(history_frame, width=50, height=5, values=['로스트아크', 'LoL', '배틀그라운드', '오버워치', '배틀필드', '콜오브듀티'])
    Gameselect.current()
    Gameselect.bind('<<ComboboxSelected>>', select_game)
    # Gameselect.bind('<Return>', enter_item)
    Gameselect.pack()

    # 테마 선택

    history_listbox = Listbox(history_frame, selectmode='multiple', height=5)
    history_listbox.insert(0, '개인정보')
    history_listbox.insert(1, '랜덤')
    history_listbox.insert(END, '기본단어')
    history_listbox.pack(side=LEFT, fill=X, expand=True)
    history_listbox.bind('<<ListboxSelect>>')
    scrollbar = Scrollbar(history_frame)
    scrollbar.pack(side=RIGHT, fill=Y)
    history_listbox.configure(yscrollcommand=scrollbar.set)
    scrollbar.configure(command=history_listbox.yview)

    # 필수 단어 입력
    label = Label(history_frame, text="필수 단어 입력")
    label.pack(anchor="w", pady=7)
    word = Entry(history_frame, width=50)
    word.pack()

    # 닉네임 조합 선택
    label = Label(history_frame, text="닉네임 구성 선택")
    label.pack(anchor="w", pady=7)
    nametype = Combobox(history_frame, width=50, height=5, values=['영어', '영어 + 숫자', '한글', '한글 + 숫자', '한글 + 영어', '한글 + 영어 + 숫자'])
    nametype.current()
    nametype.bind('<<ComboboxSelected>>', select_nametype)
    # nametype.bind('<Return>', enter_item)
    nametype.pack()


    command_frame = LabelFrame(text='Command')
    command_frame.pack(fill=BOTH, padx=5, pady=5)
    Button(command_frame, command=result, text='Make Nickname').pack(side=LEFT, expand=True, fill=BOTH, padx=5, pady=5)
    # Button(command_frame, command=make_normal_folders, text='make normal_folders').pack(side=LEFT, expand=True, fill=BOTH, padx=5, pady=5)
    # Button(command_frame, command=move_files, text='move files').pack(side=LEFT, expand=True, fill=BOTH, padx=5, pady=5)


    # menu = Menu()
    #
    # menu_File = Menu(menu, tearoff=False) # tearoff : menu 분리
    # menu_File.add_command(label="Quit", accelerator='Ctrl+Q', command=stop)
    # menu.add_cascade(label="Menu", underline=True, menu=menu_File)
    #
    #
    window.bind_all('<Control-q>', stop)
    # window.config(menu=menu)


def result(event=None):
    global command1_frame, result_frame

    history_frame.destroy()
    command_frame.destroy()

    result_frame = LabelFrame(window)
    label = Label(text="결과")
    label.pack(anchor="w", pady=7)
    history_listbox = Listbox(result_frame, selectmode='single', height=5)
    for n in range(0, len(namelist)):
        history_listbox.insert(n, namelist[n])
    # history_listbox.insert(END, '기본단어')
    history_listbox.pack(side=LEFT, fill=X, expand=True)
    history_listbox.bind('<<ListboxSelect>>')
    scrollbar = Scrollbar(result_frame)
    scrollbar.pack(side=RIGHT, fill=Y)
    history_listbox.configure(yscrollcommand=scrollbar.set)
    scrollbar.configure(command=history_listbox.yview)

    command1_frame = LabelFrame(text='Command')
    command1_frame.pack(fill=BOTH, padx=5, pady=5)
    Button(command1_frame, command=make_nickname, text='Find Untaken Nickname').pack(side=LEFT, expand=True, fill=BOTH, padx=5, pady=5)

    window.bind_all('<Control-q>', stop)


Main()
window.mainloop()