from tkinter import *
from tkinter.ttk import *
from bs4 import BeautifulSoup
import csv
import re
import exrex
import logging
import requests
import random


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

user_agent = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36'
}

namelist = []
untaken_namelist = []
nametuple = ()
find = False
nword = ['민서', '가나다라마바사', '고고']
cword = ['방탄기공']
eword = ['charlly', 'shelly']

keyword = ''
url = ''
game = ''
type = ''

def stop():
    window.quit()


def scrapword():
    global nword, cword, eword
    surl = 'https://namu.wiki/w/분류:프랑스어%20단어?namespace=문서&cfrom=실루엣'
    r = requests.get(surl, headers=user_agent)
    soup = BeautifulSoup(r.text, 'lxml')
    elms = soup.select('div[class="_1729KulV"] a')
    for e in elms:
        nword.append(e.text)

    surl = 'https://namu.wiki/w/분류:프랑스어%20단어?namespace=문서&cuntil=시스'
    r = requests.get(surl, headers=user_agent)
    soup = BeautifulSoup(r.text, 'lxml')
    elms = soup.select('div[class="_1729KulV"] a')
    for e in elms:
        nword.append(e.text)

    surl = 'https://namu.wiki/w/분류:라틴어%20단어?namespace=문서&cfrom=솔리움%20마키나%3A%20루멘'
    r = requests.get(surl, headers=user_agent)
    soup = BeautifulSoup(r.text, 'lxml')
    elms = soup.select('div[class="_1729KulV"] a')
    for e in elms:
        nword.append(e.text)

    surl = 'https://namu.wiki/w/분류:그리스어%20단어'
    r = requests.get(surl, headers=user_agent)
    soup = BeautifulSoup(r.text, 'lxml')
    elms = soup.select('div[class="_1729KulV"] a')
    for e in elms:
        nword.append(e.text)

    surl = 'https://namu.wiki/w/분류:스페인어%20단어'
    r = requests.get(surl, headers=user_agent)
    soup = BeautifulSoup(r.text, 'lxml')
    elms = soup.select('div[class="_1729KulV"] a')
    for e in elms:
        nword.append(e.text)

    surl = 'https://namu.wiki/w/분류:스페인어%20단어'
    r = requests.get(surl, headers=user_agent)
    soup = BeautifulSoup(r.text, 'lxml')
    elms = soup.select('div[class="_1729KulV"] a')
    for e in elms:
        nword.append(e.text)

    surl = 'https://namu.wiki/w/무협소설/용어'
    r = requests.get(surl, headers=user_agent)
    soup = BeautifulSoup(r.text, 'lxml')
    elms = soup.find_all(class_=re.compile(r'^DcHFMcm1'))
    for e in elms:
        cword.append(e.text)

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


def select_nametype(event=None):
    global type
    text = nametype.get()
    type = text

def select_namelen(event=None):
    global namesize
    text = nametype.get()
    size_re = re.compile(r'\d{1,2}')
    text = size_re.findall(text)
    namesize = int(text[len(text)-1])


def select_nameconcept(event=None):
    global nametuple
    text = main_listbox.curselection()
    nametuple = text


def make_nickname():
    global word, nametuple, type, find, namelist, history_listbox, namesize, nword, cword, eword
    try:
        word.get()
    except:
        pass
    namelist = []
    temp = random.choice(nword)
    name_re = re.compile(r'[0-9]{1,2}')  # 영어숫자조합 10자 이상
    # name_re = re.compile(r'')
    # check_re = re.compile(r'영어')
    # if check_re.findall(type):
    #     name_re = re.compile(r'[a-z]{4,5}[0-9]{1,2}')  # 영어숫자조합 10자 이상
    #
    # check_re = re.compile(r'한글')
    # if check_re.findall(type):
    #     name_re = re.compile(r'[a-z]{4,5}[0-9]{1,2}')  # 영어숫자조합 10자 이상
    temp = temp + exrex.getone(name_re.pattern, 2)
    # temp = exrex.getone(name_re.pattern, 2)
    if namesize - 5 <= len(temp) <= namesize:
        namelist.append(temp)

    if find:
        result()
    else:
        history_listbox.delete('0', END)
        for n in range(0, len(namelist)):
            history_listbox.insert(n, namelist[n])


def find_untaken_nickname():
    global keyword, game, untaken_namelist, untaken_listbox, url

    untaken_namelist = []
    untaken_listbox.delete('0', END)

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
        for e in elms:
            untaken_namelist.append(name)
            print(e.text)

        if not elms:
            print('False')
    # find = True
    for n in range(0, len(untaken_namelist)):
        untaken_listbox.insert(n, namelist[n])


scrapword()
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
history_listbox = Listbox()


def Main(event=None):
    global Gameselect, nametype, main_listbox, word, main_frame, command_frame, untaken_namelist, find

    find = True
    result_frame.destroy()
    command1_frame.destroy()

    main_frame = LabelFrame()
    main_frame.pack()

    untaken_namelist = []

    # 게임 선택
    label = Label(main_frame, text="게임 선택")
    label.pack(anchor="w", pady=7)
    Gameselect = Combobox(main_frame, width=50, height=5, values=['로스트아크', 'LoL', '배틀그라운드', '메이플스토리', '마인크래프트'])
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
    main_listbox.insert(3, '무협')
    main_listbox.insert(5, '사람')
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
    nametype.pack()

    # 닉네임 글자수 선택
    label = Label(main_frame, text="닉네임 글자 수 선택")
    label.pack(anchor="w", pady=7)
    nametype = Combobox(main_frame, width=50, height=5, values=['5글자 이내', '5글자 ~ 10글자', '10글자 ~ 15글자'])
    nametype.current()
    nametype.bind('<<ComboboxSelected>>', select_namelen)
    nametype.pack()


    command_frame = LabelFrame(text='Command')
    command_frame.pack(fill=BOTH, padx=5, pady=5)
    Button(command_frame, command=make_nickname, text='Make Nickname').pack(side=LEFT, expand=True, fill=BOTH, padx=5, pady=5)

    window.bind_all('<Control-q>', stop)


def result(event=None):
    global command1_frame, result_frame, untaken_namelist, untaken_listbox, find, namelist, history_listbox

    find = False
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
    Button(command1_frame, command=find_untaken_nickname, text='Find Nickname').pack(side=LEFT, expand=True, fill=BOTH, padx=5, pady=5)
    Button(command1_frame, command=make_nickname, text='ReMake').pack(side=LEFT, expand=True, fill=BOTH, padx=5, pady=5)
    Button(command1_frame, command=Main, text='Back').pack(side=LEFT, expand=True, fill=BOTH, padx=5, pady=5)

    window.bind_all('<Control-q>', stop)


Main()

window.mainloop()