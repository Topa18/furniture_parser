from selenium import webdriver
from bs4 import BeautifulSoup
import json
import os
import time


url = "https://street-beat.ru/cat/man/obuv/krossovki/"

# Получение html первой страницы
def get_first_page_by_selenium(url):
    
    options = webdriver.ChromeOptions()

    # Добавление user agent
    options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 YaBrowser/24.6.0.0 Safari/537.36")
    # Выключение видимости режима webdriver
    options.add_argument("--disable-blink-features=AutomationControlled")
    # Добавление параметра для фонового открытия браузера
    options.add_argument("--headless")

    driver = webdriver.Chrome(options=options)

    try:
        print("Загрузка 1 страницы...")
        driver.maximize_window()
        driver.get(url=url)
        driver.implicitly_wait(8)

        if not os.path.isdir('data'):
            os.mkdir('data')

        with open("data/first_page.html", 'w') as file:
            file.write(driver.page_source)

    except Exception as e:
        print(e)
    finally:
        driver.close()
        driver.quit()
    
    return print("html код 1 страницы записан.")


def get_page_quantity():
    
    with open(f"data/first_page.html") as file:
        src = file.read()
    
    soup = BeautifulSoup(src, 'lxml')

    page_quantity = soup.find('div', class_="pagination-pages").find_all('button', class_="app-button pagination-pages__btn app-button--theme-transparent app-button--without-shadow")
    page_quantity = page_quantity[-1].text.strip()
    
    return int(page_quantity)


def get_sneakers_from_page():
    
    with open(f"data/first_page.html") as file:
        src = file.read()

    soup = BeautifulSoup(src, 'lxml')

    sneakers_for_sale_list = []

    all_sneakers_at_page = soup.find_all('div', class_="product-container__standard")

    for sneakers_card in all_sneakers_at_page:
        
        sneakers_for_sale = {}
        
        sneakers_with_sale = sneakers_card.find('div', class_="product-card__price").find('span', class_="product-card__price-new")
        
        if sneakers_with_sale:
            sizes = ""

            sneakers_href = "https://street-beat.ru" + sneakers_card.find('a').get('href')
            sneakers_model = sneakers_card.find('a', class_="product-card__info").text.strip()
            old_price = sneakers_card.find('div', class_="product-card__price").find('span', class_="product-card__price-old").text.strip()
            new_price = sneakers_card.find('div', class_="product-card__price").find('span', class_="product-card__price-new").text.strip()
            discount_amount = sneakers_card.find('div', class_="product-card__badge").find('span').text.strip()
            avaliable_sizes = sneakers_card.find('div', class_="block-hover__product-size").find_all('a')
            for size in avaliable_sizes:
                sizes += size.text.strip() + ' '
                sizes.strip()
            
            sneakers_for_sale = {
                "Ссылка на товар": sneakers_href,
                "Модель кроссовок": sneakers_model,
                "Цена без скидки": old_price,
                "Цена со скидкой": new_price,
                "Описание": discount_amount,
                "Доступные размеры": sizes
            }

            sneakers_for_sale_list.append(sneakers_for_sale)

    with open("sneakers_for_sale.json", 'a') as file:
        json.dump(sneakers_for_sale_list, file, indent=4, ensure_ascii=False)
            

def main(url):
    get_first_page_by_selenium(url=url)
    get_sneakers_from_page()


if __name__ == "__main__":
    main("https://street-beat.ru/cat/man/obuv/krossovki/")
    