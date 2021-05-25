import flask, os, json
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

app = flask.Flask(__name__)
app.config.from_object('config')

app.jinja_env.globals['GLOBAL_TITLE'] = "村里界圖查詢"
app.jinja_env.globals['GLOBAL_VERSION'] = datetime.now().timestamp()
db = SQLAlchemy(app)

@app.route('/')
def index():
    return flask.render_template('index.html')

@app.route('/api/village')
def village():
    print(flask.request.args)
    _city = flask.request.args.get('city')
    _town = flask.request.args.get('town')
    _village = flask.request.args.get('village')
    _simply = flask.request.args.get('simply')
    _sql = "select ST_AsGeoJSON(geom),data from public.village_gis where "

    can_go = False
    if _simply == 'true':
        _sql = "select ST_AsGeoJSON(ST_Simplify(geom,0.0001)),data from public.village_gis where "
    if len(_city) > 0:
        _sql += f"data ->> 'COUNTYNAME' = '{_city}' and "
        can_go = True
    if len(_town) > 0:
        _sql += f"data ->> 'TOWNNAME' = '{_town}' and "
        can_go = True
    if len(_village) > 0:
        _sql += f"data ->> 'VILLNAME' = '{_village}'"
        can_go = True
    else:
        _sql = _sql[:-4]
    if not can_go:
        return "error"
    rs = db.session.execute(_sql)
    _dict = {"type" : "FeatureCollection","features":[]}
    for row in rs:
        d = {"type": "Feature", "geometry": json.loads(row['st_asgeojson']), "properties": row['data']}
        _dict['features'].append(d)
    return json.dumps(_dict, ensure_ascii = False)

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(host='0.0.0.0', threaded=True, port=5000, debug=True)