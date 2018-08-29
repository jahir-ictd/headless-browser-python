from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re
import pandas as pd
from tabulate import tabulate


from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")
chrome_driver = "E:\\DevEnv\\ChromeDriver\\chromedriver.exe"


driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver)
driver.implicitly_wait(30)


driver.get("https://github.com/TheDancerCodes")

timeout = 20

try:
    WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.XPATH, "//img[@class='avatar width-full rounded-2']")))
except TimeoutException:
    print("Timed out waiting for page to load")
    driver.quit()

# find_elements_by_xpath returns an array of selenium objects.

titles_element = driver.find_elements_by_xpath("//a[@class='text-bold']")

# use list comprehension to get the actual repo titles and not the selenium objects.

titles = [x.text for x in titles_element]

# print out all the titles.

print('titles:')
print(titles, '\n')

language_element = driver.find_elements_by_xpath("//p[@class='mb-0 f6 text-gray']")

# same concept as for list-comprehension above.
languages = [x.text for x in language_element]

print("languages:")
print(languages, '\n')

for title, language in zip(titles, languages):
    print("RepoName : Language")
    print(title + ": " + language, '\n')














