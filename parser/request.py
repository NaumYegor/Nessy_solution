from flask import Flask, request
import main as man
import datetime
import json

app: Flask = Flask(__name__)
info = {}


@app.route('/general', methods=['GET'])
def general(date=datetime.date.today()):
    if request.values.get('date') is not None:
        date = request.values.get('date')

    data = man.return_movies(date)
    r = 0
    for k, v in data.items():
        info[r] = (man.info_about(v))
        s = (man.get_mdb_info(info[r].get('translation')))
        if s.get('imdbRating') == "N/A" or s.get('imdbRating') is None:
            info[r]['imdb'] = ''
        else:
            info[r]['imdb'] = s.get('imdbRating')
        r = r + 1
    json_info = json.dumps(info, sort_keys=False, indent=4, ensure_ascii=False, separators=(',', ': '))
    return json_info


@app.route('/details', methods=['GET'])
def details():
    if request.values.get('name') is not None:
        name = request.values.get('name')
    else:
        return "Name is none"
    return man.get_mdb_info(name)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False, port=3000)
