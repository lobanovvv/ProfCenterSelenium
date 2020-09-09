from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
#from selenium.webdriver.remote.webelement import WebElement

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.set_window_size(1920,1080)
driver.get("http://prodpo.ru")

element = driver.find_elements_by_css_selector("ul.menu-top > li > a > span")
element.click()
assert driver.current_url == "https://prodpo.ru/obuchenije-po-professijam.html"

driver.quit()