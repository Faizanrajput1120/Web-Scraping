
from bs4 import BeautifulSoup as bs
from selenium import webdriver
import pandas as pd
# # Send a GET request to the webpage
# url = "https://www.flipkart.com/search?q=tv&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_8_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_8_0_na_na_na&as-pos=8&as-type=TRENDING&suggestionId=tv&requestId=9c9fa553-b7e5-454b-a65b-bbb7a9c74a29"
# response = requests.get(url)

# soup = bs(response.page_source, 'html.parser')
# #it gives us the visual representation of data
driver = webdriver.Chrome()
driver.get(f"https://www.flipkart.com/search?q=tv&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_8_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_8_0_na_na_na&as-pos=8&as-type=TRENDING&suggestionId=tv&requestId=9c9fa553-b7e5-454b-a65b-bbb7a9c74a29")
soup = bs(driver.page_source, 'html.parser')

# to get name of product
name=soup.find('div',class_="KzDlHZ")
print(name.text)


#get rating of a product
rating=soup.find('div',class_="XQDdHH")
print(rating.text)

#get other details and specifications of the product
specification=soup.find('div',class_="_6NESgJ")
spec=specification.find_all('li',class_='J+igdf')
for each in spec:
   print(each.text)

#get price of the product
price=soup.find('div',class_='Nx9bqj _4b5DiR')
print(price.text)

products=[]              #List to store the name of the product
prices=[]                #List to store price of the product
ratings=[]               #List to store rating of the product
apps = []                #List to store supported apps
os = []                  #List to store operating system
hd = []                  #List to store resolution
sound = []               #List to store sound output

for data in soup.findAll('div', class_='tUxRFH'):
   names = data.find('div', attrs={'class': 'KzDlHZ'})
   price = data.find('div', attrs={'class': 'Nx9bqj _4b5DiR'})
   rating = data.find('div', attrs={'class': 'XQDdHH'})
   specification = soup.find('div', class_="_6NESgJ")
   spec = specification.find_all('li', class_='J+igdf')
   for each in spec:
      app = spec[0].text
      os_ = spec[1].text
      hd_ = spec[2].text
      sound_ = spec[3].text
   products.append(names.text)  # Add product name to list
   prices.append(price.text)  # Add price to list
   apps.append(app)  # Add supported apps specifications to list
   os.append(os_)  # Add operating system specifications to list
   hd.append(hd_)  # Add resolution specifications to list
   sound.append(sound_)  # Add sound specifications to list
   ratings.append(rating.text)  # Add rating specifications to list

   # # printing the length of list
   # print(len(products))
   # print(len(ratings))
   # print(len(prices))
   # print(len(apps))
   # print(len(sound))
   # print(len(os))
   # print(len(hd_))
   # df=pd.DataFrame({'Product Name':products,'Supported_apps':apps,'sound_system':sound,'OS':os,"Resolution":hd,'Price':prices,'Rating':ratings})
   # df.head(10)

df = pd.DataFrame({
      'Product Name': products,
      'Supported_apps': apps,
      'sound_system': sound,
      'OS': os,
      "Resolution": hd,
      'Price': prices,
      'Rating': ratings
})

# Save the DataFrame to an Excel file
df.to_excel('output.xlsx', index=False)

print("Data saved to output.xlsx")