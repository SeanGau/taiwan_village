from sqlalchemy import create_engine
import json, os
geojson_file = 'village_moe.geojson' # https://data.gov.tw/dataset/7438 轉 geojson後之檔案
database_url = os.environ['DATABASE_URL']
table_name = 'public.village_gis'

engine = create_engine(database_url, encoding= 'utf-8', json_serializer= lambda obj: obj)
with open(geojson_file) as  json_file, open('error.log', 'w') as error_log:
	data = json.load(json_file)
	for feature in data['features']:
		with engine.connect() as con:
			properties = feature.get('properties','{}')
			properties_s = str(json.dumps(properties, ensure_ascii=False).replace('\'','\'\''))
			geometry = str(json.dumps(feature.get('geometry','{}'), ensure_ascii=False).replace('\'','\'\''))
			rs = con.execute(f"INSERT INTO {table_name} (data,geom) VALUES (\'{properties_s}\',ST_GeomFromGeoJSON(\'{geometry}\'));")
			print(properties_s)