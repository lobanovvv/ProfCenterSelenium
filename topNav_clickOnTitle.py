# Проверка переходов по клику на заголовки в верхнем меню
# Структура теста:
#   - клик на заголовок
#   - проверка url

from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.set_window_size(1920,1080)
driver.get("http://prodpo.ru")

link_url = [
"https://prodpo.ru/obuchenije-po-professijam.html",
"https://prodpo.ru/obuchenie-po-okhrane-truda.html",
"https://prodpo.ru/bezopasnyye-raboty-na-vysote.html",
"https://prodpo.ru/obuchenie-po-pozharnoi-bezopasnosti.html",
"https://prodpo.ru/instruktazhi-i-obuchenie-po-elektrobezopasnosti-v-moskve.html",
"https://prodpo.ru/obuchenie-po-promyshlennoj-bezopasnosti.html",
"https://prodpo.ru/kontakty.html"
]

i = 0
while i < len(link_url):
    element = driver.find_elements_by_css_selector("ul.menu-top > li > a > span")
    element[i].click()
    assert driver.current_url == link_url[i], "url fail"
    i += 1

driver.quit()