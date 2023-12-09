import datetime
from flask import Flask
from flask_cors import CORS
from flask_restful import Api

from read_properties import properties
from resource.ads import AdsInsert
from resource.ads import AdsUpdate
from resource.ads import AdsList

app = Flask(__name__)
api = Api(app)
CORS(app)

api.add_resource(AdsInsert, '/ads_insert')
api.add_resource(AdsUpdate, '/ads_update')
api.add_resource(AdsList, '/ads_list')

if __name__ == '__main__':
    current_timestamp = datetime.datetime.now()
    date_time = current_timestamp.strftime("%Y-%m-%d_%H-%M-%S")
    app.run(host=properties['db_host'], port=properties['db_port'], debug=False, use_reloader=False)
