from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Инициализация браузера
browser = webdriver.Chrome()

# Спрашиваем у пользователя запрос
query = input("Введите запрос для поиска на Википедии: ")

# Переход на сайт Википедии
browser.get("https://www.wikipedia.org/")

# Поиск поля ввода и введение запроса
search_box = browser.find_element(By.NAME, "search")
search_box.send_keys(query)
search_box.send_keys(Keys.RETURN)

# Ожидание загрузки страницы
time.sleep(2)

# Основной цикл программы
while True:
    print("\nВыберите действие:")
    print("1: Листать параграфы текущей статьи")
    print("2: Перейти на одну из связанных страниц")
    print("3: Выйти из программы")

    choice = input("Ваш выбор: ")

    if choice == '1':
        paragraphs = browser.find_elements(By.XPATH, "//p")
        for i, paragraph in enumerate(paragraphs):
            print(f"Параграф {i + 1}:")
            print(paragraph.text)
            print()

    elif choice == '2':
        links = browser.find_elements(By.XPATH, "//div[@id='bodyContent']//a[@href and not(contains(@href, ':'))]")
        for i, link in enumerate(links):
            print(f"{i + 1}: {link.text} - {link.get_attribute('href')}")

        link_choice = int(input("Введите номер ссылки для перехода: ")) - 1
        if 0 <= link_choice < len(links):
            browser.get(links[link_choice].get_attribute('href'))
            time.sleep(2)  # Ожидание загрузки новой страницы
        else:
            print("Некорректный выбор.")

    elif choice == '3':
        break
    else:
        print("Некорректный ввод, попробуйте снова.")

# Закрываем браузер
browser.quit()
