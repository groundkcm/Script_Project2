from tkinter import *
from tkinter.ttk import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import csv
import re
import exrex
import logging
import requests


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

user_agent = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36'
}

namelist = ['yuntaepyung', 'groundkcm', 'name1', 'name2']
untaken_namelist = []
find = False

keyword = ''
url = ''
game = ''

def stop():
    window.quit()


def select_game(event=None):
    global game
    game = Gameselect.get()


def seturl():
    global game, url
    if game == '로스트아크':
        url = f'https://lostark.game.onstove.com/Profile/Character/{keyword}'
    elif game == '메이플스토리':
        url = f'https://maple.gg/search?q={keyword}'
    elif game == '마인크래프트':
        url = f'https://ko.namemc.com/search?q={keyword}'
    elif game == 'LoL':
        url = f'https://www.op.gg/summoners/kr/{keyword}'
    elif game == '배틀그라운드':
        url = f'https://pubg.op.gg/user/{keyword}'
    elif game == '배틀필드':
        url = f'https://battlefieldtracker.com/bfv/profile/origin/{keyword}/overview'
    elif game == '오버워치':
        url = f'https://overwatch.op.gg/search/?playerName={keyword}'


def select_nametype(event=None):
    text = nametype.get()
    print(text, 'is selected')


def select_nameconcept(event=None):
    text = main_listbox.curselection()
    print(text, 'is entered')


def make_nickname():
    word.get()

    pattern = r'''
        ^
        (
            (02|051|053|010)
            |
            (\(
                [ ]*
                (02|051|053|010)
                [ ]*
            \))
        [ ]* -? 
        )?
        [ ]*
        \d{3,4}
        [ ]* -? [ ]*
        \d{4}
        $
    '''

    final_pattern = re.sub(r'[ ]{2,}|\t|\n', '', pattern)
    # password_re = re.compile(r'[0-9a-zA-Z]{,15}') # 영어숫자조합 10자 이상
    password_re = re.compile(r'[a-zA-Z]{10,}[0-9]{3,}')  # 영어숫자조합 10자 이상
    exrex.getone(password_re.pattern, 2)


def find_untaken_nickname():
    global keyword, game, untaken_namelist, find, untaken_listbox

    for name in namelist:
        keyword = name
        seturl()
        r = requests.get(url, headers=user_agent)

        soup = BeautifulSoup(r.text, 'lxml')

        if game == '로스트아크':
            elms = soup.find_all(class_=re.compile(r'^profile-attention'))
        elif game == '메이플스토리':
            elms = soup.find_all(class_=re.compile(r'^d-inline-block align-middle pl-3'))
        elif game == '마인크래프트':  #보류
            elms = soup.find_all(class_=re.compile(r'^PlayerSearchMessage'))
        elif game == 'LoL':
            elms = soup.find_all(class_=re.compile(r'^header__title'))
        elif game == '배틀그라운드':
            elms = soup.find_all(class_=re.compile(r'^not-found__desc'))
        elif game == '배틀필드':  #보류
            elms = soup.find_all(class_=re.compile(r'^PlayerSearchMessage'))
        elif game == '오버워치':  #보류
            elms = soup.find_all(class_=re.compile(r'^PlayerSearchMessage'))
        for e in elms:
            untaken_namelist.append(name)
            print(e.text)

        if not elms:
            print('False')
    # find = True
    for n in range(0, len(untaken_namelist)):
        untaken_listbox.insert(n, namelist[n])

window = Tk()
window.title("Name is already taken")
window.geometry("+100+100")
window.resizable(False, False)
window.bind('<Escape>', stop)

main_frame = LabelFrame()
result_frame = LabelFrame()
command_frame = LabelFrame()
command1_frame = LabelFrame()
untaken_listbox = Listbox()


