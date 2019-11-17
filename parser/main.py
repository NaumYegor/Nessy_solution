import requests
import config
import datetime
import bs4


def return_movies(required_date=datetime.date.today()):
    date = {
        'year': required_date.strftime('%Y'),
        'month': required_date.strftime('%m'),
        'day': required_date.strftime('%d')
    }
    params = {'date': '{}-{}-{}'.format(date['year'],
                                        date['month'],
                                        date['day'])}
    classes = {'common': 'film-box-holder actual',
               'personal': 'film-box',
               'title': 'film-title',
               'link': 'btn-buy'}

    r = requests.get(url=config.city_link,
                     params=params,
                     headers=config.headers)
    page = bs4.BeautifulSoup(r.text, features='html.parser')
    only_films = \
        page.find('div', classes['common']).find_all('div',
                                                     classes['personal'])
    for i in range(len(only_films)):
        film_name = \
            only_films[i].find('a', classes['title']).find('span').get_text()
        info_link = \
            only_films[i].find('a', classes['link']).get("href")
        only_films[i] = {film_name: info_link}

    return only_films


print(return_movies())
