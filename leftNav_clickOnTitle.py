# Проверка линков (текст, переход) левого навигационного меню при непосредственном нажатии на них мышкой
# Описание теста:
#   - Заголовки групп меню
#       -- проверка текста
#   - Пункты меню
#       -- проверка текста
#       -- клик на пункт
#       -- проверка url

from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.set_window_size(1920,1080)
driver.get("http://prodpo.ru")

title_text = [
"ОБ ОБУЧЕНИИ",
"ДОПОЛНИТЕЛЬНЫЕ УСЛУГИ",
"КЛИЕНТУ"
]

link_url = [
"https://prodpo.ru/vidy-obucheniya",
"https://prodpo.ru/pakety-obucheniya",
"https://prodpo.ru/grafik-provedeniya-obucheniya.html",
"https://prodpo.ru/obuchayushchiye-meropriyatiya",
"https://prodpo.ru/stoimost-obucheniya.html",
"https://prodpo.ru/spetsialnaya-otsenka-uslovij-truda.html",
"https://prodpo.ru/razrabotka-programmy-proizvodstvennogo-kontrolya",
"https://prodpo.ru/obsluzhivanie-po-okhrane-truda-autsorsing.html",
"https://prodpo.ru/komplekt-dokumentov-po-okhrane-truda.html",
"https://prodpo.ru/konsultatsii-pri-neschastnykh-sluchayakh.html",
"https://prodpo.ru/otzyvy-o-nas.html",
"https://prodpo.ru/discounts",
"https://prodpo.ru/articles",
"https://prodpo.ru/faq",
"https://prodpo.ru/vacancies",
"https://prodpo.ru/sposoby-oplaty",
"https://prodpo.ru/svedeniya-ob-obrazovatelnoy-organizatsii"
]

link_text = [
"Виды обучения",
"Пакеты обучения",
"График и сроки обучения",
"Обучающие мероприятия",
"Стоимость обучения",
"Спец. оценка условий труда",
"Производственный контроль",
"Аутсорсинг по охране труда",
"Разработка документов",
"Несчастные случаи",
"Отзывы о нас",
"Акции",
"Статьи",
"Частые вопросы",
"Вакансии",
"Способы оплаты",
"Сведения об образовательной организации"
]

# Проверка текста заголовков групп меню
i = 0
lenArr = len(title_text)

while i < lenArr:
    elem = driver.find_elements_by_css_selector("div.menu_title")
    assert elem[i].text == title_text[i], "title text fail"
    elem[i].click()
    assert driver.current_url == "https://prodpo.ru/", "url fail"
    
    i += 1

# Остальное левое меню
i = 0
lenArr = len(link_url)

while i < lenArr:
    elem = driver.find_elements_by_css_selector("ul.left-menu > li > a")
    assert elem[i].text == link_text[i], "text fail"
    elem[i].click()
    assert driver.current_url == link_url[i], "url fail"
    i += 1

driver.quit()