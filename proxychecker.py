#check if your proxies are working via infobyip.com/proxychecker.php
import requests, bs4, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chromeOptions = webdriver.ChromeOptions()
driver = webdriver.Chrome()
driver.get("https://www.infobyip.com/proxychecker.php")
NEXT_BUTTON_XPATH = '//input[@type="submit"]'
button = driver.find_element_by_xpath(NEXT_BUTTON_XPATH)
bet_fa = driver.find_element_by_xpath("//input[@name='url']")

url = "https://hidemy.name/en/proxy-list/#list"

res = requests.get(url)
soup = bs4.BeautifulSoup(res.text, 'html.parser')
proxys = soup.select('.proxy__t tbody tr')

for row in soup.table.find_all('tr')[1:]:
    print(row[0] )