def Main(event=None):
    global Gameselect, nametype, main_listbox, word, main_frame, command_frame, untaken_namelist

    result_frame.destroy()
    command1_frame.destroy()

    main_frame = LabelFrame()
    main_frame.pack()

    untaken_namelist = []

    # 게임 선택
    label = Label(main_frame, text="게임 선택")
    label.pack(anchor="w", pady=7)
    Gameselect = Combobox(main_frame, width=50, height=5, values=['로스트아크', 'LoL', '배틀그라운드', '오버워치', '배틀필드', '메이플스토리', '마인크래프트'])
    Gameselect.current()
    Gameselect.bind('<<ComboboxSelected>>', select_game)
    # Gameselect.bind('<Return>', enter_item)
    Gameselect.pack()

    # 테마 선택
    label = Label(main_frame, text="닉네임 컨셉 선택")
    label.pack(anchor="w")
    main_listbox = Listbox(main_frame, selectmode='multiple', height=5)
    main_listbox.insert(0, '개인정보')
    main_listbox.insert(1, '랜덤')
    main_listbox.insert(2, '사물')
    main_listbox.insert(3, '중국풍')
    main_listbox.insert(4, '도시')
    main_listbox.insert(5, '사람')
    main_listbox.insert(5, '캐릭터')
    main_listbox.insert(6, '의성어')
    main_listbox.pack(fill=X, expand=True)
    main_listbox.bind('<<ListboxSelect>>', select_nameconcept)

    # 필수 단어 입력
    label = Label(main_frame, text="필수 단어 입력")
    label.pack(anchor="w", pady=7)
    word = Entry(main_frame, width=50)
    word.pack()

    # 닉네임 조합 선택
    label = Label(main_frame, text="닉네임 구성 선택")
    label.pack(anchor="w", pady=7)
    nametype = Combobox(main_frame, width=50, height=5, values=['영어', '영어 + 숫자', '한글', '한글 + 숫자', '한글 + 영어', '한글 + 영어 + 숫자'])
    nametype.current()
    nametype.bind('<<ComboboxSelected>>', select_nametype)
    # nametype.bind('<Return>', enter_item)
    nametype.pack()


    command_frame = LabelFrame(text='Command')
    command_frame.pack(fill=BOTH, padx=5, pady=5)
    Button(command_frame, command=result, text='Make Nickname').pack(side=LEFT, expand=True, fill=BOTH, padx=5, pady=5)
    # Button(command_frame, command=make_normal_folders, text='make normal_folders').pack(side=LEFT, expand=True, fill=BOTH, padx=5, pady=5)
    # Button(command_frame, command=move_files, text='move files').pack(side=LEFT, expand=True, fill=BOTH, padx=5, pady=5)

    window.bind_all('<Control-q>', stop)


def result(event=None):
    global command1_frame, result_frame, untaken_namelist, untaken_listbox

    window.update_idletasks()

    main_frame.destroy()
    command_frame.destroy()

    result_frame = LabelFrame()
    result_frame.pack()

    label = Label(result_frame, text="결과")
    label.pack(anchor="w", pady=7)
    history_listbox = Listbox(result_frame, selectmode='single', height=5, width=50)
    for n in range(0, len(namelist)):
        history_listbox.insert(n, namelist[n])
    history_listbox.pack(fill=X, expand=True)

    # scrollbar = Scrollbar(result_frame)
    # scrollbar.pack(side=RIGHT, fill=Y)
    # history_listbox.configure(yscrollcommand=scrollbar.set)
    # scrollbar.configure(command=history_listbox.yview)

    label = Label(result_frame, text="사용가능 닉네임")
    label.pack(anchor="w", pady=7)
    untaken_listbox = Listbox(result_frame, selectmode='single', height=5, width=50)
    untaken_listbox.pack(fill=X, expand=True)

    command1_frame = LabelFrame(text='Command')
    command1_frame.pack(fill=BOTH, padx=5, pady=5)
    Button(command1_frame, command=find_untaken_nickname, text='Find Untaken Nickname').pack(side=LEFT, expand=True, fill=BOTH, padx=5, pady=5)
    Button(command1_frame, command=Main, text='Back to Select').pack(side=LEFT, expand=True, fill=BOTH, padx=5, pady=5)

    window.bind_all('<Control-q>', stop)


Main()

window.mainloop()