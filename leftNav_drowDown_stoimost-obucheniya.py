# Проверка линков (текст, переход) левоe навигационноe меню, подменю "Стоимость обучения" и его вкладки
# 
#   Описание теста:
#   - навигация до пункта
#   - проверка текста
#   - клик на пункт
#   - проверка url

from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.set_window_size(1920,1080)
driver.get("http://prodpo.ru")

link_url = [
"https://prodpo.ru/stoimost-obucheniya-dlya-byudzhetnykh-organizatsij.html"
]

link_text = [
"Стоимость обучения для бюджетных организаций"
]

# Переход к подпунктам меню "Стоимость обучения", с учетом изменения позиции пункта в дереве меню в дальнейшем
elem = driver.find_elements_by_css_selector("nav.menu-left-wrap > ul:first-of-type > li:nth-child(5) > a")
i = 0
lenArr = len(elem)

while i < lenArr:
    elem = driver.find_elements_by_css_selector("nav.menu-left-wrap > ul:first-of-type > li:nth-child(5) > a")
    if elem[i].text == "Стоимость обучения":
        elem[i].click()
    i += 1

# Проверка подменю, рекурсивно. Без учета изменения позиции подменю в дальнейшем.
i = 0
lenArr = len(link_text)

while i < lenArr:
    
    elem = driver.find_elements_by_css_selector("nav.menu-left-wrap > ul:first-of-type > li:nth-child(5) > ul > li > a")
    assert elem[i].text == link_text[i], "text fail"
    elem[i].click()
    assert driver.current_url == link_url[i], "url fail"

    i += 1
    
driver.quit()