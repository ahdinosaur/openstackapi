from flask_restful import Resource

class ServerList(Resource):
    def __init__(self, **kwargs):
        self.openstack_connection = kwargs['openstack_connection']

    def get(self):
        return self.openstack_connection.list_servers()
