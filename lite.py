from requests import get, head # Для проверки кода ответа от сайта
from random import choice # Для генерации случайной ссылки
from time import sleep
alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

site = 'https://goo.su' # Сайт для сокращения ссылок
string_len = 5 # Длинна строки для подбора

while 1:
    s = ''
    for i in range(string_len):
        s += choice(alpha)
    url = f'{site}/{s}'
    try:
        status_code = head(url).status_code
    except:
        continue
    print(f'{s} > {status_code}')
    if status_code != 404:
        if status_code == 429:
            while status_code == 429:
                sleep(1)
                status_code = head(url).status_code
            continue
        try:
            r = get(url) # head не содержит переадресованной ссылки, а get содержит, но get работает медленнеe
        except:
            continue
        print(f'{s} | {url} | {r.url}')
        if not url == r.url:   
            input('^^^^^Enter для продолжения')