from requests import head # Для проверки кода ответа от сайта
from random import choice # Для генерации случайной ссылки
site = 'https://goo.su' # Сайт для сокращения ссылок
string_len = 5 # Длинна строки для подбора
while 1:  #   ULTRA Lite Версия, где всё сведено к минимуму, даже защиты, поэтому по возможности используй основной файл
    s = ''  # или в крайнем случае Lite версию, где есть необходимые защиты для безопасности и комфорта использования
    for i in range(string_len):
        s += choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890')
    url = f'{site}/{s}'
    try:
        status_code = head(url).status_code
    except:
        continue
    print(f'{s} > {status_code}')
    if status_code != 404:
        print(f'{s} | {url}')
        input('^^^^^Enter для продолжения')