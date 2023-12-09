import data_loader

yadisk_url = 'https://disk.yandex.ru/d/gCVg9AjXBW8vkw'
save_filename = 'data.zip'

print(data_loader.dl_dataset(yadisk_url, 'data_wage.zip'))