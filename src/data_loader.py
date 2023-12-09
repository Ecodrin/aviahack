import os
import shutil
import requests
import urllib.request
import subprocess
from file_enumerate import enumerate


def loader():
    API_ENDPOINT = 'https://cloud-api.yandex.net/v1/disk/public/resources/download?public_key={}'
    def get_real_direct_link(sharing_link: str) -> str:
        pk_request = requests.get(API_ENDPOINT.format(sharing_link))

        return pk_request.json()['href']

    yadisk_url = 'https://disk.yandex.ru/d/hYY_tmmyP3WaFg'
    print(get_real_direct_link(yadisk_url))

    # get data.zip
    urllib.request.urlretrieve(get_real_direct_link(yadisk_url), "data.zip")

    # unzip data.zip
    subprocess.run(["unzip", "data.zip"])
    os.remove("data.zip")


if __name__ == '__main__':
    main()
