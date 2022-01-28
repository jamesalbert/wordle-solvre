from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.powerlanguage.co.uk/wordle/")
game_app = driver.find_element_by_tag_name("game-app")
answer = driver.execute_script("return arguments[0].solution", game_app)
driver.close()
print(f"the answer to the puzzle is {answer}")
