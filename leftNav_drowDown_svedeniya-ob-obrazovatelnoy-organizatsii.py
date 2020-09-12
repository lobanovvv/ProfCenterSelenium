# Проверка линков (текст, переход) подменю "Сведения об образовательной организации"
# и его вкладок, левого навигационного меню
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
"https://prodpo.ru/osnovnyye-svedeniya",
"https://prodpo.ru/struktura-i-organy-upravleniya-obrazovatelnoy-organizatsiyey",
"https://prodpo.ru/dokumenty",
"https://prodpo.ru/obrazovaniye",
"https://prodpo.ru/obrazovatelnyye-standarty",
"https://prodpo.ru/rukovodstvo-pedagogicheskiy-sostav",
"https://prodpo.ru/materialno-tekhnicheskoye-obespecheniye-i-osnashchennost-obrazovatelnogo-protsessa",
"https://prodpo.ru/finansovo-khozyaystvennaya-deyatelnost",
"https://prodpo.ru/vakantnyye-mesta-dlya-priyema-perevoda"
]

link_text = [
"Основные сведения",
"Структура и органы управления образовательной организацией",
"Документы",
"Образование",
"Образовательные стандарты",
"Руководство. Педагогический состав",
"Материально-техническое обеспечение и оснащенность образовательного процесса",
"Финансово-хозяйственная деятельность",
"Вакантные места для приема(перевода)"
]

# Переход к подпунктам меню "Сведения об образовательной организации",
#  с учетом изменения позиции пункта в дереве меню в дальнейшем
elem = driver.find_elements_by_css_selector("nav.menu-left-wrap > ul:last-of-type > li:nth-child(7) > a")
i = 0
lenArr = len(elem)

while i < lenArr:
    elem = driver.find_elements_by_css_selector("nav.menu-left-wrap > ul:last-of-type > li:nth-child(7) > a")
    if elem[i].text == "Сведения об образовательной организации":
        elem[i].click()
    i += 1

# Проверка подменю, рекурсивно. Без учета изменения позиции подменю в дальнейшем.
i = 0
lenArr = len(link_text)

while i < lenArr:
    
    elem = driver.find_elements_by_css_selector("nav.menu-left-wrap > ul:last-of-type > li:nth-child(7) > ul > li > a")
    assert elem[i].text == link_text[i], "text fail"
    elem[i].click()
    assert driver.current_url == link_url[i], "url fail"

    i += 1
    
driver.quit()