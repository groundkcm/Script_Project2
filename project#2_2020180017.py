import time
from tkinter import *
from tkinter.ttk import *
from bs4 import BeautifulSoup
import csv
import re
import exrex
import logging
import requests
import random
import cloudscraper

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

user_agent = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
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
inword = ''

def stop():
    window.quit()


def scrapword():
    global nword, cword, eword

    for i in range(7):
        if i == 0:
            surl = 'https://namu.wiki/w/분류:프랑스어%20단어?namespace=문서&cfrom=실루엣'
        elif i == 1:
            surl = 'https://namu.wiki/w/분류:프랑스어%20단어?namespace=문서&cuntil=시스'
        elif i == 2:
            surl = 'https://namu.wiki/w/분류:라틴어%20단어?namespace=문서&cfrom=솔리움%20마키나%3A%20루멘'
        elif i == 3:
            surl = 'https://namu.wiki/w/분류:그리스어%20단어'
        elif i == 4:
            surl = 'https://namu.wiki/w/분류:스페인어%20단어'
        elif i == 5:
            surl = 'https://namu.wiki/w/분류:영어%20단어?namespace=문서&cfrom=Moon'
        scraper = cloudscraper.CloudScraper()
        soup = BeautifulSoup(scraper.get(surl).text, 'lxml')
        elms = soup.select('div[class="yLP12cjc"] a')
        if i <= 4:
            for e in elms:
                nword.append(e.string)
        elif i == 5:
            for e in elms:
                eword.append(e.string)

    surl = 'https://namu.wiki/w/무협소설/용어'
    scraper = cloudscraper.create_scraper()
    soup = BeautifulSoup(scraper.get(surl).text, 'lxml')
    elms = soup.find_all(class_=re.compile(r'^DcHFMcm1'))
    for e in elms:
        cword.append(e.text)

    with open('단어.txt', 'w', encoding='utf-8') as f:
        for word in nword:
            f.write(word + ' ')
        f.write('\n')
        for word in eword:
            f.write(word + ' ')
        f.write('\n')
        for word in cword:
            f.write(word + ' ')
    print(nword)
    print(eword)
    print(cword)

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
    text = namelen.get()
    size_re = re.compile(r'\d{1,2}')
    text = size_re.findall(text)
    namesize = int(text[len(text)-1])


def select_nameconcept(event=None):
    global nametuple, ctext
    try:
        ctext = main_listbox.get(main_listbox.curselection())
    except:
        pass
    nametuple = ctext


