#Download a youtube playulist automatically via youtube-mp3.org
import requests, bs4, os, time, webbrowser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://www.youtube-mp3.org/")
NEXT_BUTTON_XPATH = '//input[@type="submit" and @id="submit"]'

bet_fa = driver.find_element_by_id("youtube-url")
bet_fa.clear()
bet_fa.send_keys("https://www.youtube.com/") #Youtube playlist url here

button = driver.find_element_by_xpath(NEXT_BUTTON_XPATH)
button.click()

time.sleep(1)
down = driver.find_element_by_id("details").find_elements_by_tag_name('a')

for i in range(len(down)):
    if(len(down[i].get_attribute('href')) > 63 ):
        webbrowser.open_new_tab(down[i].get_attribute('href'))

