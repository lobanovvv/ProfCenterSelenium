from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.set_window_size(1920,1080)
driver.get("http://prodpo.ru")

elem = driver.find_element_by_css_selector("ul.menu-top > li > a > span")

actions = ActionChains(driver)
actions.move_to_element()