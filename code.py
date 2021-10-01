# importing the required packages

from bs4 import BeautifulSoup 
import requests 
import csv
import pandas as pd


descriptions = [] # Create a list to store the descriptions
processors=[] # Create a list to store the processors
ram=[] # Create a list to store the ram
os=[] # Create a list to store the os
storage=[] # Create a list to store the storage
inches=[] # Create a list to store the inches
warranty=[] # Create a list to store the warranty
prices = [] # Create a list to store the prices
ratings = [] # Create a list to store the ratings

pages = list(range(1,10))
for page in pages:
  req = requests.get("https://www.flipkart.com/search?q=laptops&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off".format(page)).text # URL of the website which you want to scrape
  #content = req.content # Get the content
  soup = BeautifulSoup(req,'html.parser')
  #print(soup.prettify())

  desc = soup.find_all('div' , class_='_4rR01T')
  for i in range(len(desc)):
      descriptions.append(desc[i].text)
  len(descriptions)
  commonclass = soup.find_all('li',class_='rgWa7D') # We observe that the classnames for the different specifications are under one div.So we need to apply some method to extract the different features.
  # Create empty lists for the features
  for i in range(0,len(commonclass)):
    p=commonclass[i].text # Extracting the text from the tags
    if("Core" in p): 
        processors.append(p)
    elif("RAM" in p): 
        ram.append(p)
    elif("HDD" in p or "SSD" in p):
        storage.append(p)
    elif("Operating" in p):
        os.append(p)
    elif("Display" in p):
        inches.append(p)
    elif("Warranty" in p):
        warranty.append(p)

  price = soup.find_all('div',class_='_30jeq3 _1_WHN1') 
  # Extracting price of each laptop from the website
  for i in range(len(price)):
    prices.append(price[i].text)
    len(prices)  


print(len(descriptions))
print(len(processors))
print(len(ram))
print(len(os))
print(len(storage))
print(len(warranty))
print(len(inches))
print(len(prices))

df = {'Description':descriptions[90],'Processor':processors[90],'RAM':ram[90],'Operating System':os[slice(90)],'Storage':storage[slice(90)],'Display':inches[slice(90)],'Warranty':warranty[slice(90)],'Price':prices[slice(90)]}
dataset = pd.DataFrame(data = df) # Finally merging all the features into a single dataframe

dataset

dataset.to_excel("C://Users//rahul//Downloads//db//scraping.xlsx") # for saving dataset in excel format
