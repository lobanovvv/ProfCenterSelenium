# Проверка линков (текст, переход) левоe навигационноe меню, подменю "Виды обучения" и его вклади
# 
#   Описание теста:
#   - навигация до пункта
#   - проверка текста
#   - клик на пункт
#   - проверка url
# 
# Обнаружен баг "Пункт меню Бухгалтерский учет и налогообложение сворачивает ветку пункта меню "Виды обучения"
# Может сбоить из-за долгого открытия меню, лечится слипом в 67 строке. При появлении сбоя попробовать увеличить время слипа

import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.set_window_size(1920,1080)
driver.get("http://prodpo.ru")

link_url = [
"https://prodpo.ru/obuchenie-po-okhrane-truda.html",
"https://prodpo.ru/bezopasnost-dorozhnogo-dvizheniya",
"https://prodpo.ru/specialist-kadrovoj-sluzhby",
"https://prodpo.ru/kursy-po-nalogooblozheniyu",
"https://prodpo.ru/bezopasnyye-raboty-na-vysote.html",
"https://prodpo.ru/obuchenie-po-pozharnoi-bezopasnosti.html",
"https://prodpo.ru/instruktazhi-i-obuchenie-po-elektrobezopasnosti-v-moskve.html",
"https://prodpo.ru/obuchenie-po-teplovym-energoustanovkam-ptete.html",
"https://prodpo.ru/obuchenie-po-promyshlennoj-bezopasnosti.html",
"https://prodpo.ru/obuchenie-bezopasnaya-ekspluatatsiya-liftov",
"https://prodpo.ru/obuchenije-po-professijam.html",
"https://prodpo.ru/obuchenie-po-ekologicheskoj-bezopasnosti.html",
"https://prodpo.ru/go-i-chs"
]

link_text = [
"Охрана труда",
"Безопасность дорожного движения",
"Специалист кадровой службы",
"Бухгалтерский учёт и налогообложение",
"Безопасные работы на высоте",
"Пожарная безопасность",
"Элeктpoбeзoпacнocть",
"Обучение по тепловым энергоустановкам - ПТЭТЭ",
"Пpoмбeзoпacнocть",
"Безопасная эксплуатация лифтов",
"Обучение по профессиям",
"Экологическая безопасность",
"ГО и ЧС"
]

# Переход к подпунктам меню "Виды обучения", с учетом изменения позиции пункта в дереве меню в дальнейшем
elem = driver.find_elements_by_css_selector("ul.left-menu > li > a")
i = 0
lenArr = len(elem)

while i < lenArr:
    elem = driver.find_elements_by_css_selector("ul.left-menu > li > a")
    if elem[i].text == "Виды обучения":
        elem[i].click()
    i += 1

# Проверка подменю, рекурсивно. Без учета изменения позиции подменю в дальнейшем.
i = 0
lenArr = len(link_text)

while i < lenArr:
    
    time.sleep(0.5)
    
    # Обход бага "Пункт меню Бухгалтерский учет и налогообложение сворачивает ветку пункта меню "Виды обучения""
    if driver.current_url == "https://prodpo.ru/kursy-po-nalogooblozheniyu":
        elem_l2 = driver.find_elements_by_css_selector("ul.left-menu > li > a")
        i_l2 = 0
        lenArr_l2 = len(elem_l2)

        while i_l2 < lenArr_l2:
            elem_l2 = driver.find_elements_by_css_selector("ul.left-menu > li > a")
            if elem_l2[i_l2].text == "Виды обучения":
                elem_l2[i_l2].click()
            i_l2 += 1

    elem = driver.find_elements_by_css_selector("ul.left-menu > li:first-child > ul.level-2 > li > a")
    assert elem[i].text == link_text[i], "text fail"
    elem[i].click()
    assert driver.current_url == link_url[i], "url fail"
    
    # Рекурсия в пункте "Охрана труда"
    elem = driver.find_elements_by_css_selector("ul.left-menu > li:first-child > ul.level-2 > li > a")
    if elem[i].text == "Охрана труда":
        elem_ohranaTruda = driver.find_element_by_css_selector("ul.level-2 > li:first-child > ul.level-3 > li > a")
        assert elem_ohranaTruda.text == "Дистанционное обучение"
        elem_ohranaTruda.click()
        assert driver.current_url == "https://prodpo.ru/obuchenie-po-okhrane-truda-distancionno.html"
    
    # Рекурсия в пункте "Пожарная безопасность"
    elem = driver.find_elements_by_css_selector("ul.left-menu > li:first-child > ul.level-2 > li > a")
    if elem[i].text == "Пожарная безопасность":
        elem_fireSec = driver.find_element_by_css_selector("ul.level-2 > li:nth-child(6) > ul.level-3 > li > a")
        assert elem_fireSec.text == "Обучение ПТМ (пожарно-технический минимум) в Москве"
        elem_fireSec.click()
        assert driver.current_url == "https://prodpo.ru/pogarno-technicheskij-minimum.html"
    
     # Рекурсия в пункте "Элeктpoбeзoпacнocть"
    elem = driver.find_elements_by_css_selector("ul.left-menu > li:first-child > ul.level-2 > li > a")
    if elem[i].text == "Элeктpoбeзoпacнocть":
        elem_electroSec = driver.find_elements_by_css_selector("ul.level-2 > li:nth-child(7) > ul.level-3 > li > a")
        assert elem_electroSec[0].text == "2 группа допуска"
        assert elem_electroSec[1].text == "4 группа допуска"
        
        elem_electroSec[0].click()
        assert driver.current_url == "https://prodpo.ru/instruktazhi-i-obuchenie-po-elektrobezopasnosti-v-moskve/2-gruppa.html"
        
        elem_electroSec = driver.find_elements_by_css_selector("ul.level-2 > li:nth-child(7) > ul.level-3 > li > a")
        elem_electroSec[1].click()
        assert driver.current_url == "https://prodpo.ru/instruktazhi-i-obuchenie-po-elektrobezopasnosti-v-moskve/4-gruppa.html"

    # Рекурсия в пункте "Экологическая безопасность"
    elem = driver.find_elements_by_css_selector("ul.left-menu > li:first-child > ul.level-2 > li > a")
    if elem[i].text == "Экологическая безопасность":
        elem_ecoSec = driver.find_element_by_css_selector("ul.level-2 > li:nth-child(12) > ul.level-3 > li > a")
        assert elem_ecoSec.text == "Дистанционные курсы"
        elem_ecoSec.click()
        assert driver.current_url == "https://prodpo.ru/obuchenie-po-ekologicheskoj-bezopasnosti-distancionnoe.html"

    # Рекурсия в пункте "ГО и ЧС"
    elem = driver.find_elements_by_css_selector("ul.left-menu > li:first-child > ul.level-2 > li > a")
    if elem[i].text == "ГО и ЧС":
        elem_goChs = driver.find_element_by_css_selector("ul.level-2 > li:nth-child(13) > ul.level-3 > li > a")
        assert elem_goChs.text == "Дистанционное обучение"
        elem_goChs.click()
        assert driver.current_url == "https://prodpo.ru/go-i-chs/distancionnoe-obuchenie-go-i-chs"

    i += 1
    

driver.quit()