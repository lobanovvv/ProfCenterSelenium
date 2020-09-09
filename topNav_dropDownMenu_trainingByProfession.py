# Проверка линков (текст, переход) выпадающего меню "Обучение по профессиям" в верхнем навигационном меню
# Описание теста:
#   - Раскрытие меню
#   - Проверка текста ссылки
#   - ЛКМ по ссылке
#   - Проверка обновленного url

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.set_window_size(1920,1080)
driver.get("http://prodpo.ru")

link_url = [
    "https://prodpo.ru/obucheniye-elektromontazhnik",
    "https://prodpo.ru/obucheniye-elektromontera",
    "https://prodpo.ru/slesar-elektrik-po-remontu-elektrooborudovaniya",
    "https://prodpo.ru/obucheniye-na-liftera.html",
    "https://prodpo.ru/elektromekhanik-po-liftam.html",
    "https://prodpo.ru/dispetcher-ods.html",
    "https://prodpo.ru/rabochiy-lyulki-nakhodyashcheysya-na-podemnike.html",
    "https://prodpo.ru/elektrogazosvarshchik",
    "https://prodpo.ru/operator-podemnykh-platform-dlya-invalidov.html",
    "https://prodpo.ru/operator-gazovoy-kotelnoy",
    "https://prodpo.ru/mashinist-stroitelnogo-podyemnika",
    "https://prodpo.ru/stropalschik",
]

link_name = [
"Электромонтажник",
"Электромонтер",
"Слесарь-электрик",
"Обучение на лифтера",
"Электромеханик по лифтам",
"Диспетчер ОДС",
"Рабочий люльки",
"Электрогазосварщик",
"Оператор подъемных платформ для инвалидов",
"Оператор газовой котельной",
"Машинист строительного подъемника",
"Стропальщик"
]

i = 0
while i < len(link_url):
    
    elem = driver.find_element_by_css_selector("ul.menu-top > li > a > span")
    
    actions = ActionChains(driver)
    actions.move_to_element(elem)
    actions.perform()

    elem = driver.find_elements_by_css_selector("ul.menu-top > li:first-child > ul > li > a > span")
    assert elem[i].text == link_name[i], "name fail"
    elem[i].click()
    assert driver.current_url == link_url[i], "url fail"
    
    i += 1

driver.quit()
