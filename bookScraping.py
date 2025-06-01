from bs4 import BeautifulSoup 
import requests
import pandas as pd
import json
from urllib.parse import urljoin
'''
It's web_scraping for Books to Scrape Website
and save info in josn file and csv file and apply some analysis on it by pandas.
'''
books=[]
def star_rating(str):
  rate={'One':1,'Two':2,'Three':3,'Four':4,'Five':5}
  return rate[str]

def send_equest(page):
  try:
      global url
      url=f'https://books.toscrape.com/catalogue/page-{page}.html'
      response=requests.get(url)
      soup=BeautifulSoup(response.content,'html.parser')
      return soup
  except:
    return 0

def find_book_table(soup):
  book_table=soup.find_all('div',class_='row')[1]  
  for listt in book_table.find_all('li',class_='col-xs-6 col-sm-4 col-md-3 col-lg-3') :
    book={}
    book['title']=listt.find('h3').find('a')['title']
    book['img']=urljoin(url,listt.find('img')['src'])
    book['link']=urljoin(url,listt.find('a')['href'])
    book['rate_of_five']= star_rating(str(listt.find('p')['class'][1]))
    books.append(book)

def save_data_to_csv(path):
  df=pd.DataFrame(books)
  df.to_csv(path)

def save_data_to_json(path):
  with open(path,"w") as js:
    json.dump(books,js,indent=4)

def analysis_data(path):# symple analysis by pandas
  df=pd.read_csv(path,index_col=0)
  df.set_index('title')
  five_rate=df[df['rate_of_five'] == 5].sort_values('title').reset_index(drop=True)
  five_rate.to_csv('five_rate.csv')
  under_three_rate=df[df['rate_of_five']<3].sort_values('title').reset_index(drop=True)
  under_three_rate.to_csv('under_three_rate.csv')

def main():
  page=1
  soup=send_equest(page)
  while True:
    if page==51:
        break
    if soup==0:
      break
    is_books=soup.select_one('li',class_='col-xs-6 col-sm-4 col-md-3 col-lg-3')
    if not is_books:
      print(f'the page {page} is empty.')
      break
    find_book_table(soup)
    print(f'Page =>{page} is done.')
    page+=1
  save_data_to_csv('allBooks.csv')
  save_data_to_json('allBooks.json')
  analysis_data('allBooks.csv')

main()
print('='*50)
print('ALL book are add successfully.')
print('='*50)



