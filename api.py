from flask import Flask
from flask_restful import Api
import openstack

from resources.server_list import ServerList

openstack_connection = openstack.connect(cloud='envvars')

app = Flask(__name__)
api = Api(app)

api.add_resource(ServerList, '/servers', resource_class_kwargs={ 'openstack_connection': openstack_connection })
api.add_resource(Server, '/servers/:server_name_or_id', resource_class_kwargs={ 'openstack_connection': openstack_connection })

if __name__ == '__main__':
    openstack.enable_logging(debug=True)
    app.run(debug=True)

