# Проверка линков (текст, переход) выпадающего меню "Электробезопасность"
#  в верхнем навигационном меню
# 
# Описание теста:
#   - раскрытие меню
#   - проверка текста ссылки
#   - ЛКМ по ссылке
#   - проверка обновленного url

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.set_window_size(1920,1080)
driver.get("http://prodpo.ru")

link_url = [
"https://prodpo.ru/instruktazhi-i-obuchenie-po-elektrobezopasnosti-v-moskve/2-gruppa.html",
"https://prodpo.ru/obucheniye-po-elektrobezopasnosti-na-3-gruppu-dopuska",
"https://prodpo.ru/instruktazhi-i-obuchenie-po-elektrobezopasnosti-v-moskve/4-gruppa.html"
]

link_name = [
"2 группа допуска",
"3 группа допуска",
"4 группа допуска"
]

i = 0
lenArr = len(link_url)
while i < lenArr:
    
    elem = driver.find_element_by_css_selector("ul.menu-top > li:nth-child(5) > a > span")
    
    actions = ActionChains(driver)
    actions.move_to_element(elem)
    actions.perform()

    elem = driver.find_elements_by_css_selector("ul.menu-top > li:nth-child(5) > ul > li > a > span")
    assert elem[i].text == link_name[i], "name fail"
    elem[i].click()
    assert driver.current_url == link_url[i], "url fail"
    
    i += 1

driver.quit()
