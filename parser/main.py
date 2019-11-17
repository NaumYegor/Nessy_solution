import requests
import config
import datetime
import bs4


def return_movies(curr_date=datetime.date.today()):
    date = {
        'year': curr_date.strftime('%Y'),
        'month': curr_date.strftime('%m'),
        'day': curr_date.strftime('%d')
    }
    params = {'date': '{}-{}-{}'.format(date['year'],
                                        date['month'],
                                        date['day'])}
    classes = {'common': {'class': 'film-box-holder actual'},
               'personal': 'film-box',
               'title': 'film-title'}

    r = requests.get(url=config.city_link,
                     params=params,
                     headers=config.headers)
    page = bs4.BeautifulSoup(r.text, features='html.parser')
    only_films = \
        page.find('div', classes['common']).find_all('div',
                                                     classes['personal'])
    for i in range(len(only_films)):
        only_films[i] = \
            only_films[i].find('a', classes['title']).find('span').get_text()

    return only_films


print(return_movies())
