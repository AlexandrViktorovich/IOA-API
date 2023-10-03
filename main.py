import requests
from bs4 import BeautifulSoup
import os


def parse_images_from_url(url: str):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    image_tags = soup.find_all('img')
    image_urls = []

    for img_tag in image_tags:
        img_url = img_tag.get('src')
        image_urls.append("https:" + img_url)

    for i in image_urls:
        try:
            download_dir = "downloads"
            os.makedirs(download_dir, exist_ok=True)
            image_filename = os.path.join(download_dir, os.path.basename(i))
            response = requests.get(i)

            if response.status_code == 200:
                with open(image_filename, 'wb') as img_file:
                    img_file.write(response.content)
                print(f"Изображение успешно сохранено как {image_filename}")
            else:
                print(f"Ошибка при получении изображения. Код состояния: {response.status_code}")
        except:
            pass


if __name__ == "__main__":
    url = "https://ru.wikipedia.org/wiki/Список_пород_кошек"
    parse_images_from_url(url)
