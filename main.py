import requests
import json
import os



def get_page_count(woman=False):
    
    sex_param = ['man', 'woman']
        
    if woman == False:
        sex = sex_param[0]
        
    if woman == True:
        sex = sex_param[1]

    cookies = {
        '__ddg1_': 'ezJug2Gpo3eKy080oZ3x',
        'CLIENT_CITY_ID': '19',
        'CLIENT_CITY': '%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0',
        '_ym_uid': '1718792546776072077',
        '_ym_d': '1718792546',
        '_ga': 'GA1.1.696827334.1718792547',
        'tmr_lvid': '5661ec427c263592f4b1ff153251f849',
        'tmr_lvidTS': '1718792547155',
        'popmechanic_sbjs_migrations': 'popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1',
        'BX_USER_ID': '3c24a730191185cde769ed8a09656288',
        'adid': '171879254955231',
        'user_city': '%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0',
        'city_fias': '0c5b2444-70a0-4932-980c-b4dc0d3f02b5',
        'region_fias': '0c5b2444-70a0-4932-980c-b4dc0d3f02b5',
        'mainpagetype': f'{sex}',
        'domain_sid': 'WWJ3NzkwzjqAnSYY3fSiv%3A1719320438050',
        'PHPSESSID': 'jkpRaE5ArFoRBZYltNUCx0o477dV77OG',
        'topMenu_active': f'%2F{sex}%2F',
        '_ym_isad': '1',
        '_ym_visorc': 'b',
        'user_usee': '%5B4421828%2C4450694%2C4361310%2C4379702%2C4443460%2C4204156%2C1646512%5D',
        'mindboxDeviceUUID': '215f6c59-e421-4690-ab13-6395c63f2fcb',
        'directCrm-session': '%7B%22deviceGuid%22%3A%22215f6c59-e421-4690-ab13-6395c63f2fcb%22%7D',
        'tmr_detect': '0%7C1719399604190',
        '_ga_E3GN5VV3T0': 'GS1.1.1719396756.13.1.1719399632.26.0.0',
    }

    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'ru,en;q=0.9',
        'content-type': 'application/json; charset=UTF-8',
        # 'cookie': '__ddg1_=ezJug2Gpo3eKy080oZ3x; CLIENT_CITY_ID=19; CLIENT_CITY=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0; _ym_uid=1718792546776072077; _ym_d=1718792546; _ga=GA1.1.696827334.1718792547; tmr_lvid=5661ec427c263592f4b1ff153251f849; tmr_lvidTS=1718792547155; popmechanic_sbjs_migrations=popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1; BX_USER_ID=3c24a730191185cde769ed8a09656288; adid=171879254955231; user_city=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0; city_fias=0c5b2444-70a0-4932-980c-b4dc0d3f02b5; region_fias=0c5b2444-70a0-4932-980c-b4dc0d3f02b5; mainpagetype=man; domain_sid=WWJ3NzkwzjqAnSYY3fSiv%3A1719320438050; PHPSESSID=jkpRaE5ArFoRBZYltNUCx0o477dV77OG; topMenu_active=%2Fman%2F; _ym_isad=1; _ym_visorc=b; user_usee=%5B4421828%2C4450694%2C4361310%2C4379702%2C4443460%2C4204156%2C1646512%5D; mindboxDeviceUUID=215f6c59-e421-4690-ab13-6395c63f2fcb; directCrm-session=%7B%22deviceGuid%22%3A%22215f6c59-e421-4690-ab13-6395c63f2fcb%22%7D; tmr_detect=0%7C1719399604190; _ga_E3GN5VV3T0=GS1.1.1719396756.13.1.1719399632.26.0.0',
        'origin': 'https://street-beat.ru',
        'priority': 'u=1, i',
        'referer': f'https://street-beat.ru/cat/{sex}/obuv/krossovki/?page=1',
        'sec-ch-ua': '"Chromium";v="124", "YaBrowser";v="24.6", "Not-A.Brand";v="99", "Yowser";v="2.5"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 YaBrowser/24.6.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    json_data = {
        'pagination': {
            'page': 1,
        },
        'sorting': {
            'key': 'sort',
            'value': 'desc',
        },
        'seo': {
            'uri': f'/cat/{sex}/obuv/krossovki/?page=1',
        },
        'search': '',
    }

    response = requests.post('https://street-beat.ru/api/catalog/page', cookies=cookies, headers=headers, json=json_data)

    page_count = response.json().get('catalog').get('pagination').get('lastPage')
    
    return page_count, sex


