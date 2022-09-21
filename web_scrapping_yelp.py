import requests
import pandas as pd
from bs4 import BeautifulSoup

response = requests.get("https://www.yelp.com/search?cflt=restaurants&find_loc=San+Francisco%2C+CA") 
soup = BeautifulSoup(response.content,'html.parser')

names = soup.find_all('a',class_='css-1kb4wkh')
name = []
for i in names:
  d = i.get_text()
  name.append(d)
print(name[2:])
images = soup.find_all('img', class_=' css-xlzvdl')
image = []
for i in images:
  d = i['src']
  image.append(d)
print(image)

df = pd.DataFrame()
df['name of hotel'] = name[2:]
df['image url'] = image
print(df)
#df.to_csv("hotel_data.csv")