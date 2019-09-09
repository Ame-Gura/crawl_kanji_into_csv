# main.py
import PDFPaser
import Crawler
import pandas as pd
text = PDFPaser.PDF2String('N4830BU.pdf')

kanji_list = [char for char in text['content'] if ord(char) >= 0x4e00 and ord(char) <=0x9faf]

#한자 리스트
print(kanji_list)

#한자 갯수
print('length of kanji_list : '+str(len(kanji_list)))

#중복제거
kanji_set = set(kanji_list)

#한자 갯수
print('length of kanji_set : '+str(len(kanji_set)))

anki_data = list()
#한자 크롤링
for kanji in kanji_set:
    data = Crawler.crawl(kanji)
    print(data['kanji'])
    print(data['um'])
    print(data['hun'])
    print(data['mean'])
    anki_data.append(data)

panda = pd.DataFrame(anki_data)
panda.to_csv('anki.csv', mode='w')