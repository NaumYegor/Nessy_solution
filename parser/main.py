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
    board_link = '{}{}'.format(
        cfg.links_navigator.get('main'), cfg.links_navigator.get('board')
    )

    r = requests.get(url=board_link,
                     params=params,
                     headers=cfg.headers)
    page = bs4.BeautifulSoup(r.text, features='html.parser')
    only_films = page.find('div', classes.get('common')
                           ).find_all('div',
                                      classes.get('personal'))
    for i in range(len(only_films)):
        film_name = only_films[i].find('a', classes.get('title')
                                       ).find('span').get_text()
        info_link = '{}{}'.format(
            cfg.links_navigator.get('main'),
            only_films[i].find('a', classes.get('link')).get('href'))
        only_films[i] = {film_name: info_link}

    return only_films


def info_about(info_link):
    classes = {
        'description': {'element': 'div', 'class': 'film-description'},
        'title': {'element': 'h3', 'class': 'title'},
        'translation': {'element': 'span', 'class': 'sub-title'}
    }

    r = requests.get(info_link)
    page = bs4.BeautifulSoup(r.text, features='html.parser')
    film_data = {
        'title':
            page.find(classes.get('description').get('element'),
                      classes.get('description').get('class')
                      ).find('h3', {'class': 'title'}).get_text(),
        'translation':
            page.find(classes.get('description').get('element'),
                      classes.get('description').get('class')
                      ).find(classes.get('translation').get('element'),
                             classes.get('translation').get('class')
                             ).get_text()
    }
    return film_data


print(info_about('https://m.vkino.ua/ru/show/8010-angeli-charli/kharkov?date=2019-11-18'))
