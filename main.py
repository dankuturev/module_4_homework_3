import bs4
import requests as r
from arguments import KEYWORDS, header, url, title_url

def get_articles():
    response = r.get(url, headers=header.generate())
    response.raise_for_status()
    text = response.text
    soup = bs4.BeautifulSoup(text, features='html.parser')
    articles = soup.find_all('article')
    title_list = []
    for article in articles:
        previev = article.find_all(class_='article-formatted-body')
        previev = str(set(pre.text for pre in previev)).split()
        for pre in previev:
            if pre in KEYWORDS:
                date = article.find('time').attrs['title']
                href = title_url + article.find(class_='tm-article-snippet__title-link').attrs['href']
                title = article.find('h2').find('span').text
                title_list.append(f'{date} - {title} - {href}')
    print(*(set(title_list)), sep='\n')

if __name__ == '__main__':
    get_articles()