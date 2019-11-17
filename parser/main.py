import requests
import config as cfg
import datetime
import bs4


def return_movies(required_date=datetime.date.today()):
    date = {
        'year': required_date.strftime('%Y'),
        'month': required_date.strftime('%m'),
        'day': required_date.strftime('%d')
    }
    params = {'date': '{}-{}-{}'.format(date.get('year'),
                                        date.get('month'),
                                        date.get('day'))}
    classes = {'common': 'film-box-holder actual',
               'personal': 'film-box',
               'title': 'film-title',
               'link': 'btn-buy'}
    board_link = \
        cfg.links_navigator.get('main') + cfg.links_navigator.get('board')

    r = requests.get(url=board_link,
                     params=params,
                     headers=cfg.headers)
    page = bs4.BeautifulSoup(r.text, features='html.parser')
    only_films = \
        page.find('div', classes.get('common')).find_all('div',
                                                         classes.get('personal'))
    for i in range(len(only_films)):
        film_name = \
            only_films[i].find('a', classes.get('title')).find('span').get_text()
        info_link = '{}{}'.format(
            cfg.links_navigator.get('main'),
            only_films[i].find('a', classes.get('link')).get('href'))
        only_films[i] = {film_name: info_link}

    return only_films


print(return_movies())
