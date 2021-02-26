# pip install requests lxml beautifulsoup4

import requests
from bs4 import BeautifulSoup


def get_html(url: str):
    r = requests.get(url)
    if r.ok:
        return r.text


def get_data(html: str):
    # print(html)
    soup = BeautifulSoup(html, 'lxml')
    # html -> body -> div (id="home-welcome") -> header -> h1
    text = soup.find('div', id="home-welcome").find('header').find('h1').text
    return text


def main():
    url = 'https://wordpress.org/'
    print(get_data(get_html(url)))


if __name__ == '__main__':
    main()
