from flask_restful import Resource

class ServerList(Resource):
    def __init__(self, **kwargs):
        self.openstack_connection = kwargs['openstack_connection']

    def get(self, server_name_or_id):
        return self.openstack.get_server(
            name_or_id=server_name_or_id
        )