def make_nickname():
    global word, nametuple, type, find, namelist, history_listbox, namesize, nword, cword, eword, inword
    try:
        inword = str(word.get())
    except:
        pass
    namelist = []
    if type == '영어 + 숫자':
        for _ in range(10):
            if nametuple == '랜덤':
                name_re = re.compile(r'[a-z]{3,}[0-9]{1,2}')
                temp = inword + exrex.getone(name_re.pattern, 2)
                namelist.append(temp)
            else:
                temp = random.choice(eword)
                name_re = re.compile(r'[0-9]{1,2}')
                temp = inword + temp + exrex.getone(name_re.pattern, 2)
                if namesize - 5 <= len(temp) <= namesize:
                    namelist.append(temp)
    elif type == '영어':
        for _ in range(10):
            if nametuple == '랜덤':
                name_re = re.compile(r'[a-z]{4,5}')
                temp = inword + exrex.getone(name_re.pattern, 2)
                namelist.append(temp)
            else:
                temp = random.choice(eword)
                temp = inword + temp
                if namesize - 5 <= len(temp) <= namesize:
                    namelist.append(temp)
    elif type == '한글 + 숫자':
        for _ in range(10):
            if nametuple == '무협(한글)':
                temp = random.choice(cword)
                name_re = re.compile(r'[0-9]{1,2}')
            else:
                temp = random.choice(nword)
                name_re = re.compile(r'[0-9]{1,2}')
            temp = inword + temp + exrex.getone(name_re.pattern, 2)
            if namesize - 5 <= len(temp) <= namesize:
                namelist.append(temp)
    elif type == '한글':
        for _ in range(10):
            if nametuple == '무협(한글)':
                temp = random.choice(cword)
            else:
                temp = random.choice(nword)
            temp = inword + temp
            if namesize - 5 <= len(temp) <= namesize:
                namelist.append(temp)
    elif type == '한글 + 영어':
        for _ in range(10):
            if nametuple == '무협(한글)':
                temp = random.choice(cword)
            else:
                temp = random.choice(nword)
            etemp = random.choice(eword)
            temp = inword + temp + etemp
            if namesize - 5 <= len(temp) <= namesize:
                namelist.append(temp)
    elif type == '한글 + 영어 + 숫자':
        for _ in range(10):
            if nametuple == '무협(한글)':
                temp = random.choice(cword)
            else:
                temp = random.choice(nword)
            etemp = random.choice(eword)
            name_re = re.compile(r'[0-9]{1,2}')
            temp = inword + temp + etemp + exrex.getone(name_re.pattern, 2)
            if namesize - 5 <= len(temp) <= namesize:
                namelist.append(temp)
    if find:
        result()
    else:
        history_listbox.delete('0', END)
        for n in range(0, len(namelist)):
            history_listbox.insert(n, namelist[n])


def find_untaken_nickname():
    global keyword, game, untaken_listbox, url
    emptyname = True
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
        if not elms:
            logging.info('*taken*')
            continue

        if game == '메이플스토리':
            istake = False
            for e in elms:
                print(e)
                nre = re.compile(r'마지막 활동일')
                gre = re.compile(r'길드 이름')
                if nre.search(e.text):
                    logging.info('*taken*')
                    istake = True
                    break
                elif gre.split(e.text):
                    logging.info(name)
                    untaken_listbox.insert(END, name)
                    emptyname = False
                    istake = True
                    break
            if istake:
                continue

        emptyname = False
        for e in elms:
            logging.info(name)
            untaken_listbox.insert(END, name)
    if emptyname:
        untaken_listbox.insert(END, 'None')
    logging.info('---------')

# scrapword()
with open('단어.txt', 'r', encoding='utf-8') as f:
    readwords = f.readline()
    if readwords:
        nword = readwords.split()
    readwords = f.readline()
    if readwords:
        eword = readwords.split()
    readwords = f.readline()
    if readwords:
        cword = readwords.split()
    f.close()
    print(nword)
    print(eword)
    print(cword)

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
    global Gameselect, nametype, main_listbox, namelen, word, main_frame, command_frame, untaken_namelist, find

    find = True
    result_frame.destroy()
    command1_frame.destroy()

    main_frame = LabelFrame()
    main_frame.pack()

    untaken_namelist = []

    # 게임 선택
    label = Label(main_frame, text="게임 선택")
    label.pack(anchor="w", pady=7)
    Gameselect = Combobox(main_frame, width=50, height=5, values=['로스트아크', 'LoL', '배틀그라운드', '메이플스토리'])
    Gameselect.current()
    Gameselect.bind('<<ComboboxSelected>>', select_game)
    Gameselect.pack()

    # 테마 선택
    label = Label(main_frame, text="닉네임 컨셉 선택")
    label.pack(anchor="w")
    main_listbox = Listbox(main_frame, selectmode='single', height=5)
    main_listbox.insert(0, '기본')
    main_listbox.insert(1, '랜덤')
    main_listbox.insert(2, '무협(한글)')
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
    namelen = Combobox(main_frame, width=50, height=5, values=['5글자 이내', '5글자 ~ 10글자', '10글자 ~ 15글자'])
    namelen.current()
    namelen.bind('<<ComboboxSelected>>', select_namelen)
    namelen.pack()


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