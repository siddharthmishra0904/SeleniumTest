from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path=r'C:\Users\hello\Downloads\chromedriver.exe')
driver.get("https://www.google.com/")
driver.maximize_window()
search_bar = driver.find_element_by_name("q")
search_bar.clear()
search_bar.send_keys("gametv.com")
search_bar.send_keys(Keys.RETURN)
element = driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div/div/div/div/div[1]/a/div/cite')
element.click()
element1 = driver.find_element_by_xpath('//*[@id="game_list"]/div/a')
element1.click()
content = driver.find_elements_by_xpath('//*[@id="game_list"]/ul')
for values in content:
    print(values.text)

driver.close()
