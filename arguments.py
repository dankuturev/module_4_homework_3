from os import path

from fake_headers import Headers

KEYWORDS = ['дизайн', 'фото', 'web', 'python']
header = Headers(browser='firefox', os='win', headers=True)
url = 'https://habr.com/ru/all/'
title_url = 'https://habr.com'
tag = 'article'
tag_2 = ''.join("class_='tm-article-presenter__content tm-article-presenter__content_narrow'")

parent_dir = path.dirname(path.abspath('module_4_homework_3'))
print(parent_dir)
