#Crawler.py
from bs4 import BeautifulSoup
import requests

def search_link(kanji):
    return 'https://ja.dict.naver.com/search.nhn?range=all&q='+kanji


def crawl(kanji):
    html = requests.get(search_link(kanji))
    html.encoding = 'UTF-8'
    # html 파싱
    soup = BeautifulSoup(html.text, 'html5lib')

    # 음독
    um = soup.select('#content > div.section.all.section_word > div:nth-child(2) > dl:nth-child(2) > dd:nth-child(2)')

    # 훈독
    hun = soup.select('#content > div.section.all.section_word > div:nth-child(2) > dl:nth-child(2) > dd:nth-child(4)')

    # 뜻
    mean = soup.select(
        '#content > div.section.all.section_word > div:nth-child(2) > dl.top_dn.top_dn_v2 > dd.ft_col3 > span.ft_col3')

    try:
        um = ''.join(um[0].text.split())
    except Exception:
        um = ''

    try:
        hun = ''.join(hun[0].text.split())
    except:
        hun = ''

    try:
        mean = mean[0].text
    except:
        mean = ''
    kanjiData = {'kanji': kanji, 'um':um, 'hun': hun, 'mean':mean}
    return kanjiData
if __name__ == '__main__':
    #html 요청
    html = requests.get(search_link('検'))
    html.encoding = 'UTF-8'
    #html 파싱
    soup = BeautifulSoup(html.text, 'html5lib')

    #음독
    um = soup.select('#content > div.section.all.section_word > div:nth-child(2) > dl:nth-child(2) > dd:nth-child(2)')

    #훈독
    hun = soup.select('#content > div.section.all.section_word > div:nth-child(2) > dl:nth-child(2) > dd:nth-child(4)')

    #뜻
    mean = soup.select('#content > div.section.all.section_word > div:nth-child(2) > dl.top_dn.top_dn_v2 > dd.ft_col3 > span.ft_col3')

    print(''.join(um[0].text.split()))
    print(''.join(hun[0].text.split()))
    print(mean[0].text)