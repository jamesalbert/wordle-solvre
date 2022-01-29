from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.powerlanguage.co.uk/wordle/")
game_app = driver.find_element_by_tag_name("game-app")
answer = driver.execute_script("return arguments[0].solution", game_app)
driver.close()
print(answer)