def get_data(fn):
    
    page_count, sex = fn

    sneakers_for_sale = []

    for page in range(1, page_count + 1):
        cookies = {
            '__ddg1_': 'ezJug2Gpo3eKy080oZ3x',
            'CLIENT_CITY_ID': '19',
            'CLIENT_CITY': '%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0',
            '_ym_uid': '1718792546776072077',
            '_ym_d': '1718792546',
            '_ga': 'GA1.1.696827334.1718792547',
            'tmr_lvid': '5661ec427c263592f4b1ff153251f849',
            'tmr_lvidTS': '1718792547155',
            'popmechanic_sbjs_migrations': 'popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1',
            'BX_USER_ID': '3c24a730191185cde769ed8a09656288',
            'adid': '171879254955231',
            'user_city': '%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0',
            'city_fias': '0c5b2444-70a0-4932-980c-b4dc0d3f02b5',
            'region_fias': '0c5b2444-70a0-4932-980c-b4dc0d3f02b5',
            'mainpagetype': f'{sex}',
            'domain_sid': 'WWJ3NzkwzjqAnSYY3fSiv%3A1719320438050',
            'PHPSESSID': 'jkpRaE5ArFoRBZYltNUCx0o477dV77OG',
            'topMenu_active': f'%2F{sex}%2F',
            '_ym_isad': '1',
            '_ym_visorc': 'b',
            'user_usee': '%5B4421828%2C4450694%2C4361310%2C4379702%2C4443460%2C4204156%2C1646512%5D',
            'mindboxDeviceUUID': '215f6c59-e421-4690-ab13-6395c63f2fcb',
            'directCrm-session': '%7B%22deviceGuid%22%3A%22215f6c59-e421-4690-ab13-6395c63f2fcb%22%7D',
            'tmr_detect': '0%7C1719399604190',
            '_ga_E3GN5VV3T0': 'GS1.1.1719396756.13.1.1719399632.26.0.0',
        }

        headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'ru,en;q=0.9',
            'content-type': 'application/json; charset=UTF-8',
            # 'cookie': '__ddg1_=ezJug2Gpo3eKy080oZ3x; CLIENT_CITY_ID=19; CLIENT_CITY=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0; _ym_uid=1718792546776072077; _ym_d=1718792546; _ga=GA1.1.696827334.1718792547; tmr_lvid=5661ec427c263592f4b1ff153251f849; tmr_lvidTS=1718792547155; popmechanic_sbjs_migrations=popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1; BX_USER_ID=3c24a730191185cde769ed8a09656288; adid=171879254955231; user_city=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0; city_fias=0c5b2444-70a0-4932-980c-b4dc0d3f02b5; region_fias=0c5b2444-70a0-4932-980c-b4dc0d3f02b5; mainpagetype=man; domain_sid=WWJ3NzkwzjqAnSYY3fSiv%3A1719320438050; PHPSESSID=jkpRaE5ArFoRBZYltNUCx0o477dV77OG; topMenu_active=%2Fman%2F; _ym_isad=1; _ym_visorc=b; user_usee=%5B4421828%2C4450694%2C4361310%2C4379702%2C4443460%2C4204156%2C1646512%5D; mindboxDeviceUUID=215f6c59-e421-4690-ab13-6395c63f2fcb; directCrm-session=%7B%22deviceGuid%22%3A%22215f6c59-e421-4690-ab13-6395c63f2fcb%22%7D; tmr_detect=0%7C1719399604190; _ga_E3GN5VV3T0=GS1.1.1719396756.13.1.1719399632.26.0.0',
            'origin': 'https://street-beat.ru',
            'priority': 'u=1, i',
            'referer': f'https://street-beat.ru/cat/{sex}/obuv/krossovki/?page={page}',
            'sec-ch-ua': '"Chromium";v="124", "YaBrowser";v="24.6", "Not-A.Brand";v="99", "Yowser";v="2.5"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 YaBrowser/24.6.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
        }

        json_data = {
            'pagination': {
                'page': int(f"{page}"),
            },
            'sorting': {
                'key': 'sort',
                'value': 'desc',
            },
            'seo': {
                'uri': f'/cat/{sex}/obuv/krossovki/?page={page}',
            },
            'search': '',
        }

        response = requests.post('https://street-beat.ru/api/catalog/page', cookies=cookies, headers=headers, json=json_data)

        if not os.path.isdir('data'):
            os.mkdir('data')
        
        with open(f"data/{page}_response.json", 'w') as file:
            json.dump(response.json(), file, indent=4, ensure_ascii=False)

        
        with open(f"data/{page}_response.json") as file:
            src = json.load(file)
        
        sneakers_at_page = src.get('catalog').get('listing').get('items')
        
        for item in sneakers_at_page:
        
        # Проверка карточки товара на подлинность
            if item.get('price'):
                rec_price = item.get('price').get('recommended').get('price')
                special_price = item.get('price').get('special').get('price')
            
                if rec_price != special_price:
                    sizes = ""

                    item_url = "https://street-beat.ru" + item.get('url')
                    item_brand = item.get('brand')
                    item_model = item.get('title')
                    item_type = item.get('badge').get('text')
                    item_color = item.get('color')
                    available_sizes = item.get('sizes').get('options')
                    for size in available_sizes:
                        sizes += size.get('grid').get('rus') + '; '  

                    item_card = {
                        "Ссылка": item_url,
                        "Бренд": item_brand,
                        "Модель": item_model,
                        "Цена без скидки": rec_price,
                        "Цена по скидке" : special_price,
                        "Тип": item_type,
                        "Цвет": item_color,
                        "Размеры": sizes 
                    }

                    sneakers_for_sale.append(item_card)
        
        print(f"Обработано страниц: {page}/{page_count}")
                
    with open(f"result_for_{sex}.json", 'w') as file:
        json.dump(sneakers_for_sale, file, indent=4, ensure_ascii=False )
    
    sneakers_count = len(sneakers_for_sale)

    return print(f"Сбор данных завершен. Найдено позиций по скидке: {sneakers_count}")
                

def main():

    get_data(get_page_count(woman=True))


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Ошибка... {e}")
        







