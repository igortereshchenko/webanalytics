from datetime import datetime

from Requests.Requester import Requester
from Country.Germany.News.SPIEGEL.NewsScraper import NewsScraper
from bs4 import BeautifulSoup
from Translation.GoogleTranslator import  GoogleTranslator
from Scraper.Writters.FileWritter import FileWriter


translator = GoogleTranslator()

url = "http://www.spiegel.de/"

requester = Requester(url=url, retries=5, sleep_time=3)
response = requester.make_get_request()
html = response.data


dataset = NewsScraper.parse_articles_list(url_root=url,html=html)


for url in  list(dataset):

    requester = Requester(url=url, retries=5)
    response = requester.make_get_request()
    html = response.data

    soup = BeautifulSoup(html, 'html.parser')

    subtitle = NewsScraper.parse_article_subtitle(html=html, soup=soup)

    hours, minutes, seconds = NewsScraper.parse_article_time(html=html, soup=soup)

    html, text = NewsScraper.parse_article_text(html=html, soup=soup)

    date = NewsScraper.parse_article_date(html=html, soup=soup)

    '''date = datetime(year=2019, month=1, day=23)
    if hours:
        date = date.replace(hour=hours)
    if minutes:
        date = date.replace(minute=minutes)
    if seconds:
        date = date.replace(second=seconds)'''

    dataset[url]['date']=date
    dataset[url]['subtitle']=subtitle
    dataset[url]["text"] = text
    dataset[url]["html"] = html

    if text:
        try:
            translation_result = translator.get_translation(text)
            dataset[url]["translation_en"] = translation_result['translation']
        except Exception:
            print("Translation error with url {0} and text {1}".format(url,text))

writer = FileWriter("data/news.csv")
writer.write(dataset)