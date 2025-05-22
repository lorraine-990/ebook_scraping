import requests as req
from bs4 import BeautifulSoup as bs
import regex as re
import os, random
from time import sleep
import subprocess

# 取得頁面
url = req.get('https://www.gutenberg.org/browse/languages/zh')
soup = bs(url.text, 'lxml')

# 正則規則
zh_only = r'[\u4e00-\u9fff]+'
re_url = r'\/'
re_content = r'\*\*\*' 
rm_eng = r'[A-Za-z\'\,\:\-\(\)\_]{2,}'

# 取得書名和書本內文連結
url_prefix = 'https://www.gutenberg.org'
li_book = []

for a in soup.select("li.pgdbetext > a[href]"):
    re_title = re.match(zh_only, a.get_text())
    if re_title != None:
        book_num = re.split(re_url, a.get("href"))[-1]
        li_book.append(
            {
                'title': re_title.group(),
                'link': url_prefix + f'/cache/epub/{book_num}/pg{book_num}.txt'
            }
        )
        
# 創建放書的資料夾
folder_path = './project_gutenberg'
if not os.path.exists(folder_path):
    os.mkdir(folder_path)

# 讀取每一本內容
i = 0
all_files_path = []
for book in li_book:
    book_content = req.get(book["link"])
    soup_content = bs(book_content.text, 'lxml')
    
    # 移除非內文內容
    split_content = re.split(re_content, soup_content.get_text())[2]
    # 移除非中文內容
    main_content = re.sub(rm_eng, '', split_content).strip()
    # 寫入 list
    book['content'] = main_content

    # 建立檔案路徑清單
    file_path = f'{folder_path}/{book['title']}.txt'
    all_files_path.append(file_path)

    # 建檔，移除重複項
    if not os.path.exists(file_path):
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(book['content'])
            i += 1
            print(f'{i}. {book['title']} 已寫入')
            sleep(1)

# 隨機打開三個
selected_f = random.sample(all_files_path, 3)
for open_f in selected_f:
    subprocess.call(["open", open_f])
    
