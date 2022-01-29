from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://sweardle.com")
time.sleep(3)
answer = driver.execute_script("return cs")
driver.close()
print(answer)
