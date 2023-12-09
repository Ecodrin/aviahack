import requests
import urllib.request

try:
    API_ENDPOINT = 'https://cloud-api.yandex.net/v1/disk/public/resources/download?public_key={}'


    def get_real_direct_link(sharing_link: str) -> str:
        pk_request = requests.get(API_ENDPOINT.format(sharing_link))

        return pk_request.json()['href']


    yadisk_url = 'https://disk.yandex.ru/i/PFrvE7-fpw2a3A'

    urllib.request.urlretrieve(get_real_direct_link(yadisk_url), "inf_22_10_20_10.docx")

except Exception:
    pass