from multiprocessing import Process

import requests # request img from web
import shutil # save img locally

image_urls = ['https://blog.apify.com/content/images/2024/02/Apify-logo.png',
              'https://storage.kun.uz/source/thumbnails/_medium/10/YUiB24gHvr9WJzNxbaLlq2yDRBPIfWFC_medium.jpg',
              'https://storage.kun.uz/source/thumbnails/_medium/10/_mN-4sIn8yHGHsK76-yCrpilCoFJTA60_medium.jpg']
def download_image(url):
    res = requests.get(url,stream = True)
    filename = url.split('/')[-1]

    if res.status_code == 200:
        with open(filename,'wb') as f:
            shutil.copyfileobj(res.raw, f)

def create_protses_funksions(url_list:list):
    for url in url_list:
        task = Process(target=download_image, kwargs={'url':url})
        task.run()


create_protses_funksions(image_urls)


