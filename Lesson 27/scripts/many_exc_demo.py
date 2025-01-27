import requests

url = "https://compassplus.com/not_found"

try:
    # не получив ответ за 30 сек перестаём ждать - возможен requests.Timeout
    response = requests.get(url, timeout=30)  
    # проверяем http status code - возможен requests.HTTPError
    response.raise_for_status()               
except requests.Timeout:
    print("Ошибка timeout, url:", url)
except requests.HTTPError as err:
    http_status_code = err.response.status_code
    print("Ошибка url: {0}, code {1}".format(url, http_status_code))
except requests.RequestException as err:
    print("Ошибка скачивания url:", url)
    print("Сообщение об ошибке", err)
else:
    print(response.content)
