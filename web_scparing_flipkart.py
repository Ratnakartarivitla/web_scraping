# web scparing

import requests
import pandas as pd
from bs4 import BeautifulSoup

response = requests.get("https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&p%5B%5D=facets.brand%255B%255D%3DPOCO&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InRpdGxlIjp7Im11bHRpVmFsdWVkQXR0cmlidXRlIjp7ImtleSI6InRpdGxlIiwiaW5mZXJlbmNlVHlwZSI6IlRJVExFIiwidmFsdWVzIjpbIlNob3AgTm93Il0sInZhbHVlVHlwZSI6Ik1VTFRJX1ZBTFVFRCJ9fX19fQ%3D%3D&otracker=clp_metro_expandable_2_3.metroExpandable.METRO_EXPANDABLE_Shop%2BNow_mobile-phones-store_O1WYX08RHODP_wp2&fm=neo%2Fmerchandising&iid=M_3e531675-b2c2-4550-8056-21b8385ec626_3.O1WYX08RHODP&ppt=clp&ppn=mobile-phones-store&ssid=gedx73jaao0000001660814047341")
soup = BeautifulSoup(response.content,'html.parser')

names = soup.find_all('div', class_='_4rR01T')
name = []
for i in names:
  d = i.get_text()
  name.append(d)

prices = soup.find_all('div' , class_='_30jeq3 _1_WHN1')
price = []
for i in prices:
  d = i.get_text()
  s = d[1:]
  price.append(s)

rates = soup.find_all('div', class_='_3LWZlK')
rate = []
for i in rates:
  d = float(i.get_text())
  rate.append(d)  

images = soup.find_all('img', class_="_396cs4 _3exPp9")
image = []
for i in images:
  d = i['src']
  image.append(d)

links = soup.find_all('a',class_='_1fQZEK')
link = []
for i in links:
  d = "https://www.flipkart.com"+i['href']
  link.append(d)


df = pd.DataFrame()
df["name of mobile"] = name
df["mobile price"] = price
df["mobile rating"] = rate
df["mobile image"] = image
df["moobile link"] = link
#df.to_csv("mobile_data.csv")
print(df)