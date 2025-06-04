from bs4 import BeautifulSoup 
import requests
import pandas as pd
import json
from urllib.parse import urljoin
import os

'''
It's web_scraping for Books to Scrape Website
and save info in josn file and csv file and apply some analysis on it by pandas.
'''
books=[]

def star_rating(str):
  rate={'One':1,'Two':2,'Three':3,'Four':4,'Five':5}
  return rate[str]

def convert_price(str):
  return float(str.replace('£','').strip())

def send_equest(url):
  try:
      response=requests.get(url)
      print(response.status_code)
      soup=BeautifulSoup(response.content,'html.parser')
      return soup
  except:
    print('request falid.')
    return 0

def add_des_to_textfile(path,text):
  os.makedirs('Descriptions',exist_ok=True)
  with open(f'Descriptions/{path}.txt','w') as file:
    file.write(text)

def book_info(urll,name):
  t={}
  soup=send_equest(urll)
  info_table=soup.find('table',class_='table table-striped')
  # print(info_table.prettify())
  desc_book=soup.find_all('p')[3]
  add_des_to_textfile(name,desc_book.text)
  for item in info_table.find_all('tr'):
    if item.find('th').text =='Price (excl. tax)':
      t['Price (excl. tax)']=convert_price(item.find('td').text)
      t['Desription']=f'{name}.txt'
      continue
    if item.find('th').text =='Price (incl. tax)':
      t['Price (incl. tax)']=convert_price(item.find('td').text)
      t['Desription']=f'{name}.txt'
      continue
    t[item.find('th').text]=item.find('td').text
    t['Desription']=f'{name}.txt'
  return t

def find_book_table(url,soup):
  book_table=soup.find_all('div',class_='row')[1]
  for listt in book_table.find_all('li',class_='col-xs-6 col-sm-4 col-md-3 col-lg-3') :
    book={}
    book['title']=listt.find('h3').find('a')['title']
    book['img']=f' {urljoin(url,listt.find('img')['src'])} '
    book['link_of_book']=f' {urljoin(url,listt.find('a')['href'])} '
    book['book_info']=book_info(book['link_of_book'].strip(),str(book['title']))
    book['rate_of_five']= star_rating(str(listt.find('p')['class'][1]))
    books.append(book)

def save_data_to_csv(path):
  df=pd.DataFrame(books)
  df.to_csv(path)

def save_data_to_json(path):
  # df=pd.DataFrame(books)
  # df.to_json(path)
  with open(path,"w") as js:
    json.dump(books,js,indent=4)

def main():
  page=1
  while True:
    url=f'https://books.toscrape.com/catalogue/page-{1}.html'
    if page==2:
        break
    soup=send_equest(url)
    if soup==0:
      break
    is_books=soup.select_one('li',class_='col-xs-6 col-sm-4 col-md-3 col-lg-3')
    if not is_books:
      print(f'the page {page} is empty.')
      break
    find_book_table(url,soup)
    print(f'Page =>{page} is done.')
    page+=1
  save_data_to_csv('allBooks.csv')
  save_data_to_json('allBooks.json')

print('='*50)
print('='*50)
print('='*2,' Weclom to scrape [books.toscrape.com] websit.','='*2,sep='')
print('='*50)
print('='*50)
main()
print('='*50)
print('='*50)
print('ALL book are add successfully.')
print('='*50)
print('='*50)