import requests, logging
from bs4 import BeautifulSoup
from newsapp.glob import USER_AGENT
from newsapp import models


def scrap_onu_features(current_page=None):
    """
    fonction : 
        scrap_onu_features -- scrap l'url 

    Args:
        current_page {int} -- permet de naviguer entre les différentes pages
    """


    def get_detail(detail_url):

        detail = ""
        response = requests.get(detail_url, headers=headers)
        if response.ok:
            soup = BeautifulSoup(response.text, "html.parser")
            detail = soup.find('section', {'id': 'block-system-main'})
        return detail

    print('start')
    # logging.warning('SCRAP IS RUN')

    if current_page:
        url = f"https://news.un.org/fr/features?page={current_page}"
    else:
        url = "https://news.un.org/fr/features"

    headers = {"User-Agent": USER_AGENT}
    response = requests.get(url, headers=headers) 


    if response.ok:

        soup = BeautifulSoup(response.text, "html.parser")
        section = soup.find('section', {'id': 'block-system-main'})

        contents = list(section.findAll('div', {'class': 'views-row'}))

        if len(contents) == 0: return

        for content in contents:
            title_ = content.find('h1', {'class': 'story-title'})
            title_a = title_.find('a')
            picture = content.find('img', {'class': 'img-responsive'})
            date_publication_ = content.find('span', {'class': 'date-display-single'})
            category_ = content.find('div', {'class': 'topics'})
            
            news_source, created = models.Source.objects.get_or_create(name = "news.un.org", link ="https://news.un.org")
            news_source.save()


            news_categorie = models.Category.objects.filter(name = category_.text).first()
            if not news_categorie:
                news_categorie = models.Category(name = category_.text)
                news_categorie.save()


            v_title = title_.text
            v_picture = picture['src']
            v_link = "https://news.un.org" + title_a['href']
            v_date_publication = date_publication_.text
            r_description = str(get_detail(v_link))

            if r_description is None:
                v_description = ""
            else:
                v_description = str(r_description)


            get_article = models.Article.objects.filter(title = v_title).first()

            if not get_article:
                print('v_title', len(v_title))
                print('v_picture', len(v_picture))
                print('v_link', len(v_link))
                print('v_date_publication', len(v_date_publication))

                news_article = models.Article(title = v_title, picture = v_picture, link_detail = v_link, category = news_categorie, source = news_source, description = v_description, date_publication = v_date_publication)
                news_article.save()
        
        current_page = (current_page + 1) if current_page else 1
        print(f'end {current_page}')
        scrap_onu_features(current_page=current_page)
        

if __name__ == '__main__':
    scrap_onu_features()