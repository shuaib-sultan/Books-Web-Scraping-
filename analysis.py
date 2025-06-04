import pandas as pd
import numpy as np
import json
y=[]
with open('allBooks.json','r') as js:
  y=json.load(js)
df= pd.json_normalize(y)
# ... make the title is the index of the books ...
df.set_index('title',inplace=True)
# ...Sorting BY title...
df.sort_values('title',inplace=True)
#... get  most expisev book ..
df['book_info.Price (excl. tax)'].idxmax()
#... get the sheap book ...
df['book_info.Price (excl. tax)'] .idxmin()
#...resetindex to defult number...
df.reset_index(inplace=True,drop=True)
#... Groubing BY rate....
u=df.groupby('rate_of_five')["book_info.Price (excl. tax)"].agg(['sum','count','mean'])
u.to_csv('rating_analysis.csv')
# ...Gave index the most rate on rate_of_five...
u['count'].idxmax()
print(f'the number of books that has reat 1 is {u.at[1,"count"]}')
print(f'the number of books that has reat 2 is {u.at[2,"count"]}')
print(f'the number of books that has reat 3 is {u.at[3,"count"]}')
print(f'the number of books that has reat 4 is {u.at[4,"count"]}')
print(f'the number of books that has reat 5 is {u.at[5,"count"]}')