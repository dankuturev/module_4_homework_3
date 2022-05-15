import bs4
import requests as r
from tqdm import tqdm

from arguments import KEYWORDS, header, url, title_url, tag, tag_2, parent_dir
from logger import logger


def get_content(header, url, tag):
    response = r.get(url, headers=header.generate())
    response.raise_for_status()
    text = response.text
    soup = bs4.BeautifulSoup(text, features='html.parser')
    articles = soup.find_all(tag)
    return soup, articles


@logger(parent_dir)
def get_articles():
    title_list = []
    for article in tqdm(get_content(header, url, tag)[1]):
        href = title_url + article.find(class_='tm-article-snippet__title-link').attrs['href']
        get_content(header, href, ''.join(tag_2))
        contents = get_content(header, href, tag_2)[0].find_all(class_='article-formatted-body '
                                                                       'article-formatted-body '
                                                                       'article-formatted-body_version-2')
        contents = str(set(content.text for content in contents)).split()
        for pre in contents:
            if pre in KEYWORDS:
                date = article.find('time').attrs['title']
                href = title_url + article.find(class_='tm-article-snippet__title-link').attrs['href']
                title = article.find('h2').find('span').text
                title_list.append(f'{date} - {title} - {href}')
    return set(title_list)


if __name__ == '__main__':
    get_articles()
