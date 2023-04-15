import time
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

url = 'https://www.tokopedia.com/search?navsource=&q=smartphone&srp_component_id=02.01.00.00&srp_page_id=&srp_page_title=&st=product'
driver = webdriver.Chrome()
driver.get(url)

data = []
for page in range(1,10):
    page_url = 'https://www.tokopedia.com/search?navsource=&page={}&q=smartphone&srp_component_id=02.01.00.00&srp_page_id=&srp_page_title=&st=product'.format(page)
    driver.get(page_url)
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#zeus-root")))
    time.sleep = 3

    for j in range (21):
        driver.execute_script("window.scrollBy(0, 300)")
        time.sleep = 2
        
    driver.execute_script("window.scrollBy(50, 0)")
    time.sleep = 2

    soup = BeautifulSoup(driver.page_source, "html.parser")
    for item in soup.findAll('div', class_='css-974ipl'):
        product_name = item.find('div', class_='css-3um8ox').text
        price = item.find('div', class_='css-1ksb19c').text

        for item2 in soup.findAll('div', class_='css-1rn0irl'):
            location = item2.findAll('span', class_='css-1kdc32b')[0].text
            shop_name = item2.findAll('span', class_='css-1kdc32b')[1].text

        rtng = item.findAll('span', class_= 'css-t70v7i')
        if len(rtng) > 0:
            rating = item.find('span', class_= 'css-t70v7i').text
        else :
            rating = ''

        sld = item.findAll('span', class_= 'css-1duhs3e')
        if len(sld) > 0:
            sold = item.find('span', class_= 'css-1duhs3e').text
        else :
            sold = ''
       
        data.append(
            (product_name, price, location, shop_name, rating, sold)
        )

    time.sleep = 2

df = pd.DataFrame(data, columns=[product_name, price, location, shop_name, rating, sold])
df.to_excel('tokped_smarthone.xlsx', index=False)
print('data is saved')

