from flask import Flask
import parser as man
import datetime
import json

app: Flask = Flask(__name__)
info = []


@app.route('/general', methods=['GET'])
def general(date=datetime.date.today()):
    data = man.return_movies(date)
    r = 0
    for k, v in data.items():
        info.append(man.info_about(v))
        s = (man.get_mdb_info(info[r].get('translation')))
        if s.get('imdbRating') == "N/A" or s.get('imdbRating') is None:
            info[r]['imdb'] = ''
        else:
            info[r]['imdb'] = s.get('imdbRating')
        r = r + 1
    json_info = json.dumps(info, sort_keys=False, indent=4, ensure_ascii=False, separators=(',', ': '))
    return json_info


@app.route('/details', methods=['GET'])
def details(name=None):
    return man.get_mdb_info(name)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False, port=3000)
